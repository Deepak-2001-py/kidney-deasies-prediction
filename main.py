from src.ccnClassifier import logger
from src.ccnClassifier.pipeline.stage_01_data_ingestion import (DataIngestiontrainingpipepline)
from src.ccnClassifier.pipeline.stage_02_prepare_model import (DataPreparebasemodelpipepline)

STAGE_NAME=" Data Ingestion Stage"
if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataIngestiontrainingpipepline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<")
        
    except Exception as e:
        logger.exception(e) 
print("*************************")
STAGE_NAME1="Prepare Base Model"
if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME1} started <<<<<<")
        obj= DataPreparebasemodelpipepline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME1} completed <<<<<<")
        
    except Exception as e:
        logger.exception(e) 