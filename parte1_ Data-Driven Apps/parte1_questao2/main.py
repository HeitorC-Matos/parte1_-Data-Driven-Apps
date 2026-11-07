from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline

app = FastAPI()
tradutor = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")


class EntradaTexto(BaseModel):
    texto: str = Field(min_length=1)


@app.post("/traduzir")
def traduzir_texto(entrada: EntradaTexto):
    texto = entrada.texto.strip()

    if not texto:
        raise HTTPException(status_code=422, detail="Informe um texto em inglês.")

    tokens = tradutor.tokenizer.encode(texto, add_special_tokens=False)
    traducoes = []

    for inicio in range(0, len(tokens), 300):
        parte = tradutor.tokenizer.decode(
            tokens[inicio:inicio + 300], skip_special_tokens=True
        )
        resultado = tradutor(parte, max_length=512)
        traducoes.append(resultado[0]["translation_text"])

    return {"texto_traduzido": " ".join(traducoes)}
