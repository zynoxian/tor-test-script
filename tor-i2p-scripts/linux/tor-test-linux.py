import requests

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

try:
    r = requests.get(
        "https://icanhazip.com",
        proxies=proxies,
        timeout=30
    )

    ip = r.text.strip()
    print("Tor bağlantısı kuruldu")
    print("IP:", ip)

except requests.exceptions.ReadTimeout:
    print("Tor bağlantısı çok yavaş, zaman aşımı oluştu")

except requests.exceptions.ConnectionError:
    print("Tor bağlantısı kurulamadı (Tor kapalı olabilir)")

except Exception:
    print("Beklenmeyen bir hata oluştu")
