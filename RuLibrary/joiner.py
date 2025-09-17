import threading
import uuid
import tls_client

def joiner(tokens, invite):

    def join_task(token: str, invite: str):
        tls_session = tls_client.Session(client_identifier="safari_ios_16_0", random_tls_extension_order=True)
        get_cookie = tls_session.get("https://discord.com")
        headers = {
            "authority": "discord.com",
            "accept": "*/*",
            "accept-language": "en",
            "authorization": token,
            "cookie": "; ".join([f"{cookie.name}={cookie.value}" for cookie in get_cookie.cookies]) + "; locale=en-US",
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9168 Chrome/128.0.6613.36 Electron/32.0.0 Safari/537.36",
            "x-discord-locale": "en-US",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6ICJXaW5kb3dzIiwgImJyb3dzZXIiOiAiRGlzY29yZCBDbGllbnQiLCAicmVsZWFzZV9jaGFubmVsIjogInN0YWJsZSIsICJjbGllbnRfdmVyc2lvbiI6ICIxLjAuOTAyMyIsICJvc192ZXJzaW9uIjogIjEwLjAuMTkwNDUiLCAib3NfYXJjaCI6ICJ4NjQiLCAiYXBwX2FyY2giOiAiaWEzMiIsICJzeXN0ZW1fbG9jYWxlIjogImVuIiwgImJyb3dzZXJfdXNlcl9hZ2VudCI6ICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgZGlzY29yZC8xLjAuOTAyMyBDaHJvbWUvMTA4LjAuNTM1OS4yMTUgRWxlY3Ryb24vMjIuMy4yNiBTYWZhcmkvNTM3LjM2IiwgImJyb3dzZXJfdmVyc2lvbiI6ICIyMi4zLjI2IiwgImNsaWVudF9idWlsZF9udW1iZXIiOiAyNDQzNTgsICJuYXRpdmVfYnVpbGRfbnVtYmVyIjogMzkzMzQsICJjbGllbnRfZXZlbnRfc291cmNlIjogbnVsbCwgImRlc2lnbl9pZCI6IDB9",
        }

        resp = tls_session.post(
            f"https://discord.com/api/v9/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true",
            headers=headers,
            json={"session_id": uuid.uuid4().hex}
        )

        if 200 <= resp.status_code <= 299:
            print(f"Joined | {resp.status_code} | {token[:15]} | discord.gg/{invite}")
        elif resp.status_code == 403:
            print(f"Banned | {resp.status_code} | {token[:15]} | discord.gg/{invite}")
        elif resp.status_code == 404:
            print(f"Server Not Found | {resp.status_code} | {token[:15]} | discord.gg/{invite}")
        elif "captcha_key" in resp.text:
            print(f"Captcha | {resp.status_code} | {token[:15]} | discord.gg/{invite}")
        else:
            print(f"Failed | {resp.status_code} | {token[:15]} | discord.gg/{invite}")

    threads = []
    for token in tokens:
        t = threading.Thread(target=join_task, args=(token, invite), daemon=True)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
