#!/usr/bin/env python3

__project__  = "Price monitor for Investment, send to Telegram"
__part__    = 'Coins config'

defaultThreshold = 0.5 # %
coinlist = {
	# close a position
	'SUIUSDT': {
		#'threshold': 0.3, # %
		'prices': [ 0.9528, 0.9082 ],
	},
	'APTUSDT': {
		'prices': [ 7.6299, 6.9511 ],
	},

}
'''
	# докупить на spot
#	'NOTUSDT': {
#		'prices': [0.020321],
#	},
#	'BONKUSDT': {
#		'prices': [0.0000287],
#	},
	'FLOKIUSDT': {
		'prices': [0.00024, 0.00021, 0.00017],
	},
	'BLURUSDT': {
		'prices': [0.36],
	},
	'WLDUSDT': {
		'prices': [4.6],
	},
#	'MEWUSDT': { # no at Binance
#		'prices': [0.41],
#	},
	# потенциал роста
	'ETHUSDT': {
		'threshold': 1., # %
		'prices': [3060.],
	},
	'STRKUSDT': {
		'prices': [1.17, 1.09],
	},
	'BNBUSDT': {
		'prices': [599.],
	},
	'ATOMUSDT': {
		'prices': [8.23, 7.73],
	},
	'MATICUSDT': {
		'prices': [0.6517, 0.69],
	},
	'SOLUSDT': {
		'prices': [142.],
	},
	'WUSDT': {
		'prices': [0.56, 0.62],
	},
	'PEPEUSDT': {
		'prices': [ 0.0000124, 0.000011 ],
	},
	'DOGEUSDT': {
		'prices': [0.12197],
	},
	'SHIBUSDT': {
		'prices': [0.0000219, 0.0000237],
	},
	'PEOPLEUSDT': {
		'prices': [0.103, 0.077],
	},
	'ARBUSDT': {
		'prices': [1.031, 0.979],
	},
	'OPUSDT': {
		'prices': [2.34],
	},
#	'LTCUSDT': {
#		'prices': [76.],
#	},
#	'WAXPUSDT': {
#		'prices': [0.05826],
#	},
#	'RADUSDT': {
#		'prices': [1.624],
#	},
#	'CELRUSDT': {
#		'prices': [0.0205, 0.0161],
#	},
#	'KNCUSDT': {
#		'prices': [0.511],
#	},
#	'LITUSDT': {
#		'prices': [0.815],
#	},
#	'SUSHIUSDT': {
#		'prices': [0.9495],
#	},
#	'NEOUSDT': {
#		'prices': [14.1, 11.2],
#	},
#	'HBARUSDT': {
#		'prices': [0.0796],
#	},
#	'XRPUSDT': {
#		'prices': [0.499],
#	},
#	'TIAUSDT': {
#		'prices': [8.917],
#	},
#	'COMPUSDT': {
#		'threshold': 1.5, # %
#		'prices': [53.27],
#	},
#	'OCEANUSDT': {
#		'prices': [0.8106],
#	},
#	'AAVEUSDT': {
#		'prices': [81.22],
#	},
#	'ADAUSDT': {
#		'prices': [0.4451],
#	},
#	'APEUSDT': {
#		'prices': [1.131, 1.025],
#	},
#	'ENSUSDT': {
#		'prices': [11.5],
#	},
#	'XTZUSDT': {
#		'prices': [1.0017],
#	},
#	'BANDUSDT': {
#		'prices': [1.351],
#	},
#	'ZILUSDT': {
#		'prices': [0.02298],
#	},
#	'ETCUSDT': {
#		'prices': [25.53],
#	},
#	'ANKRUSDT': {
#		'prices': [0.04137],
#	},
#	'SANDUSDT': {
#		'prices': [0.4258],
#	},
#	'FILUSDT': {
#		'prices': [5.720],
#	},
#	'WAVESUSDT': {
#		'prices': [2.288],
#	},
#	'AXSUSDT': {
#		'prices': [6.744],
#	},
#	'CELOUSDT': {
#		'prices': [0.706],
#	},
#	'BTCUSDT': {
#		'threshold': 1.0, # %
#		'prices': [73978., 68045., 65797., 61838., 59150.],
#	},
'''
if __name__ == '__main__':
	print(__part__)
	for coin in coinlist:
		print(coin, coinlist[coin])
