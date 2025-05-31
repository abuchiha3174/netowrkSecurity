from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging
from networkSecurity.entity.config_entity import DataIngestionConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig
from networkSecurity.components.data_validation import (
    DataValidation,
    DataValidationConfig,
)


import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        data_ingestionConfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(data_ingestionConfig)

        logging.info("Initiate the data ingestion")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(
            data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config=data_validation_config,
        )
        logging.info("Initiate the data validation")
        validation_artifcat = data_validation.initiate_data_validation()
        print("Data validation artifact:", validation_artifcat)
        print("Data validation completed successfully")

    except Exception as e:
        raise NetworkSecurityException(e, sys)
