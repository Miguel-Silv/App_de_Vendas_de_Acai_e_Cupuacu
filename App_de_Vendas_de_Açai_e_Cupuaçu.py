#App de Vendas de Açaí e Cupuaçu
print('Bem-vindo a Loja Açaíaçu do Miguel Silveira')
print('|------------------Cardápio-------------------|')
print('|-------|Tamanho|Cupuaçu(CP)| Açaí(AC)|-------|')
print('|-------|   P   |   R$9.00  | R$11.00 |-------|')
print('|-------|   M   |   R$14.00 | R$16.00 |-------|')
print('|-------|   G   |   R$18.00 | R$20.00 |-------|')
#Acumulador de Valor de Pedidos
total=0
#Sabor
while True:
      while True:
            sabor=input('Qual sabor você deseja ?(CP/AC): ').upper()
            if sabor=='CP' or sabor=='AC':
                  break
            else:
                  print('Sabor inválido. Tente novamente.')
                  continue
#Tamanho
      while True:
            tamanho=input('Qual tamanho você deseja?(P/M/G): ').upper()
            if tamanho=='P' or tamanho=='M' or tamanho =='G':
                  break
            else:
                  print('Tamanho inválido. Tente novamente.')
#Preço
      preco=0
#Cupuaçu
      if sabor=='CP' and tamanho=='P':
            preco=9.00
      elif sabor=='CP' and tamanho=='M':
            preco=14.00
      elif sabor=='CP' and tamanho=='G':
            preco=18.00
      elif sabor=='AC' and tamanho=='P':
            preco=11.00
      elif sabor=='AC' and tamanho=='M':
            preco=16.00
      elif sabor=='AC' and tamanho=='G':
            preco=20.00
#Saída
      print(f'Você pediu um {'Cupuaçu' if sabor== 'cp' else 'Açaí'}, de tamanho {tamanho}, assim ficou R${preco:.2f} ')
#Acumulador de Valor de Pedidos
      total +=preco
#Rpetição
      while True:
            repeticao=input('Deseja mais alguma coisa ?(S/N): ').upper()
            if repeticao=='S':
                  break
            elif repeticao=='N':
                  print(f'O total ficou por: R${total:.2f}')
                  print('Obrigado pela preferência! Volte sempre!')
                  exit()
            else:
                  print("Resposta inválida. Tente responder com 'S' para sim e 'N' para não.")