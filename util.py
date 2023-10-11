def GetTextUser(message):
    text = ""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]
        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")    

    else:
        print ("sin mensaje")

    return text        


def TextMessage(text, number):
    data = {
    "messaging_product": "whatsapp",
    "to": number,
    "type": "text",
    "text": {
      "body": text
    }
}
    return data

def TextFormatMessage(number):
    data ={
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {
        "body": " *hola* - _hola_ - ~hola~ - ```hola``` "
        }}
    return data



def ImageMessage(number):
    data ={
        "messaging_product": "whatsapp",
        "to": number,
        "type": "image",
        "image": {
            "link": "https://imgs.search.brave.com/C-DnW3dZHGbutMvVebRkoDkhMjBhpFMowldif9GvX9E/rs:fit:860:0:0/g:ce/aHR0cDovL3N0YXRp/Yy5pcGF1dGEuY29t/L3VwbG9hZHMvMjAy/Mi8wNC9Nb3JhLU1p/Y3JvZG9zaXMtRnJv/bnRhbC1pUGF1dGEu/anBn"
        }}
    return data

def AudioMessage(number):
    data ={
    "messaging_product": "whatsapp",
    "to": number,
    "type": "audio",
    "audio": {
        "link": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    }
}
    return data


def VideoMessage(number):
    data ={
        "messaging_product": "whatsapp",
        "to": number,
        "type": "video",
        "video": {
            "link": "https://media.istockphoto.com/id/1150321396/es/v%C3%ADdeo/leisure-lagoon.mp4?s=mp4-640x640-is&k=20&c=EA7WI5ABp1Xb5KDn3cD3cYi5SSbMcMxXddMe_LowdeA="
        }}
    return data

def DocumentMessage(number):
    data ={
        "messaging_product": "whatsapp",
        "to": number,
        "type": "document",
        "document": {
            "link": "https://www.uma.es/ejemplo-grupo-de-investigacion/navegador_de_ficheros/repositorio-grupos-de-investigacion/descargar/documentaci%C3%B3n%20becas%20junta/documento%20de%20prueba.pdf"
        }}
    return data

def LocationMessage(number):
    data ={
    "messaging_product": "whatsapp",
    "to": number,
      "type": "location",
    "location": {
        "latitude" : "-14.071508899756285",
        "longitude" : "-75.73580787106545",
        "name" : "Utp Ica",
        "address" : "Av. Ayabaca S/N, Sector San José, al costado de la SUNAT, Ica 11001"
    }
}
    return data