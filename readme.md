Create .env file in directory of the bot and put WEATHER_API_KEY from weatherbit.io and telegram TOKEN of your bot. You need to get something like this:
```
TOKEN=0000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
WEATHER_API_KEY=a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1
```
Run Docker container (it will run bot) by this command:
```
docker compose up --build
```