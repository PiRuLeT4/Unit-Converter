

#.. Weight: milligram, gram, kilogram, ounce, pound.
def calc_weight(value, unit1, unit2):
    to_gram = {
        'milligram': 0.001,
        'gram': 1,
        'kilogram': 1000,
        'ounce': 28.3495,
        'pound': 453.592
    }

    if unit1 not in to_gram or unit2 not in to_gram:
        return 'Invalid unit'
    
    if unit1 == unit2:
        return f'{value} {unit1.capitalize()}{'s' if value != 1 else ''} (no conversion needed)'
    
    #.. convert to grams
    value_in_grams = to_gram[unit1] * value

    #.. convert from grams to unit2 
    result = value_in_grams / to_gram[unit2]
    return f'{value} {unit1} = {result:.2f} {unit2}{'s' if result != 1 else ''}'

#.. Temperature: Celsius, Fahrenheit, Kelvin.
def calc_temperature(value, unit1, unit2):
    conversions = {
        ('celsius', 'kelvin'): lambda x: x + 273.15,
        ('kelvin', 'celsius'): lambda x: x - 273.15,
        ('celsius', 'fahrenheit'): lambda x: (x - 32) * 5/9,
        ('fahrenheit', 'celsus'): lambda x: (x * 9/5) + 32,
        ('fahrenheit', 'kelvin'): lambda x: (x - 32) * 5/9 + 273.15,
        ('kelvin', 'fahrenheit'): lambda x: ((x - 273.15) * 9/5) + 32
    }

    if unit1 == unit2:
        return f'{value} {unit1.capitalize()}{'s' if value != 1 else ''} (no conversion needed)'

    func = conversions[(unit1, unit2)]
    if not func: 
        return 'Unsoported conversion'
    
    result = func(value)
    return f'{value} {unit1} = {result:.2f} {unit2}{'s' if result != 1 else ''}'
    
        

#.. Length: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile
def calc_length(value, unit1, unit2):
    
    to_meters = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1,
        'kilometer': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34
    }

    if unit1 == unit2:
        return f'{value} {unit1.capitalize()}{'s' if value != 1 else ''} (no conversion needed)'

    if unit1 not in to_meters or unit2 not in to_meters:
        return 'Invalid unit'
    
    #.. first we convert to meters 
    value_in_meters = value * to_meters[unit1]

    #.. second we convert from meters to unit2 so we dont have to check every posibility
    result = value_in_meters / to_meters[unit2]
    return f'{value} {unit1} = {result:.2f} {unit2}{'s' if result != 1 else ''}'
    
    
