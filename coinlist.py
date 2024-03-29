#!/usr/bin/env python3

__project__ = "Price monitor for Bybit, send to Telegram"
__part__    = 'Coins config'


coinlist = {
	'BTCUSDT': {
		'threshold': 1.5, # %
		'prices': [73800, 61100, 63000],
	},
	'ETHUSDT': {
		'threshold': 2.0, # %
		'prices': [4060., 2300.],
	},
	'SOLUSDT': {
		'threshold': 5., # %
		'prices': [85.5, 202.3],
	},
}

# more coins to watch:
#	DOT  SUI  TIA   LTC   TKO   INJ  ARB   BEAM
#	TWT  OP	  FLM   BLUR  ING   BNB  ATOM  AXS
#	XVS  FLR  HIGH  BONK  BEAM  SOL  FXS   KEY
#	XVS  DOT  ARB   AI    HOT


if __name__ == '__main__':
	print(__part__)
