import json 
from datetime import datetime
import calendar
import pytz
import random

def get_day_today():
	timezone = pytz.timezone('Africa/Kampala')
	date_today = datetime.now(timezone)
	return str(calendar.day_name[date_today.weekday()])

def get_complete_message(title,subtitle,msg):
	return str(title) + '\n' + str(subtitle) + '\n' + str(msg)

def parse_json_as_dict(filename):
	try:
		f = open(filename)
		ddict = json.load(f) 
		f.close()
		return ddict
	except Exception as e:
		print(e)

def get_ready_message(filename='sms_file.json'):

	data_dict = parse_json_as_dict(filename=filename)

	today = get_day_today()
	today_found = False

	while not today_found:

		language_list = list(data_dict.keys())
		language = random.choice(language_list)

		crop_list = list(data_dict[language].keys())
		crop = random.choice(crop_list)

		day_list = list(data_dict[language][crop].keys())

		today_found = True if today in day_list else False

	msg_dict = data_dict[language][crop][today]

	complete_msg_list = [get_complete_message(title,subtitle,msg) \
	for title,subtitle,msg in zip(msg_dict['title'], msg_dict['subtitle'], msg_dict['msg'])]

	msg = random.choice(complete_msg_list)

	return language, crop, today, msg


language, crop, day, msg = get_ready_message()

print(language)
print(crop)
print(day)
print(msg)
