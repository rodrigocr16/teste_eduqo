n = input('Digite o tamanho de n: ')
print(' ')
for i in range(0, int(n)):
    buffer = ""
    for j in range (0, int(n) + (int(n) - 1)):
        if j < (int(n) - i - 1) or j > (int(n) + i - 1):
            buffer = buffer + "_"
        else:
            buffer = buffer + "*"
    print(buffer)
