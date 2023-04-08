print('Bem-vindo ao Calculador de Água Residual')
print('\nCarregando...')

histograma = [] # Cria a Lista para armazenar litros de água
tamanho = int(input('\nDigite o tamanho do Histograma: ')) # Atribuir um tamanho para o histograma

# Atribuir valores para cada posição do Histograma
for i in range(tamanho):
    pos = int(input(f'Digite o {i+1}º elemento: '))
    histograma.append(pos)

totalResiduo = 0 # Variavel inteira para somar todo resíduo e retornar no valor final

# Imprime o histograma na tela
print('\nEsses são os valores das barras do Histograma: ')
print(histograma)
print('')

# Loop para percorrer o histograma 
for i in range(1, tamanho-1):
    if histograma[i] < histograma[i-1] and histograma[i] < histograma[i+1]: # Verifica o espaçamento para o resíduo entre as barras

         # Verifica qual barra é maior, a do antecessor da posição que há espaço ou do sucessor
         # Se a primeira barra é a maior, subtrai a barra do meio com a próxima barra, para descobrir o espaço vago em que irá ficar resíduos
        if histograma[i-1] > histograma[i+1]: 
            residuo = histograma[i+1] - histograma[i] 
            i += 1
        else:
            # Se a última barra é a maior, subtrai a barra do meio com a barra anterior, para descobrir o espaço vago em que irá ficar resíduos
            residuo = histograma[i-1] - histograma[i] 
            i += 1

        # Imprime na tela quantos litros de resíduo irá ficar em cada barra
        print(f'Na {i}º Barra, possuí {residuo} Litros de água')
        totalResiduo += residuo # Soma de todo o resíduo descoberto

print(f'\nO valor total de água residual no Histograma é de: {totalResiduo}\n') # Imprime o valor total de resíduos de todo o Histograma