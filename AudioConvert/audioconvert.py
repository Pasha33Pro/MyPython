import subprocess
from pathlib import Path


def check_ffmpeg():
    try:
        subprocess.run(
            ['ffmpeg', '-version'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Ошибка: ffmpeg не установлен или недоступен в PATH.")
        exit(1)


def convert_audio_files():
    """Конвертирует аудиофайлы в формат MP3"""
    # Настройка путей
    source_dir = Path('.')
    output_dir = source_dir / 'mp3'

    output_dir.mkdir(exist_ok=True)
    print(f"📁 Целевая папка: {output_dir.resolve()}")

    # Поддерживаемые форматы (flac, m4a)
    supported_ext = ['.flac', '.m4a']
    converted = 0

    # Обработка
    for file in source_dir.iterdir():
        if not file.is_file():
            continue

        ext = file.suffix.lower()
        if ext not in supported_ext:
            continue

        # Формируем путь
        output_file = output_dir / (file.stem + '.mp3')

        try:
            print(f"🔄 Конвертируем: {file.name} → {output_file.name}")
            subprocess.run(
                [
                    'ffmpeg',
                    '-y',  # Авто перезапись
                    '-i', str(file),  # Входной
                    '-q:a', '0',  # Качество MP3 (0 = лучшее)
                    '-map_metadata', '0',  # Сохраняем мета
                    str(output_file)
                ],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(f"✅ Успешно: {output_file.name}\n")
            converted += 1
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode().strip()[:200]
            print(f"❌ Ошибка при конвертации {file.name}: {error_msg}\n")

    # Итог
    print(f"\n{'=' * 50}")
    if converted > 0:
        print(f"✨ Успешно конвертировано: {converted} файлов")
        print(f"📁 Результаты сохранены в: {output_dir}")
    else:
        print("⚠️  Не найдено файлов для конвертации (.flac, .m4a)")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    print("🚀 Запуск конвертера аудио файлов\n")
    check_ffmpeg()
    convert_audio_files()
