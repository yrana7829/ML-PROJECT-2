from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    object = DataIngestion()
    train_data, test_data = object.initiate_data_ingestion()

    transformer = DataTransformation()
    (
        train_array,
        test_array,
    ) = transformer.initiate_data_transformation(train_data, test_data)

    model = ModelTrainer()
    r2_score = model.initiate_model_training(train_array, test_array)
