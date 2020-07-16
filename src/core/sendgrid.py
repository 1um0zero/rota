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
                "email": "rotafestival@gmail.com",
                "name": "ROTA - Festival de Roteiro Audiovisual"
            },

            "content": [ {
                "type": "text/html",
                "value": message
            } ]
        }

    )

