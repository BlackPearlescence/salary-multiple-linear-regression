import joblib
import pandas as pd
from flask import Flask, jsonify, make_response, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

preprocessor = joblib.load("salary_preprocessor.joblib")
pipeline = joblib.load("salary_pipeline.joblib")

class HelloWorld(Resource):
    def get(self):
        return make_response({"message" : "Hello, World!"},200)
    
api.add_resource(HelloWorld, "/")

class SalaryPrediction(Resource):
    
    def post(self):
        input_data = request.get_json()
        input_frame = {
            "Age": [input_data["age"]],
            "Gender" : [input_data["gender"]],
            "Education Level" : [input_data["education_level"]],
            "Job Title": [input_data["job_title"]],
            "Years of Experience": [input_data["years_of_experience"]],
        }
        input_df = pd.DataFrame(input_frame)

        predicted_value = pipeline.predict(input_df)
        return make_response({
            "salary_prediction" : predicted_value.item()
        }, 200)
        
api.add_resource(SalaryPrediction, "/salary")
if __name__ == "__main__":
    app.run(debug=True)