import yaml
from networksecurity.exception.exception import NetworkSecurityException
import sys,os
from networksecurity.logging.logger import logging
import numpy as np
# import dill
import pickle

def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns its contents as a dictionary.

    Args:
        file_path (str): The path to the YAML file.
    Returns:
        dict: The contents of the YAML file as a dictionary.        
    Raises:
        NetworkSecurityException: If there is an error reading the YAML file.       
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def write_yaml_file(file_path:str,content: object,replace: bool=True)->None:
    """
    Writes content to a YAML file.
    Args:
        file_path (str): The path to the YAML file.
        content (object): The content to be written to the YAML file.
        replace (bool): Whether to replace the existing file if it exists.
    Returns: None
    Raises:
        NetworkSecurityException: If there is an error writing to the YAML file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as yaml_file:
                yaml.dump(content, yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
        