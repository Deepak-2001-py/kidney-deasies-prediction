from ccnClassifier.constants import *
from ccnClassifier.utils.common import read_yaml,create_directories
from ccnClassifier.entity.config_entity import (Dataingestionconfig,Preparebasemodelconfig,Trainingconfig,EvaluationConfig)
import os

class ConfigurationManager:
    def __init__(self,
    config_filepath= CONFIG_FILE_PATH,
    params_filepath = PARAMS_FILE_PATH):
        
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
        
        
    def get_data_ingestion_config(self)->Dataingestionconfig:
        config=self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config=Dataingestionconfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir= config.unzip_dir
            )
        
        return data_ingestion_config
        
            
    def get_data_prepare_base_model_config(self)->Preparebasemodelconfig:
        config=self.config.prepare_base_model
        params=self.params
        create_directories([config.root_dir])
      
        data_prepare_base_model_config=Preparebasemodelconfig(
            root_dir = config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path= config.updated_base_model_path,
            params_image_size=params.IMAGE_SIZE,
            params_include_top=params.INCLUDE_TOP,
            params_weights=params.WEIGHTS,
            params_classes=params.CLASSES,
            params_learning_rate=params.LEARNING_RATE
            )
        
        return data_prepare_base_model_config
    
    def get_training_config(self)->Trainingconfig:
        training=self.config.training
        training_data=self.config.data_ingestion
        params=self.params
        prepare_base_model_path=self.config.prepare_base_model
        create_directories(
            [Path(training.root_dir)]
        )
        
        training_config=Trainingconfig(
            root_dir = Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path= Path(prepare_base_model_path.updated_base_model_path),
            training_data=Path(os.path.join(training_data.unzip_dir,"kidney-ct-scan-image")),
            params_epochs=params.EPOCHES,
            params_batch=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
            
            )
        
        return training_config
    def get_evaluation_config(self)->EvaluationConfig:
        eval_config=EvaluationConfig(path_of_model="artifacts/training/model.h5",
                                    training_data="artifacts/data_ingestion/kidney-ct-scan-image",
                                    mlflow_uri="https://dagshub.com/deepakrajbhar363/kidney-deasies-prediction.mlflow",
                                    all_params=self.params,
                                    params_image_size=self.params.IMAGE_SIZE,
                                    params_batch_size=self.params.BATCH_SIZE
                                    )
        return eval_config
    