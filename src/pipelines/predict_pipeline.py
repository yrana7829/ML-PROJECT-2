import sys
import os
from src.exception import CustomException
from src.logger import logging
from utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    # Define the prediction function
    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")

            # Print information about the features
            print("Features:")
            print(features)

            # Apply the preprocessor on the data before predictions
            print("Preprocessor:")
            print(preprocessor)
            preprocessed_data = preprocessor.transform(features)
            print("Preprocessed Data:")
            print(preprocessed_data)

            prediction = model.predict(preprocessed_data)
            return prediction

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, age, sex, bmi, children, smoker, region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region

    def get_data_as_df(self):
        try:
            # Create a dictionary
            custom_data_input_dict = {
                "age": [self.age],
                "sex": [self.sex],
                "bmi": [self.bmi],
                "children": [self.children],
                "smoker": [self.smoker],
                "region": [self.region],
            }

            # Convert it to a DataFrame
            df = pd.DataFrame(custom_data_input_dict)

            cat_columns = df.select_dtypes(include="object").columns
            num_columns = df.select_dtypes(exclude="object").columns

            # Replace missing values in categorical columns
            for c in cat_columns:
                most_frequent_value = df[c].mode()[0]
                df[c].fillna(most_frequent_value, inplace=True)

            # Replace missing values with the median value
            for c in num_columns:
                most_frequent_value = df[c].mode()[0]
                df.fillna(value=df.median(), inplace=True)

            return df

        except Exception as e:
            raise CustomException(e, sys)
