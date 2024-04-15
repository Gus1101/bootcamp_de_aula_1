#Programa para retornar uma mensagem com o nome e o tamanho do mesmo

nome = str(input("Bom dia, amigo! Qual o seu nome: ").capitalize().strip())
print("Tenha uma ótima manhã,{}".format(nome))
print(len(nome))

#Programa para retornar a soma de dois valores

valor_1 = int(input("Digite o primeiro valor: "))
valor_2 = int(input("Digite o segundo valor: "))
sum_valor = valor_1 + valor_2
print(sum_valor)

#Programa para retornar calculo de kpi simples

nome  = str(input("Digite seu nome: "))
salario = float(input("Digite o seu salario: "))
bonus = float(input("Digite o seu bônus: " ))

vl_bonus = 1000 + salario *  1 + (bonus/100)

print("Olá, {}. Seu bônus é de {}".format(nome,vl_bonus))