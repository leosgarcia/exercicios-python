preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.95 # 5% de desconto calculo direto
novo_preco = preco - (preco * 5 / 100) # 5% de desconto calculo indireto

print(f'O preço do produto com 5% de desconto é R$ {desconto}')

print(f'O preço do produto com 5% de desconto é R$ {novo_preco}')

