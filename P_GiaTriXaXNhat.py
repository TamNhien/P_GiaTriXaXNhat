def find_value_farthest_from_x(lst, x):
    return max(lst, key=lambda num: abs(num - x))

lst = list(map(int, input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy : ").split(',')))
x = int(input("Nhập vào số nguyên x: "))
print("Giá trị trong danh sách xa", x, "nhất là : ", find_value_farthest_from_x(lst, x))
