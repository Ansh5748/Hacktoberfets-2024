import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def power(x, y):
    return x ** y

def logarithm(x, base):
    if x > 0 and base > 1:
        return math.log(x, base)
    else:
        return "Error! Logarithm undefined."

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def calculator():
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Pangkat")
    print("6. Logaritma")
    print("7. Sinus")
    print("8. Cosinus")
    print("9. Tangen")

    choice = input("Masukkan pilihan (1-9): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))

        if choice == '1':
            print(f"Hasil: {add(num1, num2)}")
        elif choice == '2':
            print(f"Hasil: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Hasil: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Hasil: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Hasil: {power(num1, num2)}")

    elif choice in ['6', '7', '8', '9']:
        num = float(input("Masukkan angka: "))
        
        if choice == '6':
            base = float(input("Masukkan basis logaritma: "))
            print(f"Hasil: {logarithm(num, base)}")
        elif choice == '7':
            print(f"Hasil: {sine(num)}")
        elif choice == '8':
            print(f"Hasil: {cosine(num)}")
        elif choice == '9':
            print(f"Hasil: {tangent(num)}")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    calculator()
