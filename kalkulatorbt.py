print("Python Calculator")
print("-----------------")

print("1. pertambahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")
print("-----------------")

# Logic
def penjumlahan(x, y):
    return x + y

def pengurangan(x, y):
    return x - y

def perkalian(x, y):
    return x * y

def pembagian(x, y):
    return x / y

tipe = input("pilih perintahnya yg bener:")

if tipe in ('1', '2', '3', '4'):
    angka1 = float(input("Enter the first number:"))
    angka2 = float(input("Enter the second number:"))
    print("-----------------")
    if tipe == '1':
        print("jawabannya adalah:", penjumlahan(angka1, angka2))
    if tipe == '2':
        print("jawabannya adalah:", pengurangan(angka1, angka2))
    if tipe == '3':
        print("jawabannya adalah:", perkalian(angka1, angka2))
    if tipe == '4':
        print("jawabannya adalah:", pembagian(angka1, angka2))
    print("-----------------")
else:
    print("Invalid input. Please choose a valid command.")