a = input()
print(a)
b, c = a.split() 
b = int(b)
c = int(c) 
s = b + c 
print(s) 
m = b*c 
print(m) 
with open("rez", "w") as fin: 
    fin.write(f"{s}\n")
    fin.write(f"{m}\n")
