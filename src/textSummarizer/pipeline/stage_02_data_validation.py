from textSummarizer.logging import logger
from textSummarizer.components.data_validation import DataValiadtion
from textSummarizer.config.configuration import ConfigurationManager


class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation=DataValiadtion(data_validation_config)
        data_validation.validate_all_files_exist()


