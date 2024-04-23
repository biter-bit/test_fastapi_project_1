from fastapi import FastAPI
from rembg import remove
import time

input_path = 'aig.png'
output_path = 'aaa.png'

app = FastAPI()


@app.get("/")
async def root():
    start_time = time.time()
    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)
    end_time = time.time()  # Завершение таймера после выполнения кода
    execution_time = end_time - start_time  # Вычисление времени выполнения
    return {"message": "Hello World", "execution_time": execution_time}
