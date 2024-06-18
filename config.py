#!/usr/bin/env python3

__project__  = "Price monitoring for Investment/Trading, notify Telegram"
__part__     = 'Main config'
__author__   = "Sergey V Musenko"
__email__    = "sergey@musenko.com"
__copyright__= "© 2024, musenko.com"
__license__  = "MIT"
__credits__  = ["Sergey Musenko"]
__date__     = "2024-03-29"
__version__  = "0.1"
__status__   = "dev"


lastPricesJS = 'last_prices.json'
lastPricesAvgLen = 6 # store n last prices, 6 * 10min = 1 last hour

lastSentJS   = 'last_sent.json'

# notify via Telegram, bot:
TMapiToken   = '' # '' means do not send
TMchatID     = '' # to user personally, '' means DO NOT SEND


if __name__ == '__main__':
	print(__part__)
