import vosk
import pyaudio
import json
from pynput.keyboard import Key, Controller
import time
import random
import threading
from vosk import SetLogLevel

SetLogLevel(-1)

keyboard = Controller()


def command():
    model = vosk.Model("model-ru")
    recognizer = vosk.KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

    print("Говорите...")
    print("-" * 25)

    stream.start_stream()

    try:
        while True:
            data = stream.read(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                result_json = json.loads(result)
                zadanie = result_json["text"].lower()
                print("Вы сказали: " + zadanie + '.')
                return zadanie
    except KeyboardInterrupt:
        pass


def get_task():
    while True:
        zadanie = command()
        some_data = zadanie

        if 'на взлёт' in some_data or 'на взлет' in some_data or 'взлетаем' in some_data or 'взлетай' in some_data:
            threading.Thread(target=take_off).start()

        elif 'защита' in some_data or 'лтц' in some_data or 'ltc' in some_data or 'отстрел' in some_data:
            threading.Thread(target=ltc).start()

        elif 'зависни' in some_data or 'виси' in some_data or 'замри' in some_data or 'лети' in some_data or 'от висни' in some_data or 'на месте' in some_data:
            threading.Thread(target=hang).start()

        elif 'вираж' in some_data or 'крути' in some_data:
            threading.Thread(target=turn).start()

        elif 'ниже' in some_data or 'вниз' in some_data:
            threading.Thread(target=get_down).start()
        elif 'очень низко' in some_data:
            threading.Thread(target=get_down_down).start()

        elif 'выше' in some_data or 'вверх' in some_data:
            threading.Thread(target=get_up).start()
        elif 'очень высоко' in some_data:
            threading.Thread(target=get_up_up).start()

        elif 'шасси' in some_data or 'колёса' in some_data or 'колеса' in some_data:
            threading.Thread(target=get_wheels).start()

        elif 'захват' in some_data or 'захвати' in some_data:
            threading.Thread(target=get_focus).start()

        elif 'огонь' in some_data or 'стреляй' in some_data or 'стрелок' in some_data:
            threading.Thread(target=get_shoot).start()
        elif 'пушки' in some_data:
            threading.Thread(target=get_guns).start()
        elif 'ракета' in some_data:
            threading.Thread(target=get_rocket).start()
        elif 'ракеты' in some_data or 'залп' in some_data:
            threading.Thread(target=get_rockets).start()
        elif 'пуск' in some_data or 'птур' in some_data or 'земля' in some_data:
            threading.Thread(target=get_ptyr).start()

        elif 'ближе' in some_data or 'приблизь' in some_data or 'отдали' in some_data or 'дальше' in some_data or 'приблизить' in some_data:
            threading.Thread(target=get_zoom).start()
        elif 'стоп' in some_data or 'хватит' in some_data:
            exit('done')


def take_off():
    keyboard.press(Key.shift)
    time.sleep(2)
    keyboard.release(Key.shift)


def ltc():
    for _ in range(6):
        keyboard.press('k')
        time.sleep(0.15)
        keyboard.release('k')
        time.sleep(0.15)


def hang():
    keyboard.press('h')
    time.sleep(0.15)
    keyboard.release('h')


def turn():
    choose = random.randint(1, 3)
    if choose == 1:
        keyboard.press('a')
        time.sleep(5)
        keyboard.release('a')
    elif choose == 2:
        keyboard.press('d')
        time.sleep(5)
        keyboard.release('d')
    else:
        keyboard.press('s')
        time.sleep(7)
        keyboard.release('s')


def get_move(turn):
    keyboard.press(turn)
    time.sleep(5)
    keyboard.release(turn)


# ------- ВНИЗ ------- #
def get_down():
    keyboard.press(Key.ctrl_l)
    time.sleep(0.2)
    keyboard.release(Key.ctrl_l)


def get_down_down():
    keyboard.press(Key.ctrl_l)
    time.sleep(2)
    keyboard.release(Key.ctrl_l)


# ------- ВВЕРХ ------- #
def get_up():
    keyboard.press(Key.shift)
    time.sleep(0.2)
    keyboard.release(Key.shift)


def get_up_up():
    keyboard.press(Key.shift)
    time.sleep(2)
    keyboard.release(Key.shift)


def get_wheels():
    keyboard.press('g')
    time.sleep(0.15)
    keyboard.release('g')


def get_focus():
    keyboard.press('f')
    time.sleep(0.15)
    keyboard.release('f')


def get_shoot():
    keyboard.press('1')
    time.sleep(4)
    keyboard.release('1')


def get_guns():
    keyboard.press('2')
    time.sleep(2)
    keyboard.release('2')


def get_rocket():
    keyboard.press('4')
    time.sleep(0.15)
    keyboard.release('4')


def get_rockets():
    for _ in range(5):
        keyboard.press('4')
        time.sleep(0.15)
        keyboard.release('4')
        time.sleep(0.15)


def get_ptyr():
    keyboard.press(Key.space)
    time.sleep(0.15)
    keyboard.release(Key.space)


def get_zoom():
    keyboard.press('z')
    time.sleep(0.15)
    keyboard.release('z')


get_task()
