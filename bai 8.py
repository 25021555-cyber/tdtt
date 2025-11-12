ten = input("Ten chu ho: ")
chi_so_truoc = int(input("Chi so thang truoc: "))
chi_so_nay = int(input("Chi so thang nay: "))
so_kwh = chi_so_nay - chi_so_truoc
tien = 0
kwh = so_kwh
if kwh > 0:
    if kwh > 400:
        tien = (kwh - 400) * 3460
        kwh = 400
    if kwh > 300:
        tien = (kwh - 300) * 3350
        kwh = 300
    if kwh > 200:
        tien = (kwh - 200) * 2998
        kwh = 200
    if kwh > 100:
        tien = (kwh - 100) * 2380
        kwh = 100
    if kwh > 50:
        tien = (kwh - 50) * 2050
        kwh = 50
    if kwh > 0:
        tien = kwh * 1984
tien = int(tien * 1.08)
print("Ho va ten:", ten)
print("Tien phai tra la:", tien)