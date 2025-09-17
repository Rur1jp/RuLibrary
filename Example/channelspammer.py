import asyncio
from RuLibrary import discordSpam
tokens = ["MTQ……","MTQ……"]
channels = ["123456789"]
unko = "@everyone I am using this tool\nhttps://github.com/rur1jp/RuLibrary"
kaisuu = 10
asyncio.run(discordSpam(tokens, channels, msg=unko, repeat=kaisuu))
