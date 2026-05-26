import os
from dotenv import load_dotenv
from groq import Groq
from knowledge_base import get_knowledge_base

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

_kb_cache = None

def get_kb():
    global _kb_cache
    if _kb_cache is None:
        _kb_cache = get_knowledge_base()
    return _kb_cache

def get_response(user_message: str, history: list) -> str:
    kb = get_kb()

    system_prompt = f"""Sos un asistente de atención al cliente.
Respondé SIEMPRE en base a la siguiente información:

---
{kb}
---

Si la pregunta no está cubierta en esa información, decí amablemente que no tenés esa información disponible.
Sé conciso, amable y respondé en el mismo idioma que el usuario."""

    messages = [{"role": "system", "content": system_prompt}]
    messages += history
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    return response.choices[0].message.content




"""
Prueba para verificar el funcionamiento correcto de la IA Groq
if __name__ == "__main__":
    print("Iniciando prueba...")
    respuesta = get_response("Hola, ¿qué información tenés?", [])
    print("Respuesta recibida:")
    print(respuesta)
"""