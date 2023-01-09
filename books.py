import requests
import os
os.system("cls")

response = requests.get("https://docs.google.com/document/d/1ScZYzuyiMooBidLtG3fR2x0gKnNOV_fRNG1SioNM7No/edit#heading=h.rfhe1kzd7pnw")
request = response.request

