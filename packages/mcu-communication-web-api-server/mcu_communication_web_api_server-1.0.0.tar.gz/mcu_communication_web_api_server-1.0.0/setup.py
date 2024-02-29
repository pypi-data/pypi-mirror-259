# setup.py
from setuptools import setup, find_packages

setup(
    name='mcu_communication_web_api_server',
    version='1.0.0',
    description='Python package for MCU communication tcp mcu_protocol through web api',
    packages=find_packages(),
    install_requires=["flatbuffers","uvicorn","uvloop","python-multipart","mcu_communication_tcp","fastapi[swagger]"]
)
