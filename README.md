A small Python script that can tell you the weather of any city/town anywhere in the world over the command line.

Weather data is accessed over the internet using the *OpenWeather* API. You'll need an API key, which you can get by simply [sigining up](https://openweathermap.org/ "Link to website") to their website, signing in, and then going to "My API keys" under your profile.

The program has a proper command line interface with optional flags, help messages and so forth. Run `show_weather --help` to see more.

## Install

```
% pip install show-weather
```

## Example

To get the current weather in Toronto, for example, run

```
% show_weather <API_KEY> toronto
```

which outputs to the terminal

```
--------------------------------------------------

      Place:    Toronto
    Country:    Canada
Temperature:    -10.6°C

--------------------------------------------------
```
