from PIL import Image, ImageDraw, ImageFont
import random
import operator

# Операции, которые будем использовать (сложение, вычитание, умножение, деление)
operations = ['+', '-' ,'*' ,'**', '*', '*','*','**' ,'**' ]

def generate_math_problem():
    # Генерация случайных чисел
    num1 = random.randint(1000000, 10000000)  
    num2 = random.randint(1000000, 10000000)
    num3 = random.randint(1000000, 10000000)
    num4 = random.randint(1000000, 10000000)  
    
    # Выбор случайной операции
    operation1 = random.choice(operations)
    operation2 = random.choice(operations)
    operation3 = random.choice(operations)
    if operation1 == '**' and operation2 == '**':
        operation2 = "*"
    if operation3 == '**' and operation2 == '**':
        operation2 = "*"
    if operation1 == '**':
        num2 = random.randint(2, 10)
    if operation2 == '**':
        num3 = random.randint(2, 10)
    if operation3 == '**':
        num4 = random.randint(2, 10)
    
    
    # Формирование задачи
    problem = f"{num1} {operation1} {num2} {operation2} {num3} {operation3} {num4}"
    
    # Подсчет ответа
    answer = eval(problem)
    # problem += " = ?"
    return problem, answer

def generate_captcha(problem, path):
    img = Image.new('RGB', (1400, 200), 'black')
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", size=40)
    idraw = ImageDraw.Draw(img)
    idraw.text((25, 25), problem, font=font)
    img.save(path)


if __name__ == "__main__":
    # Пример использования
    problem, answer = generate_math_problem()
    print(f"Задача: {problem}")
    print(f"Ответ: {answer}")
    img = Image.new('RGB', (1400, 200), 'black')
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", size=40)
    idraw = ImageDraw.Draw(img)
    idraw.text((25, 25), problem, font=font)
    img.save('test_text.jpg')
