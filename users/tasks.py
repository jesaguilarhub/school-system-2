from school_system.celery import app
from django.core.mail import send_mail

@app.task(name='send_email')
def send_email():
    send_mail(
        subject='Un nuevo usuario ha sido registrado',
        message=f'Se ha registrado el usario',
        from_email='hola@biblioteca.com',
        recipient_list=[],
        html_message=f'<h1>Un nuevo usuario ha sido creado.</h1>'
    )