import requests
import xmltodict

# Lista de URLs do RSS
URLS = [
    "https://rss.app/feeds/zuLqVABUuWY1LVA8.xml"
]

def buscar_e_converter_rss_para_json():
    resultados = []
    for url in URLS:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                rss_dict = xmltodict.parse(response.content)
                # Pega apenas os itens do feed
                items = rss_dict.get('rss', {}).get('channel', {}).get('item', [])
                # Garante que sempre seja uma lista
                if isinstance(items, dict):
                    items = [items]
                resultados.extend(items)
            else:
                resultados.append({"error": f"Não foi possível acessar {url}"})
        except requests.exceptions.RequestException as e:
            resultados.append({"error": f"Erro ao acessar {url}: {str(e)}"})
    return resultados
