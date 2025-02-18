from Datasource.Problem import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
import itertools


def definingPoints(input: str) -> [Problem]:
    splited_list = [s.strip() for s in input.split(',')]
    values = [item.replace(" ", "") for item in splited_list]
    result = []
    for item in Problem:
        for value in values:
            if item.value == value:
                result.append(item)

    return result


def getAge(birthday) -> int:
    today = datetime.today()
    age = relativedelta(today, birthday).years
    return age


def getSex(input: [str]):
    withoutSpacesList = input.replace(" ", "")
    for item in Sex:
        if item.value == withoutSpacesList:
            return item
    return Sex.Genderless


def getAgePeriodization(sex: Sex, age: int):
    if sex == Sex.Male:
        return AgePeriodization.Male

    if sex == Sex.Female:
        if age < 40:
            return AgePeriodization.YoungFemale
        else:
            return AgePeriodization.OldFemale


def handleDoctors(problems: [Problem], sex: Sex, cabinetsDict: {}):
    all = []
    for problem in problems:
        doctors = [doctor.value for doctor in problem.doctors(sex)]
        all.append(doctors)

    unique = list(set(itertools.chain(*all)))
    doctorsDict = {}
    for doctor in unique:
        for name, number in cabinetsDict.items():
            if doctor == name:
                doctorsDict[doctor] = number

    return doctorsDict


def getUniqueDoctors(problems: [Problem], sex: Sex, cabinetsDict: {}):
    return handleDoctors(problems, sex, cabinetsDict)


def handleCabinets(problems: [Problem], sex: Sex, age: AgePeriodization, cabinetsDict: {}):
    all = []
    for problem in problems:
        cabinets = [cabinets.value for cabinets in problem.cabinets(sex, age)]
        all.append(cabinets)

    unique = list(set(itertools.chain(*all)))

    finalCabinetsDict = {}
    for cabinet in unique:
        for name, number in cabinetsDict.items():
            if cabinet == name:
                finalCabinetsDict[cabinet] = number

    return finalCabinetsDict


def getUniqueCabinets(problems: [Problem], sex: Sex, age: AgePeriodization, cabinetsDict: {}):
    return handleCabinets(problems, sex, age, cabinetsDict)
