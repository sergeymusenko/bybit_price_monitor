#!/usr/bin/env python3

__project__  = "Price monitor for Bybit, send to Telegram"
__part__     = 'Main config'
__author__   = "Sergey V Musenko"
__email__    = "sergey@musenko.com"
__copyright__= "© 2024, musenko.com"
__license__  = "MIT"
__credits__  = ["Sergey Musenko"]
__date__     = "2024-03-29"
__version__  = "0.1"
__status__   = "dev"


category     = 'linear' # 'spot' or 'linear

lastSentJS   = 'last_sent.json'

sign_buy     = '🟢'
sign_sell    = '🔴'

# notify via Telegram, bot:
TMapiToken   = '' # '' means do not send
TMchatID     = '' # to user personally, '' means DO NOT SEND


if __name__ == '__main__':
	print(__part__)
