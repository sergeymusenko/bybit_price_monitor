# coin_price_monitor

For Crypto Exchange: Price monitor, using Binance public API.

https://github.com/sergeymusenko/coin_price_monitor

Works as cron script. Start it each hour. Use: `crontab -e`
> \# coin_price_monitor: each *:01<br/>
> 1 * * * *   /path.../coin_price_monitor/main.py 2>&1 | tee -a /path.../coin_price_monitor/cron-log.txt

Checks prices of coins comparing to price levels in `coinlist.py` and sends Telegram signals on getting close.<br/>
Checks prices on Binance 'spot', does not support 'futures'.

In Telegram message:
> "green" mark means we going down to the price level - time to buy,<br/>
> "red" mark means we going up to the price level - time to sell.

Send signal again if we moved closer or changed price level. Otherwize no repeat same coin signal.

Last sent json file format: `{'symbol': ['%', 'priceLevel', 'lastPrice', 'dateTime'],}`

How to connect to Telegram: see instructions in `simple_telegram.py` module.<br/>
You can send to a group or to user account personally, see `config.py`.

**Telegram message example:<br/>**
<img src="screenshot1.png" alt="Telegram message">