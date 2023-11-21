from django.core.validators import RegexValidator

DriverNameValidator = RegexValidator(r'^[a-zA-Zа-яА-Я ]+$', 
                                     message="Введите только имя без цифр и символов !;№@")