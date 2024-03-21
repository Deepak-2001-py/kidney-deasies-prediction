
from src.ccnClassifier.config.configuration import ConfigurationManager
from src.ccnClassifier.components.data_ingestion import DataIngestion
from src.ccnClassifier import logger


 


class DataIngestiontrainingpipepline:
    def __init__(self):
        pass

    def main(self):
        
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.exract_zip_file()
    

STAGE_NAME="Data ingestion"
if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataIngestiontrainingpipepline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<")
        
    except Exception as e:
        logger.exception(e) 