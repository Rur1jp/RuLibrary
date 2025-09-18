import time
import tls_client
from typing import List

def thread(tokens: List[str], channelid: str, name: str, count: int, kankaku):
    
    def ozeisession():
        return tls_client.Session(
            client_identifier="safari_ios_16_0",
            random_tls_extension_order=True
        )

    for token in tokens:
        session = ozeisession()
        headers = {
            "authorization": token,
            "content-type": "application/json",
            "user-agent":     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "discord/1.0.9168 Chrome/128.0.6613.36 "
            "Electron/32.0.0 Safari/537.36",
            "referer": "https://discord.com/channels/@me"
        }

        for i in range(1, count + 1):

            payload = {"name": name, "type": 11}
            url = f"https://discord.com/api/v9/channels/{channelid}/threads"

            try:
                resp = session.post(url, headers=headers, json=payload)
                status = resp.status_code

            except Exception as e:
                print("[-]Sent failure")
                time.sleep(kankaku)
                continue

            if 200 <= status <= 299:
                print(f"[+]Sent success｜{token[:10]}**｜status:{status}")
            else:
                print(f"[-]Sent failure｜{token[:10]}**｜status:{status}")

            time.sleep(kankaku)
