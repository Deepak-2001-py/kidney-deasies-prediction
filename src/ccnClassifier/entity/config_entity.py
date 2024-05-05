from dataclasses import dataclass
from pathlib import Path 
@dataclass(frozen=True)
class Dataingestionconfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass    
class Preparebasemodelconfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_include_top: float
    params_weights: str
    params_classes: int
    params_learning_rate: float
    

@dataclass
class Trainingconfig:
    root_dir: Path
    trained_model_path:Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch: int
    params_is_augmentation: bool
    params_image_size: list
    
@dataclass(frozen=True) 
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params:dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int
