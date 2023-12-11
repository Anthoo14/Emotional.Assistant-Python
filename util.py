#Obtener el mensaje que está siendo enviado por el usuario, para verificar que tipo de mensaje es.
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
        print("sin mensaje")

    return text

#JSON del mensaje que contiene solo letras
def TextMessage(text, number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {"body": text},
    }
    return data


#JSON del mensaje que envia texto e imagen
def MultimediaMessage(text, number, image_url):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "image",
        "image": {
            "link": {
                "url": image_url,
            },
            "caption": text,  # Aquí agregamos el texto como pie de foto de la imagen
        }
    }
    return data



#JSON del mensaje en diferentes estilos
def TextFormatMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {"body": " *hola* - _hola_ - ~hola~ - ```hola``` "},
    }
    return data


#JSON para enviar imagenes
def ImageMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "image",
        "image": {
            "link": "https://user-images.githubusercontent.com/138251036/278851167-db190f85-773b-4d78-a208-05fa3b169424.JPG"
        },
    }
    return data

#JSON para enviar audios
def AudioMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "audio",
        "audio": {
            "link": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        },
    }
    return data

#JSON para enviar videos
def VideoMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "video",
        "video": {
            "link": "https://media.istockphoto.com/id/1150321396/es/v%C3%ADdeo/leisure-lagoon.mp4?s=mp4-640x640-is&k=20&c=EA7WI5ABp1Xb5KDn3cD3cYi5SSbMcMxXddMe_LowdeA="
        },
    }
    return data

#JSON para enviar documentos
def DocumentMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "document",
        "document": {
            "link": "https://www.uma.es/ejemplo-grupo-de-investigacion/navegador_de_ficheros/repositorio-grupos-de-investigacion/descargar/documentaci%C3%B3n%20becas%20junta/documento%20de%20prueba.pdf"
        },
    }
    return data

#JSON para enviar una ubicacion
def LocationMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "location",
        "location": {
            "latitude": "-14.071508899756285",
            "longitude": "-75.73580787106545",
            "name": "Utp Ica",
            "address": "Av. Ayabaca S/N, Sector San José, al costado de la SUNAT, Ica 11001",
        },
    }
    return data

#JSON para enviar botones
def ButtonMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {"text": "¿Como te sientes en estos momentos? 🔍"},
            "action": {
                "buttons": [
                    {"type": "reply", "reply": {"id": "001", "title": "😃 Bien"}},
                    {"type": "reply", "reply": {"id": "002", "title": "😔 Mal"}},
                ]
            },
        },
    }
    return data

#JSON para enviar una lista con mensajes predeterminados
def ListMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {"text": "✅ Tienes estas opciones"},
            "footer": {"text": "Selecciona una de ellas"},
            "action": {
                "button": "Ver opciones",
                "sections": [
                    {
                        "title": "",
                        "rows": [
                            {
                                "id": "main-1",
                                "title": "Manejo del Estrés"
                            },
                            {
                                "id": "main-2",
                                "title": "Crisis o Emergencia"
                            },
                            {
                                "id":"main-3",
                                "title": "hablar con un asesor"
                            },
                            {
                                "id":"main-4",
                                "title": "Relaciones sanas"
                            },
                            {
                                "id":"main-5",
                                "title": "Tu Bienestar"
                            },
                            {
                                "id":"main-6",
                                "title": "Consejos"
                            },   
                        ],
                    },
                ],
            },
        },
    }
    return data