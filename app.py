from flask import Flask, request
import util
import whatsappService
import texts
import random

app = Flask(__name__)


@app.route("/Welcome", methods=["GET"])
def index():
    return "Welcome Sr."

#metodo para verificar el token de whatsapp generado.
@app.route("/Whatsapp", methods=["GET"])
def VerifyToken():
    try:
        accessToken = "NDSVIH30R910FN1D103DN13J41FD1D"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "", 400
    except:
        return "", 400



#metodo para recibir todo el cuerpo del mensaje en whatsapp
@app.route("/Whatsapp", methods=["POST"])
def ReceivedMessage():
    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]

        text = util.GetTextUser(message)

       # ResponseGPT = chatgptService.GetResponse(text)
        #if ResponseGPT != "error":
         #   data = util.TextMessage(ResponseGPT,number)
        #else:
         #   data= util.TextMessage("Lo siento, ocurrio un problema",number) 

          #  whatsappService.SendMessageWhatsapp(data) 

        ProcessMesage(text, number)
        print(text)

        return "EVENT_RECEIVED"
    except:
        return "EVENT_RECEIVED"


def ProcessMesage(text, number):

    text= text.lower()
    listData = []

    if any(keyword in text for keyword in texts.saludo):
        text1 = random.choice(texts.resp_saludo)
        data = util.TextMessage(text1, number)
        listData.append(data)
    
    elif any(keyword in text for keyword in texts.gracias):
        text2 = random.choice(texts.agradecer)
        data = util.TextMessage(text2, number)
        data_image = util.ImageMessage(number)
        listData.append(data)
        listData.append(data_image)

    elif any(keyword in text for keyword in texts.estado_animo_bueno):
        text3=random.choice(texts.resp_animo_bueno)
        data= util.TextMessage(text3,number)
        listData.append(data)

    elif any(keyword in text for keyword in texts.html):
        text9 = random.choice(texts.resp_html)
        data = util.TextMessage(text9, number)
        listData.append(data)

    elif any(keyword in text for keyword in texts.estado_animo_malo):
        text4=random.choice(texts.resp_animo_malo)
        data= util.TextMessage(text4,number)
        listData.append(data)
        
    elif any(keyword in text for keyword in texts.option1):
        text5=random.choice(texts.resp_option1)
        data=util.TextMessage(text5, number)
        listData.append(data) 
    
    elif any(keyword in text for keyword in texts.test):
        text13=random.choice(texts.test1)
        data=util.TextMessage(text13, number)
        listData.append(data) 

    elif any(keyword in text for keyword in texts.option2):
        text6=random.choice(texts.resp_option2)
        data=util.TextMessage(text6, number)
        listData.append(data)

    elif any(keyword in text for keyword in texts.option3):
        text7=random.choice(texts.resp_option3)
        data=util.TextMessage(text7, number)
        listData.append(data) 

    elif any(keyword in text for keyword in texts.option4):
        text8=random.choice(texts.resp_option4)
        data=util.TextMessage(text8, number)
        listData.append(data)  

    elif any(keyword in text for keyword in texts.option5):
        text10=random.choice(texts.resp_option5)
        data=util.TextMessage(text10, number)
        listData.append(data)  

    elif any(keyword in text for keyword in texts.option6):
        text11=random.choice(texts.resp_option1)
        data=util.TextMessage(text11, number)
        listData.append(data)        
        
    else:
        error=random.choice(texts.error)
        data = util.TextMessage(error, number)
        dataMenu = util.ListMessage(number)
        listData.append(data)
        listData.append(dataMenu)

    for item in listData:
        whatsappService.SendMessageWhatsapp(item) 





if __name__ == "__main__":
    app.run()



    
# def GenerateMessage(text, number):


#     text=text.lower()
#     if "text" in text:
#         data = util.TextMessage("Text", number)
#     if "format" in text:
#         data = util.TextFormatMessage(number)
#     if "image" in text:
#         data = util.ImageMessage(number)
#     if "video" in text:
#         data = util.VideoMessage(number)
#     if "audio" in text:
#         data = util.AudioMessage(number)
#     if "document" in text:
#         data = util.DocumentMessage(number)
#     if "location" in text:
#         data = util.LocationMessage(number)
#     if "button" in text:
#         data = util.ButtonMessage(number)    
#     if "list" in text:
#         data= util.ListMessage(number) 


#     whatsappService.SendMessageWhatsapp(data)
