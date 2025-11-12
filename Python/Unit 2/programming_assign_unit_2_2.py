item1 = 200.0
item2 = 400.0
item3 = 600.0

def combo1():
    combo1 = (item1 + item2) * 0.90
    return combo1

def combo2():
    combo2 = (item2 + item3) * 0.90
    return combo2

def combo3():
    combo3 = (item1 + item3) * 0.90
    return combo3

def combo4():
    combo4 = (item1 + item2 + item3) * 0.75
    return combo4

print("Output:")
print("Online Store")
print("---------------------")
print(f"{'Product(s)':<30}{"Price"}")
print(f"{'Item 1':<30}{item1}")
print(f"{'Item 2':<30}{item2}")
print(f"{'Item 3':<30}{item3}")
print(f"{'Combo 1 (Item 1 + 2)':<30}{combo1()}")
print(f"{'Combo 2 (Item 2 + 3)':<30}{combo2()}")
print(f"{'Combo 3 (Item 1 + 3)':<30}{combo3()}")
print(f"{'Combo 4 (Item 1 + 2 + 3)':<30}{combo4()}")
print(" ")
print("---------------------")
print("For delivery Contact:98764678899")
