def main():
    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?


def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

    if not item_prices:
        return 0

    for price in item_prices:
        if type(price) == str:
            return 0

    item_prices.sort()

    lowest_price = item_prices[0]

    if type(lowest_price) == int:
        list_length = len(item_prices)
        if list_length >= 3:
            return lowest_price
        else:
            return 0
    else:
        return 0


if __name__ == '__main__':
    main()
