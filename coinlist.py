#!/usr/bin/env python3

__project__  = "Price monitoring for Investment/Trading, notify Telegram"
__part__     = 'Coins config'

defaultThreshold = 0.5 # %
coinlist = {
	# close a position
	'SUIUSDT': {
		'threshold': 0.3, # %
		'prices': [ 0.9528, 0.9082 ],
	},
	'APTUSDT': {
		'prices': [ 7.6299, 6.9511, 6.68 ],
	},
	# buy more on spot:
	'NOTUSDT': {
		'prices': [0.020321],
	},
	'BONKUSDT': {
		'prices': [0.0000287],
	},
	'FLOKIUSDT': {
		'prices': [0.00024, 0.00021, 0.00017],
	},
	'BLURUSDT': {
		'prices': [0.36],
	},
	'WLDUSDT': {
		'prices': [4.6],
	},
#	'MEWUSDT': { # not at Binance yet
#		'prices': [0.41],
#	},
}

if __name__ == '__main__':
	print(__part__)
	for coin in coinlist:
		print(coin, coinlist[coin])
