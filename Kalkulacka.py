#Basic calculator created by me in Slovak langue
def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
def krat(a,b):
    return a * b
def deleno(a,b):
    return a / b

print("Vyber operaciu! ")
print("1. Plus")
print("2. Minus")
print("3. Krat")
print("4. Deleno")

while True:
    vyber=input("Zadaj vyber: ")

    if vyber in ("1","2","3","4"):
        num1= float(input("Zadaj prve cislo: "))
        num2= float(input("Zadaj druhe cislo: "))


        if vyber == "1":
            plus1=plus(a=num1,b=num2)
            print(plus1)
            
        elif vyber == "2":
            minus1=minus(a=num1,b=num2)
            print(minus1)

        elif vyber == "3":
            krat1=krat(a=num1,b=num2)
            print(krat1)

        elif vyber == "4":
            deleno1=deleno(a=num1,b=num2)
            print(deleno1)
    dalsia_kalkulacia=input("Chces znova pocitat? Ano/Nie: ")
    if dalsia_kalkulacia == "Nie":
        break
