import requests
import socket
from config import key



def chat1(chat):
    api_key = "VF.DM.65e8baf40c2f4220de069122.xhoCfDAGOyGmvU2Q"
    user_id = "User_123"
    user_input = chat
    body = {"request": {"type": "text", "payload": user_input}}

    try:
        response = requests.post(
            f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact",
            json=body,
            headers={"Authorization": api_key},
        )
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and item.get('type') == 'text':
                    message_payload = item['payload'].get('message')
                    if message_payload:
                        print("Response from Voiceflow assistant:", message_payload)
                        return message_payload
            else:
                print("No text message received from the Voiceflow assistant.")
        else:
            print("Unexpected response format from the Voiceflow assistant.")

    except requests.exceptions.RequestException as e:
        print("Error occurred during API request:", e)


def get_ip(host):
    try:
        result = socket.getaddrinfo("google.com", None)
    except Exception as e:
        print (e)
        result = f"Error in finding the IP,{e}"
    return result    

def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":city,"format":"json","u":"f"}

    headers = {
        "X-RapidAPI-Key": "3a93048d60msh51d0b162efad95dp1fe489jsn169d9d54b874",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    d1=response.json()
    d1=d1.get("current_observation")
    humidity=d1.get('atmosphere').get('humidity')
    temperature=d1.get('condition').get('temperature')
    temperature=round((temperature-32)*5/9,2) #Celsius
    return(f"humidity :{humidity},  temperature :{temperature}")


definitions = [
    {
        "name": "chat1", # name of the function to be called
        "description": "hi, hello ", # description
        "parameters":
        {
            "type": "object",
            "properties": 
            {
                "chat": {           # arguments for function temp_city
                    "type": "string",
                    "description": "full query asked by user"
                }
            }
        }
    },

    {
        "name": "temp_city", # name of the function to be called
        "description": "Get current weather, temperature data for a city.", # description
        "parameters":
        {
            "type": "object",
            "properties": 
            {
                "city": {           # arguments for function temp_city
                    "type": "string",
                    "description": "City name."
                }
            }
        }
    },

    {
        "name": "get_ip", # name of the function to be called
        "description": "Find the IP address of the given url or domain name", # description
        "parameters":
        {
            "type": "object",
            "properties": 
            {
                "host":
                {           # arguments for function temp_city
                    "type": "string",
                    "description": "get url or domain name"
                }
            }
        }
    }
]


if __name__ == "__main__":
    print(temp_city("gurugram"))
    #print(get_ip)
