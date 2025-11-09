c=input('nhập kí tự : ')
if c.isupper():
    print('kí tự thường tương là :' ,c.lower())
elif c.islower():
    print('kí tự hoa tương ứng là :' ,c.upper())
else:
    print('đây không phải là kí tự chữ cái !')

