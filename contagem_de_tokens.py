import tiktoken

codificador = tiktoken.encoding_for_model('gpt-3.5-turbo-16k')
lista_tokens = codificador.encode('Você é um categorizador de produtos.')

print(lista_tokens)
print(len(lista_tokens))

custo_entrada = (len(lista_tokens)/1000) * 0.0015
print(f'O custo é: {custo_entrada}')