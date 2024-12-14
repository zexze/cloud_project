import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")


# route to display the home page
@app.route('/',methods=['GET']) 
def homePage():
    return render_template("home.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    prediction_text = None

    try:
        age = int(request.form['Age'])
        income = float(request.form['Income'])
        loan_amount = float(request.form['LoanAmount'])
        credit_score = int(request.form['CreditScore'])
        months_employed = int(request.form['MonthsEmployed'])
        num_credit_lines = int(request.form['NumCreditLines'])
        interest_rate = float(request.form['InterestRate'])
        loan_term = int(request.form['LoanTerm'])
        dti_ratio = float(request.form['DTIRatio'])
        education = request.form['Education']
        employment_type = request.form['EmploymentType']
        marital_status = request.form['MaritalStatus']
        loan_purpose = request.form['LoanPurpose']
        has_mortgage = int(request.form['HasMortgage']) #1 Yes, 0 No
        has_dependents = int(request.form['HasDependents']) #1 Yes, 0 No
        has_cosigner = int(request.form['HasCoSigner']) #1 Yes, 0 No

        # For categorical 
        education_mapping = {"Bachelor's": 0, 'High School': 1, "Master's": 2, 'PhD': 3}
        employment_mapping = {'Full-time': 0, 'Part-time': 1, 'Self-employed': 2,'Unemployed': 3}
        marital_mapping = {'Divorced': 0, 'Married': 1, 'Single': 2}
        loan_purpose_mapping = {'Auto': 0, 'Business': 1, 'Education': 2, 'Home': 3, 'Other': 4}

        # One-hot encoded 
        education_encoded = education_mapping[education]
        employment_encoded = employment_mapping[employment_type]
        marital_encoded = marital_mapping[marital_status]
        loan_purpose_encoded = loan_purpose_mapping[loan_purpose]
        
        # Can't change the order, must match with the X_train columns order 
        features = np.array([[age, income, loan_amount, credit_score, months_employed, 
                                  num_credit_lines, interest_rate, loan_term, dti_ratio,
                                  education_encoded, employment_encoded, marital_encoded, 
                                  has_mortgage, has_dependents, loan_purpose_encoded, has_cosigner]])

    
        # Predict Result 
        prediction = model.predict(features)[0]

        if prediction == 0:
            prediction_text = f"Predicted Loan Default: No."
        
        if prediction == 1:
            prediction_text = f"Predicted Loan Default: Yes."

        return render_template('home.html', prediction_text=prediction_text)
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
