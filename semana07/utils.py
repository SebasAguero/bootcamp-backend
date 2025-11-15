import smtplib
from os import environ
from email.message import EmailMessage

def enviarCorreoDeValidacion(destinatarios, token):
    SMTP_HOST = 'smtp.gmail.com'
    # Correo         Servidor               Puerto
    # OUTLOOK        smtp-mail.outlook.com  587
    # GMAIL          smtp.gmail.com         587
    # APPLE          smtp.mail.me.com       587
    # YAHOO          smtp.mail.yahoo.com    587

    SMTP_PORT = 587
    USER = environ.get('EMAIL_USERNAME')
    PASSWORD = environ.get('EMAIL_PASSWORD')

    msg = EmailMessage()
    # Titulo del correo
    msg['Subject'] = 'Validacion de Registro'
    # Emisor del correo
    msg['From'] = USER
    # Destinarios del correo
    msg['To'] = destinatarios
    # Contenido
    msg.set_content('''Bienvenido a la aplicación mas chevere de todas. 
                    Por favor, haz click en el siguiente enlace para validar tu cuenta: http://127.0.0.1:5000/validar-usuario?token={}'''.format(token))

    # Adicional a ello podemos agregar un html si el servidor de correos del destinatario lo permite
    msg.add_alternative('''
<html>
    <body>
        <h3>Bienvenido a la aplicación mas chévere de todas!</h3>
        <p>Por favor, haz click en el siguiente <a href="http://127.0.0.1:5000/validar-usuario?token={}">enlace</a> para validar tu cuenta.</p>
    </body>
</html>'''.format(token), subtype='html')

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        # Aca enviamos el correo
        smtp.starttls()
        smtp.login(USER, PASSWORD)
        smtp.send_message(msg)