from fastapi import FastAPI
from pydantic import BaseModel, Field
from transformers import pipeline # type: ignore

app = FastAPI()
gerador = pipeline("text-generation", model="openai-community/gpt2")


class EntradaTexto(BaseModel):
    texto: str = Field(min_length=1)


@app.post("/gerar")
def gerar_texto(entrada: EntradaTexto):
    resultado = gerador(
        entrada.texto,
        max_new_tokens=50,
        do_sample=True,
        pad_token_id=gerador.tokenizer.eos_token_id
    )
    return {"texto_gerado": resultado[0]["generated_text"]}