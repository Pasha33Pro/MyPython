import speech_recognition

array = [1]
print(array.index(1))
r = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Говорите...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language="ru-RU")
    print("Вы сказали:", text)
except speech_recognition.UnknownValueError:
    print("Не удалось распознать речь")
except speech_recognition.RequestError as error:
    print(f"Ошибка сервиса распознавания речи; {error}")



a = """
N = []
a = 7

for k in range(a):
    N.append(int(input("Введите число: ")))

for k in N:
    print(k, end=" - ")
    if k > 0:
        print('Положительное число')
    elif k < 0:
        print('Отрицательное число')
    else:
        print('Число равно 0')
"""
