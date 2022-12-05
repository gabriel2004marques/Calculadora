print("Calculadora")
n1 = float(input("Digite um número : "))
op = input("Digite (1) para soma , (2) para subtração , (3) para divisão e (4) para multiplicação : ")
n2 = float(input("Digite outro número : "))
if op == '1':
    r = n1 + n2
    print("A soma entre {} e {} é igual a : {}.".format(n1 , n2 , r))
elif op == '2':
    r = n1 - n2
    print("A subtração entre {} e {} é igual a : {}".format(n1 , n2 , r))
elif op == '3':
    r = n1 / n2
    print("A divisão entre {} e {} é igual a : {}".format(n1 , n2 , r))
elif op == '4':
    r = n1 * n2
    print("A multiplicação entre {} e {} é igual a : {}".format(n1 , n2 , r))
    