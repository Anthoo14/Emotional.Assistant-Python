from flask import Flask, request
import util
import whatsappService
import texts

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

    if "hola" in text or "option" in text:
        text1=texts.obtener_saludo()
        data=util.TextMessage(text1, number)
        dataMenu=util.ListMessage(number)

        listData.append(data)
        listData.append(dataMenu)

    elif "gracias" in text:
        text2=texts.obtener_despedida()
        data=util.TextMessage(text2, number)
        listData.append(data)

    elif "manejo del estrés" in text:
        text3=texts.obtener_consejos_de_manejo_de_estres()
        data=util.TextMessage(text3, number)
        listData.append(data)

    elif "crisis o emergencia" in text:
        data=util.TextMessage('''*Comunicate con estos numeros si estas presentando una crisis:*
                                  *Servicio de Orientación y Consejería Telefónica en Salud – Infosalud:* 0800-10828
                                    ''',number)
        listData.append(data)

    elif "hablar con un asesor" in text:
        text5= texts.obtener_asesor()
        data=util.TextMessage(text5, number)
        listData.append(data)

    elif "relaciones sanas" in text:
        text6=texts.obtener_consejo_relaciones_sanas()
        data=util.TextMessage(text6, number)  
        
        listData.append(data)      

    elif "tu bienestar" in text:
        data=util.TextMessage("*Numero de contacto:* \n 381-3695", number)  
        listData.append(data)   


    else:
        text8=texts.obtener_error()
        data = util.TextMessage(text8, number)
        dataMenu = util.ListMessage(number)
        listData.append(data)
        listData.append(dataMenu)

    for item in listData:
        whatsappService.SendMessageWhatsapp(item) 




    
def GenerateMessage(text, number):


    text=text.lower()
    if "text" in text:
        data = util.TextMessage("Text", number)
    if "format" in text:
        data = util.TextFormatMessage(number)

    if "image" in text:
        data = util.ImageMessage(number)
    if "video" in text:
        data = util.VideoMessage(number)
    if "audio" in text:
        data = util.AudioMessage(number)
    if "document" in text:
        data = util.DocumentMessage(number)
    if "location" in text:
        data = util.LocationMessage(number)
    if "button" in text:
        data = util.ButtonMessage(number)    
    if "list" in text:
        data= util.ListMessage(number) 


    whatsappService.SendMessageWhatsapp(data)



if __name__ == "__main__":
    app.run()
