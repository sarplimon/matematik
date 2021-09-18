def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
print("işlem seç.")
print("1.toplama")
print("2.çıkarma")
print("3.çarpma")
print("4.bölme")
choice = input("Hangi işlemi yapmak istiyorsun(1/2/3/4): ")
num1 = float(input("İlk sayıyı gir: "))
num2 = float(input("İkinici sayıyı gir: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Geçersiz Giriş")