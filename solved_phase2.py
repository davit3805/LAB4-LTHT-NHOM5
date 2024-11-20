ans="Xsfpj"
result=""
for i in ans:
    if i.islower():
        result += chr((ord(i) - ord('a') - 5) % 26 + ord('a'))
    elif i.isupper():
        result += chr((ord(i) - ord('A') - 5) % 26 + ord('A'))
print ("Chuoi goc:", ans)    
print ("Dap an:",result)