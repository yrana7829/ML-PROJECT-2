from flask import Flask, request, render_template
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

# create the flask app
app = Flask(__name__)


# Define routes
@app.route("/")
def index():
    return render_template("index.html")


# Define the prediction page route
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("home.html")
    else:
        data = CustomData(
            age=request.form.get("age"),
            sex=request.form.get("sex"),
            bmi=request.form.get("bmi"),
            children=request.form.get("children"),
            smoker=request.form.get("smoker"),
            region=request.form.get("region"),
        )

        # convert it into df
        data_df = data.get_data_as_df()

        # initialize the prediction pipeline now
        print(data_df)
        print("Before making the Prediction")

        predict_pipeline = PredictPipeline()

        results = predict_pipeline.predict(data_df)
        print("after Prediction")
        print(results[0])
        return render_template("home.html", results=results[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
