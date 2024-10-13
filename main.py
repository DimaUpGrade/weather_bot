import telebot
from telebot import types
from config import TOKEN
from SI import mbar_to_mm_hg
from weather import current_weather, daily_weather, today_weather


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет! Я могу подсказать погоду в твоём городе на ближайшее время! Напиши название своего города!")


@bot.message_handler()
def send_welcome(message):
    if data := current_weather(message.text):
        kb = types.InlineKeyboardMarkup(row_width=2)
        today_forecast_btn = types.InlineKeyboardButton(text="Прогноз на день", callback_data=f"today_forecast&{data['city_name']}&{data['country_code']}&{message.chat.id}")
        daily_forecast_btn = types.InlineKeyboardButton(text="Прогноз на 16 дней", callback_data=f"daily_forecast&{data['city_name']}&{data['country_code']}&{message.chat.id}")
        kb.add(today_forecast_btn, daily_forecast_btn)
        bot.send_message(message.chat.id, f"<b>{data['city_name']} [{data['country_code']}]</b>, сейчас:\n\n<b>Температура:</b> {data['temp']} °C\n<b>Влажность:</b> {data['rh']}%\n<b>Давление:</b> {mbar_to_mm_hg(data['pres'])} мм. рт. ст.", parse_mode='HTML',
                         reply_markup=kb)
    else:
        bot.send_message(message.chat.id, "Что-то пошло не так...")


@bot.callback_query_handler(func=lambda call: True)
def check_callback_data(call):
    if call.data:
        call_data = call.data.split("&")
        if call_data[0] == "daily_forecast":
            if data := daily_weather(call_data[1]):
                bot.send_message(call_data[3], f"<b>Погода в городе {call_data[1]} [{call_data[2]}] на 16 дней:</b>", parse_mode='HTML')
                for daily in data:
                    bot.send_message(call_data[3], f"<b><i>{call_data[1]} [{call_data[2]}], {daily['datetime']}</i></b>\n\n<b>Средняя температура:</b> {daily['temp']} °C\n<b>Максимальная температура:</b> {daily['max_temp']} °C\n<b>Минимальная температура:</b> {daily['min_temp']} °C\n<b>Вероятность осадков:</b> {daily['pop']}%\n<b>Ветер:</b> {daily['wind_cdir']}, {daily['wind_spd']} м/с\n<b>Давление:</b> {mbar_to_mm_hg(daily['pres'])} мм. рт. ст.\n<b>Влажность:</b> {daily['rh']}%", parse_mode='HTML')
            else:
                bot.send_message(call_data[3], "Что-то пошло не так...")
        elif call_data[0] == "today_forecast":
            if data := today_weather(call_data[1]):
                bot.send_message(call_data[3], f"<b>Погода в городе {call_data[1]} [{call_data[2]}] на 24 часа:</b>", parse_mode='HTML')
                for hour in range(24):
                    bot.send_message(call_data[3], f"<b><i>{call_data[1]} [{call_data[2]}], {', '.join(data[hour]['timestamp_local'].split('T'))} (местное)</i></b>\n\n<b>Температура:</b> {data[hour]['temp']} °C\n<b>Ощущается:</b> {data[hour]['app_temp']} °C\n<b>Вероятность осадков:</b> {data[hour]['pop']}%\n<b>Облачность:</b> {data[hour]['clouds']}%\n<b>Ветер:</b> {data[hour]['wind_cdir']}, {data[hour]['wind_spd']} м/с\n<b>Давление:</b> {mbar_to_mm_hg(data[hour]['pres'])} мм. рт. ст.\n<b>Влажность:</b> {data[hour]['rh']}%", parse_mode='HTML')


bot.infinity_polling()
