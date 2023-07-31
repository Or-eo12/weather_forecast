import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "b6907d289e10d714a6e88b30761fae22"

# Function to fetch weather data from the API for a given city and date
def get_weather_data(city, date):
    url = f"{API_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast_list = data.get('list')
        for forecast in forecast_list:
            if date in forecast['dt_txt']:
                return forecast['main']['temp'], forecast['wind']['speed'], forecast['main']['pressure']
        print(f"No data available for {date}")
        return None, None, None
    else:
        print("Error fetching weather data.")
        return None, None, None

# Main function to prompt the user for options and handle input
def main():
    city = input("Enter the city name: ")

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature, _, _ = get_weather_data(city, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature} °C")
        elif option == '2':
            date = input("Enter the date (YYYY-MM-DD): ")
            _, wind_speed, _ = get_weather_data(city, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
        elif option == '3':
            date = input("Enter the date (YYYY-MM-DD): ")
            _, _, pressure = get_weather_data(city, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
        elif option == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
