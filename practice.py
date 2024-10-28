def process_items(prices: dict[str,float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


items={"apple":20.10, "banana":40.40}
process_items(items)