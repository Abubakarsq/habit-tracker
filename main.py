import requests
from datetime import datetime
import os

APP_ID = "2ff7e7e7"
API_KEY = "270be9530bc6fca36dcffa9c41dc2fa6"

EX_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f50e4ea2e3849db065f4e33dca7b951c/workoutTracking/workouts"

GENDER = "male"
WEIGHT_KG = "55"
HEIGHT_CM = "180"
AGE = "20"

keys = {
    "query": input("what exercise did you do??  "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
response = requests.post(url=EX_ENDPOINT, json=keys, headers=header)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=("sirrdeeqq", "Nas090@"))


