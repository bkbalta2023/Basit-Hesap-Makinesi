print("""*********************************
Hesap Makinesi Programı

işlemler;

+ Toplama İşlemi

- Çıkarma İşlemi

* Çarpma İşlemi

/ Bölme İşlemi
*********************************
""")


a = float(input("Birinci Sayi:"))
islem = input("Islemi giriniz:")
b = float(input("Ikinci Sayi:"))


if islem == "+":
    print("{} + {} = {}".format(a,b,a+b))
elif islem == "-":
    print("{} - {} = {}".format(a,b,a-b))
elif islem == "*":
    print("{} * {} = {}".format(a,b,a*b))
elif islem == "/":
    print("{} / {} = {}".format(a,b,a/b))
else:
    print("Gecersiz islem...")
