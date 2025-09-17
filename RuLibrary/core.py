import random
import string
import asyncio
import aiohttp

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

class RuDiscord:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }

    async def msgSend(self, session, channel_id: str, content: str):
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        payload = {"content": content}
        async with session.post(url, headers=self.headers, json=payload) as resp:
            text = await resp.text()

            if resp.status in (200, 201):
                print(f"{GREEN}[+]Sent success｜{self.token[:8]}**｜status:{resp.status}{RESET}")
            elif resp.status == 429:
                try:
                    data = await resp.json()
                    wait1 = data.get("retry_after", "unknown")
                except:
                    wait1 = "unknown"
                    sine = float(wait1) + 0.2
                print(f"{YELLOW}[-]Limited｜{self.token[:8]}**｜wait->{wait1}s{RESET}")
                await asyncio.sleep(0.2)
            else:
                print(f"{RED}[-] Failed｜{self.token[:8]}**｜status:{resp.status}｜{text}{RESET}")
                
def random_string(length=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

async def discordSpam(tokens, channels, msg="@everyone discord.gg/aarr", repeat=1):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(repeat):
            for token in tokens:
                client = RuDiscord(token)
                for channel in channels:
                    content = f"{msg}\n{random_string(8)}"
                    tasks.append(client.msgSend(session, channel, content))
        await asyncio.gather(*tasks)
