#!/usr/bin/env python3

__project__  = "Price monitor for Investment, send to Telegram"
__part__    = 'Coins config'

defaultTreshold = 0.5 # %
coinlist = {
	'SUIUSDT': {
		'prices': [1.0759, 1.0098, 0.885],
	},

	'ARBUSDT': {
		'prices': [1.031, 0.979],
	},
	'OPUSDT': {
		'prices': [2.1-4],
	},
	'STRKUSDT': {
		'prices': [1.132],
	},
	'ATOMUSDT': {
		'prices': [7.8, 7.33],
	},
	'APTUSDT': {
		'prices': [8.1988],
	},
	'FLOKIUSDT': {
		'prices': [0.000148, 0.000128,],
	},
	'SOLUSDT': {
		'prices': [133., 122.6],
	},
	'DOGEUSDT': {
		'prices': [0.12197],
	},

	'ETHUSDT': {
		'threshold': 1., # %
		'prices': [2919., 2846.7],
	},
	'LTCUSDT': {
		'threshold': 1.5, # %
		'prices': [68.6],
	},
	'WAXPUSDT': {
		'prices': [0.05826],
	},
	'BONKUSDT': {
		'prices': [0.00001106],
	},
	'RADUSDT': {
		'prices': [1.624],
	},
	'CELRUSDT': {
		'prices': [0.0205, 0.0161],
	},
	'KNCUSDT': {
		'prices': [0.511],
	},
	'SHIBUSDT': {
		'prices': [0.00002091, 0.00001944],
	},
	'LITUSDT': {
		'prices': [0.815],
	},
	'SUSHIUSDT': {
		'prices': [0.9495],
	},
	'PEOPLEUSDT': {
		'prices': [0.02211],
	},
	'NEOUSDT': {
		'prices': [14.1, 11.2],
	},
	'HBARUSDT': {
		'prices': [0.0796],
	},
#	'XRPUSDT': {
#		'prices': [0.499],
#	},
#	'PEPEUSDT': {
#		'prices': [0.0000041877, 0.0000048591],
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
#	'MATICUSDT': {
#		'prices': [0.6881],
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
}
# more coins to watch:
# AI  BEAM BLUR BNB  DOT  FLM  FLR  FXS  HIGH  XVS
# HOT INJ  KEY  LTC  SUI  TIA  TKO  JTO  TWT
# WIF GRT  JUP  PYTH AKT  GMT  RAY

if __name__ == '__main__':
	print(__part__)
	for coin in coinlist:
		print(coin, coinlist[coin])
