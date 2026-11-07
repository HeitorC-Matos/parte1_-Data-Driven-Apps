# Parte 1 - Questão 1: FastAPI com GPT-2

Aplicação simples que recebe uma frase em JSON e utiliza o modelo GPT-2 da Hugging Face para gerar uma continuação do texto.

## Tecnologias

- Python 3.11 ou superior
- FastAPI
- Transformers
- PyTorch
- Uvicorn

## Arquivos

- `main.py`: código da aplicação.
- `requirements.txt`: bibliotecas necessárias.

## Como executar no VS Code (Windows)

1. Instale o Python e abra o VS Code.
2. Extraia o projeto e abra sua pasta no VS Code em **Arquivo > Abrir Pasta**.
3. Abra um terminal em **Terminal > Novo Terminal**.
4. Crie o ambiente virtual:

   ```powershell
   py -3.14 -m venv .venv
   ```

   Se você utiliza outra versão compatível, substitua `py -3.14` por `py`.

5. Instale as bibliotecas:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

6. Execute a aplicação:

   ```powershell
   .\.venv\Scripts\python.exe -m uvicorn main:app --reload
   ```

7. Acesse no navegador:

   http://127.0.0.1:8000/docs

8. Abra **POST /gerar**, clique em **Try it out**, informe o JSON e clique em **Execute**.

## Exemplo de entrada

```json
{
  "texto": "My name is Heitor, i am studying python"
}
```

## Formato da resposta

```json
{
  "texto_gerado": "My name is Heitor, i am studying python. I am a computer science..."
}
```

## Observações

- Na primeira execução, o modelo GPT-2 será baixado da Hugging Face. É necessário ter acesso à internet e espaço em disco.
- Depois de baixado, o modelo fica armazenado em cache.
- O GPT-2 original foi treinado principalmente com textos em inglês. Por isso, é melhor testar inicialmente com frases em inglês.
- A API retorna o texto de entrada junto com a continuação gerada.
- Para encerrar o servidor, pressione `Ctrl + C` no terminal.