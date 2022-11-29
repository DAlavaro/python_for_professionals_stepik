
def phone(text):
    if r'\d-\d{3}-\d{3}-\d{2}-d{2}' in text:
        yield 1




text = 'Перезвони мне, пожалуйста: 7-919-667-21-19'
print(list(phone(text)))