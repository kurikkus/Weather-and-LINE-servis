# -*- coding: utf-8 -*-

import requests

WEATHER_API_KEY = 'openweathermap APIkey'
# 地元の都市名を入れる
WEATHER_CITY_NAME = '仙台'


def get_weather():

    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    url = f'{base_url}?q={WEATHER_CITY_NAME}&appid={WEATHER_API_KEY}'
    # HTTP通信用ライブラリを使って、openweatherサーバから情報を取得する。
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        return None

    # json文字列を辞書に変換
    data = response.json()
    temp = round(data["main"]["temp"] - 273.15, 1)
    weather = {
        'city_name': WEATHER_CITY_NAME,
        'weather': f'{data["weather"][0]["main"]}',
        'temperature': f'{temp}度',
    }

    return weather

if __name__ == '__main__':
    weather = get_weather()
    if weather != None:
        print(f'都市名: {weather["city_name"]}')
        print(f'天気: {weather["weather"]}')
        print(f'温度: {weather["temperature"]}')
t = f'温度: {weather["temperature"]}'
w = f'天気: {weather["weather"]}'
c = f'都市名: {weather["city_name"]}'
def main():
    send_line_notify(t) #温度
    send_line_notify(w) #天気
    send_line_notify(c) #都市名

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = 'Line notify token'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    main()
 