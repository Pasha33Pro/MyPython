from ultralytics import YOLO
import cv2
import numpy as np
import time
from PIL import Image, ImageDraw, ImageFont
import os

# Загрузка модели YOLOv8
model = YOLO('yolov8n.pt')

# Словарь для перевода английских названий классов на русский
class_names_ru = {
    'person': 'Человек',
    'bicycle': 'Велосипед',
    'car': 'Автомобиль',
    'motorcycle': 'Мотоцикл',
    'airplane': 'Самолет',
    'bus': 'Автобус',
    'train': 'Поезд',
    'truck': 'Грузовик',
    'boat': 'Лодка',
    'traffic light': 'Светофор',
    'fire hydrant': 'Пожарный гидрант',
    'stop sign': 'Знак "Стоп"',
    'parking meter': 'Парковочный счетчик',
    'bench': 'Скамейка',
    'bird': 'Птица',
    'cat': 'Кошка',
    'dog': 'Собака',
    'horse': 'Лошадь',
    'sheep': 'Овца',
    'cow': 'Корова',
    'elephant': 'Слон',
    'bear': 'Медведь',
    'zebra': 'Зебра',
    'giraffe': 'Жираф',
    'backpack': 'Рюкзак',
    'umbrella': 'Зонт',
    'handbag': 'Сумка',
    'tie': 'Галстук',
    'suitcase': 'Чемодан',
    'frisbee': 'Фрисби',
    'skis': 'Лыжи',
    'snowboard': 'Сноуборд',
    'sports ball': 'Спортивный мяч',
    'kite': 'Воздушный змей',
    'baseball bat': 'Бейсбольная бита',
    'baseball glove': 'Бейсбольная перчатка',
    'skateboard': 'Скейтборд',
    'surfboard': 'Серфборд',
    'tennis racket': 'Теннисная ракетка',
    'bottle': 'Бутылка',
    'wine glass': 'Бокал',
    'cup': 'Кружка',
    'fork': 'Вилка',
    'knife': 'Нож',
    'spoon': 'Ложка',
    'bowl': 'Миска',
    'banana': 'Банан',
    'apple': 'Яблоко',
    'sandwich': 'Бутерброд',
    'orange': 'Апельсин',
    'broccoli': 'Брокколи',
    'carrot': 'Морковь',
    'hot dog': 'Хот-дог',
    'pizza': 'Пицца',
    'donut': 'Пончик',
    'cake': 'Торт',
    'chair': 'Стул',
    'couch': 'Диван',
    'potted plant': 'Комнатное растение',
    'bed': 'Кровать',
    'dining table': 'Обеденный стол',
    'toilet': 'Унитаз',
    'tv': 'Телевизор',
    'laptop': 'Ноутбук',
    'mouse': 'Мышь',
    'remote': 'Пульт',
    'keyboard': 'Клавиатура',
    'cell phone': 'Телефон',
    'microwave': 'Микроволновка',
    'oven': 'Духовка',
    'toaster': 'Тостер',
    'sink': 'Раковина',
    'refrigerator': 'Холодильник',
    'book': 'Книга',
    'clock': 'Часы',
    'vase': 'Ваза',
    'scissors': 'Ножницы',
    'teddy bear': 'Плюшевый мишка',
    'hair drier': 'Фен',
    'toothbrush': 'Зубная щетка'
}

# Список цветов для различных классов
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255),
    (255, 0, 255), (192, 192, 192), (128, 128, 128), (128, 0, 0), (128, 128, 0),
    (0, 128, 0), (128, 0, 128), (0, 128, 128), (0, 0, 128), (72, 61, 139),
    (47, 79, 79), (47, 79, 47), (0, 206, 209), (148, 0, 211), (255, 20, 147)
]


# Функция для отрисовки русского текста
def put_ru_text(image, text, position, font_size=20, color=(0, 255, 0)):
    # Создаем копию изображения
    img_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)

    # Определяем путь к шрифту в зависимости от ОС
    font_path = ""
    if os.name == 'nt':  # Windows
        font_path = "C:/Windows/Fonts/arial.ttf"
    elif os.name == 'posix':  # Linux/Mac
        # Проверяем возможные пути для Linux
        if os.path.exists('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'):
            font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
        elif os.path.exists('/usr/share/fonts/truetype/freefont/FreeSans.ttf'):
            font_path = '/usr/share/fonts/truetype/freefont/FreeSans.ttf'
        # Для Mac
        elif os.path.exists('/System/Library/Fonts/SFNSText.ttf'):
            font_path = '/System/Library/Fonts/SFNSText.ttf'
        elif os.path.exists('/System/Library/Fonts/Supplemental/Arial Unicode.ttf'):
            font_path = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'

    # Если не нашли системный шрифт, используем шрифт из проекта
    if not font_path or not os.path.exists(font_path):
        # Создаем временный шрифт
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
    else:
        try:
            font = ImageFont.truetype(font_path, font_size)
        except:
            font = ImageFont.load_default()

    # Рисуем текст
    draw.text(position, text, font=font, fill=(color[2], color[1], color[0]))  # PIL использует RGB, OpenCV - BGR

    # Конвертируем обратно в формат OpenCV
    img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    return img


# Открытие веб-камеры
capture = cv2.VideoCapture(0)

# Проверка, открыта ли камера
if not capture.isOpened():
    print("Не удалось открыть веб-камеру")
    exit()

# Чтение параметров видео
fps = int(capture.get(cv2.CAP_PROP_FPS))
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Настройка выходного файла (если нужно сохранять видео)
output_video_path = 'detect.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter(output_video_path, fourcc, fps, (1000, 800))  # Установка размера выходного видео

# Параметры для плавности
conf_threshold = 0.48  # Увеличенный порог вероятности
frame_skip = 1  # Обрабатывать каждый кадр
frame_counter = 0  # Счетчик кадров для пропуска

# Переменные для отслеживания FPS
prev_frame_time = 0
curr_frame_time = 0

# Создание окна для отображения
cv2.namedWindow('YOLOv8 Webcam Detection')


# Функция для обработки трекбара порога уверенности
def set_confidence_threshold(val):
    global conf_threshold
    conf_threshold = val / 100.0


# Функция для обработки трекбара пропуска кадров
def set_frame_skip(val):
    global frame_skip
    frame_skip = max(1, val)


# Создание трекбаров
cv2.createTrackbar('Confidence', 'YOLOv8 Webcam Detection', int(conf_threshold * 100), 100, set_confidence_threshold)
cv2.createTrackbar('Frame Skip', 'YOLOv8 Webcam Detection', frame_skip, 10, set_frame_skip)

print("Нажмите 'q' для выхода")

while True:
    # Захват кадра
    ret, frame = capture.read()
    if not ret:
        print("Не удалось получить кадр")
        break

    # Изменение размера кадра до 1000x800
    frame_resized = cv2.resize(frame, (1000, 800), interpolation=cv2.INTER_LINEAR)

    # Рассчет FPS
    curr_frame_time = time.time()
    fps_value = 1 / (curr_frame_time - prev_frame_time) if prev_frame_time != 0 else 0
    prev_frame_time = curr_frame_time

    # Отображение FPS в окне (используем стандартный putText, так как это латиница)
    cv2.putText(frame_resized, f"FPS: {int(fps_value)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Пропуск кадров в соответствии с настройкой
    frame_counter += 1
    if frame_counter % frame_skip != 0:
        # Отображение кадра без обработки
        cv2.imshow('YOLOv8 Webcam Detection', frame_resized)

        # Запись необработанного кадра в выходной файл
        writer.write(frame_resized)

        # Проверка на выход
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    # Обработка кадра с помощью модели YOLO с отслеживанием объектов
    results = model.track(frame_resized, persist=True, conf=conf_threshold, iou=0.5)[0]

    # Получение данных об объектах
    classes_names = results.names
    boxes = results.boxes.xyxy.cpu().numpy().astype(np.int32)
    confs = results.boxes.conf.cpu().numpy()

    # Получение ID отслеживаемых объектов
    track_ids = results.boxes.id.cpu().numpy().astype(int) if results.boxes.id is not None else None

    # Обработка и отрисовка объектов
    for i, (box, conf) in enumerate(zip(boxes, confs)):
        x1, y1, x2, y2 = box
        class_id = int(results.boxes.cls[i].item())
        class_name_en = classes_names[class_id]

        # Получаем русское название класса, если оно есть в словаре, иначе используем английское
        class_name_ru = class_names_ru.get(class_name_en, class_name_en)

        color = colors[class_id % len(colors)]

        # Рисование рамки
        cv2.rectangle(frame_resized, (x1, y1), (x2, y2), color, 2)

        # Формируем текст для отображения
        label = f"{class_name_ru} {conf:.2f}"
        if track_ids is not None:
            label += f" ID:{track_ids[i]}"

        # Используем нашу функцию для русского текста
        frame_resized = put_ru_text(frame_resized, label, (x1 + 10, y1 + 10), font_size=16, color=color)

    # Запись обработанного кадра в выходной файл
    writer.write(frame_resized)

    # Отображение кадра
    cv2.imshow('YOLOv8 Webcam Detection', frame_resized)

    # Выход по нажатию 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов и закрытие окон
capture.release()
writer.release()
cv2.destroyAllWindows()
