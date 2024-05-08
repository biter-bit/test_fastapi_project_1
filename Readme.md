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
4. Создать виртуальное окружение и активировать его:
   ```
   python -m venv <название окружения>
   source <название окружения>/bin/activate
   ```
5. Установить зависимости: `pip install -r requirements.txt`
6. Добавить файл .env в корень проекта по структуре файла example.env и внести данные в него.
7. Запустить бот командой: `python manage.py start_bot`

### Структура проекта

my_project/
│
├── README.md
├── requirements.txt
├── setup.py
├── LICENSE
│
├── docs/
│   └── documentation.md
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
└── data/
    ├── input_data/
    │   └── input.txt
    └── output_data/
        └── output.txt

