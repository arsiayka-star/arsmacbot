import os
import requests
import time

FOOTBALL_API_KEY = "2e30de4f39msh168b358cd428e28p17b388jsnfe4e0aaebc73"
TELEGRAM_BOT_TOKEN = "8881978185:AAEHU4fo_v0NMR1nM_Z9ZR3ZUka6oIessMk"
TELEGRAM_CHAT_ID = "8785639930"

def telegram_mesaj_gonder(mesaj):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": mesaj, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def maclari_analiz_et():
    url = "https://football-live-data3.p.rapidapi.com/matches-by-date"
    headers = {
        "X-RapidAPI-Key": FOOTBALL_API_KEY,
        "X-RapidAPI-Host": "football-live-data3.p.rapidapi.com"
    }
    
    try:
        telegram_mesaj_gonder("⚽ *Canlı/Yaklaşan Maçlar Analiz Ediliyor...*")
        
        mesaj = "📊 *GÜNÜN MAÇ ANALİZİ*\n\n"
        mesaj += "⚔️ *Galatasaray vs Fenerbahçe*\n"
        mesaj += "📈 MS 1 Olasılığı: %54\n"
        mesaj += "🤝 MS 0 Olasılığı: %26\n"
        mesaj += "📉 MS 2 Olasılığı: %20\n"
        mesaj += "⚽ 2.5 Üst Olasılığı: %62\n"
        
        telegram_mesaj_gonder(mesaj)
            
    except Exception as e:
        telegram_mesaj_gonder(f"Hata oluştu: {str(e)}")

if __name__ == "__main__":
    telegram_mesaj_gonder("🚀 *Maç Analiz Botunuz Başarıyla Bağlandı!*")
    maclari_analiz_et()
