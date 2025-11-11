# import os, json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import joblib
# import pandas as pd
# from django.conf import settings
# import requests

# # Toggle mock advice for testing
# use_mock = True  # ✅ Set to False when you're ready to use real RapidAPI

# # RapidAPI setup
# RAPIDAPI_URL = "https://ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com/chat?noqueue=1"
# RAPIDAPI_KEY = "your-new-api-key-here"
# RAPIDAPI_HOST = "ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com"

# def get_rapidapi_advice(message, specialization="general", language="en"):
#     headers = {
#         "Content-Type": "application/json",
#         "x-rapidapi-key": RAPIDAPI_KEY,
#         "x-rapidapi-host": RAPIDAPI_HOST
#     }
#     payload = {
#         "message": message,
#         "specialization": specialization,
#         "language": language
#     }

#     try:
#         response = requests.post(RAPIDAPI_URL, json=payload, headers=headers)
#         result = response.json()
#         return result.get("message", "No advice available.")
#     except Exception as e:
#         return f"Error fetching advice: {str(e)}"

# # Load model and encoder
# NB_MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor/naive_bayes_model.pkl')
# LE_PATH = os.path.join(settings.BASE_DIR, 'predictor/label_encoder.pkl')

# nb_model = joblib.load(NB_MODEL_PATH)
# le = joblib.load(LE_PATH)
# all_symptoms = list(nb_model.feature_names_in_)

# @csrf_exempt
# def predict_disease(request):
#     if request.method != "POST":
#         return JsonResponse({"error": "POST request required"})

#     try:
#         data = json.loads(request.body)
#         symptoms = data.get("symptoms")
#         specialization = data.get("specialization", "general")
#         language = data.get("language", "en")
#         include_advice = data.get("include_advice", False)

#         if not isinstance(symptoms, list):
#             return JsonResponse({"error": "Symptoms must be a list"})

#         # Prepare input for prediction
#         input_data = {s: 0 for s in all_symptoms}
#         for s in symptoms:
#             if s in input_data:
#                 input_data[s] = 1
#         df_input = pd.DataFrame([input_data])

#         # Predict disease
#         pred_encoded = nb_model.predict(df_input)[0]
#         pred_disease = le.inverse_transform([pred_encoded])[0]

#         # Get advice if requested
#         if include_advice:
#             if use_mock:
#                 advice_text = "🧪 Mock advice: Stay hydrated, rest well, and consult a doctor if symptoms persist."
#             else:
#                 rapidapi_message = f"I am experiencing {', '.join(symptoms).replace('_', ' ')}. What could be the cause and what should I do?"
#                 advice_text = get_rapidapi_advice(rapidapi_message, specialization, language)
#         else:
#             advice_text = "Advice not requested."

#         return JsonResponse({
#             "naive_bayes_prediction": pred_disease,
#             "medical_advice": advice_text
#         })

#     except Exception as e:
#         return JsonResponse({"error": str(e)})



# import os
# import json
# import joblib
# import pandas as pd
# from django.conf import settings
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import requests


# reports_cache = []


# # Toggle mock advice for testing
# use_mock = True  # Set False to enable real RapidAPI advice

# # RapidAPI setup
# RAPIDAPI_URL = "https://ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com/chat?noqueue=1"
# RAPIDAPI_KEY = "your-new-api-key-here"
# RAPIDAPI_HOST = "ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com"

# def get_rapidapi_advice(message, specialization="general", language="en"):
#     headers = {
#         "Content-Type": "application/json",
#         "x-rapidapi-key": RAPIDAPI_KEY,
#         "x-rapidapi-host": RAPIDAPI_HOST
#     }
#     payload = {
#         "message": message,
#         "specialization": specialization,
#         "language": language
#     }
#     try:
#         response = requests.post(RAPIDAPI_URL, json=payload, headers=headers)
#         result = response.json()
#         return result.get("message", "No advice available.")
#     except Exception as e:
#         return f"Error fetching advice: {str(e)}"

# # Load model and encoder
# NB_MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor/naive_bayes_model.pkl')
# LE_PATH = os.path.join(settings.BASE_DIR, 'predictor/label_encoder.pkl')

# nb_model = joblib.load(NB_MODEL_PATH)
# le = joblib.load(LE_PATH)
# all_symptoms = list(nb_model.feature_names_in_)

# @csrf_exempt
# def predict_disease(request):
#     if request.method != "POST":
#         return JsonResponse({"error": "POST request required"})

#     try:
#         data = json.loads(request.body)
#         symptoms = data.get("symptoms")
#         specialization = data.get("specialization", "general")
#         language = data.get("language", "en")
#         include_advice = data.get("include_advice", False)

#         if not isinstance(symptoms, list):
#             return JsonResponse({"error": "Symptoms must be a list"})

#         input_data = {s: 0 for s in all_symptoms}
#         for s in symptoms:
#             if s in input_data:
#                 input_data[s] = 1
#         df_input = pd.DataFrame([input_data])

#         pred_encoded = nb_model.predict(df_input)[0]
#         pred_disease = le.inverse_transform([pred_encoded])[0]

#         if include_advice:
#             if use_mock:
#                 advice_text = "🧪 Mock advice: Stay hydrated, rest well, and consult a doctor if symptoms persist."
#             else:
#                 rapidapi_message = f"I am experiencing {', '.join(symptoms).replace('_', ' ')}. What could be the cause and what should I do?"
#                 advice_text = get_rapidapi_advice(rapidapi_message, specialization, language)
#         else:
#             advice_text = "Advice not requested."

#         return JsonResponse({
#             "naive_bayes_prediction": pred_disease,
#             "medical_advice": advice_text
#         })

#     except Exception as e:
#         return JsonResponse({"error": str(e)})

# def reports_list(request):
#     # Example static reports data - replace with your DB-backed data retrieval later
#     reports = [
#         {
#             "date": "2025-11-09T22:00:00Z",
#             "disease": "Diabetes",
#             "symptoms": ["Increased thirst", "Frequent urination"],
#             "medicines": ["Metformin", "Insulin"],
#             "notes": "Monitor blood sugar regularly and follow prescribed medication."
#         },
#         {
#             "date": "2025-11-07T18:30:00Z",
#             "disease": "Common Cold",
#             "symptoms": ["Sneezing", "Runny nose"],
#             "medicines": ["Decongestants", "Pain relievers"],
#             "notes": "Recommended rest and hydration."
#         }
#     ]
#     return JsonResponse(reports, safe=False)




# import os
# import json
# import joblib
# import pandas as pd
# from datetime import datetime
# from django.conf import settings
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import requests


# reports_cache = []  # Global in-memory reports list

#  const medicineData =   {
#   "(vertigo) Paroymsal Positional Vertigo": [
#     { name: "Vestibular rehabilitation exercises", dosage: "As advised", notes: "Physical therapy exercises" },
#     { name: "Meclizine", dosage: "25 mg 1-3 times daily", notes: "Use cautiously" }
#   ],
#   "AIDS": [
#     { name: "Antiretroviral therapy (ART)", dosage: "As prescribed", notes: "Combination therapy" }
#   ],
#   "Acne": [
#     { name: "Benzoyl peroxide", dosage: "Apply topically once or twice a day", notes: "For mild to moderate acne" },
#     { name: "Salicylic acid", dosage: "Apply topically", notes: "Clears pores" },
#     { name: "Topical retinoids", dosage: "Apply daily", notes: "Promotes skin renewal" }
#   ],
#   "Alcoholic hepatitis": [
#     { name: "Corticosteroids", dosage: "As prescribed", notes: "Reduces liver inflammation" },
#     { name: "Pentoxifylline", dosage: "As prescribed", notes: "Improves blood flow" }
#   ],
#   "Allergy": [
#     { name: "Antihistamines", dosage: "Once daily or as needed", notes: "Relieves allergy symptoms" },
#     { name: "Corticosteroids", dosage: "Nasal sprays or oral", notes: "For severe allergy" }
#   ],
#   "Arthritis": [
#     { name: "NSAIDs", dosage: "As recommended by physician", notes: "Reduces pain and inflammation" },
#     { name: "DMARDs", dosage: "As prescribed", notes: "Disease modifying drugs" }
#   ],
#   "Bronchial Asthma": [
#     { name: "Inhaled corticosteroids", dosage: "Daily preventive use", notes: "Reduces airway inflammation" },
#     { name: "Bronchodilators", dosage: "Use as needed", notes: "Relieves bronchospasm" }
#   ],
#   "Cervical spondylosis": [
#     { name: "NSAIDs", dosage: "As needed", notes: "Pain and inflammation management" },
#     { name: "Muscle relaxants", dosage: "As prescribed", notes: "Relieves muscle spasms" }
#   ],
#   "Chicken pox": [
#     { name: "Acyclovir", dosage: "800 mg 5 times daily", notes: "Start within 24 hours of rash onset" },
#     { name: "Pain relievers", dosage: "As needed", notes: "Avoid aspirin" }
#   ],
#   "Chronic cholestasis": [
#     { name: "Ursodeoxycholic acid", dosage: "As prescribed", notes: "Improves bile flow" }
#   ],
#   "Common Cold": [
#     { name: "Decongestants", dosage: "As directed", notes: "Relieves nasal congestion" },
#     { name: "Pain relievers", dosage: "As needed", notes: "For headache and fever" }
#   ],
#   "Dengue": [
#     { name: "Supportive care", dosage: "Maintain hydration", notes: "No specific antiviral" },
#     { name: "Acetaminophen", dosage: "As needed", notes: "Avoid NSAIDs due to bleeding risk" }
#   ],
#   "Diabetes": [
#     { name: "Metformin", dosage: "500mg twice daily", notes: "Take after meals" },
#     { name: "Insulin", dosage: "As prescribed", notes: "Individualized dosing" }
#   ],
#   "Dimorphic hemmorhoids(piles)": [
#     { name: "Topical steroids", dosage: "Apply to affected area", notes: "Reduces inflammation" },
#     { name: "Pain relievers", dosage: "As needed", notes: "For discomfort" },
#     { name: "Fiber supplements", dosage: "Daily", notes: "Improves stool consistency" }
#   ],
#   "Drug Reaction": [
#     { name: "Discontinue offending drug", dosage: "Immediately", notes: "Consult physician" },
#     { name: "Antihistamines", dosage: "As needed", notes: "Controls allergic symptoms" },
#     { name: "Corticosteroids", dosage: "As prescribed", notes: "Severe reactions" }
#   ],
#   "Fungal infection": [
#     { name: "Topical antifungal creams", dosage: "Apply daily", notes: "Common for skin infections" },
#     { name: "Oral antifungals", dosage: "As prescribed", notes: "For extensive infections" }
#   ],
#   "GERD": [
#     { name: "Proton pump inhibitors", dosage: "Once daily before meals", notes: "Reduces stomach acid" },
#     { name: "H2 blockers", dosage: "As directed", notes: "Relieves heartburn" }
#   ],
#   "Gastroenteritis": [
#     { name: "Oral rehydration salts", dosage: "As needed", notes: "Prevent dehydration" },
#     { name: "Antiemetics", dosage: "As needed", notes: "Controls nausea" }
#   ],
#   "Heart attack": [
#     { name: "Aspirin", dosage: "75-325 mg daily", notes: "Immediate antiplatelet therapy" },
#     { name: "Nitroglycerin", dosage: "Sublingual tablets as needed", notes: "Relieves chest pain" },
#     { name: "Beta blockers", dosage: "As prescribed", notes: "Reduces heart workload" }
#   ],
#   "Hepatitis A": [
#     { name: "Supportive care", dosage: "Rest and hydration", notes: "No specific antiviral" }
#   ],
#   "Hepatitis B": [
#     { name: "Antiviral medications", dosage: "As prescribed", notes: "Suppresses viral replication" }
#   ],
#   "Hepatitis C": [
#     { name: "Direct-acting antivirals", dosage: "Dependent on genotype", notes: "Cure rates >90%" }
#   ],
#   "Hepatitis D": [
#     { name: "Interferon alpha", dosage: "Weekly injection", notes: "Limited efficacy" }
#   ],
#   "Hepatitis E": [
#     { name: "Supportive care", dosage: "Rest and hydration", notes: "Self-limiting" }
#   ],
#   "Hypertension": [
#     { name: "ACE inhibitors", dosage: "As prescribed", notes: "Blood pressure control" },
#     { name: "Calcium channel blockers", dosage: "Daily", notes: "Relaxes blood vessels" },
#     { name: "Diuretics", dosage: "Once daily", notes: "Reduces fluid retention" }
#   ],
#   "Hyperthyroidism": [
#     { name: "Methimazole", dosage: "5-30 mg daily", notes: "Inhibits thyroid hormone synthesis" },
#     { name: "Beta blockers", dosage: "As needed", notes: "Controls symptoms" }
#   ],
#   "Hypoglycemia": [
#     { name: "Glucose tablets", dosage: "15-20 g", notes: "Raise blood sugar quickly" },
#     { name: "Intravenous glucose", dosage: "In severe cases", notes: "Hospital treatment" }
#   ],
#   "Hypothyroidism": [
#     { name: "Levothyroxine", dosage: "Individualized", notes: "Synthetic thyroid hormone" }
#   ],
#   "Impetigo": [
#     { name: "Topical antibiotics", dosage: "Apply 2-3 times daily", notes: "Mild localized infections" },
#     { name: "Oral antibiotics", dosage: "As prescribed", notes: "Extensive disease" }
#   ],
#   "Jaundice": [
#     { name: "Treat underlying cause", dosage: "Varies", notes: "Symptomatic care" },
#     { name: "Supportive care", dosage: "Hydration & rest", notes: "--" }
#   ],
#   "Malaria": [
#     { name: "Chloroquine", dosage: "As per guidelines", notes: "Sensitive areas only" },
#     { name: "Artemisinin-based combination therapy", dosage: "Standard course", notes: "Widespread resistance" }
#   ],
#   "Migraine": [
#     { name: "Triptans", dosage: "Single dose during attack", notes: "Relieves headache" },
#     { name: "NSAIDs", dosage: "As needed", notes: "Pain relief" },
#     { name: "Anti-nausea drugs", dosage: "As needed", notes: "--" }
#   ],
#   "Osteoarthristis": [
#     { name: "NSAIDs", dosage: "As prescribed", notes: "Pain and inflammation relief" },
#     { name: "Acetaminophen", dosage: "As needed", notes: "Mild pain" },
#     { name: "Physical therapy", dosage: "Regular sessions", notes: "Improves function" }
#   ],
#   "Paralysis (brain hemorrhage)": [
#     { name: "Supportive care", dosage: "In hospital", notes: "Manage complications" },
#     { name: "Rehabilitation therapy", dosage: "Long-term", notes: "Regain function" }
#   ],
#   "Peptic ulcer diseae": [
#     { name: "Proton pump inhibitors", dosage: "Once or twice daily", notes: "Reduces acid" },
#     { name: "Antibiotics for H. pylori", dosage: "Combination for 10-14 days", notes: "Eradicates bacteria" }
#   ],
#   "Pneumonia": [
#     { name: "Antibiotics", dosage: "As indicated", notes: "Based on cause" },
#     { name: "Supportive care", dosage: "Oxygen and fluids", notes: "Symptomatic relief" }
#   ],
#   "Psoriasis": [
#     { name: "Topical corticosteroids", dosage: "Apply once or twice daily", notes: "Reduces inflammation" },
#     { name: "Vitamin D analogues", dosage: "Apply as directed", notes: "Slows skin cell growth" },
#     { name: "Phototherapy", dosage: "As advised", notes: "UV light treatment" }
#   ],
#   "Tuberculosis": [
#     { name: "Isoniazid", dosage: "300 mg daily", notes: "Part of multi-drug regimen" },
#     { name: "Rifampin", dosage: "600 mg daily", notes: "Bactericidal" },
#     { name: "Ethambutol", dosage: "15 mg/kg daily", notes: "Prevent resistance" },
#     { name: "Pyrazinamide", dosage: "25 mg/kg daily", notes: "Shortens treatment duration" }
#   ],
#   "Typhoid": [
#     { name: "Ciprofloxacin", dosage: "500 mg twice daily for 7 days", notes: "Effective for sensitive strains" },
#     { name: "Azithromycin", dosage: "500 mg daily for 5 days", notes: "Alternative therapy" }
#   ],
#   "Urinary tract infection": [
#     { name: "Trimethoprim/sulfamethoxazole", dosage: "160/800 mg twice daily for 3 days", notes: "Common antibiotic" },
#     { name: "Nitrofurantoin", dosage: "100 mg twice daily for 5 days", notes: "Inhibits bacterial enzymes" }
#   ],
#   "Varicose veins": [
#     { name: "Compression stockings", dosage: "Wear daily", notes: "Improves venous return" },
#     { name: "Pain relievers", dosage: "As needed", notes: "Reduces discomfort" }
#   ]
# };


# # Toggle mock advice for testing
# use_mock = True  # Set False to enable real RapidAPI advice


# # RapidAPI setup
# RAPIDAPI_URL = "https://ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com/chat?noqueue=1"
# RAPIDAPI_KEY = "your-new-api-key-here"
# RAPIDAPI_HOST = "ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com"


# def get_rapidapi_advice(message, specialization="general", language="en"):
#     headers = {
#         "Content-Type": "application/json",
#         "x-rapidapi-key": RAPIDAPI_KEY,
#         "x-rapidapi-host": RAPIDAPI_HOST
#     }
#     payload = {
#         "message": message,
#         "specialization": specialization,
#         "language": language
#     }
#     try:
#         response = requests.post(RAPIDAPI_URL, json=payload, headers=headers)
#         result = response.json()
#         return result.get("message", "No advice available.")
#     except Exception as e:
#         return f"Error fetching advice: {str(e)}"


# # Load model and encoder
# NB_MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor/naive_bayes_model.pkl')
# LE_PATH = os.path.join(settings.BASE_DIR, 'predictor/label_encoder.pkl')

# nb_model = joblib.load(NB_MODEL_PATH)
# le = joblib.load(LE_PATH)
# all_symptoms = list(nb_model.feature_names_in_)


# @csrf_exempt
# def predict_disease(request):
#     global reports_cache  # Use the global reports cache
#     if request.method != "POST":
#         return JsonResponse({"error": "POST request required"})

#     try:
#         data = json.loads(request.body)
#         symptoms = data.get("symptoms")
#         specialization = data.get("specialization", "general")
#         language = data.get("language", "en")
#         include_advice = data.get("include_advice", False)

#         if not isinstance(symptoms, list):
#             return JsonResponse({"error": "Symptoms must be a list"})

#         input_data = {s: 0 for s in all_symptoms}
#         for s in symptoms:
#             if s in input_data:
#                 input_data[s] = 1
#         df_input = pd.DataFrame([input_data])

#         pred_encoded = nb_model.predict(df_input)[0]
#         pred_disease = le.inverse_transform([pred_encoded])[0]

#         if include_advice:
#             if use_mock:
#                 advice_text = "🧪 Mock advice: Stay hydrated, rest well, and consult a doctor if symptoms persist."
#             else:
#                 rapidapi_message = f"I am experiencing {', '.join(symptoms).replace('_', ' ')}. What could be the cause and what should I do?"
#                 advice_text = get_rapidapi_advice(rapidapi_message, specialization, language)
#         else:
#             advice_text = "Advice not requested."

#         # Append new report to in-memory cache
#         new_report = {
#             "date": datetime.now().isoformat(),
#             "disease": pred_disease,
#             "symptoms": symptoms,
#             "medicines": [],  # Add medicines if you have them
#             "notes": advice_text
#         }
#         reports_cache.append(new_report)

#         return JsonResponse({
#             "naive_bayes_prediction": pred_disease,
#             "medical_advice": advice_text
#         })

#     except Exception as e:
#         return JsonResponse({"error": str(e)})


# def reports_list(request):
#     global reports_cache
#     return JsonResponse(reports_cache, safe=False)



# import os
# import json
# import joblib
# import pandas as pd
# from datetime import datetime
# from django.conf import settings
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import requests


# reports_cache = []  # Global in-memory reports list


# medicineData = {
#   "(vertigo) Paroymsal Positional Vertigo": [
#     { "name": "Vestibular rehabilitation exercises", "dosage": "As advised", "notes": "Physical therapy exercises" },
#     { "name": "Meclizine", "dosage": "25 mg 1-3 times daily", "notes": "Use cautiously" }
#   ],
#   "AIDS": [
#     { "name": "Antiretroviral therapy (ART)", "dosage": "As prescribed", "notes": "Combination therapy" }
#   ],
#   "Acne": [
#     { "name": "Benzoyl peroxide", "dosage": "Apply topically once or twice a day", "notes": "For mild to moderate acne" },
#     { "name": "Salicylic acid", "dosage": "Apply topically", "notes": "Clears pores" },
#     { "name": "Topical retinoids", "dosage": "Apply daily", "notes": "Promotes skin renewal" }
#   ],
#   "Alcoholic hepatitis": [
#     { "name": "Corticosteroids", "dosage": "As prescribed", "notes": "Reduces liver inflammation" },
#     { "name": "Pentoxifylline", "dosage": "As prescribed", "notes": "Improves blood flow" }
#   ],
#   "Allergy": [
#     { "name": "Antihistamines", "dosage": "Once daily or as needed", "notes": "Relieves allergy symptoms" },
#     { "name": "Corticosteroids", "dosage": "Nasal sprays or oral", "notes": "For severe allergy" }
#   ],
#   "Arthritis": [
#     { "name": "NSAIDs", "dosage": "As recommended by physician", "notes": "Reduces pain and inflammation" },
#     { "name": "DMARDs", "dosage": "As prescribed", "notes": "Disease modifying drugs" }
#   ],
#   "Bronchial Asthma": [
#     { "name": "Inhaled corticosteroids", "dosage": "Daily preventive use", "notes": "Reduces airway inflammation" },
#     { "name": "Bronchodilators", "dosage": "Use as needed", "notes": "Relieves bronchospasm" }
#   ],
#   "Cervical spondylosis": [
#     { "name": "NSAIDs", "dosage": "As needed", "notes": "Pain and inflammation management" },
#     { "name": "Muscle relaxants", "dosage": "As prescribed", "notes": "Relieves muscle spasms" }
#   ],
#   "Chicken pox": [
#     { "name": "Acyclovir", "dosage": "800 mg 5 times daily", "notes": "Start within 24 hours of rash onset" },
#     { "name": "Pain relievers", "dosage": "As needed", "notes": "Avoid aspirin" }
#   ],
#   "Chronic cholestasis": [
#     { "name": "Ursodeoxycholic acid", "dosage": "As prescribed", "notes": "Improves bile flow" }
#   ],
#   "Common Cold": [
#     { "name": "Decongestants", "dosage": "As directed", "notes": "Relieves nasal congestion" },
#     { "name": "Pain relievers", "dosage": "As needed", "notes": "For headache and fever" }
#   ],
#   "Dengue": [
#     { "name": "Supportive care", "dosage": "Maintain hydration", "notes": "No specific antiviral" },
#     { "name": "Acetaminophen", "dosage": "As needed", "notes": "Avoid NSAIDs due to bleeding risk" }
#   ],
#   "Diabetes": [
#     { "name": "Metformin", "dosage": "500mg twice daily", "notes": "Take after meals" },
#     { "name": "Insulin", "dosage": "As prescribed", "notes": "Individualized dosing" }
#   ],
#   "Dimorphic hemmorhoids(piles)": [
#     { "name": "Topical steroids", "dosage": "Apply to affected area", "notes": "Reduces inflammation" },
#     { "name": "Pain relievers", "dosage": "As needed", "notes": "For discomfort" },
#     { "name": "Fiber supplements", "dosage": "Daily", "notes": "Improves stool consistency" }
#   ],
#   "Drug Reaction": [
#     { "name": "Discontinue offending drug", "dosage": "Immediately", "notes": "Consult physician" },
#     { "name": "Antihistamines", "dosage": "As needed", "notes": "Controls allergic symptoms" },
#     { "name": "Corticosteroids", "dosage": "As prescribed", "notes": "Severe reactions" }
#   ],
#   "Fungal infection": [
#     { "name": "Topical antifungal creams", "dosage": "Apply daily", "notes": "Common for skin infections" },
#     { "name": "Oral antifungals", "dosage": "As prescribed", "notes": "For extensive infections" }
#   ],
#   "GERD": [
#     { "name": "Proton pump inhibitors", "dosage": "Once daily before meals", "notes": "Reduces stomach acid" },
#     { "name": "H2 blockers", "dosage": "As directed", "notes": "Relieves heartburn" }
#   ],
#   "Gastroenteritis": [
#     { "name": "Oral rehydration salts", "dosage": "As needed", "notes": "Prevent dehydration" },
#     { "name": "Antiemetics", "dosage": "As needed", "notes": "Controls nausea" }
#   ],
#   "Heart attack": [
#     { "name": "Aspirin", "dosage": "75-325 mg daily", "notes": "Immediate antiplatelet therapy" },
#     { "name": "Nitroglycerin", "dosage": "Sublingual tablets as needed", "notes": "Relieves chest pain" },
#     { "name": "Beta blockers", "dosage": "As prescribed", "notes": "Reduces heart workload" }
#   ],
#   "Hepatitis A": [
#     { "name": "Supportive care", "dosage": "Rest and hydration", "notes": "No specific antiviral" }
#   ],
#   "Hepatitis B": [
#     { "name": "Antiviral medications", "dosage": "As prescribed", "notes": "Suppresses viral replication" }
#   ],
#   "Hepatitis C": [
#     { "name": "Direct-acting antivirals", "dosage": "Dependent on genotype", "notes": "Cure rates >90%" }
#   ],
#   "Hepatitis D": [
#     { "name": "Interferon alpha", "dosage": "Weekly injection", "notes": "Limited efficacy" }
#   ],
#   "Hepatitis E": [
#     { "name": "Supportive care", "dosage": "Rest and hydration", "notes": "Self-limiting" }
#   ],
#   "Hypertension": [
#     { "name": "ACE inhibitors", "dosage": "As prescribed", "notes": "Blood pressure control" },
#     { "name": "Calcium channel blockers", "dosage": "Daily", "notes": "Relaxes blood vessels" },
#     { "name": "Diuretics", "dosage": "Once daily", "notes": "Reduces fluid retention" }
#   ],
#   "Hyperthyroidism": [
#     { "name": "Methimazole", "dosage": "5-30 mg daily", "notes": "Inhibits thyroid hormone synthesis" },
#     { "name": "Beta blockers", "dosage": "As needed", "notes": "Controls symptoms" }
#   ],
#   "Hypoglycemia": [
#     { "name": "Glucose tablets", "dosage": "15-20 g", "notes": "Raise blood sugar quickly" },
#     { "name": "Intravenous glucose", "dosage": "In severe cases", "notes": "Hospital treatment" }
#   ],
#   "Hypothyroidism": [
#     { "name": "Levothyroxine", "dosage": "Individualized", "notes": "Synthetic thyroid hormone" }
#   ],
#   "Impetigo": [
#     { "name": "Topical antibiotics", "dosage": "Apply 2-3 times daily", "notes": "Mild localized infections" },
#     { "name": "Oral antibiotics", "dosage": "As prescribed", "notes": "Extensive disease" }
#   ],
#   "Jaundice": [
#     { "name": "Treat underlying cause", "dosage": "Varies", "notes": "Symptomatic care" },
#     { "name": "Supportive care", "dosage": "Hydration & rest", "notes": "--" }
#   ],
#   "Malaria": [
#     { "name": "Chloroquine", "dosage": "As per guidelines", "notes": "Sensitive areas only" },
#     { "name": "Artemisinin-based combination therapy", "dosage": "Standard course", "notes": "Widespread resistance" }
#   ],
#   "Migraine": [
#     { "name": "Triptans", "dosage": "Single dose during attack", "notes": "Relieves headache" },
#     { "name": "NSAIDs", "dosage": "As needed", "notes": "Pain relief" },
#     { "name": "Anti-nausea drugs", "dosage": "As needed", "notes": "--" }
#   ],
#   "Osteoarthristis": [
#     { "name": "NSAIDs", "dosage": "As prescribed", "notes": "Pain and inflammation relief" },
#     { "name": "Acetaminophen", "dosage": "As needed", "notes": "Mild pain" },
#     { "name": "Physical therapy", "dosage": "Regular sessions", "notes": "Improves function" }
#   ],
#   "Paralysis (brain hemorrhage)": [
#     { "name": "Supportive care", "dosage": "In hospital", "notes": "Manage complications" },
#     { "name": "Rehabilitation therapy", "dosage": "Long-term", "notes": "Regain function" }
#   ],
#   "Peptic ulcer diseae": [
#     { "name": "Proton pump inhibitors", "dosage": "Once or twice daily", "notes": "Reduces acid" },
#     { "name": "Antibiotics for H. pylori", "dosage": "Combination for 10-14 days", "notes": "Eradicates bacteria" }
#   ],
#   "Pneumonia": [
#     { "name": "Antibiotics", "dosage": "As indicated", "notes": "Based on cause" },
#     { "name": "Supportive care", "dosage": "Oxygen and fluids", "notes": "Symptomatic relief" }
#   ],
#   "Psoriasis": [
#     { "name": "Topical corticosteroids", "dosage": "Apply once or twice daily", "notes": "Reduces inflammation" },
#     { "name": "Vitamin D analogues", "dosage": "Apply as directed", "notes": "Slows skin cell growth" },
#     { "name": "Phototherapy", "dosage": "As advised", "notes": "UV light treatment" }
#   ],
#   "Tuberculosis": [
#     { "name": "Isoniazid", "dosage": "300 mg daily", "notes": "Part of multi-drug regimen" },
#     { "name": "Rifampin", "dosage": "600 mg daily", "notes": "Bactericidal" },
#     { "name": "Ethambutol", "dosage": "15 mg/kg daily", "notes": "Prevent resistance" },
#     { "name": "Pyrazinamide", "dosage": "25 mg/kg daily", "notes": "Shortens treatment duration" }
#   ],
#   "Typhoid": [
#     { "name": "Ciprofloxacin", "dosage": "500 mg twice daily for 7 days", "notes": "Effective for sensitive strains" },
#     { "name": "Azithromycin", "dosage": "500 mg daily for 5 days", "notes": "Alternative therapy" }
#   ],
#   "Urinary tract infection": [
#     { "name": "Trimethoprim/sulfamethoxazole", "dosage": "160/800 mg twice daily for 3 days", "notes": "Common antibiotic" },
#     { "name": "Nitrofurantoin", "dosage": "100 mg twice daily for 5 days", "notes": "Inhibits bacterial enzymes" }
#   ],
#   "Varicose veins": [
#     { "name": "Compression stockings", "dosage": "Wear daily", "notes": "Improves venous return" },
#     { "name": "Pain relievers", "dosage": "As needed", "notes": "Reduces discomfort" }
#   ]
# }


# # Toggle mock advice for testing
# use_mock = True  # Set False to enable real RapidAPI advice


# # RapidAPI setup
# RAPIDAPI_URL = "https://ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com/chat?noqueue=1"
# RAPIDAPI_KEY = "your-new-api-key-here"
# RAPIDAPI_HOST = "ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com"


# def get_rapidapi_advice(message, specialization="general", language="en"):
#     headers = {
#         "Content-Type": "application/json",
#         "x-rapidapi-key": RAPIDAPI_KEY,
#         "x-rapidapi-host": RAPIDAPI_HOST
#     }
#     payload = {
#         "message": message,
#         "specialization": specialization,
#         "language": language
#     }
#     try:
#         response = requests.post(RAPIDAPI_URL, json=payload, headers=headers)
#         result = response.json()
#         return result.get("message", "No advice available.")
#     except Exception as e:
#         return f"Error fetching advice: {str(e)}"


# # Load model and encoder
# NB_MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor/naive_bayes_model.pkl')
# LE_PATH = os.path.join(settings.BASE_DIR, 'predictor/label_encoder.pkl')

# nb_model = joblib.load(NB_MODEL_PATH)
# le = joblib.load(LE_PATH)
# all_symptoms = list(nb_model.feature_names_in_)


# @csrf_exempt
# def predict_disease(request):
#     global reports_cache  # Use the global reports cache
#     if request.method != "POST":
#         return JsonResponse({"error": "POST request required"})

#     try:
#         data = json.loads(request.body)
#         symptoms = data.get("symptoms")
#         specialization = data.get("specialization", "general")
#         language = data.get("language", "en")
#         include_advice = data.get("include_advice", False)

#         if not isinstance(symptoms, list):
#             return JsonResponse({"error": "Symptoms must be a list"})

#         input_data = {s: 0 for s in all_symptoms}
#         for s in symptoms:
#             if s in input_data:
#                 input_data[s] = 1
#         df_input = pd.DataFrame([input_data])

#         pred_encoded = nb_model.predict(df_input)[0]
#         pred_disease = le.inverse_transform([pred_encoded])[0]

#         if include_advice:
#             if use_mock:
#                 advice_text = "🧪 Mock advice: Stay hydrated, rest well, and consult a doctor if symptoms persist."
#             else:
#                 rapidapi_message = f"I am experiencing {', '.join(symptoms).replace('_', ' ')}. What could be the cause and what should I do?"
#                 advice_text = get_rapidapi_advice(rapidapi_message, specialization, language)
#         else:
#             advice_text = "Advice not requested."

#         medicines = medicineData.get(pred_disease, [])

#         new_report = {
#             "date": datetime.now().isoformat(),
#             "disease": pred_disease,
#             "symptoms": symptoms,
#             "medicines": medicines,
#             "notes": advice_text
#         }
#         reports_cache.append(new_report)

#         return JsonResponse({
#             "naive_bayes_prediction": pred_disease,
#             "medical_advice": advice_text
#         })

#     except Exception as e:
#         return JsonResponse({"error": str(e)})


# def reports_list(request):
#     global reports_cache
#     return JsonResponse(reports_cache, safe=False)






# import os
# import json
# import joblib
# import pandas as pd
# from datetime import datetime
# from django.conf import settings
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import requests


# reports_cache = []  # Global in-memory reports list

# medicineData = {
#    "(vertigo) Paroymsal Positional Vertigo": [
#      { "name": "Vestibular rehabilitation exercises", "dosage": "As advised", "notes": "Physical therapy exercises" },
#      { "name": "Meclizine", "dosage": "25 mg 1-3 times daily", "notes": "Use cautiously" }
#    ],
#    "AIDS": [
#      { "name": "Antiretroviral therapy (ART)", "dosage": "As prescribed", "notes": "Combination therapy" }
#    ],
#    "Acne": [
#      { "name": "Benzoyl peroxide", "dosage": "Apply topically once or twice a day", "notes": "For mild to moderate acne" },
#      { "name": "Salicylic acid", "dosage": "Apply topically", "notes": "Clears pores" },
#      { "name": "Topical retinoids", "dosage": "Apply daily", "notes": "Promotes skin renewal" }
#    ],
#    "Alcoholic hepatitis": [
#      { "name": "Corticosteroids", "dosage": "As prescribed", "notes": "Reduces liver inflammation" },
#      { "name": "Pentoxifylline", "dosage": "As prescribed", "notes": "Improves blood flow" }
#    ],
#    "Allergy": [
#      { "name": "Antihistamines", "dosage": "Once daily or as needed", "notes": "Relieves allergy symptoms" },
#      { "name": "Corticosteroids", "dosage": "Nasal sprays or oral", "notes": "For severe allergy" }
#    ],
#    "Arthritis": [
#      { "name": "NSAIDs", "dosage": "As recommended by physician", "notes": "Reduces pain and inflammation" },
#      { "name": "DMARDs", "dosage": "As prescribed", "notes": "Disease modifying drugs" }
#    ],
#    "Bronchial Asthma": [
#      { "name": "Inhaled corticosteroids", "dosage": "Daily preventive use", "notes": "Reduces airway inflammation" },
#      { "name": "Bronchodilators", "dosage": "Use as needed", "notes": "Relieves bronchospasm" }
#    ],
#    "Cervical spondylosis": [
#      { "name": "NSAIDs", "dosage": "As needed", "notes": "Pain and inflammation management" },
#      { "name": "Muscle relaxants", "dosage": "As prescribed", "notes": "Relieves muscle spasms" }
#    ],
#    "Chicken pox": [
#      { "name": "Acyclovir", "dosage": "800 mg 5 times daily", "notes": "Start within 24 hours of rash onset" },
#      { "name": "Pain relievers", "dosage": "As needed", "notes": "Avoid aspirin" }
#    ],
#    "Chronic cholestasis": [
#      { "name": "Ursodeoxycholic acid", "dosage": "As prescribed", "notes": "Improves bile flow" }
#    ],   "Common Cold": [
#      { "name": "Decongestants", "dosage": "As directed", "notes": "Relieves nasal congestion" },
#      { "name": "Pain relievers", "dosage": "As needed", "notes": "For headache and fever" }
#    ],
#    "Dengue": [     { "name": "Supportive care", "dosage": "Maintain hydration", "notes": "No specific antiviral" },
#      { "name": "Acetaminophen", "dosage": "As needed", "notes": "Avoid NSAIDs due to bleeding risk" }   ],
#    "Diabetes": [
#     { "name": "Metformin", "dosage": "500mg twice daily", "notes": "Take after meals" },
#     { "name": "Insulin", "dosage": "As prescribed", "notes": "Individualized dosing" }
#   ],
#   "Dimorphic hemmorhoids(piles)": [
#      { "name": "Topical steroids", "dosage": "Apply to affected area", "notes": "Reduces inflammation" },
#      { "name": "Pain relievers", "dosage": "As needed", "notes": "For discomfort" },
#      { "name": "Fiber supplements", "dosage": "Daily", "notes": "Improves stool consistency" }
#    ],
#    "Drug Reaction": [     { "name": "Discontinue offending drug", "dosage": "Immediately", "notes": "Consult physician" },
#      { "name": "Antihistamines", "dosage": "As needed", "notes": "Controls allergic symptoms" },
#      { "name": "Corticosteroids", "dosage": "As prescribed", "notes": "Severe reactions" }
#   ],
#    "Fungal infection": [
#      { "name": "Topical antifungal creams", "dosage": "Apply daily", "notes": "Common for skin infections" },
#      { "name": "Oral antifungals", "dosage": "As prescribed", "notes": "For extensive infections" }
#    ],
#    "GERD": [
#      { "name": "Proton pump inhibitors", "dosage": "Once daily before meals", "notes": "Reduces stomach acid" },
#      { "name": "H2 blockers", "dosage": "As directed", "notes": "Relieves heartburn" }
#    ],
#    "Gastroenteritis": [
#      { "name": "Oral rehydration salts", "dosage": "As needed", "notes": "Prevent dehydration" },
#      { "name": "Antiemetics", "dosage": "As needed", "notes": "Controls nausea" }
#    ],
#    "Heart attack": [
#      { "name": "Aspirin", "dosage": "75-325 mg daily", "notes": "Immediate antiplatelet therapy" },
#      { "name": "Nitroglycerin", "dosage": "Sublingual tablets as needed", "notes": "Relieves chest pain" },
#      { "name": "Beta blockers", "dosage": "As prescribed", "notes": "Reduces heart workload" }
#    ],
#    "Hepatitis A": [
#      { "name": "Supportive care", "dosage": "Rest and hydration", "notes": "No specific antiviral" }
#    ],
#    "Hepatitis B": [
#      { "name": "Antiviral medications", "dosage": "As prescribed", "notes": "Suppresses viral replication" }
#    ],
#    "Hepatitis C": [
#      { "name": "Direct-acting antivirals", "dosage": "Dependent on genotype", "notes": "Cure rates >90%" }
#    ],
#    "Hepatitis D": [
#      { "name": "Interferon alpha", "dosage": "Weekly injection", "notes": "Limited efficacy" }
#    ],   "Hepatitis E": [
#      { "name": "Supportive care", "dosage": "Rest and hydration", "notes": "Self-limiting" }
#    ],
#   "Hypertension": [
#     { "name": "ACE inhibitors", "dosage": "As prescribed", "notes": "Blood pressure control" },
#     { "name": "Calcium channel blockers", "dosage": "Daily", "notes": "Relaxes blood vessels" },
#     { "name": "Diuretics", "dosage": "Once daily", "notes": "Reduces fluid retention" }
#   ],
#   "Hyperthyroidism": [
#     { "name": "Methimazole", "dosage": "5-30 mg daily", "notes": "Inhibits thyroid hormone synthesis" },
#     { "name": "Beta blockers", "dosage": "As needed", "notes": "Controls symptoms" }
#   ],
#   "Hypoglycemia": [
#     { "name": "Glucose tablets", "dosage": "15-20 g", "notes": "Raise blood sugar quickly" },
#     { "name": "Intravenous glucose", "dosage": "In severe cases", "notes": "Hospital treatment" }
#   ],
#   "Hypothyroidism": [
#     { "name": "Levothyroxine", "dosage": "Individualized", "notes": "Synthetic thyroid hormone" }
#   ],
#   "Impetigo": [
#     { "name": "Topical antibiotics", "dosage": "Apply 2-3 times daily", "notes": "Mild localized infections" },
#     { "name": "Oral antibiotics", "dosage": "As prescribed", "notes": "Extensive disease" }
#   ],
#   "Jaundice": [
#     { "name": "Treat underlying cause", "dosage": "Varies", "notes": "Symptomatic care" },
#     { "name": "Supportive care", "dosage": "Hydration & rest", "notes": "--" }
#   ],
#   "Malaria": [
#     { "name": "Chloroquine", "dosage": "As per guidelines", "notes": "Sensitive areas only" },
#     { "name": "Artemisinin-based combination therapy", "dosage": "Standard course", "notes": "Widespread resistance" }
#   ],
#   "Migraine": [
#     { "name": "Triptans", "dosage": "Single dose during attack", "notes": "Relieves headache" },
#     { "name": "NSAIDs", "dosage": "As needed", "notes": "Pain relief" },
#     { "name": "Anti-nausea drugs", "dosage": "As needed", "notes": "--" }
#   ],
#   "Osteoarthristis": [
#     { "name": "NSAIDs", "dosage": "As prescribed", "notes": "Pain and inflammation relief" },
#     { "name": "Acetaminophen", "dosage": "As needed", "notes": "Mild pain" },
#     { "name": "Physical therapy", "dosage": "Regular sessions", "notes": "Improves function" }
#   ],
#   "Paralysis (brain hemorrhage)": [
#     { "name": "Supportive care", "dosage": "In hospital", "notes": "Manage complications" },
#     { "name": "Rehabilitation therapy", "dosage": "Long-term", "notes": "Regain function" }
#   ],
#   "Peptic ulcer diseae": [
#     { "name": "Proton pump inhibitors", "dosage": "Once or twice daily", "notes": "Reduces acid" },
#     { "name": "Antibiotics for H. pylori", "dosage": "Combination for 10-14 days", "notes": "Eradicates bacteria" }
#   ],
#   "Pneumonia": [
#     { "name": "Antibiotics", "dosage": "As indicated", "notes": "Based on cause" },
#     { "name": "Supportive care", "dosage": "Oxygen and fluids", "notes": "Symptomatic relief" }
#   ],
#   "Psoriasis": [
#     { "name": "Topical corticosteroids", "dosage": "Apply once or twice daily", "notes": "Reduces inflammation" },
#     { "name": "Vitamin D analogues", "dosage": "Apply as directed", "notes": "Slows skin cell growth" },
#     { "name": "Phototherapy", "dosage": "As advised", "notes": "UV light treatment" }
#   ],
#   "Tuberculosis": [
#     { "name": "Isoniazid", "dosage": "300 mg daily", "notes": "Part of multi-drug regimen" },
#     { "name": "Rifampin", "dosage": "600 mg daily", "notes": "Bactericidal" },
#     { "name": "Ethambutol", "dosage": "15 mg/kg daily", "notes": "Prevent resistance" },
#     { "name": "Pyrazinamide", "dosage": "25 mg/kg daily", "notes": "Shortens treatment duration" }
#   ],
#   "Typhoid": [
#     { "name": "Ciprofloxacin", "dosage": "500 mg twice daily for 7 days", "notes": "Effective for sensitive strains" },
#     { "name": "Azithromycin", "dosage": "500 mg daily for 5 days", "notes": "Alternative therapy" }
#   ],
#   "Urinary tract infection": [
#     { "name": "Trimethoprim/sulfamethoxazole", "dosage": "160/800 mg twice daily for 3 days", "notes": "Common antibiotic" },
#     { "name": "Nitrofurantoin", "dosage": "100 mg twice daily for 5 days", "notes": "Inhibits bacterial enzymes" }
#   ],
#   "Varicose veins": [
#     { "name": "Compression stockings", "dosage": "Wear daily", "notes": "Improves venous return" },
#     { "name": "Pain relievers", "dosage": "As needed", "notes": "Reduces discomfort" }
#   ]
# }

# # Disable mock advice to enable real API calls
# use_mock = False

# # Put your actual RapidAPI key here
# RAPIDAPI_KEY = "4a221730cdmsh5264d3aee6ad2dep1c843ejsnb0161184b0de"
# RAPIDAPI_HOST = "ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com"
# RAPIDAPI_URL = "https://ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com/chat?noqueue=1"


# def get_rapidapi_advice(message, specialization="general", language="en"):
#     headers = {
#         "Content-Type": "application/json",
#         "x-rapidapi-key": RAPIDAPI_KEY,
#         "x-rapidapi-host": RAPIDAPI_HOST
#     }
#     payload = {
#         "message": message,
#         "specialization": specialization,
#         "language": language
#     }
#     try:
#         response = requests.post(RAPIDAPI_URL, json=payload, headers=headers)
#         result = response.json()
#         print("RapidAPI full response:", result) 
#         return result.get("message", "No advice available.")
#     except Exception as e:
#         return f"Error fetching advice: {str(e)}"


# # Load model and label encoder
# NB_MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor/naive_bayes_model.pkl')
# LE_PATH = os.path.join(settings.BASE_DIR, 'predictor/label_encoder.pkl')

# nb_model = joblib.load(NB_MODEL_PATH)
# le = joblib.load(LE_PATH)
# all_symptoms = list(nb_model.feature_names_in_)


# @csrf_exempt
# def predict_disease(request):
#     global reports_cache  # Use the global reports cache
#     if request.method != "POST":
#         return JsonResponse({"error": "POST request required"})

#     try:
#         data = json.loads(request.body)
#         symptoms = data.get("symptoms")
#         specialization = data.get("specialization", "general")
#         language = data.get("language", "en")
#         include_advice = data.get("include_advice", False)

#         if not isinstance(symptoms, list):
#             return JsonResponse({"error": "Symptoms must be a list"})

#         input_data = {s: 0 for s in all_symptoms}
#         for s in symptoms:
#             if s in input_data:
#                 input_data[s] = 1
#         df_input = pd.DataFrame([input_data])

#         pred_encoded = nb_model.predict(df_input)[0]
#         pred_disease = le.inverse_transform([pred_encoded])[0]

#         if include_advice:
#             if use_mock:
#                 advice_text = "🧪 Mock advice: Stay hydrated, rest well, and consult a doctor if symptoms persist."
#             else:
#                 rapidapi_message = f"I am experiencing {', '.join(symptoms).replace('_', ' ')}. What could be the cause and what should I do?"
#                 advice_text = get_rapidapi_advice(rapidapi_message, specialization, language)
#         else:
#             advice_text = "Advice not requested."

#         medicines = medicineData.get(pred_disease, [])

#         new_report = {
#             "date": datetime.now().isoformat(),
#             "disease": pred_disease,
#             "symptoms": symptoms,
#             "medicines": medicines,
#             "notes": advice_text
#         }
#         reports_cache.append(new_report)

#         return JsonResponse({
#             "naive_bayes_prediction": pred_disease,
#             "medical_advice": advice_text
#         })

#     except Exception as e:
#         return JsonResponse({"error": str(e)})


# def reports_list(request):
#     global reports_cache
#     return JsonResponse(reports_cache, safe=False)


import os
import json
import joblib
import pandas as pd
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests


reports_cache = []  # Global in-memory reports list

medicineData = {
   "(vertigo) Paroymsal Positional Vertigo": [
     { "name": "Vestibular rehabilitation exercises", "dosage": "As advised", "notes": "Physical therapy exercises" },
     { "name": "Meclizine", "dosage": "25 mg 1-3 times daily", "notes": "Use cautiously" }
   ],
   "AIDS": [
     { "name": "Antiretroviral therapy (ART)", "dosage": "As prescribed", "notes": "Combination therapy" }
   ],
   "Acne": [
     { "name": "Benzoyl peroxide", "dosage": "Apply topically once or twice a day", "notes": "For mild to moderate acne" },
     { "name": "Salicylic acid", "dosage": "Apply topically", "notes": "Clears pores" },
     { "name": "Topical retinoids", "dosage": "Apply daily", "notes": "Promotes skin renewal" }
   ],
   "Alcoholic hepatitis": [
     { "name": "Corticosteroids", "dosage": "As prescribed", "notes": "Reduces liver inflammation" },
     { "name": "Pentoxifylline", "dosage": "As prescribed", "notes": "Improves blood flow" }
   ],
   "Allergy": [
     { "name": "Antihistamines", "dosage": "Once daily or as needed", "notes": "Relieves allergy symptoms" },
     { "name": "Corticosteroids", "dosage": "Nasal sprays or oral", "notes": "For severe allergy" }
   ],
   "Arthritis": [
     { "name": "NSAIDs", "dosage": "As recommended by physician", "notes": "Reduces pain and inflammation" },
     { "name": "DMARDs", "dosage": "As prescribed", "notes": "Disease modifying drugs" }
   ],
   "Bronchial Asthma": [
     { "name": "Inhaled corticosteroids", "dosage": "Daily preventive use", "notes": "Reduces airway inflammation" },
     { "name": "Bronchodilators", "dosage": "Use as needed", "notes": "Relieves bronchospasm" }
   ],
   "Cervical spondylosis": [
     { "name": "NSAIDs", "dosage": "As needed", "notes": "Pain and inflammation management" },
     { "name": "Muscle relaxants", "dosage": "As prescribed", "notes": "Relieves muscle spasms" }
   ],
   "Chicken pox": [
     { "name": "Acyclovir", "dosage": "800 mg 5 times daily", "notes": "Start within 24 hours of rash onset" },
     { "name": "Pain relievers", "dosage": "As needed", "notes": "Avoid aspirin" }
   ],
   "Chronic cholestasis": [
     { "name": "Ursodeoxycholic acid", "dosage": "As prescribed", "notes": "Improves bile flow" }
   ],   "Common Cold": [
     { "name": "Decongestants", "dosage": "As directed", "notes": "Relieves nasal congestion" },
     { "name": "Pain relievers", "dosage": "As needed", "notes": "For headache and fever" }
   ],
   "Dengue": [     { "name": "Supportive care", "dosage": "Maintain hydration", "notes": "No specific antiviral" },
     { "name": "Acetaminophen", "dosage": "As needed", "notes": "Avoid NSAIDs due to bleeding risk" }   ],
   "Diabetes": [
    { "name": "Metformin", "dosage": "500mg twice daily", "notes": "Take after meals" },
    { "name": "Insulin", "dosage": "As prescribed", "notes": "Individualized dosing" }
  ],
  "Dimorphic hemmorhoids(piles)": [
     { "name": "Topical steroids", "dosage": "Apply to affected area", "notes": "Reduces inflammation" },
     { "name": "Pain relievers", "dosage": "As needed", "notes": "For discomfort" },
     { "name": "Fiber supplements", "dosage": "Daily", "notes": "Improves stool consistency" }
   ],
   "Drug Reaction": [     { "name": "Discontinue offending drug", "dosage": "Immediately", "notes": "Consult physician" },
     { "name": "Antihistamines", "dosage": "As needed", "notes": "Controls allergic symptoms" },
     { "name": "Corticosteroids", "dosage": "As prescribed", "notes": "Severe reactions" }
  ],
   "Fungal infection": [
     { "name": "Topical antifungal creams", "dosage": "Apply daily", "notes": "Common for skin infections" },
     { "name": "Oral antifungals", "dosage": "As prescribed", "notes": "For extensive infections" }
   ],
   "GERD": [
     { "name": "Proton pump inhibitors", "dosage": "Once daily before meals", "notes": "Reduces stomach acid" },
     { "name": "H2 blockers", "dosage": "As directed", "notes": "Relieves heartburn" }
   ],
   "Gastroenteritis": [
     { "name": "Oral rehydration salts", "dosage": "As needed", "notes": "Prevent dehydration" },
     { "name": "Antiemetics", "dosage": "As needed", "notes": "Controls nausea" }
   ],
   "Heart attack": [
     { "name": "Aspirin", "dosage": "75-325 mg daily", "notes": "Immediate antiplatelet therapy" },
     { "name": "Nitroglycerin", "dosage": "Sublingual tablets as needed", "notes": "Relieves chest pain" },
     { "name": "Beta blockers", "dosage": "As prescribed", "notes": "Reduces heart workload" }
   ],
   "Hepatitis A": [
     { "name": "Supportive care", "dosage": "Rest and hydration", "notes": "No specific antiviral" }
   ],
   "Hepatitis B": [
     { "name": "Antiviral medications", "dosage": "As prescribed", "notes": "Suppresses viral replication" }
   ],
   "Hepatitis C": [
     { "name": "Direct-acting antivirals", "dosage": "Dependent on genotype", "notes": "Cure rates >90%" }
   ],
   "Hepatitis D": [
     { "name": "Interferon alpha", "dosage": "Weekly injection", "notes": "Limited efficacy" }
   ],   "Hepatitis E": [
     { "name": "Supportive care", "dosage": "Rest and hydration", "notes": "Self-limiting" }
   ],
  "Hypertension": [
    { "name": "ACE inhibitors", "dosage": "As prescribed", "notes": "Blood pressure control" },
    { "name": "Calcium channel blockers", "dosage": "Daily", "notes": "Relaxes blood vessels" },
    { "name": "Diuretics", "dosage": "Once daily", "notes": "Reduces fluid retention" }
  ],
  "Hyperthyroidism": [
    { "name": "Methimazole", "dosage": "5-30 mg daily", "notes": "Inhibits thyroid hormone synthesis" },
    { "name": "Beta blockers", "dosage": "As needed", "notes": "Controls symptoms" }
  ],
  "Hypoglycemia": [
    { "name": "Glucose tablets", "dosage": "15-20 g", "notes": "Raise blood sugar quickly" },
    { "name": "Intravenous glucose", "dosage": "In severe cases", "notes": "Hospital treatment" }
  ],
  "Hypothyroidism": [
    { "name": "Levothyroxine", "dosage": "Individualized", "notes": "Synthetic thyroid hormone" }
  ],
  "Impetigo": [
    { "name": "Topical antibiotics", "dosage": "Apply 2-3 times daily", "notes": "Mild localized infections" },
    { "name": "Oral antibiotics", "dosage": "As prescribed", "notes": "Extensive disease" }
  ],
  "Jaundice": [
    { "name": "Treat underlying cause", "dosage": "Varies", "notes": "Symptomatic care" },
    { "name": "Supportive care", "dosage": "Hydration & rest", "notes": "--" }
  ],
  "Malaria": [
    { "name": "Chloroquine", "dosage": "As per guidelines", "notes": "Sensitive areas only" },
    { "name": "Artemisinin-based combination therapy", "dosage": "Standard course", "notes": "Widespread resistance" }
  ],
  "Migraine": [
    { "name": "Triptans", "dosage": "Single dose during attack", "notes": "Relieves headache" },
    { "name": "NSAIDs", "dosage": "As needed", "notes": "Pain relief" },
    { "name": "Anti-nausea drugs", "dosage": "As needed", "notes": "--" }
  ],
  "Osteoarthristis": [
    { "name": "NSAIDs", "dosage": "As prescribed", "notes": "Pain and inflammation relief" },
    { "name": "Acetaminophen", "dosage": "As needed", "notes": "Mild pain" },
    { "name": "Physical therapy", "dosage": "Regular sessions", "notes": "Improves function" }
  ],
  "Paralysis (brain hemorrhage)": [
    { "name": "Supportive care", "dosage": "In hospital", "notes": "Manage complications" },
    { "name": "Rehabilitation therapy", "dosage": "Long-term", "notes": "Regain function" }
  ],
  "Peptic ulcer diseae": [
    { "name": "Proton pump inhibitors", "dosage": "Once or twice daily", "notes": "Reduces acid" },
    { "name": "Antibiotics for H. pylori", "dosage": "Combination for 10-14 days", "notes": "Eradicates bacteria" }
  ],
  "Pneumonia": [
    { "name": "Antibiotics", "dosage": "As indicated", "notes": "Based on cause" },
    { "name": "Supportive care", "dosage": "Oxygen and fluids", "notes": "Symptomatic relief" }
  ],
  "Psoriasis": [
    { "name": "Topical corticosteroids", "dosage": "Apply once or twice daily", "notes": "Reduces inflammation" },
    { "name": "Vitamin D analogues", "dosage": "Apply as directed", "notes": "Slows skin cell growth" },
    { "name": "Phototherapy", "dosage": "As advised", "notes": "UV light treatment" }
  ],
  "Tuberculosis": [
    { "name": "Isoniazid", "dosage": "300 mg daily", "notes": "Part of multi-drug regimen" },
    { "name": "Rifampin", "dosage": "600 mg daily", "notes": "Bactericidal" },
    { "name": "Ethambutol", "dosage": "15 mg/kg daily", "notes": "Prevent resistance" },
    { "name": "Pyrazinamide", "dosage": "25 mg/kg daily", "notes": "Shortens treatment duration" }
  ],
  "Typhoid": [
    { "name": "Ciprofloxacin", "dosage": "500 mg twice daily for 7 days", "notes": "Effective for sensitive strains" },
    { "name": "Azithromycin", "dosage": "500 mg daily for 5 days", "notes": "Alternative therapy" }
  ],
  "Urinary tract infection": [
    { "name": "Trimethoprim/sulfamethoxazole", "dosage": "160/800 mg twice daily for 3 days", "notes": "Common antibiotic" },
    { "name": "Nitrofurantoin", "dosage": "100 mg twice daily for 5 days", "notes": "Inhibits bacterial enzymes" }
  ],
  "Varicose veins": [
    { "name": "Compression stockings", "dosage": "Wear daily", "notes": "Improves venous return" },
    { "name": "Pain relievers", "dosage": "As needed", "notes": "Reduces discomfort" }
  ]
}

# Disable mock advice to enable real API calls
use_mock = False

RAPIDAPI_KEY = "dc096258famshbe3f458dccf048bp1babcajsnb59f2f034f6f"
RAPIDAPI_HOST = "ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com"
RAPIDAPI_URL = "https://ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com/chat?noqueue=1"


def get_rapidapi_advice(message, specialization="general", language="en"):
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }
    payload = {
        "message": message,
        "specialization": specialization,
        "language": language
    }
    try:
        response = requests.post(RAPIDAPI_URL, json=payload, headers=headers)
        result = response.json()
        # Extract detailed chatbot advice from nested JSON
        advice = result.get("result", {}).get("response", {}).get("message")
        if not advice:
            advice = result.get("message", "No advice available.")
        return advice
    except Exception as e:
        return f"Error fetching advice: {str(e)}"


NB_MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor/naive_bayes_model.pkl')
LE_PATH = os.path.join(settings.BASE_DIR, 'predictor/label_encoder.pkl')

nb_model = joblib.load(NB_MODEL_PATH)
le = joblib.load(LE_PATH)
all_symptoms = list(nb_model.feature_names_in_)


@csrf_exempt
def predict_disease(request):
    global reports_cache  # Use the global reports cache
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"})

    try:
        data = json.loads(request.body)
        symptoms = data.get("symptoms")
        specialization = data.get("specialization", "general")
        language = data.get("language", "en")
        include_advice = data.get("include_advice", False)

        if not isinstance(symptoms, list):
            return JsonResponse({"error": "Symptoms must be a list"})

        input_data = {s: 0 for s in all_symptoms}
        for s in symptoms:
            if s in input_data:
                input_data[s] = 1
        df_input = pd.DataFrame([input_data])

        pred_encoded = nb_model.predict(df_input)[0]
        pred_disease = le.inverse_transform([pred_encoded])[0]

        if include_advice:
            if use_mock:
                advice_text = "🧪 Mock advice: Stay hydrated, rest well, and consult a doctor if symptoms persist."
            else:
                rapidapi_message = f"I am experiencing {', '.join(symptoms).replace('_', ' ')}. What could be the cause and what should I do?"
                advice_text = get_rapidapi_advice(rapidapi_message, specialization, language)
        else:
            advice_text = "Advice not requested."

        medicines = medicineData.get(pred_disease, [])

        new_report = {
            "date": datetime.now().isoformat(),
            "disease": pred_disease,
            "symptoms": symptoms,
            "medicines": medicines,
            "notes": advice_text
        }
        reports_cache.append(new_report)

        return JsonResponse({
            "naive_bayes_prediction": pred_disease,
            "medical_advice": advice_text
        })

    except Exception as e:
        return JsonResponse({"error": str(e)})


def reports_list(request):
    global reports_cache
    return JsonResponse(reports_cache, safe=False)







