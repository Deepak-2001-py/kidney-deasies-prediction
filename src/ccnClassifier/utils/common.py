import os
from box.exceptions import BoxValueError
import yaml
from src.ccnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """read yaml file
    
    args:
    path_to_yaml(str): path like input
    
    raises:
    valueError : if yaml file is empty
    
    e:empty file
    
    retruns: Configbox
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml_file:{path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        return e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """create list  of directories

    Args:
        path_to_directories (list): list of path dirctories
        verbose (bool, optional): ignore if multipules dirs is to be created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")
            
            
            
@ensure_annotations
def save_json(path:Path,data:dict):
    """save json file

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path,"w") as f:
        json.dump(f)
        
    logger.info(f"json file saved at:{path}")
    
@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """load json data

    Args:
        path (path): path to json file

    Returns:
        ConfigBox:  data as class atteributes instead of dict
    """
    with open(path,"r") as f:
        content= json.load(f)
        
    logger.info(f"json file loaded sucessfully")
    
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:any, path:Path):
    """save file in binary

    Args:
        data (any): data to be saved as binary
        path (Path): path to be saved binary file
        
    """
    
    joblib.dump(data,path)
    logger.info(f"binary saved at :{path}")
    
@ensure_annotations
def load_bin(path:Path)->Any:
    """load binary data
    

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in file
    """
    data=joblib.load(path)
    logger.info(f"binary data loaded from :{path}")
    return data

@ensure_annotations
def get_size(path:Path)->str:
    """get size in kb

    Args:
        path (Path): path of the file

    Returns:
        path: size in kb
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} kb"

@ensure_annotations
def decodeImage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,"wb") as f:
        f.write(imgdata)
        f.close()
        
@ensure_annotations
def encodeImage(croppediamgepath):
    with open(croppediamgepath,"rb") as f:
        return base64.b64encode(f.read())