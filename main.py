from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging
from networkSecurity.entity.config_entity import DataIngestionConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig
from networkSecurity.entity.config_entity import DataTransformationConfig
from networkSecurity.components.data_validation import (
    DataValidation,
    DataValidationConfig,
)

from networkSecurity.components.data_transformation import DataTransformation
from networkSecurity.entity.config_entity import ModelTrainerConfig
from networkSecurity.components.model_trainer import ModelTrainer


import sys

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestionConfig = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestionConfig)

        logging.info("Initiate the data ingestion")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)

        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(
            data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config=data_validation_config,
        )
        logging.info("Initiate the data validation")
        validation_artifcat = data_validation.initiate_data_validation()
        print("Data validation artifact:", validation_artifcat)
        print("Data validation completed successfully")

        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        logging.info("data Transformation started")
        data_transformation = DataTransformation(
            validation_artifcat, data_transformation_config
        )
        data_transformation_artifact = (
            data_transformation.initiate_data_transformation()
        )
        print(data_transformation_artifact)
        logging.info("data Transformation completed")

        logging.info("Model Training started")
        model_trainer_config = ModelTrainerConfig(training_pipeline_config)
        model_trainer = ModelTrainer(
            model_trainer_config=model_trainer_config,
            data_transformation_artifact=data_transformation_artifact,
        )
        model_trainer_artifact = model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")

    except Exception as e:
        raise NetworkSecurityException(e, sys)
