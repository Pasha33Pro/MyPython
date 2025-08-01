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
    'person': 'Человек', 'bicycle': 'Велосипед', 'car': 'Автомобиль',
    'motorcycle': 'Мотоцикл', 'airplane': 'Самолет', 'bus': 'Автобус',
    'train': 'Поезд', 'truck': 'Грузовик', 'boat': 'Лодка',
    'traffic light': 'Светофор', 'fire hydrant': 'Пожарный гидрант',
    'stop sign': 'Знак "Стоп"', 'parking meter': 'Парковочный счетчик',
    'bench': 'Скамейка', 'bird': 'Птица', 'cat': 'Кошка', 'dog': 'Собака',
    'horse': 'Лошадь', 'sheep': 'Овца', 'cow': 'Корова', 'elephant': 'Слон',
    'bear': 'Медведь', 'zebra': 'Зебра', 'giraffe': 'Жираф', 'backpack': 'Рюкзак',
    'umbrella': 'Зонт', 'handbag': 'Сумка', 'tie': 'Галстук', 'suitcase': 'Чемодан',
    'frisbee': 'Фрисби', 'skis': 'Лыжи', 'snowboard': 'Сноуборд',
    'sports ball': 'Спортивный мяч', 'kite': 'Воздушный змей',
    'baseball bat': 'Бейсбольная бита', 'baseball glove': 'Бейсбольная перчатка',
    'skateboard': 'Скейтборд', 'surfboard': 'Серфборд', 'tennis racket': 'Теннисная ракетка',
    'bottle': 'Бутылка', 'wine glass': 'Бокал', 'cup': 'Кружка', 'fork': 'Вилка',
    'knife': 'Нож', 'spoon': 'Ложка', 'bowl': 'Миска', 'banana': 'Банан',
    'apple': 'Яблоко', 'sandwich': 'Бутерброд', 'orange': 'Апельсин',
    'broccoli': 'Брокколи', 'carrot': 'Морковь', 'hot dog': 'Хот-дог',
    'pizza': 'Пицца', 'donut': 'Пончик', 'cake': 'Торт', 'chair': 'Стул',
    'couch': 'Диван', 'potted plant': 'Комнатное растение', 'bed': 'Кровать',
    'dining table': 'Обеденный стол', 'toilet': 'Унитаз', 'tv': 'Телевизор',
    'laptop': 'Ноутбук', 'mouse': 'Мышь', 'remote': 'Пульт', 'keyboard': 'Клавиатура',
    'cell phone': 'Телефон', 'microwave': 'Микроволновка', 'oven': 'Духовка',
    'toaster': 'Тостер', 'sink': 'Раковина', 'refrigerator': 'Холодильник',
    'book': 'Книга', 'clock': 'Часы', 'vase': 'Ваза', 'scissors': 'Ножницы',
    'teddy bear': 'Плюшевый мишка', 'hair drier': 'Фен', 'toothbrush': 'Зубная щетка'
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
    img_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)

    font_path = ""
    if os.name == 'nt':
        font_path = "C:/Windows/Fonts/arial.ttf"
    elif os.name == 'posix':
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            '/usr/share/fonts/truetype/freefont/FreeSans.ttf',
            '/System/Library/Fonts/SFNSText.ttf',
            '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'
        ]
        for path in font_paths:
            if os.path.exists(path):
                font_path = path
                break

    try:
        if font_path and os.path.exists(font_path):
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()

    draw.text(position, text, font=font, fill=(color[2], color[1], color[0]))
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# Открытие веб-камеры
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("Не удалось открыть веб-камеру")
    exit()

# Получение параметров видео
fps = int(capture.get(cv2.CAP_PROP_FPS)) or 30
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Исходное разрешение камеры: {width}x{height}, FPS: {fps}")

# Размеры для выходного видео
output_width, output_height = 1280, 720  # Изменено на стандартное соотношение 16:9

# Настройка выходного файла - используем XVID кодек
output_video_path = 'detect.avi'  # Изменено на .avi для лучшей совместимости
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Используем XVID вместо mp4v
writer = cv2.VideoWriter(output_video_path, fourcc, fps, (output_width, output_height))

# Проверка успешного создания VideoWriter
if not writer.isOpened():
    print("Не удалось создать видеофайл. Попробуем альтернативный кодек...")
    # Альтернативный кодек
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    writer = cv2.VideoWriter(output_video_path, fourcc, fps, (output_width, output_height))
    if not writer.isOpened():
        print("Не удалось создать видеофайл даже с альтернативным кодеком")
        exit()

print(f"Видео будет сохранено как: {output_video_path}")
print(f"Разрешение: {output_width}x{output_height}, FPS: {fps}")

# Параметры для плавности
conf_threshold = 0.48
frame_skip = 1
frame_counter = 0

# Переменные для отслеживания FPS
prev_frame_time = 0
curr_frame_time = 0

# Создание окна
cv2.namedWindow('YOLOv8 Webcam Detection')

# Функции для трекбаров
def set_confidence_threshold(val):
    global conf_threshold
    conf_threshold = val / 100.0

def set_frame_skip(val):
    global frame_skip
    frame_skip = max(1, val)

# Создание трекбаров
cv2.createTrackbar('Confidence', 'YOLOv8 Webcam Detection', int(conf_threshold * 100), 100, set_confidence_threshold)
cv2.createTrackbar('Frame Skip', 'YOLOv8 Webcam Detection', frame_skip, 10, set_frame_skip)

print("Нажмите 'q' для выхода")

while True:
    ret, frame = capture.read()
    if not ret:
        print("Не удалось получить кадр")
        break

    # Изменение размера кадра
    frame_resized = cv2.resize(frame, (output_width, output_height), interpolation=cv2.INTER_LINEAR)

    # Расчет FPS
    curr_frame_time = time.time()
    fps_value = 1 / (curr_frame_time - prev_frame_time) if prev_frame_time != 0 else 0
    prev_frame_time = curr_frame_time

    # Отображение FPS
    cv2.putText(frame_resized, f"FPS: {int(fps_value)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    frame_counter += 1
    if frame_counter % frame_skip != 0:
        writer.write(frame_resized)
        cv2.imshow('YOLOv8 Webcam Detection', frame_resized)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    # Обработка кадра
    try:
        results = model.track(frame_resized, persist=True, conf=conf_threshold, iou=0.5)[0]
    except Exception as e:
        print(f"Ошибка обработки кадра: {e}")
        writer.write(frame_resized)
        cv2.imshow('YOLOv8 Webcam Detection', frame_resized)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    # Получение данных
    if hasattr(results, 'boxes') and results.boxes is not None:
        classes_names = results.names
        boxes = results.boxes.xyxy.cpu().numpy().astype(np.int32) if results.boxes.xyxy is not None else np.array([])
        confs = results.boxes.conf.cpu().numpy() if results.boxes.conf is not None else np.array([])
        track_ids = results.boxes.id.cpu().numpy().astype(int) if results.boxes.id is not None else None

        # Обработка объектов
        if len(boxes) > 0:
            for i, (box, conf) in enumerate(zip(boxes, confs)):
                if i < len(results.boxes.cls):
                    x1, y1, x2, y2 = box
                    class_id = int(results.boxes.cls[i].item())
                    class_name_en = classes_names[class_id]
                    class_name_ru = class_names_ru.get(class_name_en, class_name_en)
                    color = colors[class_id % len(colors)]

                    # Рисование рамки
                    cv2.rectangle(frame_resized, (x1, y1), (x2, y2), color, 2)

                    # Формирование метки
                    label = f"{class_name_ru} {conf:.2f}"
                    if track_ids is not None and i < len(track_ids):
                        label += f" ID:{track_ids[i]}"

                    # Добавление текста
                    frame_resized = put_ru_text(frame_resized, label, (x1 + 10, y1 + 10),
                                              font_size=16, color=color)

    # Запись кадра
    writer.write(frame_resized)
    cv2.imshow('YOLOv8 Webcam Detection', frame_resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
capture.release()
writer.release()
cv2.destroyAllWindows()

print(f"Видео сохранено как: {output_video_path}")