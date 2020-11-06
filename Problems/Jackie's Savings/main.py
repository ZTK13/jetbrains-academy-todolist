def final_deposit_amount(*args, amount=1000):
    for i in args:
        amount *= (1 + (i / 100.0))
    return round(amount, 2)
