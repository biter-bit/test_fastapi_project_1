# НЕЙРОСЕТИ.COM

НЕЙРОСЕТИ.COM - это агрегатор нейросетей, мы предоставляем удобный доступ к популярным нейросетям, таким как:
ChatGPT, Midjourney, Kandinsky, Gemini, Dall-E, StableDiffusion, и многим другим.

## Что умеет?

- Генерировать текст - ChatGPT4, Gemini 1.0 PRO, Yandex, Claude 3
- Генерировать фото - Midjourney v6, Kandinsky, Dalle-2, Dalle-3, Stable Diffusion
- Генерировать работы для учебы - Дипломы, Рефераты, Курсовые, Эссе
- Обрабатывать файлы - формата txt или word
- Решать задачи по фото - с помощью ChatGPT 4 Vision
- Задавать вопросы голосом - с помощью микрофона
- Синтезировать речь - 100 разных голосов
- И еще 100 других полезных нейросетей

Ссылка на бота - https://t.me/chatgpt_tgm_bot/
Ссылка на сайт - https://xn--e1aajcsinjk.com/
Cсылка на админку - https://xn--e1aajcsinjk.com/admin/

## Зависимости

1. python 3.10.12
2. pip 22.0.2
3. Зависимости из requirements.txt

### Установка Linux

1. Клонировать репозиторий: `git clone https://git@github.com:antomin/tgm_bot.git`
2. Перейти в корень проекта: `cd <путь проекта>`
3. Установить python 3.10.12 и pip 22.0.2:

   ```
   sudo apt update
   sudo apt install python3.10
   ```
   
5. Создать виртуальное окружение и активировать его:

   ```
   python -m venv <название окружения>
   source <название окружения>/bin/activate
   ```
   
6. Установить зависимости: `pip install -r requirements.txt`
7. Добавить файл .env в корень проекта по структуре файла example.env и внести данные в него.
8. Запустить бот командой: `python manage.py start_bot`

### Структура проекта

- `accounts_app`: приложение django по работе с пользователями
- `accounts_app/migrations/`: расположены файлы миграций
- `accounts_app/__init__.py`: файл инициализации пакета python
- `accounts_app/admin.py`: файл для регистрации и настройки моделей в админке
- `README.md`: файл с описанием проекта.
- `requirements.txt`: файл с перечислением зависимостей проекта.
- `setup.py`: скрипт для установки пакета Python.
- `LICENSE`: файл с лицензией проекта (например, MIT, Apache, GPL).
- `docs/`: директория с документацией проекта.
- `src/`: директория с исходным кодом проекта.
- `tests/`: директория с модулями тестирования.
- `data/`: директория для хранения данных.

