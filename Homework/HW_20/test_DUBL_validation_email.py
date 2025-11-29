import pytest
from validation import validate_email

@pytest.mark.parametrize('email', [
    ("testexample.com"),
    ("invalid"),
])
def test_email_1(email):
    with pytest.raises(ValueError, match='Email must contain @'):
        validate_email(email)


@pytest.mark.parametrize('email', [
    ("no@dot"),
    ("user@"),
    ('user@domain')
])
def test_email_2(email):
    with pytest.raises(ValueError, match='Email must have domain with dot'):
        validate_email(email)

@pytest.mark.parametrize('email', [
    ('test@example.com'),
    ("user@gmail.com"),
    ('hello@domain.co.uk')
])
def test_email_3(email):
    assert validate_email(email) == True


# Функция для валидации email
# def validate_email(email):
#     if "@" not in email:
#         raise ValueError("Email must contain @")
#     if "." not in email.split("@")[-1]:
#         raise ValueError("Email must have domain with dot")
#     return True