#!/usr/bin/env python3
"""\
main.py - Price monitor for Investment

Works as cron script. Start it each hour.
# coin_price_monitor:, since 2024-04-11
each 10 min
*/10 * * * *   /path/coin_price_monitor/main.py 2>&1 | tee -a /path/coin_price_monitor/cron-log.txt

Can send Telegram message. In message:
	"green" mark means we going down to the price level - time to buy
	"red" mark means we going up to the price level - time to sell
	"+n% to nnn.nn" means "higher then nnn.n"
	"-n% to nnn.nn" means "lower then nnn.n"
Send signal again if we moved closer or changed price level. Otherwize no repeat same coin signal.
Last sent json file format: {'symbol': ['%', 'priceLevel', 'lastPrice', 'dateTime'],}

How to connect to Telegram: see instructions in simple_telegram.py module.
You can send to a group or to user account personally, see config.py

Uses binance public API: https://api.binance.com/api/v3/ticker/price?symbols=[...]
"""


__project__  = "Price monitor for Investment, notify Telegram"
__part__     = 'Main script'
__author__   = "Sergey V Musenko"
__email__    = "sergey@musenko.com"
__copyright__= "© 2024, musenko.com"
__license__  = "MIT"
__credits__  = ["Sergey Musenko"]
__date__     = "2024-03-29"
__version__  = "0.1"
__status__   = "dev"


from config import *
from coinlist import *
from simple_telegram import *
from datetime import datetime
import json

# get my secret LOCAL_CONFIG:
import socket
if socket.gethostname() == 'sereno':
	from config_local import *

# go to working directory to save status file
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
	time_mark = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

	# get symbol prices from Binance
	try:
		# make symbols list
		symbols = []
		for coin in coinlist:
			symbols.append(coin)
		# make request url
		URL = "https://api.binance.com/api/v3/ticker/price?symbols=" \
			+ json.dumps(symbols).replace(' ', '')
		# requesting data from url
		tickers = requests.get(URL).json()
		# debug: tickers = [{'symbol': 'ETHUSDT', 'price': '3143.86000000'},{'symbol': 'SOLUSDT', 'price': '140.26000000'},{'symbol': 'FILUSDT', 'price': '6.02600000'},{'symbol': 'APEUSDT', 'price': '1.19700000'},{'symbol': 'OPUSDT', 'price': '2.32500000'},{'symbol': 'APTUSDT', 'price': '9.32250000'},{'symbol': 'ARBUSDT', 'price': '1.18670000'},{'symbol': 'PEPEUSDT', 'price': '0.00000510'},{'symbol': 'TIAUSDT', 'price': '9.63000000'},{'symbol': 'STRKUSDT', 'price': '1.34900000'}]
		coinPrice = {}
		for tick in tickers:
			coinPrice[tick['symbol']] = float(tick['price'])
	except Exception as e:
		print(f"Error getting ticker: {str(e)}")
		return False

	# check coins and build message
	countCoins = 0
	TGmessage = ''
	for coin in coinlist:
		try:
			coinlist[coin]['message'] = False
			coinlist[coin]['lastThreshold'] = 0.
			# prepare
			if 'prices' in coinlist[coin] and type(coinlist[coin]['prices']) is list:
				coinlist[coin]['prices'].sort() # sort prices ascending
			else: # prices not defined...
				print(f"Error: there is no 'prices' for '{coin}'")
				continue
			if 'threshold' not in coinlist[coin]:
				coinlist[coin]['threshold'] = defaultTreshold
			threshold = float(coinlist[coin]['threshold'])

			# get coin price
			if coin not in coinPrice:
				print(f"Error: unknown price for '{coin}'")
				continue
			lastPrice = coinPrice[coin]
			coinlist[coin]['lastPrice'] = lastPrice
			countCoins += 1

			# check prices and select nearest to lastPrice
			minTreshold = 100. # will detect real value below
			for price in coinlist[coin]['prices']:
				diff = lastPrice - price # >0 aboce, <0 below
				diffSign = '+' if diff>=0 else '-' # forcing '+' and '-' sign for %%
				diffMark = sign_buy if diff>=0 else sign_sell # color marks for message
				curTreshold = abs(round(100 * diff / price, 1)) # in %
				if curTreshold <= threshold and curTreshold < minTreshold:
					coinlist[coin]['message'] = f"{diffMark}{coin} {lastPrice}:\n{diffSign}{curTreshold}% to {price}"
					coinlist[coin]['checkPrice'] = price
					coinlist[coin]['lastThreshold'] = curTreshold # save nearest % to coin
					minTreshold = curTreshold # to check next price level

		except Exception as e:
			print(f"Error on coin '{coin}': {str(e)}")
			continue

	# get last sent data saved to file before
	try:
		with open(lastSentJS) as infile: lastSent = json.load(infile)
	except Exception as e: # no problem if file does not exist
		lastSent = {}

	# check coins and prepare messages
	countMsg = 0
	lastSentChanged = False
	for coin in coinlist:
		if not coinlist[coin]['message']:
			continue
		lastCheckPrice = lastSent[coin][1] if coin in lastSent else 0.
		if lastCheckPrice != coinlist[coin]['checkPrice']: # last message was on different price level (or never was sent)
			lastSentThreshold = 100. # force to renew and send
		else:
			lastSentThreshold = lastSent[coin][0] if coin in lastSent else 100. # '100' means not found
		# send only if it is closer then last sent
		if lastSentThreshold > coinlist[coin]['lastThreshold']:
			TGmessage += coinlist[coin]['message'] + '\n' # save into TG message
			countMsg += 1
			lastSent[coin] = [
				coinlist[coin]['lastThreshold'],
				coinlist[coin]['checkPrice'],
				coinlist[coin]['lastPrice'],
				time_mark,
			] # % and last price
			lastSentChanged = True

	# save last sent data to file
	if lastSentChanged:
		try:
			with open(lastSentJS, "w") as outfile: outfile.write(json.dumps(lastSent))
		except Exception as e: # no problem if file does not exist
			print(f"Error saving LastSent: {str(e)}")

	# if message not empty send messages
	if TGmessage and TMchatID:
		send_to_telegram(TMapiToken, TMchatID, TGmessage.strip())

	# print report
	if not countMsg: countMsg = 'no'
	print(f'{time_mark} {__project__}: {countCoins} coin{s(countCoins)}, {countMsg} signal{s(countMsg)}')


def s(n):
	try: n = int(n)
	except Exception as e: n = 0
	return 's' if n>1 else ''


if __name__ == '__main__':
	main()

# that's all folks!
