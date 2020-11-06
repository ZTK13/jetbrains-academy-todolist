def get_percentage(number, round_digits=None):
    pct = round(number * 100, round_digits)
    return f"{pct}%"
