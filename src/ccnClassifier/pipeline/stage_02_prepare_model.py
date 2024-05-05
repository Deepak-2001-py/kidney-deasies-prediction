
from ccnClassifier.config.configuration import ConfigurationManager
from ccnClassifier.components.Preparebasedmodel import Preparebasedmodel
from ccnClassifier import logger



class DataPreparebasemodelpipepline:
    def __init__(self):
        pass

    def main(self):
        
        config=ConfigurationManager()
        data_prepare_base_model_config=config.get_data_prepare_base_model_config()
        prepare_base_model=Preparebasedmodel(config=data_prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
    
print("*************************")
STAGE_NAME="Prepare Base Model"
if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataPreparebasemodelpipepline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<")
        
    except Exception as e:
        logger.exception(e) 