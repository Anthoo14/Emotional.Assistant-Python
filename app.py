from flask import Flask, request 

app = Flask(__name__)
@app.route('/Welcome', methods=['GET'])
def index():
    return "Welcome Sr."

@app.route('/Whatsapp', methods=['GET'])
def VerifyToken():

 try:
    accessToken= "NDSVIH30R910FN1D103DN13J41FD1D"
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token != None and challenge != None and token == accessToken:
        return challenge
    else:
        return "", 400
 except:
    return "",400
  

@app.route('/Whatsapp', methods=['POST'])
def ResiveMrssage():
    return "recived message"

if(__name__ == "__main__"):
    app.run()