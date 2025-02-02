from decimal import Decimal
from Datasource.Problem import *

def numberHandler(input: str):
    splited_list = [s.strip() for s in str(input).split(',')]
    values = [item.replace(" ", "") for item in splited_list]

    finalList = []
    for item in Problem:
        for cleanedItem in values:
            if item.value == cleanedItem:
                finalList.append(item)
    return finalList