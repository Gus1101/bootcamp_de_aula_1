#Programa para retornar uma mensagem com o nome e o tamanho do mesmo

nome = str(input("Bom dia, amigo! Qual o seu nome: ").capitalize().strip())
print("Tenha uma ótima manhã,{}".format(nome))
print(len(nome))

#Programa para retornar a some de dois valores

valor_1 = int(input("Digite o primeiro valor: "))
valor_2 = int(input("Digite o segundo valor: "))
sum_valor = valor_1 + valor_2
print(sum_valor)