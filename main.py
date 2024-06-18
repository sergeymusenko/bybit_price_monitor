#!/usr/bin/env python3
"""\
main.py - Price monitoring for Investment/Trading

Uses Binance public API to get tickers: https://api.binance.com/api/v3/ticker/price?symbols=[...]
Send signal again if price moved closer or changed price setting level. Otherwize no repeat same signal.

Works as a cron script. Start it each 5-10 min. Crontab:
# coin_price_monitor:, since 2024-04-11
*/10 * * * *   /pathto/coin_price_monitor/main.py 2>&1 | tee -a /pathto/coin_price_monitor/cron-log.txt

Can send Telegram message. In message:
	"green/up" mark means price is going up
	"red/down" mark means price going down
	"+n% to nnn.nn" means "higher then nnn.n price setting"
	"-n% to nnn.nn" means "lower then nnn.n price setting"

Last sent json file format: {'symbol': ['%', 'priceLevel', 'lastPrice', 'dateTime'],}
Last price json file format: {'symbol': [priceold, ..., pricenew],}

How to connect to Telegram: see instructions in simple_telegram.py module.
You can send to a group or to user account personally. Set config.py
"""


__project__  = "Price monitoring for Investment/Trading, notify Telegram"
__part__     = 'Main script'
__author__   = "Sergey V Musenko"
__email__    = "sergey@musenko.com"
__copyright__= "© 2024, musenko.com"
__license__  = "MIT"
__credits__  = ["Sergey Musenko"]
__date__     = "2024-06-18"
__version__  = "0.2"
__status__   = "dev"


# last price src (Binance, code logic depends on it)
srcURL = "https://api.binance.com/api/v3/ticker/price?symbols="

# mesage mark (direction):
sign_buy     = '🟢'
sign_sell    = '🔴'
sign_nothig  = '🔵'
sign_uparr   = '⏫' # '▲' '↗'
sign_dnarr   = '⏬' # '▼'  '↘'
sign_noarr   = '⏯'  # '-'


from config import *
from coinlist import *
from simple_telegram import *
from datetime import datetime
import json
import os
import statistics

# go to working directory to save status file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# get my secret LOCAL_CONFIG:
import socket
if socket.gethostname() in ['sereno', 'vostro']:
	from config_local import *


def main():
	global sign_buy, sign_sell, sign_nothig, sign_uparr, sign_dnarr, sign_noarr

	if not coinlist: exit(0)
	time_mark = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

	# get last prices to show a direction
	try:
		with open(lastPricesJS) as infile: lastPricesSrc = json.load(infile)
	except Exception as e: # no problem if file does not exist
		lastPricesSrc = {}
	lastPrices = {} # we will drop symbols from src if it is not in coinlist any more

	# get symbol prices from Binance
	try:
		# make symbols list
		symbols = []
		for coin in coinlist:
			symbols.append(coin)
		# make request url
		URL = srcURL + json.dumps(symbols).replace(' ', '')
		# requesting data from url
		tickers = requests.get(URL).json()
		# debug: tickers = [{'symbol': 'ETHUSDT', 'price': '3143.86000000'},{'symbol': 'SOLUSDT', 'price': '140.26000000'},{'symbol': 'FILUSDT', 'price': '6.02600000'},{'symbol': 'APEUSDT', 'price': '1.19700000'},{'symbol': 'OPUSDT', 'price': '2.32500000'},{'symbol': 'APTUSDT', 'price': '9.32250000'},{'symbol': 'ARBUSDT', 'price': '1.18670000'},{'symbol': 'PEPEUSDT', 'price': '0.00000510'},{'symbol': 'TIAUSDT', 'price': '9.63000000'},{'symbol': 'STRKUSDT', 'price': '1.34900000'}]
		if 'msg' in tickers: # {'code': -1121, 'msg': 'Invalid symbol.'}
			print('Request Tickers error: ' + tickers['msg'])
			exit(0)
		coinPrice = {}
		for tick in tickers:
			symbol = tick['symbol']
			symbprice = float(tick['price'])
			coinPrice[symbol] = symbprice
			# update last prices stacks
			if symbol not in lastPricesSrc: # symbol was not in src file
				lastPrices[symbol] = [symbprice]
			else:
				lastPrices[symbol] = lastPricesSrc[symbol].copy()
				if len(lastPrices[symbol]) >= lastPricesAvgLen: # keep {n} last elements in list
					lastPrices[symbol].pop(0) # remove oldest element
				lastPrices[symbol].append(symbprice) # save as last element

	except Exception as e:
		print(f"Error getting Symbols: {str(e)}")
		return False

	del lastPricesSrc, tickers # do not need them any more

	# save last prices
	try:
		with open(lastPricesJS, "w") as outfile: outfile.write(json.dumps(lastPrices))
	except Exception as e: # no problem if file does not exist
		print(f"Error saving LastPrices file: {str(e)}")

	# check coins and build messages
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
				print(f"Warning: there is no 'prices' for '{coin}'")
				continue
			if 'threshold' not in coinlist[coin]:
				coinlist[coin]['threshold'] = defaultThreshold
			threshold = float(coinlist[coin]['threshold'])

			# get coin price
			if coin not in coinPrice:
				print(f"Error: unknown last price for '{coin}'")
				continue
			lastPrice = coinPrice[coin]
			coinlist[coin]['lastPrice'] = lastPrice

			countCoins += 1 # symbol counted, next:
			# check prices and select nearest to lastPrice
			minTreshold = 100. # will detect real value below
			for price in coinlist[coin]['prices']:
				price = float(price) # coinlist can have int or string
				diff = lastPrice - price # >0 above, <0 below

				# detect a direction
				diffSign = '+' if diff>=0 else '-' # forcing '+' and '-' sign for %%

				# 1. above/below from config price:
				# diffMark = sign_buy if diff>=0 else sign_sell # color marks for message

				# 2. moving up or down from average:
				avgPrice = statistics.fmean(lastPrices[coin])
				# color balls:
				diffMark = sign_buy if lastPrice > avgPrice else sign_sell if lastPrice < avgPrice else sign_nothing
				# arrows:
				#diffMark = sign_uparr if lastPrice > avgPrice else sign_dnarr if lastPrice < avgPrice else sign_noarr

				# show a message? we will select closest price from coinlist prices
				curTreshold = abs(round(100 * diff / price, 1)) # float, in %
				if curTreshold==0.:
					curTreshold = 0 # int, just to be shorter
					diffSign = ''
				if curTreshold <= threshold and curTreshold < minTreshold: # have to show a message!
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
	else: # no message so print it
		print(TGmessage)

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
