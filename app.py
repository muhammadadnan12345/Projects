from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained Linear Regression model
model_path = r'C:\Users\ma578\OneDrive\Documents\Motive\DataSets\IPHONE\project 2\best_lr_model.joblib'
lr_model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve form data
        area = float(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        stories = int(request.form['stories'])
        mainroad = 1 if request.form['mainroad'] == 'Yes' else 0
        guestroom = 1 if request.form['guestroom'] == 'Yes' else 0
        basement = 1 if request.form['basement'] == 'Yes' else 0
        hotwaterheating = 1 if request.form['hotwaterheating'] == 'Yes' else 0
        airconditioning = 1 if request.form['airconditioning'] == 'Yes' else 0
        parking = int(request.form['parking'])
        prefarea = 1 if request.form['prefarea'] == 'Yes' else 0
        furnishingstatus_semi_furnished = 1 if request.form['furnishingstatus'] == 'Semi-Furnished' else 0
        furnishingstatus_unfurnished = 1 if request.form['furnishingstatus'] == 'Unfurnished' else 0
        area_per_story = area / stories

        # Input data for prediction
        input_data = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating,
                                airconditioning, parking, prefarea, furnishingstatus_semi_furnished, furnishingstatus_unfurnished, area_per_story]])

        # Predict price
        predicted_price = lr_model.predict(input_data)[0]

        return render_template('index.html', prediction=f'Predicted Price: ₹ {predicted_price:,.2f}')
    
    except Exception as e:
        return render_template('index.html', error=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
