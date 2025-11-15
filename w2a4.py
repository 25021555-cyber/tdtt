a1,b1,c1,a2,b2,a3=map(float,input("nhập 6 điểm cách nhau bởi dấu cách: ").split())
TB=((a1+b1+c1)+(a2+b2)*2+a3*3)/10
print("Điểm trung bình là:",round(TB, 1))