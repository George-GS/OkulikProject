# Функция для валидации email
def validate_email(email):
    if "@" not in email:
        raise ValueError("Email must contain @")
    if "." not in email.split("@")[-1]:
        raise ValueError("Email must have domain with dot")
    return True