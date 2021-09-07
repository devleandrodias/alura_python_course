print(30 * "*")
print(5 * " ","JOGO DA ADIVINHAÇÃO")
print(30 * "*")

numero_secreto = 42

total_tentativas = 3

rodada = 1

while(total_tentativas >= rodada): 
  print("{0}Tentativa {1} de {2}".format("\n",rodada, total_tentativas))
  chute = int(input("\nDigite seu número: "))

  acertou = numero_secreto == chute

  print("\nVocê digitou: ", chute)

  if(acertou):
    print("\nVocê acertou o número secreto!")

  else:
    rodada += 1

    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if(chute_maior):
      print("\nVocê errou! Seu chute foi maior que número secreto!")
    elif(chute_menor):
      print("\nVocê errou! Seu chute foi menor que número secreto!")

print("\nFim de jogo!")

