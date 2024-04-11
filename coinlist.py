#!/usr/bin/env python3

__project__ = "Price monitor for Bybit, send to Telegram"
__part__    = 'Coins config'


coinlist = {
	'BTCUSDT': {
		'threshold': 1.5, # %
		'prices': [73978., 68045., 65797., 61838., 59150.],
	},
	'ETHUSDT': {
		'threshold': 2.0, # %
		'prices': [3404., 3387., 3304., 2939.],
	},
	'SOLUSDT': {
		'threshold': 5., # %
		'prices': [164., 750.],
	}, # WIF, GRT, JUP, BONK, PYTH, AKT, GMT, RAY, JTO
}

# more coins to watch:
# AI  ARB  AXS  BEAM  BLUR  BNB  DOT  FLM  FLR  FXS  HIGH  XVS
# HOT ING  INJ  ATOM  BONK  KEY  LTC  OP   SUI  TIA  TKO   TWT


if __name__ == '__main__':
	print(__part__)
