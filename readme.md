To run this bot you need to create python virtual environment (venv) in directory of the bot with this command:
```
python -m venv venv
```
Open Python virtual python environment with terminal by this command:
```
venv/Scripts/Activate
```
Install necessary packages in venv with this command:
```
pip install -r requirements.txt
```
Create .env file in directory of the bot and put WEATHER_API_KEY from weatherbit.io and telegram TOKEN of your bot. You need to get something like this:
```
TOKEN=0000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
WEATHER_API_KEY=a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1
```
After these steps you can start your bot with this command:
```
python main.py
```