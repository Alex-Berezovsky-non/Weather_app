import requests
from plyer import notification

# Константы
API_KEY = '23496c2a58b99648af590ee8a29c5348'
CITY = 'Москва'
def get_weather(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Ошибка при получении данных: {response.status_code}")
    return response.json()
def format_weather_message(weather_dict):
    temp = weather_dict['main']['temp']
    feels_like = weather_dict['main']['feels_like']
    description = weather_dict['weather'][0]['description']
    return f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}'
def notify_weather(message):
    notification.notify(
        title='Погода в Москве',
        message=message,
        app_name='Weather',
        app_icon=None
    )
def main():
    try:
        weather_dict = get_weather(CITY, API_KEY)
        message = format_weather_message(weather_dict)
        notify_weather(message)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
if __name__ == "__main__":
    main()
