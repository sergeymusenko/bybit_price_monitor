#!/usr/bin/env python3
"""\
main.py - Price monitor for Bybit

Works as cron script. Start it each hour.
Not using auth at Bybit.
Can send Telegram message to a Group or to personal account, see config.py
In message:
	"green" mark means we going down to the price level - time to buy
	"red" mark means we going up to the price level - time to sell
Send signal again if we moved closer or changed price level. Otherwize no repeat same coin signal.
Last sent json file format: {'symbol': ['%', 'priceLevel', 'lastPrice', 'dateTime'],}

How to connect to Telegram: see instructions in simple_telegram.py module.
You can send to a group or to user account personally.

docs: https://bybit-exchange.github.io/docs/v5/intro
pip install pybit
"""

__project__	= "Price monitor for Bybit, send to Telegram"
__part__	= 'Main script'
__author__	= "Sergey V Musenko"
__email__	= "sergey@musenko.com"
__copyright__= "© 2024, musenko.com"
__license__	= "MIT"
__credits__	= ["Sergey Musenko"]
__date__	= "2024-03-29"
__version__	= "0.2"
__status__	= "dev"

from config import *
from coinlist import *
from simple_telegram import *
from datetime import datetime
import json
from pybit.unified_trading import HTTP

# get my secret LOCAL_CONFIG:
import socket
if socket.gethostname() == 'sereno':
	from config_local import *


def s(n):
	try: n = int(n)
	except Exception as e: n = 0
	return 's' if n>1 else ''


def main():
	time_mark = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

	# open Bybit session
	session = HTTP()

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
				continue
			if 'threshold' not in coinlist[coin]:
				coinlist[coin]['threshold'] = 1. # default is 1%
			threshold = float(coinlist[coin]['threshold'])

			# print(f"checking {coin}")

			# get data from Bybit
			res = session.get_tickers(category=category, symbol=coin)
			rlst = res.get('result', {}).get('list',[])[0]
			lastPrice = float(rlst.get('lastPrice', 0))
			coinlist[coin]['lastPrice'] = lastPrice
			countCoins += 1

			# check prices and select nearest to lastPrice
			minTreshold = 100.
			for price in coinlist[coin]['prices']:
				diff = lastPrice - price # >0 aboce, <0 below
				diffSign = '+' if diff>=0 else '-' # forcing '+' and '-' sign for %%
				diffMark = sign_buy if diff>=0 else sign_sell # color marks for message
				curTreshold = abs(round(100 * diff / price, 1)) # in %
				if curTreshold <= threshold and curTreshold < minTreshold:
					coinlist[coin]['message'] = f"{diffMark}{coin} {lastPrice}:\n{diffSign}{curTreshold}% to {price}{', spot' if category=='spot' else ''}"
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
			TGmessage += coinlist[coin]['message'] # save into TG message
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
		send_to_telegram(TMapiToken, TMchatID, TGmessage)

	# print report
	if not countMsg: countMsg = 'no'
	print(f'{time_mark} {__project__}: {countCoins} coins, {countMsg} signal{s(countMsg)}')


if __name__ == '__main__':
	main()

# that's all folks!
