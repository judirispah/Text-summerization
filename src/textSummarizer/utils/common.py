import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
     """reads yaml file and returns
    
    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
     try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            #PyYAML, the contents of a YAML file are often converted into a dictionary 
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        # python-box library that allows dot notation access to dictionary items.
     except BoxValueError:
        #Exception specific to the python-box library, raised when an operation cannot be performed due to invalid values.
        raise ValueError("yaml file is empty")
     except Exception as e:
        raise e
     

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            #verbose: A boolean parameter that, when set to True, enables logging of directory creation messages.
            logger.info(f"created directory at: {path}")     
    
