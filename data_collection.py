import requests, time, json
while True:
    binance_rune_Price = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=RUNEBUSD").json()
    binance_price = float((binance_rune_Price['price']))
    pule_rune_Price = requests.get("https://midgard.thorchain.info/v2/stats").json()
    pule_price = float((pule_rune_Price["runePriceUSD"]))
    price_difference = binance_price - pule_price
    info = {
        "price_difference": price_difference,
        "time": time.time()
    }
    with open('price_info.txt', 'r') as file:
        a = file.readlines()
        a.insert(0, json.dumps(info) + "\n")
    with open('price_info.txt', 'w') as file:
        file.writelines(a)
    time.sleep(5)