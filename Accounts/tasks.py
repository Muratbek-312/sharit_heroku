from django.core.mail import send_mail
from Sharit.celery import app

@app.task
def send_activation_mail(user):
    code = user.create_activation_code()
    send_mail('Активация аккаунта', f'Вы успешно зарегистрировались. Пожалуйста автивируйте свой аккаунт. Для этого пройдите по ссылке http://127.0.0.1:8000/account/activate/{code}/',
              'Murat@test.com',
              [user.email, ])