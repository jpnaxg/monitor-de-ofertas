import os
import requests
from bs4 import BeautifulSoup

# Configurações do seu Telegram guardadas com segurança
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# Link do produto que você quer monitorar (exemplo: Mercado Livre)

URL = "https://meli.la/2hBz5hs"
URL = "COLE_AQUI_A_URL_DO_PRODUTO"
URL = "COLE_AQUI_A_URL_DO_PRODUTO"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def checar_preco():
    resposta = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resposta.content, 'html.parser')
    
    # Busca o elemento de preço da página
    preco_elem = soup.find('span', {'class': 'andes-money-amount__fraction'})
    
    if preco_elem:
        preco = preco_elem.text
        mensagem = f"🤖 Alerta de Preço!\nO produto está custando: R$ {preco}\nLink: {URL}"
        
        # Envia a mensagem para o seu Telegram
        telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(telegram_url, data={"chat_id": CHAT_ID, "text": mensagem})

if __name__ == "__main__":
    checar_preco()
