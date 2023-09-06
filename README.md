# Rain-Checker App

This simple Python app fetches weather data from an open API and texts the user a message warning them if it will rain that day. 

The users location in latitude and longitude is passed to the Open Weather Map api, which returns a forecast of the local weather for that day.

If conditions are wet, the app utilises Twilio to send a text message to the user's phone number telling them to bring an umbrella.

API keys and authentication tokens are stored using local environment variables for security.