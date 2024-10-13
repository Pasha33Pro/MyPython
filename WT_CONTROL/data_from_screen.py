import easyocr
import pyautogui


class DataInfo:
    def __init__(self):
        self.height = 0
        self.height_array = []


DI = DataInfo()


def screen():
    pyautogui.screenshot('height.png', region=(1180, 520, 100, 40))


def text_recognition(file_path):
    reader = easyocr.Reader(['ru'])
    res = reader.readtext(file_path, detail=0)
    for i in res:
        try:
            DI.height_array.append(i)
        except Exception:
            pass
    print(DI.height_array)
    DI.height = int(DI.height_array[0])
    print(DI.height)




if __name__ == '__main__':
    screen()
    text_recognition('height.png')