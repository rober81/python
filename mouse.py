import pyautogui as pag
import random
import time
import math

def mover_circulos(a, b):
    w = 20  
    m = (2*math.pi)/w 
    r = 200       
    for i in range(0, w+1):
        x = int(a+r*math.sin(m*i))  
        y = int(b+r*math.cos(m*i))
        pag.moveTo(x,y)
        time.sleep(0.2)

def mover_random():
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    pag.moveTo(x, y)
    print(f"Movido a: {x}, {y}")

def main():
    x_original, y_original = pag.position()
    print(f"Original: {x_original}, {y_original}")

    while True:
        x_actual, y_actual = pag.position()
        print(f"Actual: {x_actual}, {y_actual}")
        if (x_actual, y_actual) == (x_original, y_original):
            x = 1920/2
            y = 1080/2
            mover_circulos(x, y)
        x_original, y_original = pag.position()
        time.sleep(10)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print("Keep up the good work... ;-)")
    