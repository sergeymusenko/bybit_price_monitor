#!/usr/bin/env python3

__project__  = "Price monitor for Investment, send to Telegram"
__part__    = 'Coins config'

defaultTreshold = 0.5 # %
coinlist = {
	'ETHUSDT': {
		'threshold': 1.5, # %
		'prices': [2980.],
	},
	'PEPEUSDT': {
		'prices': [0.0000041877],
	},
	'TIAUSDT': {
		'prices': [8.917],
	},
	'LITUSDT': {
		'prices': [0.9533],
	},
	'WAXPUSDT': {
		'prices': [0.05826],
	},
	'BONKUSDT': {
		'prices': [0.0000134326],
	},
	'RADUSDT': {
		'prices': [1.624],
	},
	'AAVEUSDT': {
		'prices': [81.22],
	},
	'CELRUSDT': {
		'prices': [0.02057],
	},
	'KNCUSDT': {
		'prices': [0.5108],
	},
	'SHIBUSDT': {
		'prices': [0.00001944],
	},
	'OCEANUSDT': {
		'prices': [0.8106],
	},
	'DOGEUSDT': {
		'threshold': 2., # %
		'prices': [0.11691],
	},
#	'ADAUSDT': {
#		'prices': [0.4451],
#	},
#	'MATICUSDT': {
#		'prices': [0.6881],
#	},
#	'APTUSDT': {
#		'prices': [8.1988],
#	},
#	'SOLUSDT': {
#		'prices': [135.3],
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
# HOT ING  INJ  KEY  LTC  OP   SUI  TIA  TKO
# WIF GRT  JUP  PYTH AKT  GMT  RAY  JTO  TWT

if __name__ == '__main__':
	print(__part__)
	for coin in coinlist:
		print(coin, coinlist[coin])
