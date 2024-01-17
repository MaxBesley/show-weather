# current-weather-command

A small Python script that can tell you the weather of any city/town anywhere in the world over the command line.

Weather data is accessed over the internet using the *OpenWeatherMap* API. You'll need an API key, which you can get by simply [sigining up](https://openweathermap.org/ "Link to their website") to their website, signing in, and then going to "My API keys" under your profile.

The program also has a proper command line interface with optional flags, help messages and so forth. Run the command `python3 weather.py --help` to see more.

## Example

To get the current weather in Toronto, for example, run

```
% python3 weather.py <API_KEY> toronto
```

which outputs to the terminal

```
--------------------------------------------------

      Place:    Toronto
    Country:    Canada
Temperature:    -10.6
Description:    "overcast clouds"

--------------------------------------------------
```



