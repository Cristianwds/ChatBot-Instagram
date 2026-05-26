import os
import urllib.request
import urllib.error
from dotenv import load_dotenv

load_dotenv()

DOC_ID = os.getenv("GOOGLE_DOCS_ID")

def get_knowledge_base() -> str:
    url = f"https://docs.google.com/document/d/{DOC_ID}/export?format=txt"
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8").strip()
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"Failed to fetch knowledge base: {error.code} {error.reason}") from error



"""
Prueba para verificar el funcionamiento del acceso a knowledge_base
if __name__ == "__main__":
    content = get_knowledge_base()
    print(content[:500])
"""