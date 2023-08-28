def city_country(city,country, population =''):
    if population:
        value = f"{city}, {country} Population = {population}".title()
    else:
        value = f"{city}, {country}".title()
    return value

print(city_country('lagos', 'Nigeria', '5000'))
