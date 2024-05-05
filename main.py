from ccnClassifier import logger
from ccnClassifier.pipeline.stage_01_data_ingestion import (DataIngestiontrainingpipepline)
from ccnClassifier.pipeline.stage_02_prepare_model import (DataPreparebasemodelpipepline)
from ccnClassifier.pipeline.stage_03_training import (Trainingpipeline)
from ccnClassifier.pipeline.stage_04_evaluation import (Evaluationpipeline)


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
 
 
print("*************************")
STAGE_NAME="Traning Base Model"
if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj=Trainingpipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<")
        
    except Exception as e:
        logger.exception(e)        

print("*************************")
STAGE_NAME="Model Evaluation"
if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj=Evaluationpipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<")
        
    except Exception as e:
        logger.exception(e) 