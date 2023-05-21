import os
import sys
import dill
from src.exception import CustomException
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV


# A function to save any object in the project at a given file path
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

    # A function to load object in the project at a given file path


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            loaded_object = dill.load(file_obj)
            return loaded_object

    except Exception as e:
        raise CustomException(e, sys)


# A function to evaluate the models


def model_evaluation(X_train, Y_train, X_test, Y_test, models, param):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, Y_train)
            model.set_params(**gs.best_params_)

            model.fit(X_train, Y_train)
            Y_pred_train = model.predict(X_train)
            Y_pred_test = model.predict(X_test)

            train_r2_score = r2_score(Y_train, Y_pred_train)
            test_r2_score = r2_score(Y_test, Y_pred_test)

            report[list(models.keys())[i]] = test_r2_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
