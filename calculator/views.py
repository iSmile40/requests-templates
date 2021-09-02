from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def calc_recipes(request, dish):
    msg = DATA[dish]
    quantity = request.GET.get('servings', 1)
    dictionary = {}
    for i in msg.keys():
        dictionary[i] = msg[i] * int(quantity)
    result = '<br> '.join([f'{key}: {value}' for key, value in dictionary.items()])
    return HttpResponse(str(result))
