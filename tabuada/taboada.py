# num = int(input("Digite um número:"))

for tab in range(1, 11):
    print("TABUADA DE {}".format(tab))
    print("--------------")
    for num in range(1, 11):
        print("|{0:2d} X {1:2d} = {2:2d}|".format(num, tab, num * tab))
    print("--------------\n")