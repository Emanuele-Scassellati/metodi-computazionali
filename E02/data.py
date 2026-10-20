import numpy as np
#import datetime
from datetime import datetime, timedelta

date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')

date = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")


datenow = datetime.now()
print(datenow.year)
print(datenow.hour)
print(datenow.second)


condizione = True
while condizione == True:
	if( data.month>12 or date.month<1):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.day>31 or date.day<1):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==2 and date.day>28):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==1 and date.day > 31):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==3 and date.day>31):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==4 and date.day>30):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==5 and date.day>31):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==6 and date.day>30):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==7 and date.day>31):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==8 and date.day>31):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==9 and date.day>30):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==10 and date.day>31):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==11 and date.day>30):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(date.month==12 and date.day>31):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(Y<0 or Y>12):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(H<0 or H>24):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(M>60 or M<0):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')
	if(S>60 or S<0):
		condizione = False
		date_str = input('Immettere la data si nascita scrivendo per esempio 12-10-1980 21:15:45: ')

	timediff = datenow - date
	condizione = False

print(timediff)
