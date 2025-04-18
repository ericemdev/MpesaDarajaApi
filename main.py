import requests
import base64
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth


load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")

print("KEY:", consumer_key)
print("SECRET:", consumer_secret)


if not consumer_key or not consumer_secret:
    raise Exception("consumer Key or Secret not found")


credentials = f" {consumer_key} : {consumer_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode("utf-8")

url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"


response = requests.get(url, auth=HTTPBasicAuth(consumer_key, consumer_secret))


# Parse the JSON response
if response.status_code == 200:
    access_token = response.json().get("access_token")
    expires_in = response.json().get("expires_in")
    print(f"Your Access Token✅✅✅: {access_token}")
    print(f"⏳ Expires In: {expires_in} seconds")
else:
    print(f"Failed to get access token. Status Code: {response.status_code}")
    print("Response:", response.text)