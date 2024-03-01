#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import numpy as np
import pandas as pd
import yaml
from pathlib import Path


def get_material_files_dir(subdir: str) -> Path:
    """
    Returns the directory path for material files.

    Parameters:
    - subdir: Subdirectory within the material files directory.

    Returns:
    - A Path object pointing to the specified subdirectory.
    """
    return Path(__file__).parent / 'material_files' / subdir


def list_material_files():
    """
    Prints the list of SellMeier and measurement material files.
    """
    sellmeier_dir = get_material_files_dir('sellmeier')
    measurement_dir = get_material_files_dir('measurements')

    sellmeier_files = [f.stem for f in sellmeier_dir.glob('*.yaml')]
    measurement_files = [f.stem for f in measurement_dir.glob('*.yml')]

    print('SellMeier files:')
    print('\n'.join(f'\t{s}' for s in sellmeier_files))

    print('Measurement files:')
    print('\n'.join(f'\t{m}' for m in measurement_files))


def load_yaml_file(file_path: Path) -> dict:
    """
    Loads a YAML file into a dictionary.

    Parameters:
    - file_path: Path to the YAML file.

    Returns:
    - A dictionary containing the YAML file content.
    """
    if not file_path.exists():
        available = '\n'.join(f.stem for f in file_path.parent.glob('*.yaml'))
        raise FileNotFoundError(f'File not found: \n{available}')
    return yaml.safe_load(file_path.read_text())


def dispersion_formula(parameters: dict, wavelength: float) -> float:
    """
    Calculates the refractive index using the Sellmeier dispersion formula.

    Parameters:
    - parameters: Sellmeier parameters.
    - wavelength: Wavelength in meters.

    Returns:
    - The calculated refractive index.
    """
    wavelength_um = wavelength * 1e6  # Convert wavelength to micrometers
    B = [parameters.get(f'B_{i}') for i in range(1, 4)]
    C = [parameters.get(f'C_{i}')**2 if parameters['C_squared'] else parameters.get(f'C_{i}') for i in range(1, 4)]
    index_squared = 1 + sum(B[i] * wavelength_um**2 / (wavelength_um**2 - C[i]) for i in range(3))
    return np.sqrt(index_squared)


def get_material_index(material_name: str, wavelength: float, subdir: str = 'sellmeier') -> float:
    """
    Gets the material refractive index using the dispersion formula or measurement data.

    Parameters:
    - material_name: The material name.
    - wavelength: Wavelength in meters.
    - subdir: Subdirectory name ('sellmeier' or 'measurements').

    Returns:
    - The material refractive index.
    """
    file_path = get_material_files_dir(subdir) / f'{material_name}.yaml'
    parameters = load_yaml_file(file_path)
    if subdir == 'sellmeier':
        return dispersion_formula(parameters['sellmeier'], wavelength)
    else:
        # Handle measurement data logic here if needed.
        pass


def get_silica_index(wavelength: float, subdir: str = 'sellmeier') -> float:
    return get_material_index(
        material_name='silica',
        wavelength=wavelength,
        subdir=subdir
    )


def load_material_measurements(material_name: str) -> pd.DataFrame:
    """
    Loads material measurement data into a pandas DataFrame.

    Parameters:
    - material_name: The name of the material.

    Returns:
    - A pandas DataFrame containing the material measurement data.
    """
    material_data = get_material_index(material_name, 0, 'measurements')  # Example use, adjust as necessary
    # Assuming material_data contains CSV-like string data; adjust loading logic as necessary
    return pd.read_csv(io.StringIO(material_data), sep=' ')

# Adjustments may be necessary for `load_material_measurements` and handling of measurement data.


# -
