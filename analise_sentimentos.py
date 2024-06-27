import os
import openai
import dotenv
import time

def analise_sentimento(nome_do_produto):
    
    prompt_sistema = """
    Você é um analisador de sentimentos de avaliações de produtos.
    Escreva um parágrafo com até 50 palavras resumindo as avaliações e depois atribua qual o sentimento geral para o produto.
    Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

    #### Formato de saída

    Nome do produto: 
    Resumo das avaliações:
    Sentimento geral: [aqui deve ser POSITIVO, NEUTRO ou NEGATIVO]
    Pontos fortes: [3 bullet points]
    Pontos fracos: [3 bullet points]
    """

    prompt_usuario = carrega(f"./dados/avaliacoes-{nome_do_produto}.txt")
    print(f'Iniciando análise do produto: {nome_do_produto}')

    tentativas = 0
    tempo_espera = 5
    while tentativas < 3:
        tentativas += 1
        print(f'Tentativa {tentativas}')
        try:
            resposta = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {
                    "role": "system",
                    "content": prompt_sistema
                },
                {
                    "role": "user",
                    "content": prompt_usuario
                }
            ]
            )

            salva(f"./dados/analise-{nome_do_produto}", resposta.choices[0].message.content)
            print('Analise concluida com sucesso')
            return
        except openai.AuthenticationError as e:
            print(f'Erro de Autenticação: {e}')
        # except openai.APIError as e:
        #     print(f'Erro da API: {e}')
        #     time.sleep(5)
        except openai.RateLimitError as e:
            print(f'Erro de limite de requisições: {e}')
            time.sleep(tempo_espera)
            tempo_espera *= 2
        




def carrega(nome_do_arquivo): 
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

lista_de_produtos = ['Balança de cozinha digital', 'Boia inflável para piscina','DVD player automotivo','Esteira elétrica para fitness','Grill elétrico para churrasco','Jogo de copos e taças de cristal','Miniatura de carro colecionável','Mixer de sucos e vitaminas','Tabuleiro de xadrez de madeira', 'Tapete de yoga']

for nome_do_produto in lista_de_produtos:
    analise_sentimento(nome_do_produto)