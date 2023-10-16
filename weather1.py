import requests
import json

print("\nWelcome to the Weather Information App!\n")

try:
    # Prompt the user for a city name
    city = input("Enter the name of the city: ")

    # Create the URL for the WeatherAPI request
    URL = f"http://api.weatherapi.com/v1/current.json?key=4c8fc4835fcd42e594d231853232208&q={city}"

    # Send a GET request to the specified URL
    response = requests.get(URL)
    
    if response.status_code != 200:
        raise requests.exceptions.RequestException("API request failed")

    # Parse the JSON response into a Python dictionary
    data = json.loads(response.text)

    # Extract relevant data from the response
    location = data['location']
    current = data['current']

    # Display weather information
    print(f"Location: {location['name']}, {location['region']}, {location['country']}")
    print(f"Local Time: {location['localtime']}")
    print(f"Temperature: {current['temp_c']}°C ({current['temp_f']}°F)")
    print(f"Condition: {current['condition']['text']}")

except requests.exceptions.RequestException as e:
    print("Error: Failed to fetch weather data. Please check your internet connection or the city name.")
except json.JSONDecodeError:
    print("Error: Failed to parse the JSON response. Please try again later or check the city name.")

print("\n🌞 Thank you for using our weather service! Have a great day! ☔️")
