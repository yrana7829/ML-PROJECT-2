from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":
    object = DataIngestion()
    train_data, test_data = object.initiate_data_ingestion()

    transformer = DataTransformation()
    (
        train_array,
        test_array,
    ) = transformer.initiate_data_transformation(train_data, test_data)
