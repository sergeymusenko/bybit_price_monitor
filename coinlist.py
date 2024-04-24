#!/usr/bin/env python3

__project__  = "Price monitor for Investment, send to Telegram"
__part__    = 'Coins config'

defaultTreshold = 0.5 # %
coinlist = {
	'ETHUSDT': {
		'threshold': 1., # %
		'prices': [2919., 2846.7],
	},
	'LTCUSDT': {
		'threshold': 1.5, # %
		'prices': [64.54],
	},
	'PEPEUSDT': {
		'prices': [0.0000041877, 0.0000048591],
	},
	'TIAUSDT': {
		'prices': [8.917],
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
		'prices': [0.02057],
	},
	'KNCUSDT': {
		'prices': [0.5108],
	},
	'SHIBUSDT': {
		'prices': [0.00002091, 0.00001944],
	},
	'DOGEUSDT': {
		'prices': [0.11691],
	},
	'LITUSDT': {
		'prices': [0.815],
	},
	'SOLUSDT': {
		'prices': [135.4],
	},
	'XRPUSDT': {
		'prices': [0.499],
	},
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
#	'APTUSDT': {
#		'prices': [8.1988],
#	},
#	'OPUSDT': {
#		'prices': [2.152, 1.8, 1.5],
#	},
#	'APEUSDT': {
#		'prices': [1.131, 1.025],
#	},
#	'ARBUSDT': {
#		'prices': [1.031, 0.912],
#	},
#	'ATOMUSDT': {
#		'prices': [7.43],
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
#	'STRKUSDT': {
#		'prices': [1.29],
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
#	'FLOKIUSDT': {
#		'prices': [0.0001305],
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
