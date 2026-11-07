# Parte 1 - Questão 2: FastAPI com tradução de inglês para francês

Aplicação simples que recebe um texto em inglês em formato JSON e retorna sua tradução para o francês utilizando o modelo `Helsinki-NLP/opus-mt-en-fr`, da Hugging Face.

## Tecnologias

- Python 3.11 ou 3.12
- FastAPI
- Transformers (versão 4)
- PyTorch
- SentencePiece
- Sacremoses
- Uvicorn

## Arquivos

- `main.py`: código da aplicação.
- `requirements.txt`: bibliotecas necessárias.

## Como executar no VS Code (Windows)

1. Extraia o arquivo ZIP da Questão 2 e abra **a pasta extraída que contém o `main.py` e o `requirements.txt`** no VS Code, usando **Arquivo > Abrir Pasta**.
2. Abra **Terminal > Novo Terminal** e execute `dir`. Confirme que `main.py` e `requirements.txt` aparecem na listagem.
3. Crie um ambiente virtual exclusivo desta questão:

   ```powershell
   py -m venv .venv
   ```

   Se `py` não funcionar, use `python -m venv .venv`. Não utilize o ambiente virtual da Questão 1.

4. Instale as dependências:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

5. Inicie a API:

   ```powershell
   .\.venv\Scripts\python.exe -m uvicorn main:app --reload
   ```

6. Abra no navegador: <http://127.0.0.1:8000/docs>.
7. Escolha **POST /traduzir**, clique em **Try it out**, cole um dos JSONs abaixo e clique em **Execute**.
8. Verifique se o código da resposta é **200** e se o campo `texto_traduzido` contém uma tradução para o francês.
9. Para encerrar a aplicação, pressione **Ctrl + C** no terminal.

## Teste com frase curta

Entrada:

```json
{
  "texto": "Good morning! How are you today?"
}
```

Exemplo de resposta:

```json
{
  "texto_traduzido": "Bonjour ! Comment allez-vous aujourd'hui ?"
}
```

A redação exata da tradução pode variar.

## Como funciona

A aplicação recebe o texto em JSON, valida a entrada, converte o texto em tokens, divide a entrada em partes de até 300 tokens, traduz cada parte e reúne os resultados em uma única resposta JSON. A divisão permite processar textos maiores do que uma única entrada do modelo.

## Observações

- Na primeira execução, o modelo será baixado da Hugging Face. É necessária uma conexão à internet e espaço livre em disco.
- O modelo é carregado quando a aplicação é iniciada. O primeiro carregamento pode demorar.
- O modelo foi desenvolvido para tradução de inglês para francês.
- Em textos longos, a divisão em partes pode reduzir a qualidade da tradução, especialmente quando uma frase é interrompida entre duas partes.
- O Transformers 5 não oferece o pipeline de tradução usado neste projeto. Por isso, o `requirements.txt` utiliza a versão 4.
- A rota rejeita textos vazios ou compostos apenas por espaços.
- Não é necessário utilizar uma chave da API da OpenAI.
