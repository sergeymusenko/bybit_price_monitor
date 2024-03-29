#!/usr/bin/env python3

__project__	= "Price monitor for Bybit, send to Telegram"
__part__	= 'Main config'
__author__	= "Sergey V Musenko"
__email__	= "sergey@musenko.com"
__copyright__= "© 2024, musenko.com"
__license__	= "MIT"
__credits__	= ["Sergey Musenko"]
__date__	= "2024-03-290"
__version__	= "0.1"
__status__	= "dev"


category = 'linear' # 'spot' or 'linear

lastSentJS = 'last_sent.json'

sign_buy	= '🟢'
sign_sell	= '🔴'

# notify via Telegram, bot:
TMapiToken	= '6975060974:AAF3MblXLT0q2plsge7pNt3OMsogo-8fXBc' # '' means do not send
TMchatID	= '723039352' # to user personally, '' means DO NOT SEND


if __name__ == '__main__':
	print(__part__)
