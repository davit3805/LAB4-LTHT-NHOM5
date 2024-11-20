def try1(file, result, index=0, a=[]):
    if index == len(result):
        file.write(''.join(a) + '\n')
        return
    for char in result[index]:
        try1(file, result, index + 1, a + [char])

array_3855 = ['m', 'a', 'd', 'u', 'i', 'e', 'r', 's', 'n', 'f', 'o', 't', 'v', 'b', 'y', 'l']
s = "flames"
s1 = "y_Q@Ew"

result = []

for ch in s:
    row = []  
    for i in range(48, 126):
        if array_3855[i & 0xF] == ch:
            row.append(chr(i)) 
    result.append(row) 

for i in range(6):
    print(s[i], ":", end="")
    for ch in result[i]:
        print(ch, end=" ")
    print('\n')

with open("result.txt", "w", encoding="utf-8") as file:
    try1(file, result)
print("Tất cả các trường hợp được lưu trong file result.txt")