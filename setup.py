from setuptools import find_packages, setup

setup(
    name="voicebot",
    version="0.0.1",
    author="Riitu",
    author_email="ritu.khurana2711@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask']
)