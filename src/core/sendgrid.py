import requests

API_KEY = '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'

def send(destination, subject, message):

    post = requests.post(
        "https://api.sendgrid.com/v3/mail/send",
        headers={
            "Authorization": "Bearer " + API_KEY,
            "Content-Type": "application/json"
        },
        json = {
            "personalizations": [ {
                "to": [ { "email": destination } ],
                "subject": subject
            } ],

            "from": {
                "email": "nao-responda@rotafestival.com",
                "name": "ROTA - Festival de Roteiro Audiovisual"
            },

            "content": [ {
                "type": "text/html",
                "value": message
            } ]
        }

    )

