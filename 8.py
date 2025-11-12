n=int(input('nhập năm: '))
if (n%400 == 0) or (n%4 == 0 and n%100 != 0) :
    print('năm nhuận')
else:
    print('năm không nhuận')