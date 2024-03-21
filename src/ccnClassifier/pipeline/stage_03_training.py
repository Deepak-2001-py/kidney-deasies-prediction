from src.ccnClassifier.config.configuration import ConfigurationManager
from src.ccnClassifier.components.Trainng import Training
from src.ccnClassifier import logger


class Trainingpipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
    
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