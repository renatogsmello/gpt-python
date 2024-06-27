import os
from openai import OpenAI
from dotenv import load_dotenv

def categorizaProduto(nome_do_produto, categorias_validas):
    prompt_sistema= f"""
    Você é um categorizador de produtos.
    Você deve escolher uma categoria da lista abaixo:
    #### Lista de categorias válidas
    {categorias_validas}
    #### Exemplo
    bola de tênis
    Esportes
    """

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": prompt_sistema
            }
        ]
        },{
            "role": "user",
            "content": nome_do_produto
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,

    )

    
    print(response.choices[0].message.content)
        

load_dotenv()

print("Digite as categorias válidas:")
categorias_validas = input()
while True:
    print("Digite o nome do produto:")
    nome_do_produto = input()
    categorizaProduto(nome_do_produto, categorias_validas)


