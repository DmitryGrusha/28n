from Datasource.Problem import *
from datetime import datetime
from dateutil.relativedelta import relativedelta

import itertools

# //
from decimal import Decimal

def numberHandler(input: str):
    cleaned_list = [s.strip() for s in str(input).split(',')]
    withoutSpacesList = [item.replace(" ", "") for item in cleaned_list]

    new_array = []
    for value in withoutSpacesList:
        try:
            print(Decimal(value))
            # if value == "1.50":
            #     num_value = float(value)
            # elif value == "1.40":
            #     num_value = float(value)
            # elif value == "1.30":
            #     num_value = float(value)
            # elif value == "1.20":
            #     num_value = float(value)
            # elif value == "1.10":
            #     num_value = float(value)
            #
            # elif value == "1.5":
            #     num_value = float("1.05")
            # elif value == "1.4":
            #     num_value = float("1.04")
            # elif value == "1.3":
            #     num_value = float("1.03")
            # elif value == "1.2":
            #     num_value = float("1.02")
            # elif value == "1.1":
            #     num_value = float("1.01")
            #
            # else:
            #     num_value = float(value)
            #
            # if num_value.is_integer():
            #     new_array.append(str(int(num_value)))
            # else:
            #     new_array.append(str(num_value))
        except ValueError:
            new_array.append(value)

    return []
    # finalList = []
    # for item in Problem:
    #     for cleanedItem in new_array:
    #         if item.value == cleanedItem:
    #             finalList.append(item)
    # return finalList

#Doctors
def handleDoctors(problemsList: [Problem], sex: Sex, cabinetsDict: {}):
    all = []
    for problem in problemsList:
        doctors = [doctor.value for doctor in problem.doctors(sex)]
        all.append(doctors)

    unique = list(set(itertools.chain(*all)))
    doctorsDict = {}
    for doctor in unique:
        for name, number in cabinetsDict.items():
            if doctor == name:
                doctorsDict[doctor] = number

    return doctorsDict

def getUniqueDoctors(input: [str], sex: Sex, cabinetsDict: {}):
    problemsList = numberHandler(input)
    return handleDoctors(problemsList, sex, cabinetsDict)


#Age
def getAge(birthday) -> int:
    today = datetime.today()
    age = relativedelta(today, birthday).years
    return age

#Cabinets
def handleCabinets(problemsList: [Problem], sex: Sex, age: AgePeriodization, cabinetsDict: {}):
    all = []
    for problem in problemsList:
        cabinets = [cabinets.value for cabinets in problem.cabinets(sex, age)]
        all.append(cabinets)

    unique = list(set(itertools.chain(*all)))

    finalCabinetsDict = {}
    for cabinet in unique:
        for name, number in cabinetsDict.items():
            if cabinet == name:
                finalCabinetsDict[cabinet] = number

    return finalCabinetsDict

def getUniqueCabinets(input: [str], sex: Sex, age: AgePeriodization, cabinetsDict: {}):
    problemsList = numberHandler(input)
    return handleCabinets(problemsList, sex, age, cabinetsDict)


#Sex
def getCurrentSex(input: [str]):
    withoutSpacesList = input.replace(" ", "")
    for item in Sex:
        if item.value == withoutSpacesList:
            return item
    return Sex.Genderless


#AgePeriodization
def getCurrentAgePeriodization(sex: Sex, age: int):
    if sex == Sex.Male:
        return AgePeriodization.Male

    if sex == Sex.Female:
        if age < 39:
            return AgePeriodization.YoungFemale
        else:
            return AgePeriodization.OldFemale