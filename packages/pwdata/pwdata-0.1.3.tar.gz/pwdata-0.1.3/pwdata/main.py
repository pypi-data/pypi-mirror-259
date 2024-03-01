import numpy as np
import os, sys, glob
from math import ceil
from collections import Counter
from typing import (List, Union, Optional)
# import time
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from pwdata.image import Image
from pwdata.movement import MOVEMENT
from pwdata.outcar import OUTCAR
from pwdata.poscar import POSCAR
from pwdata.atomconfig import CONFIG
from pwdata.dump import DUMP
from pwdata.lammpsdata import LMP
from pwdata.cp2kdata import CP2KMD, CP2KSCF
from pwdata.movement_saver import save_to_movement
from pwdata.extendedxyz import save_to_extxyz
from pwdata.datasets_saver import save_to_dataset, get_pw, save_to_raw, save_to_npy
from pwdata.build.write_struc import write_config, write_vasp, write_lammps
from pwdata.build.supercells import make_supercell
from pwdata.pertub.perturbation import BatchPerturbStructure
from pwdata.pertub.scale import BatchScaleCell

class Save_Data(object):
    def __init__(self, data_path, datasets_path = "./PWdata", train_data_path = "train", valid_data_path = "valid", 
                 train_ratio = None, random = True, seed = 2024, format = None, retain_raw = False, atom_names:list[str] = None) -> None:
        if format.lower() == "pwmat/config":
            self.image_data = CONFIG(data_path)
        elif format.lower() == "vasp/poscar":
            self.image_data = POSCAR(data_path)
        elif format.lower() == "lammps/dump":
            self.image_data = DUMP(data_path, atom_names)
        elif format.lower() == "lammps/lmp":
            self.image_data = LMP(data_path)
        else:
            assert train_ratio is not None, "train_ratio must be set when format is not config or poscar (inference)"
            self.data_name = os.path.basename(data_path)
            self.labels_path = os.path.join(datasets_path, self.data_name)
            if os.path.exists(datasets_path) is False:
                os.makedirs(datasets_path, exist_ok=True)
            if not os.path.exists(self.labels_path):
                os.makedirs(self.labels_path, exist_ok=True)
            if len(glob.glob(os.path.join(self.labels_path, train_data_path, "*.npy"))) > 0:
                print("Data %s has been processed!" % self.data_name)
                return
            if format.lower() == "pwmat/movement":
                self.image_data = MOVEMENT(data_path)
            elif format.lower() == "vasp/outcar":
                self.image_data = OUTCAR(data_path)
            elif format.lower() == "extxyz":
                pass
            elif format.lower() == "vasp/xml":
                pass
            elif format.lower() == 'cp2k/md':
                self.image_data = CP2KMD(data_path)
            elif format.lower() == 'cp2k/scf':
                self.image_data = CP2KSCF(data_path)
        self.lattice, self.position, self.energies, self.ei, self.forces, self.virials, self.atom_type, self.atom_types_image, self.image_nums = get_pw(self.image_data.get())

        if train_ratio is not None:  # inference 时不存数据
            self.train_ratio = train_ratio        
            self.split_and_save_data(seed, random, self.labels_path, train_data_path, valid_data_path, retain_raw)
    
    def split_and_save_data(self, seed, random, labels_path, train_path, val_path, retain_raw):
        if seed:
            np.random.seed(seed)
        indices = np.arange(self.image_nums)    # 0, 1, 2, ..., image_nums-1
        if random:
            np.random.shuffle(indices)              # shuffle the indices
        train_size = ceil(self.image_nums * self.train_ratio)
        train_indices = indices[:train_size]
        val_indices = indices[train_size:]
        # image_nums = [self.image_nums]
        atom_types_image = self.atom_types_image.reshape(1, -1)

        train_data = [self.lattice[train_indices], self.position[train_indices], self.energies[train_indices], 
                      self.forces[train_indices], atom_types_image, self.atom_type,
                      self.ei[train_indices]]
        val_data = [self.lattice[val_indices], self.position[val_indices], self.energies[val_indices], 
                    self.forces[val_indices], atom_types_image, self.atom_type,
                    self.ei[val_indices]]

        if len(self.virials) != 0:
            train_data.append(self.virials[train_indices])
            val_data.append(self.virials[val_indices])
        else:
            train_data.append([])
            val_data.append([])

        if self.train_ratio == 1.0 or len(val_indices) == 0:
            labels_path = os.path.join(labels_path, train_path)
            if not os.path.exists(labels_path):
                os.makedirs(labels_path)
            if retain_raw:
                save_to_raw(train_data, train_path)
            save_to_npy(train_data, labels_path)
        else:
            train_path = os.path.join(labels_path, train_path) 
            val_path = os.path.join(labels_path, val_path)
            if not os.path.exists(train_path):
                os.makedirs(train_path)
            if not os.path.exists(val_path):
                os.makedirs(val_path)
            if retain_raw:
                save_to_raw(train_data, train_path)
                save_to_raw(val_data, val_path)
            save_to_npy(train_data, train_path)
            save_to_npy(val_data, val_path)
                
                
class Configs(object):
    @staticmethod
    def read(format: str, data_path: str, pbc = None, atom_names = None, index = ':', **kwargs):
        """ Read the data from the input file. 
            index: int, slice or str
            The last configuration will be returned by default.  Examples:

            * ``index=0``: first configuration
            * ``index=-2``: second to last
            * ``index=':'`` or ``index=slice(None)``: all
            * ``index='-3:'`` or ``index=slice(-3, None)``: three last
            * ``index='::2'`` or ``index=slice(0, None, 2)``: even
            * ``index='1::2'`` or ``index=slice(1, None, 2)``: odd

            kwargs: dict
            Additional keyword arguments for reading the input file.
            retain_raw: bool, optional. Whether to retain raw data. Default is False.
            unit: str, optional. for lammps, the unit of the input file. Default is 'metal'.
            style: str, optional. for lammps, the style of the input file. Default is 'atomic'.
            sort_by_id: bool, optional. for lammps, whether to sort the atoms by id. Default is True.

        """
        if isinstance(index, str):
            try:
                index = string2index(index)
            except ValueError:
                pass

        if format.lower() == "pwmat/config":
            image = CONFIG(data_path, pbc).image_list[0]
        elif format.lower() == "vasp/poscar":
            image = POSCAR(data_path, pbc).image_list[0]
        elif format.lower() == "lammps/dump":
            assert atom_names is not None, "atom_names must be set when format is dump"
            image = DUMP(data_path, atom_names).image_list[index]
        elif format.lower() == "lammps/lmp":
            image = LMP(data_path, atom_names, **kwargs).image_list[0]
        elif format.lower() == "pwmat/movement":
            image = MOVEMENT(data_path).image_list[index]
        elif format.lower() == "vasp/outcar":
            image = OUTCAR(data_path).image_list[index]
        elif format.lower() == "extxyz":
            image = None
        elif format.lower() == "vasp/xml":
            image = None
        elif format.lower() == 'cp2k/md':
            image = CP2KMD(data_path).image_list[index]
        elif format.lower() == 'cp2k/scf':
            image = CP2KSCF(data_path).image_list[0]
        else:
            raise Exception("Error! The format of the input file is not supported!")
        return image
    
    @staticmethod
    def to(image, output_path, file_name = None, file_format = None, direct = True, sort = False, wrap = False, train_ratio = 0.8, **kwargs):
        """
        Write atoms object to a new file.

        Note: Set sort to False for CP2K, because data from CP2K is already sorted!!!. It will result in a wrong order if sort again.

        Args:
        output_path (str): The path to save the file.
        file_name (str): Save name of the configuration file.
        file_format (str): The format of the file. Default is None.
        direct (bool): The coordinates of the atoms are in fractional coordinates or cartesian coordinates. (0 0 0) -> (1 1 1)
        sort (bool): Whether to sort the atoms by atomic number. Default is False.
        wrap (bool): hether to wrap the atoms into the simulation box (for pbc). Default is False.
        train_ratio (float): The ratio of the training dataset. Default is 0.8.

        Kwargs:
        Additional keyword arguments for 'pwmlff/npy' format.

        train_data_path (str): Save path of the training dataset. Default is "train". ("./output_path/train")
        valid_data_path (str): Save path of the validation dataset. Default is "valid". ("./output_path/valid")
        random (bool): Whether to shuffle the raw data and then split the data into the training and validation datasets. Default is True.
        seed (int): Random seed. Default is 2024.
        retain_raw (bool): Whether to retain the raw data. Default is False.

        """
        assert file_format is not None, "output file format is not specified"
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        if file_format.lower() == 'pwmat/config':
            write_config(output_path, file_name, image, sort=sort, wrap=wrap)
        elif file_format.lower() == 'vasp/poscar':
            write_vasp(output_path, file_name, image, direct=direct, sort=sort, wrap=wrap)
        elif file_format.lower() == "lammps/lmp":
            write_lammps(output_path, file_name, image, sort=sort, wrap=wrap)
        elif file_format.lower() == "pwmat/movement":
            save_to_movement(image, output_path, file_name)
        elif file_format.lower() == "extxyz":
            save_to_extxyz(image, output_path, file_name)
        elif file_format.lower() == "pwmlff/npy":
            save_to_dataset(image, datasets_path = output_path, train_ratio = train_ratio, data_name = file_name, **kwargs)
        else:
            raise RuntimeError('Unknown file format')

class SUPERCELL(object):
    def __init__(self, config: Image, output_path = "./", output_file = "supercell", 
                 supercell_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 
                 direct = True, sort = True, pbc = None, save_format: str = None) -> None:
        """
        Args:
            config (Image): Image object.
            output_path (str): Path to the output directory.
            output_file (str): Name of the output file.
            supercell_matrix (list): supercell matrix (3x3)
            direct (bool): Whether to write the positions in direct coordinates.
            sort (bool): Whether to sort the atoms by atomic number.
            pbc (list): three bool, Periodic boundary conditions flags.  Examples: [True, True, False] or [1, 1, 0]. True (1) means periodic, False (0) means non-periodic.
            save_format (str): Format of the output file.
        """

        self.output_path = os.path.abspath(output_path)
        self.output_file = output_file
        self.supercell_matrix = supercell_matrix   
        # Make a supercell     
        supercell = make_supercell(config, self.supercell_matrix, pbc)
        # Write out the structure
        supercell.to(file_path = self.output_path,
                     file_name = self.output_file,
                     file_format = save_format,
                     direct = direct,
                     sort = sort)
        # from build.write_struc import write_config, write_vasp
        # if format.lower() == "config":
        #     write_config(self.output_path, self.output_file, supercell, direct=direct, sort=sort)
        # elif format.lower() == "poscar":
        #     write_vasp(self.output_path, self.output_file, supercell, direct=direct, sort=sort)

class PerturbStructure(object):
    def __init__(self, perturbed_file: Image, pert_num = 50, cell_pert_fraction = 0.03, atom_pert_distance = 0.01,
                 output_path = "./", direct = True, sort = None, pbc = None, save_format: str = None) -> None:
        """
        Perturb the structure.

        Args:
            perturbed_file (Image): Image object.
            pert_num (int): Number of perturbed structures.
            cell_pert_fraction (float): Fraction of the cell perturbation.
            atom_pert_distance (float): Distance of the atom perturbation.
            output_path (str): Path to the output directory.
            direct (bool): Whether to write the positions in direct coordinates.
            sort (bool): Whether to sort the atoms by atomic number.
            pbc (list): three bool, Periodic boundary conditions flags.  Examples: [True, True, False] or [1, 1, 0]. True (1) means periodic, False (0) means non-periodic.
            save_format (str): Format of the output file.

        Returns:
            None
        """

        self.pert_num = pert_num
        self.cell_pert_fraction = cell_pert_fraction
        self.atom_pert_distance = atom_pert_distance
        self.output_path = os.path.abspath(output_path)
        self.perturbed_structs = BatchPerturbStructure.batch_perturb(perturbed_file, self.pert_num, self.cell_pert_fraction, self.atom_pert_distance)
        for tmp_perturbed_idx, tmp_pertubed_struct in enumerate(self.perturbed_structs):
            tmp_pertubed_struct.to(file_path = self.output_path,
                                   file_name = "{0}_pertubed.{1}".format(tmp_perturbed_idx, save_format.lower()),
                                   file_format = save_format,
                                   direct = direct,
                                   sort = sort) 
        
class ScaleCell(object):
    def __init__(self, scaled_file: Image, scale_factor = 1.0, output_path = "./", direct = True, sort = None, pbc = None, save_format: str = None) -> None:
        """
        Scale the lattice.

        Args:
            scaled_file (Image): Image object.
            scale_factor (float): Scale factor.
            output_path (str): Path to the output directory.
            direct (bool): Whether to write the positions in direct coordinates.
            sort (bool): Whether to sort the atoms by atomic number.
            pbc (list): three bool, Periodic boundary conditions flags.  Examples: [True, True, False] or [1, 1, 0]. True (1) means periodic, False (0) means non-periodic.
            save_format (str): Format of the output file.

        Returns:
            None
        """
        
        self.scale_factor = scale_factor
        self.output_path = os.path.abspath(output_path)
        self.scaled_struct = BatchScaleCell.batch_scale(scaled_file, self.scale_factor)
        self.scaled_struct.to(file_path = self.output_path,
                              file_name = "scaled.{0}".format(save_format.lower()),
                              file_format = save_format,
                              direct = direct,
                              sort = sort)

def string2index(string: str) -> Union[int, slice, str]:
    """Convert index string to either int or slice"""
    if ':' not in string:
        # may contain database accessor
        try:
            return int(string)
        except ValueError:
            return string
    i: List[Optional[int]] = []
    for s in string.split(':'):
        if s == '':
            i.append(None)
        else:
            i.append(int(s))
    i += (3 - len(i)) * [None]
    return slice(*i)

if __name__ == "__main__":
    import argparse
    SUPERCELL_MATRIX = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
    data_file = "/data/home/hfhuang/2_MLFF/2-DP/19-json-version/8-Si2/atom.config"
    # data_file = "/data/home/hfhuang/9_cp2k/1-SiO2/cp2k.out"
    # data_file = "/data/home/hfhuang/software/mlff/Si/Si64-vasprun.xml"
    # data_file = "/data/home/hfhuang/2_MLFF/3-outcar2movement/0/OUTCARC3N4"
    output_path = "/data/home/hfhuang/2_MLFF/2-DP/19-json-version/8-Si2/mlff/"
    output_file = "supercell.config"
    format = "config"
    pbc = [1, 1, 1]
    # config = Configs.read(format, data_file, atom_names=["Si"], index=-1)   # read dump
    config = Configs.read(format, data_file)   
    # SUPERCELL(config, output_path, output_file, SUPERCELL_MATRIX, pbc=pbc, save_format=format)
    PerturbStructure(config, output_path = "/data/home/hfhuang/Si64", save_format=format)
    # ScaleCell(config, scale_factor = 1.1, output_path = "/data/home/hfhuang/Si64", save_format=format)
    config.to(file_path = output_path,
                     file_name = output_file,
                     file_format = 'config',
                     direct = True,
                     sort = False)
    # OUTCAR2MOVEMENT(data_path, output_path, output_file)
    parser = argparse.ArgumentParser(description='Convert and build structures.')
    parser.add_argument('--format', type=str, required=False, help='Format of the input file', default="outcar")
    parser.add_argument('--save_format', type=str, required=False, help='Format of the output file', default="config")
    parser.add_argument('--outcar_file', type=str, required=False, help='Path to the OUTCAR file')
    parser.add_argument('--movement_file', type=str, required=False, help='Path to the MOVEMENT file')
    parser.add_argument('--output_path', type=str, required=False, help='Path to the output directory', default="./")
    parser.add_argument('--output_file', type=str, required=False, help='Name of the output file', default="MOVEMENT")
    parser.add_argument('--supercell_matrix', type=list, required=False, help='Supercell matrix', default=[[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    parser.add_argument('--pbc', type=list, required=False, help='Periodic boundary conditions flags', default=[1, 1, 1])
    parser.add_argument('--direct', type=bool, required=False, help='Whether to write the positions in direct (frac) coordinates', default=True)
    parser.add_argument('--sort', type=bool, required=False, help='Whether to sort the atoms by atomic number', default=True)
    parser.add_argument('--pert_num', type=int, required=False, help='Number of perturbed structures', default=50)
    parser.add_argument('--cell_pert_fraction', type=float, required=False, help='Fraction of the cell perturbation', default=0.03)
    parser.add_argument('--atom_pert_distance', type=float, required=False, help='Distance of the atom perturbation', default=0.01)
    parser.add_argument('--retain_raw', type=bool, required=False, help='Whether to retain raw data', default=False)
    parser.add_argument('--train_ratio', type=float, required=False, help='Ratio of training data', default=0.8)
    parser.add_argument('--random', type=bool, required=False, help='Whether to shuffle the data', default=True)
    parser.add_argument('--scale_factor', type=float, required=False, help='Scale factor of the lattice', default=1.0)
    parser.add_argument('--seed', type=int, required=False, help='Random seed', default=2024)
    parser.add_argument('--index', type=Union[int, slice, str], required=False, help='Index of the configuration', default=-1)
    parser.add_argument('--atom_names', type=list, required=False, help='Names of the atoms', default=["H"])
    parser.add_argument('--style', type=str, required=False, help='Style of the lammps input file', default="atomic")

    
    args = parser.parse_args()
    
