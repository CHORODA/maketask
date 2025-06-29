import requests
import datetime

TOKEN = "7252966911:AAGoMScYmGhz5sWg5C6O_19EzOr1FfNoB_g"
CHAT_ID = "7949474997"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

if __name__ == "__main__":
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    message = f"✅ 자동 요약 테스트 메시지\n시간: {now}"
    send_telegram_message(message)
