import requests

proxies = {
    "http": "socks5h://127.0.0.1:4447",
    "https": "socks5h://127.0.0.1:4447"
}

try:
    # I2P üzerinden IP kontrolü (IPv4 için api.ipify)
    r = requests.get("https://api.ipify.org?format=text", proxies=proxies, timeout=30)
    ip = r.text.strip()
    print("I2P bağlantısı kuruldu")
    print("IP:", ip)

except requests.exceptions.ReadTimeout:
    print("I2P bağlantısı çok yavaş, zaman aşımı oluştu")

except requests.exceptions.ConnectionError:
    print("I2P bağlantısı kurulamadı (I2P kapalı olabilir)")

except Exception:
    print("Beklenmeyen bir hata oluştu")
