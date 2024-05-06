from ccnClassifier.config.configuration import ConfigurationManager
from ccnClassifier.components.Evaluation import Evaluation
from ccnClassifier import logger


class Evaluationpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
        # evaluation.log_into_mlflow()
      
    
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