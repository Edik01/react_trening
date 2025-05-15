import requests

# Константы для API
EXCHANGE_API = "https://api.exchangerate-api.com/v4/latest/"
WEATHER_API = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = "fef9a7cade8ebaf536dda87676ea2bb3"
UNSPLASH_API = "https://api.unsplash.com/photos/random"
UNSPLASH_API_KEY = "B7ZooC56OIaCMwZRge_nfcjYABshLWLFluTYKf4NHsw"

# Пример данных по визам (можно расширить)
VISA_INFO = {
    "France": "For Ukrainian citizens, visa is required.",
    "Turkey": "For Ukrainian citizens, visa is not required.",
    "Japan": "For Ukrainian citizens, visa is required.",
}

def get_exchange_rate(base, target):
    url = f"{EXCHANGE_API}{base}"
    resp = requests.get(url)
    data = resp.json()
    rate = data['rates'].get(target)
    return rate

def get_weather(city):
    params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric", "lang": "ru"}
    resp = requests.get(WEATHER_API, params=params)
    data = resp.json()
    if data.get("main"):
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"{temp}°C, {desc}"
    return "Нет данных о погоде"

def get_visa_info(country):
    return VISA_INFO.get(country, "Нет информации о визе для этой страны.")

def get_photo(query):
    headers = {"Authorization": f"Client-ID {UNSPLASH_API_KEY}"}
    params = {"query": query, "orientation": "landscape"}
    resp = requests.get(UNSPLASH_API, headers=headers, params=params)
    data = resp.json()
    return data.get("urls", {}).get("regular", "Нет фото")

def main():
    country = input("Введите страну назначения: ")
    city = input("Введите город: ")
    base_currency = input("Ваша валюта (например, USD): ")
    target_currency = input("Валюта страны назначения (например, EUR): ")

    print("\n--- Информация о путешествии ---")
    print("Курс валют:")
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        print(f"1 {base_currency} = {rate} {target_currency}")
    else:
        print("Не удалось получить курс валют.")

    print("\nВизовая информация:")
    print(get_visa_info(country))

    print("\nПогода:")
    print(get_weather(city))

    print("\nФото города:")
    print(get_photo(city))

if __name__ == "__main__":
    main()