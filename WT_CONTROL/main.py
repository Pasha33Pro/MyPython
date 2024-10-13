import speech_recognition as sr
import pyautogui as pag
from pynput.keyboard import Key, Controller
import time
import random

keyboard = Controller()


class DataInfo:
    def __init__(self):
        self.height = 0
        self.height_array = []


DI = DataInfo()


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите...")
        print("-" * 25)
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + zadanie + '.')
    except sr.UnknownValueError:
        zadanie = command()
    return zadanie


def makeSomething(zadanie):
    some_data = zadanie

    if 'на взлёт' in some_data or 'на взлет' in some_data or 'взлетаем' in some_data or 'взлетай' in some_data:
        keyboard.press(Key.shift)
        time.sleep(2)
        keyboard.release(Key.shift)
        time.sleep(5)
        keyboard.press('g')
        time.sleep(0.15)
        keyboard.release('g')
        time.sleep(3)

    elif 'отстрел' in some_data or 'лтц' in some_data or 'ltc' in some_data:
        keyboard.press('k')
        time.sleep(0.15)
        keyboard.release('k')
        time.sleep(0.15)
        keyboard.press('k')
        time.sleep(0.15)
        keyboard.release('k')
        time.sleep(0.15)
        keyboard.press('k')
        time.sleep(0.15)
        keyboard.release('k')
        time.sleep(0.15)
        keyboard.press('k')
        time.sleep(0.15)
        keyboard.release('k')
        time.sleep(0.15)
        keyboard.press('k')
        time.sleep(0.15)
        keyboard.release('k')

    elif 'зависни' in some_data or 'виси' in some_data or 'замри' in some_data or 'лети' in some_data or 'от висни' in some_data:
        keyboard.press('h')
        time.sleep(0.15)
        keyboard.release('h')

    elif 'ниже' in some_data or 'вниз' in some_data:
        keyboard.press(Key.ctrl_l)
        time.sleep(0.2)
        keyboard.release(Key.ctrl_l)
    elif 'очень низко' in some_data:
        keyboard.press(Key.ctrl_l)
        time.sleep(2)
        keyboard.release(Key.ctrl_l)

    elif 'выше' in some_data or 'вверх' in some_data:
        keyboard.press(Key.shift)
        time.sleep(0.2)
        keyboard.release(Key.shift)
    elif 'очень высоко' in some_data:
        keyboard.press(Key.shift)
        time.sleep(2)
        keyboard.release(Key.shift)

    elif 'ближе' in some_data or 'приблизь' in some_data or 'отдали' in some_data or 'дальше' in some_data:
        keyboard.press('z')
        time.sleep(0.15)
        keyboard.release('z')

    elif 'шасси' in some_data or 'колёса' in some_data or 'колеса' in some_data:
        keyboard.press('g')
        time.sleep(0.15)
        keyboard.release('g')

    elif 'выключи двигатель' in some_data or 'выключи' in some_data:
        keyboard.press(Key.ctrl_l)
        time.sleep(0.2)
        keyboard.release(Key.ctrl_l)
        time.sleep(0.15)
        keyboard.press('i')
        time.sleep(5)
        keyboard.release('i')

    elif 'включи двигатель' in some_data or 'запусти двигатель' in some_data:
        keyboard.press(Key.shift)
        time.sleep(2)
        keyboard.release(Key.shift)
        time.sleep(0.15)
        keyboard.press('i')
        time.sleep(5)
        keyboard.release('i')

    elif 'захват' in some_data or 'захвати' in some_data:
        keyboard.press('f')
        time.sleep(0.15)
        keyboard.release('f')

    elif 'огонь' in some_data or 'стреляй' in some_data:
        keyboard.press('1')
        time.sleep(4)
        keyboard.release('1')

    elif 'пушки' in some_data:
        keyboard.press('2')
        time.sleep(2)
        keyboard.release('2')

    elif 'ракета' in some_data:
        keyboard.press('4')
        time.sleep(0.15)
        keyboard.release('4')

    elif 'залп' in some_data:
        keyboard.press('4')
        time.sleep(0.15)
        keyboard.release('4')
        time.sleep(0.15)
        keyboard.press('4')
        time.sleep(0.15)
        keyboard.release('4')
        time.sleep(0.15)
        keyboard.press('4')
        time.sleep(0.15)
        keyboard.release('4')
        time.sleep(0.15)
        keyboard.press('4')
        time.sleep(0.15)
        keyboard.release('4')

    elif 'птур' in some_data:
        keyboard.press(Key.space)
        time.sleep(0.15)
        keyboard.release(Key.space)

    elif 'вираж' in some_data:
        choose = random.randint(1, 2)
        if choose == 1:
            keyboard.press('a')
            time.sleep(5)
            keyboard.release('a')
        else:
            keyboard.press('d')
            time.sleep(5)
            keyboard.release('d')
    elif some_data == 'стоп' or some_data == 'хватит':
        exit(0)

    else:
        print('Чего чего?')
    '''
    elif some_data == 'назад' or some_data == 'обратно':
        print('backward')
    '''



while True:
    makeSomething(command())
