import os
import requests
from bs4 import BeautifulSoup

# Configurações do seu Telegram guardadas com segurança
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# Link do produto que você quer monitorar (exemplo: Mercado Livre)
"https://produto.mercadolivre.com.br/MLB-3355527004-cinto-tatico-hanger-para-porte-velado-preto-invictus-_JM?searchVariation=177341082647#polycard_client=recommendations_home_navigation-trend-recommendations&reco_backend=machinalis-homes-univb&reco_client=home_navigation-trend-recommendations&reco_item_pos=0&reco_backend_type=function&reco_id=492ae0d7-7702-48c7-ae22-e71d98100dcb&sid=recos&c_id=/home/navigation-trend-recommendations/element&c_uid=5536cf2d-a7f9-4c5e-98c1-ba5a7e51166b"
"https://www.mercadolivre.com.br/parafusadeira-furadeira-the-black-tools-tb12a-38-a-bateria-cor-amarelo-frequencia-60hz/p/MLB24076624#polycard_client=recommendations_home-deals&reco_backend=deals-model-odin&wid=MLB3371578831&reco_client=home-deals&reco_item_pos=2&reco_backend_type=low_level&reco_id=da13c521-3d19-48d9-be79-686e4e4516fb&sid=recos&c_id=/home/promotions-recommendations/element&c_uid=27a1497e-dd82-4fd6-bfa6-bf840878ac65"
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
