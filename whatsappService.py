import requests
import json

def SendMessageWhatsapp(data):
    try:
      
        token = "EAAYwUiJnzrcBO2UT1rvgOBQizLGH9JJ7aZAZBce8tcO24IKS1bIFsudWikZClUsLg7kPbkZAtEENjHf5DMX63FrGXt8r5wSdQVPun4x1eSDKLqT6H7NYNLYEgXmJatxFLX90O2yJ38lNZADiOtYjajlsursRZASHwUZBsnx9YzcL3BFSxxyopLsSusYjPx3QZArXnfwAdSa0ZCgqzYXxo"
        api_url = "https://graph.facebook.com/v17.0/100397936499756/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)
        if response.status_code == 200:
            return True
        
        return False
    except Exception as exception:
        print(exception)
        return False