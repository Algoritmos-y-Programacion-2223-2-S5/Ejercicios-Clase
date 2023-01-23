word = ""
while word != "salir":
    word = input("Enter a word:")
    print(word)

for i in range(10):
    if i % 2 ==0:
        continue
    print(i)