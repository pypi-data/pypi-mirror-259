from setuptools import setup, find_packages

setup(
    name="ATH",
    version="0.1.2",
    packages=find_packages(),
    install_requires=["pyttsx3", "cryptography", "speechrecognition", "ursina"]
)