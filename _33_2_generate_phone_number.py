def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(country="+91", area="942", first="535", last="0699")

print(phone_num)
