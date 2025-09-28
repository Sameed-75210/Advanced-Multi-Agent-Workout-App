from langflow.load import run_flow_from_json
from dotenv import load_dotenv
import requests
from typing import Optional
import json
import os

load_dotenv()
# print("DEBUG LANGFLOW_API_KEY:", os.getenv("LANGFLOW_API_KEY"))

BASE_API_URL="https://api.langflow.astra.datastax.com"
LANGFLOW_ID="34c16f5c-70e4-4bb6-9c51-89a41a653efd"
APPLICATION_TOKEN=os.getenv("LANGFLOW_API_KEY")


def dict_to_string(obj, level=0):
    strings = []
    indent = "  " * level  # Indentation for nested levels
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                nested_string = dict_to_string(value, level + 1)
                strings.append(f"{indent}{key}: {nested_string}")
            else:
                strings.append(f"{indent}{key}: {value}")
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            nested_string = dict_to_string(item, level + 1)
            strings.append(f"{indent}Item {idx + 1}: {nested_string}")
    else:
        strings.append(f"{indent}{obj}")

    return ", ".join(strings)


# def ask_ai(profile, question):
#     TWEAKS = {
#         "TextInput-XjIKI": {
#             "input_value": question
#         },
#         "TextInput-176Ns": {
#             "input_value": dict_to_string(profile)
#         },
#     }
#     result = run_flow(
#     message=question,
#     tweaks=TWEAKS,
#     application_token=APPLICATION_TOKEN
#     )
#     return result

def ask_ai(profile, question):
    TWEAKS = {
        "TextInput-XjIKI": {"input_value": question},
        "TextInput-176Ns": {"input_value": dict_to_string(profile)}  # General Profile info
    }

    result = run_flow(
        message=question,
        tweaks=TWEAKS,
        application_token=APPLICATION_TOKEN
    )

    return result 


def get_macros(profile, goals):
    TWEAKS = {
        "TextInput-PR5Jb": {
            "input_value": ", ".join(goals)
        },
        "TextInput-PrfY9": {
            "input_value": dict_to_string(profile)
        }
    }
    return run_flow("", tweaks=TWEAKS, application_token=APPLICATION_TOKEN)


def run_flow(message: str,
             output_type: str = "chat",
             input_type: str = "chat",
             tweaks: Optional[dict] = None,
             application_token: Optional[str] = None) -> str:
    api_url = "http://localhost:7860/api/v1/run/macros"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    if tweaks:
        payload["tweaks"] = tweaks

    headers = {"Content-Type": "application/json"}
    if application_token:
        headers["Authorization"] = f"Bearer {application_token}"

    response = requests.post(api_url, json=payload, headers=headers)

    try:
        data = response.json()
    except Exception:
        return f"❌ API returned non-JSON: {response.text}"

    # Debugging: see full response if 'outputs' is missing
    if "outputs" not in data:
        return f"❌ Unexpected response: {json.dumps(data, indent=2)}"

    try:
        return data["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"]
    except Exception:
        # print("Sameed" ,data)
        return f"❌ Could not parse AI response: {json.dumps(data, indent=2)}"

# def run_flow(message: str,
#              output_type: str = "chat",
#              input_type: str = "chat",
#              tweaks: Optional[dict] = None,
#              application_token: Optional[str] = None) -> str:
#     api_url = "http://localhost:7860/api/v1/run/macros"

#     payload = {
#         "input_value": message,
#         "output_type": output_type,
#         "input_type": input_type,
#     }
#     if tweaks:
#         payload["tweaks"] = tweaks

#     headers = {"Content-Type": "application/json"}
#     if application_token:
#         headers["Authorization"] = f"Bearer {application_token}"

#     response = requests.post(api_url, json=payload, headers=headers)

#     try:
#         data = response.json()
#     except Exception:
#         return f"❌ API returned non-JSON: {response.text}"

#     # Debugging: Show full response if 'outputs' is missing
#     if "outputs" not in data:
#         return f"❌ Unexpected response: {json.dumps(data, indent=2)}"

#     # Safely attempt to extract AI response
#     try:
#         ai_response = data.get("outputs", [{}])[0].get("message", {}).get("text", "No response text found.")
#         return ai_response
#     except Exception as e:
#         # Debug any missing keys or errors during parsing
#         return f"❌ Could not parse AI response: {e}\nFull response: {json.dumps(data, indent=2)}"
