
import os 
import zipfile
import gdown
from src.ccnClassifier import logger
from src.ccnClassifier.utils.common import get_size
from src.ccnClassifier.entity.config_entity import (Dataingestionconfig)

class DataIngestion:
    def __init__(self, config: Dataingestionconfig):
        self.config=config
        
    def download_file(self)->str:
        """fetch data from url

        Returns:
            str:size 
        """
        try:
            dataset_url=self.config.source_url
            zip_download_dir=self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True) 
            logger.info(f"downloading data from {dataset_url} into file {zip_download_dir}")
            
            file_id=dataset_url.split('/')[-2]
            prefix="https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id,zip_download_dir)
            
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
        
        except Exception as e:
            raise e
    
    def exract_zip_file(self):
        """ 
        zip_file_path: str
        extracts the zip file into directory
        function returns None
        """
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_file:
            zip_file.extractall(unzip_path)