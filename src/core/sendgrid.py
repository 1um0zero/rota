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

