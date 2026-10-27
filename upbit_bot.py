import requests, time, os
TELEGRAM_TOKEN=os.getenv("TELEGRAM_TOKEN")
CHAT_ID=os.getenv("CHAT_ID","6051737830")
UPBIT_URL="https://api.upbit.com/v1/market/all?isDetails=false"
TELE_URL=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
def send(msg):
    try:
        requests.post(TELE_URL,json={"chat_id":CHAT_ID,"text":msg},timeout=10)
    except: pass
def get_markets():
    try:
        data=requests.get(UPBIT_URL,timeout=5).json()
        return set([m['market'] for m in data if m['market'].startswith('KRW-')])
    except: return None
known=get_markets() or set()
send(f"✅ Bot Upbit conectado - {len(known)} mercados")
while True:
    time.sleep(3)
    cur=get_markets()
    if not cur: continue
    nuevos=cur-known
    for m in nuevos:
        send(f"🚨 PRE-LISTING {m} Detectado ANTES del anuncio oficial")
    if nuevos: known=cur
