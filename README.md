Weather App
Overview
This is a weather forecasting application built using Django. The app allows users to input a city name and get real-time weather information, including the current temperature, weather description, and weather icon. Additionally, the app tracks and displays the most recent city searches made by users.

Features
City Search: Users can search for weather information by entering a city name.
Weather Details: Displays current temperature, weather description, and an icon representing the weather condition.
Recent Searches: Displays the last 5 cities searched, with timestamps.
Error Handling: Handles cases where the city is not found or network errors occur.
Technologies Used
Django: A high-level Python web framework for building the web application.
Requests: A simple HTTP library to make requests to the OpenWeatherMap API for weather data.
OpenWeatherMap API: Provides real-time weather data.
SQLite: The default database for storing recent search data.
