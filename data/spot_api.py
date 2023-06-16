from binance.spot import Spot

client = Spot()

if __name__ == "__main__":
    print(client.time())
