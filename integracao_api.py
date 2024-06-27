import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

resposta = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": 'system', 'content': 'Gere nomes de produtos ficticios sem descrição de acordo com a requisição do usuário'},
        {'role':'user', 'content':'Gere 5 produtos'}
    ]
)

print(resposta)