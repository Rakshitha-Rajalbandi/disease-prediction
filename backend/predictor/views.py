# from django.shortcuts import render

# # Create your views here.

# from django.http import JsonResponse
# import pickle
# import pandas as pd

# # Load the trained model and label encoder
# with open('backend/predictor/naive_bayes_model.pkl', 'rb') as f:
#     model = pickle.load(f)

# with open('backend/predictor/label_encoder.pkl', 'rb') as f:
#     le = pickle.load(f)

# def predict_disease(request):
#     # Example: symptoms passed as query parameters like ?fever=Yes&cough=No
#     symptoms = request.GET.dict()
    
#     # Convert to DataFrame
#     df = pd.DataFrame([symptoms])
    
#     # Ensure all symptom columns exist and fill missing with 'No'
#     for col in model.feature_names_in_:
#         if col not in df.columns:
#             df[col] = 'No'
    
#     # Predict
#     prediction_encoded = model.predict(df)
#     prediction = le.inverse_transform(prediction_encoded)
    
#     return JsonResponse({'predicted_disease': prediction[0]})

import os, json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import joblib
import pandas as pd
from django.conf import settings

# Paths
NB_MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor/naive_bayes_model.pkl')
LE_PATH = os.path.join(settings.BASE_DIR, 'predictor/label_encoder.pkl')

# Load model and label encoder once
nb_model = joblib.load(NB_MODEL_PATH)
le = joblib.load(LE_PATH)

# Use model's own feature names to avoid mismatch
all_symptoms = list(nb_model.feature_names_in_)

@csrf_exempt
def predict_disease(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"})

    try:
        data = json.loads(request.body)
        symptoms = data.get("symptoms")
        if not isinstance(symptoms, list):
            return JsonResponse({"error": "Symptoms must be a list"})

        # Create binary input in the correct order
        input_data = {s: 0 for s in all_symptoms}
        for s in symptoms:
            if s in input_data:
                input_data[s] = 1

        df_input = pd.DataFrame([input_data])

        # Predict
        pred_encoded = nb_model.predict(df_input)[0]
        pred_disease = le.inverse_transform([pred_encoded])[0]

        return JsonResponse({"disease": pred_disease})

    except Exception as e:
        return JsonResponse({"error": str(e)})

