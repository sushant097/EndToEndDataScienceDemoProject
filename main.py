from src.datascienceDemo import logger
from src.datascienceDemo.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    logger.exception(e)
    raise e



