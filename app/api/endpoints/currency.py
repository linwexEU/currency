from app.config import settings
import requests
import json


class Currency: 

    @classmethod
    def currency_data_list(cls): 
        url = "https://api.apilayer.com/currency_data/list"

        payload = {}
        headers= {
        "apikey": settings.APIKEY
        }

        response = requests.request("GET", url, headers=headers, data = payload)
        currencies = json.dumps(response.text, indent=4)

        return json.loads(json.loads(currencies))["currencies"]
    

    @classmethod
    def convert_currency(cls, to, from_, amount):
        url = f"https://api.apilayer.com/currency_data/convert?to={to}&from={from_}&amount={amount}"

        payload = {}
        headers= {
        "apikey": settings.APIKEY
        }

        response = requests.request("GET", url, headers=headers, data = payload)
        result = json.dumps(response.text, indent=4)
        
        return json.loads(json.loads(result))
    

if __name__ == "__main__": 
    print(Currency.currency_data_list())








