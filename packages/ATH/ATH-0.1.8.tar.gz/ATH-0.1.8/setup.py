from setuptools import setup, find_packages

setup(
    name="ATH",
    version="0.1.8",
    packages=find_packages(),
    install_requires=["pyttsx3", "cryptography", "speechrecognition", "asyncio", "discord", "discord.py"]
)