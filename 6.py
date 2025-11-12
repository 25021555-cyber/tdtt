n=input('nhập kí tự: ')
if n.isalpha() :
    print('kí tự là chữ cái')
elif n.isdigit() :
    print('kí tự là số')
else:
    print('kí tự không phải là số và chữ cái')