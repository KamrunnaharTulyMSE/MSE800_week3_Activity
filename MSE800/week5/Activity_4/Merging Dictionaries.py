Key1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'a']
Value1 = [20, 3, 1, 88, 55, 92, 6, 90, 910]
Key2 = ['u', 'b', 'o', 'x', 'e', 'a']
Value2 = [200, 30, 10, 88, 55, 920]

dic1 = {k: v for k, v in zip(Key1, Value1) if v % 2 != 0}
dic2 = {k: v for k, v in zip(Key2, Value2) if v % 2 != 0}

print("dic1:", dic1)
print("dic2:", dic2)