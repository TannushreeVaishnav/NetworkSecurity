from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig,DataTransformationConfig

import sys
if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiated data ingestion")
        dataingestionsrtifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed and artifact")
        print(dataingestionsrtifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionsrtifact,data_validation_config)
        logging.info("Initiated data validation")
        data_validation_artifact=data_validation.initiate_data_vallidation()
        logging.info("Data validation completed and artifact")
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info("Initiated data transformation")
        
        data_transformation = DataTransformation(
                                data_validation_artifact,
                                data_transformation_config
                )
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data transformation completed and artifact")
    except Exception as e:
        raise NetworkSecurityException(e,sys)

