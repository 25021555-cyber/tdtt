n = int(input("Nhập số (0-9): "))
match n:
    case 0:
        print("Không")
    case 1:
        print("Một")
    case 2:
        print("Hai")
    case 3:
        print("Ba")
    case 4:
        print("Bốn")
    case 5:
        print("Năm")
    case 6:
        print("Sáu")
    case 7:
        print("Bảy")
    case 8:
        print("Tám")
    case 9:
        print("Chín")
    case _:
        print("Số không hợp lệ! Vui lòng nhập từ 0 đến 9.")