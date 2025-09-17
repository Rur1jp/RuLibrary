from setuptools import setup, find_packages

setup(
    name="RuLibrary",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
    ],
    python_requires=">=3.8",
    description="discordを楽しく遊ぶために作りました。",
    author="るる",
    url="https://github.com/rur1jp/RuLibrary",
)
