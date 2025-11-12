a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Dien tich tam giac =", round(s, 1))
else:
    print("Khong phai 3 canh cua tam giac")