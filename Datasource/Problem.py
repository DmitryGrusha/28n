from enum import Enum
from typing import List

class Sex(Enum):
    Male = "М"
    Female = "Ж"
    Genderless = "Нет пола"

class AgePeriodization:
    Male = "Мужщина"
    YoungFemale = "Молодая женщина"
    OldFemale = "Старая женщина"

class Doctors(Enum):
    Dermatovenerologist = "Дерматовенеролог"
    Otorhinolaryngologist = "ЛОР"
    Ophthalmologist = "Офтальмолог"
    Surgeon = "Хирург"
    Dentist = "Стоматолог"

    PsychiatristNarcology = "Психиатр-Нарколог"
    Neurologist = "Невролог"
    Therapist = "Терапевт"
    ObstetricianGynecologist = "Гинеколог"

    def __init__(self, value):
        self._value_ = value

class Cabinet(Enum):
    BloodCollection = "Забор крови"
    FLO = "ФЛО"
    ECG = "ЭКГ"

    ClinicalUrineAnalysis = "Анализ мочи"
    CollectionBiomaterial = "Забор биоматериала"
    Mammography = "Маммография"
    Ultrasound = "УЗИ ОБП"
    Audiometry = "Аудиометрия"
    UltrasoundSmallTaz = "УЗИ ОМТ"

    def __init__(self, value):
        self._value_ = value

class Problem(Enum):

    a1_1 = '1.1'
    a1_2 = '1.2'
    a1_3 = '1.3'
    a1_4 = '1.4'
    a1_5 = '1.5'
    a1_5_1 = '1.5.1'
    a1_6 = '1.6'
    a1_7 = '1.7'
    a1_7_1 = '1.7.1'
    a1_7_2 = '1.7.2'
    a1_8_1 = '1.8.1'
    a1_8_1_1 = '1.8.1.1'
    a1_8_1_2 = '1.8.1.2'
    a1_8_2 = '1.8.2'
    a1_8_2_1 = '1.8.2.1'
    a1_8_2_2 = '1.8.2.2'
    a1_8_3 = '1.8.3'
    a1_8_3_1 = '1.8.3.1'
    a1_8_3_2 = '1.8.3.2'
    a1_8_4 = '1.8.4'
    a1_8_4_1 = '1.8.4.1'
    a1_8_4_2 = '1.8.4.2'
    a1_9 = '1.9'
    a1_10 = '1.10'
    a1_11 = '1.11'
    a1_12 = '1.12'
    a1_13 = '1.13'
    a1_14 = '1.14'
    a1_14_1 = '1.14.1'
    a1_14_2 = '1.14.2'
    a1_15 = '1.15'
    a1_15_1 = '1.15.1'
    a1_16 = '1.16'
    a1_17 = '1.17'
    a1_18_1 = '1.18.1'
    a1_18_2 = '1.18.2'
    a1_18_3 = '1.18.3'
    a1_19_1 = '1.19.1'
    a1_19_2 = '1.19.2'
    a1_19_3 = '1.19.3'
    a1_20 = '1.20'
    a1_21 = '1.21'
    a1_22 = '1.22'
    a1_23 = '1.23'
    a1_24 = '1.24'
    a1_25 = '1.25'
    a1_26 = '1.26'
    a1_27 = '1.27'
    a1_27_1 = '1.27.1'
    a1_27_2 = '1.27.2'
    a1_28 = '1.28'
    a1_29 = '1.29'
    a1_29_1 = '1.29.1'
    a1_29_2 = '1.29.2'
    a1_29_3 = '1.29.3'
    a1_29_4 = '1.29.4'
    a1_29_5 = '1.29.5'
    a1_30 = '1.30'
    a1_30_1 = '1.30.1'
    a1_31 = '1.31'
    a1_32 = '1.32'
    a1_33 = '1.33'
    a1_34 = '1.34'
    a1_34_1 = '1.34.1'
    a1_34_2 = '1.34.2'
    a1_35 = '1.35'
    a1_36 = '1.36'
    a1_36_1 = '1.36.1'
    a1_36_2 = '1.36.2'
    a1_36_3 = '1.36.3'
    a1_37_1 = '1.37.1'
    a1_37_1_1 = '1.37.1.1'
    a1_37_1_2 = '1.37.1.2'
    a1_37_2 = '1.37.2'
    a1_38 = '1.38'
    a1_39 = '1.39'
    a1_40 = '1.40'
    a1_40_1 = '1.40.1'
    a1_40_2 = '1.40.2'
    a1_41 = '1.41'
    a1_42 = '1.42'
    a1_43 = '1.43'
    a1_43_1 = '1.43.1'
    a1_43_2 = '1.43.2'
    a1_44 = '1.44'
    a1_45 = '1.45'
    a1_45_1 = '1.45.1'
    a1_45_2 = '1.45.2'
    a1_45_3 = '1.45.3'
    a1_46 = '1.46'
    a1_47 = '1.47'
    a1_47_1 = '1.47.1'
    a1_47_2 = '1.47.2'
    a1_47_3 = '1.47.3'
    a1_47_4 = '1.47.4'
    a1_47_5 = '1.47.5'
    a1_47_6 = '1.47.6'
    a1_47_7 = '1.47.7'
    a1_47_8 = '1.47.8'
    a1_47_9 = '1.47.9'
    a1_47_10 = '1.47.10'
    a1_47_11 = '1.47.11'
    a1_47_12 = '1.47.12'
    a1_47_13 = '1.47.13'
    a1_47_14 = '1.47.14'
    a1_47_15 = '1.47.15'
    a1_47_16 = '1.47.16'
    a1_48 = '1.48'
    a1_49 = '1.49'
    a1_49_1 = '1.49.1'
    a1_49_2 = '1.49.2'
    a1_49_3 = '1.49.3'
    a1_49_4 = '1.49.4'
    a1_49_5 = '1.49.5'
    a1_49_6 = '1.49.6'
    a1_49_7 = '1.49.7'
    a1_49_8 = '1.49.8'
    a1_49_9 = '1.49.9'
    a1_49_10 = '1.49.10'
    a1_49_11 = '1.49.11'
    a1_49_12 = '1.49.12'
    a1_49_13 = '1.49.13'
    a1_49_14 = '1.49.14'
    a1_50 = '1.50'
    a1_51_1 = '1.51.1'
    a1_51_2 = '1.51.2'
    a1_52_1 = '1.52.1'
    a1_52_2 = '1.52.2'
    a1_52_3 = '1.52.3'
    a1_52_4 = '1.52.4'
    a1_52_5 = '1.52.5'
    a1_52_6 = '1.52.6'
    a1_52_7 = '1.52.7'
    a1_53 = '1.53'
    a1_53_1 = '1.53.1'
    a1_53_2 = '1.53.2'

    a2_1 = '2.1'
    a2_2 = '2.2'
    a2_3 = '2.3'
    a2_4_1 = '2.4.1'
    a2_4_2 = '2.4.2'
    a2_4_3 = '2.4.3'
    a2_4_4 = '2.4.4'
    a2_4_5 = '2.4.5'

    a3_1_1 = '3.1.1'
    a3_1_2 = '3.1.2'
    a3_1_3 = '3.1.3'
    a3_1_4 = '3.1.4'
    a3_1_5 = '3.1.5'
    a3_1_6 = '3.1.6'
    a3_1_7 = '3.1.7'
    a3_1_8_1 = '3.1.8.1'
    a3_1_8_2 = '3.1.8.2'
    a3_1_8_3 = '3.1.8.3'
    a3_1_9_1 = '3.1.9.1'
    a3_1_9_2 = '3.1.9.2'
    a3_1_9_3 = '3.1.9.3'
    a3_1_9_4 = '3.1.9.4'
    a3_1_10 = '3.1.10'
    a3_2 = '3.2'
    a3_3 = '3.3'
    a3_4 = '3.4'

    a4_1 = '4.1'
    a4_2 = '4.2'
    a4_2_1 = '4.2.1'
    a4_2_2 = '4.2.2'
    a4_2_3 = '4.2.3'
    a4_2_4 = '4.2.4'
    a4_2_5 = '4.2.5'
    a4_3_1 = '4.3.1'
    a4_3_2 = '4.3.2'
    a4_4 = '4.4'
    a4_5 = '4.5'
    a4_6 = '4.6'
    a4_7 = '4.7'
    a4_8 = '4.8'
    a4_9 = '4.9'
    a4_10 = '4.10'

    a5_1 = '5.1'
    a5_2_1 = '5.2.1'
    a5_2_2 = '5.2.2'

    a6 = '6'
    a6_1 = '6.1'
    a6_2 = '6.2'
    a7 = '7'
    a8 = '8'
    a9 = '9'
    a10 = '10'
    a11 = '11'
    a11_1 = '11.1'
    a11_2 = '11.2'
    a11_3 = '11.3'
    a11_4 = '11.4'
    a12 = '12'
    a13 = '13'
    a14 = '14'
    a15 = '15'
    a16 = '16'
    a17 = '17'
    a18_1 = '18.1'
    a18_2 = '18.2'
    a22 = '22'
    a23 = '23'
    a24 = '24'
    a25 = '25'
    a26 = '26'
    a27 = '27'


    def __init__(self, value):
        self._value_ = value

    def doctors(self, sex: Sex) -> [Doctors]:

        defaultDoctors: [Doctors] = [Doctors.Dermatovenerologist, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist]

        problems_to_doctors = {
            Problem.a1_2: [Doctors.Surgeon],
            Problem.a1_3: [Doctors.Dermatovenerologist, Doctors.Ophthalmologist, Doctors.Surgeon],
            Problem.a1_4: [Doctors.Dermatovenerologist, Doctors.Otorhinolaryngologist],
            Problem.a1_6: [Doctors.Surgeon],
            Problem.a1_7_1: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a1_8_4_1: [Doctors.Surgeon],
            Problem.a1_12: [Doctors.Surgeon],
            Problem.a1_14: [Doctors.Dermatovenerologist, Doctors.Otorhinolaryngologist],
            Problem.a1_14_2: [Doctors.Surgeon],
            Problem.a1_17: [Doctors.Otorhinolaryngologist, Doctors.Surgeon],
            Problem.a1_18_1: [Doctors.Dermatovenerologist, Doctors.Otorhinolaryngologist],
            Problem.a1_18_2: [Doctors.Dermatovenerologist, Doctors.Otorhinolaryngologist],
            Problem.a1_18_3: [Doctors.Dermatovenerologist, Doctors.Otorhinolaryngologist, Doctors.Surgeon],
            Problem.a1_19_3: [Doctors.Surgeon],
            Problem.a1_20: [Doctors.Dentist, Doctors.Surgeon],
            Problem.a1_21: [Doctors.Dermatovenerologist, Doctors.Otorhinolaryngologist, Doctors.Surgeon],
            Problem.a1_22: [Doctors.Dermatovenerologist, Doctors.Otorhinolaryngologist],
            Problem.a1_23: [Doctors.Otorhinolaryngologist],
            Problem.a1_24: [Doctors.Surgeon],
            Problem.a1_25: [Doctors.Dermatovenerologist, Doctors.Otorhinolaryngologist],
            Problem.a1_26: [Doctors.Dermatovenerologist, Doctors.Otorhinolaryngologist],
            Problem.a1_27: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a1_27_1: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist, Doctors.Surgeon],
            Problem.a1_27_2: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a1_28: [Doctors.Otorhinolaryngologist],
            Problem.a1_29: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a1_29_1: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a1_29_2: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a1_29_3: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist, Doctors.Surgeon],
            Problem.a1_29_4: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a1_30: [Doctors.Ophthalmologist],
            Problem.a1_30_1: [Doctors.Surgeon],
            Problem.a1_31: [Doctors.Surgeon],
            Problem.a1_32: [Doctors.Dermatovenerologist, Doctors.Ophthalmologist],
            Problem.a1_33: [Doctors.Otorhinolaryngologist],
            Problem.a1_34_1: [Doctors.Surgeon],
            Problem.a1_34_2: [Doctors.Surgeon],
            Problem.a1_36_2: [Doctors.Surgeon],
            Problem.a1_37_1: [Doctors.Surgeon],
            Problem.a1_37_1_1: [Doctors.Ophthalmologist],
            Problem.a1_37_2: [Doctors.Surgeon],
            Problem.a1_39: [Doctors.Ophthalmologist, Doctors.Surgeon],
            Problem.a1_40_2: [Doctors.Surgeon],
            Problem.a1_42: [Doctors.Surgeon],
            Problem.a1_43_2: [Doctors.Surgeon],
            Problem.a1_45_1: [Doctors.Surgeon],
            Problem.a1_49_3: [Doctors.Surgeon],
            Problem.a1_50: [Doctors.Surgeon],
            Problem.a1_52_6: [Doctors.Ophthalmologist],
            Problem.a2_4_1: [Doctors.Dermatovenerologist, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a3_1_8_1: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a3_1_9_1: [Doctors.Otorhinolaryngologist, Doctors.Dermatovenerologist],
            Problem.a3_1_7: [Doctors.Surgeon],
            Problem.a3_2: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a3_3: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a4_1: [Doctors.Ophthalmologist, Doctors.Dermatovenerologist],
            Problem.a4_2: [Doctors.Ophthalmologist, Doctors.Dermatovenerologist],
            Problem.a4_2_1: [Doctors.Ophthalmologist, Doctors.Dermatovenerologist],
            Problem.a4_2_2: [Doctors.Ophthalmologist, Doctors.Dermatovenerologist],
            Problem.a4_2_3: [Doctors.Ophthalmologist, Doctors.Dermatovenerologist],
            Problem.a4_2_4: [Doctors.Ophthalmologist, Doctors.Dermatovenerologist],
            Problem.a4_2_5: [Doctors.Ophthalmologist, Doctors.Dermatovenerologist],
            Problem.a4_3_1: [Doctors.Surgeon, Doctors.Ophthalmologist, Doctors.Otorhinolaryngologist,
                             Doctors.Dermatovenerologist],
            Problem.a4_3_2: [Doctors.Surgeon, Doctors.Ophthalmologist, Doctors.Otorhinolaryngologist,
                             Doctors.Dermatovenerologist],
            Problem.a4_4: [Doctors.Otorhinolaryngologist],
            Problem.a4_5: [Doctors.Otorhinolaryngologist],
            Problem.a4_6: [Doctors.Otorhinolaryngologist],
            Problem.a4_7: [Doctors.Surgeon, Doctors.Ophthalmologist, Doctors.Otorhinolaryngologist],
            Problem.a4_8: [Doctors.Ophthalmologist, Doctors.Otorhinolaryngologist],
            Problem.a4_9: [Doctors.Ophthalmologist],
            Problem.a4_10: [Doctors.Dermatovenerologist, Doctors.Surgeon, Doctors.Ophthalmologist, Doctors.Otorhinolaryngologist],
            Problem.a5_1: [Doctors.Surgeon, Doctors.Ophthalmologist],
            Problem.a5_2_1: [Doctors.Ophthalmologist],
            Problem.a5_2_2: [Doctors.Otorhinolaryngologist],
            Problem.a6: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist, Doctors.Surgeon],
            Problem.a6_1: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist, Doctors.Surgeon],
            Problem.a6_2: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist, Doctors.Surgeon],
            Problem.a7: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist, Doctors.Surgeon],
            Problem.a8: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist, Doctors.Surgeon],
            Problem.a9: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a10: [Doctors.Surgeon, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a11: [Doctors.Dentist, Doctors.Surgeon, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a11_1: [Doctors.Dentist, Doctors.Surgeon, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a11_2: [Doctors.Dentist, Doctors.Surgeon, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a11_3: [Doctors.Dentist, Doctors.Surgeon, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a11_4: [Doctors.Dentist, Doctors.Surgeon, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a12: [Doctors.Dentist, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a13: [Doctors.Dentist, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a14: [Doctors.Dentist, Doctors.Surgeon, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a15: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a16: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a17: [Doctors.Dentist, Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a18_1: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a18_2: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist],
            Problem.a22: [Doctors.Otorhinolaryngologist, Doctors.Ophthalmologist, Doctors.Surgeon],
            Problem.a23: [Doctors.Otorhinolaryngologist, Doctors.Dermatovenerologist, Doctors.Dentist],
            Problem.a24: [Doctors.Otorhinolaryngologist, Doctors.Dermatovenerologist, Doctors.Dentist],
            Problem.a25: [Doctors.Otorhinolaryngologist, Doctors.Dermatovenerologist, Doctors.Dentist],
            Problem.a26: [Doctors.Otorhinolaryngologist, Doctors.Dermatovenerologist, Doctors.Dentist],
            Problem.a27: [Doctors.Otorhinolaryngologist, Doctors.Dermatovenerologist, Doctors.Dentist],
        }

        problem_list: [Doctors] = problems_to_doctors.get(self)
        if problem_list is None:
            problem_list = []

        doctors_list: [Doctors] = defaultDoctors + problem_list

        defaultMale: [Doctors] = [Doctors.PsychiatristNarcology, Doctors.Neurologist, Doctors.Therapist]
        defaultFemale: [Doctors] = [Doctors.ObstetricianGynecologist, Doctors.PsychiatristNarcology, Doctors.Neurologist, Doctors.Therapist]

        if sex == Sex.Male:
            doctors_list.extend(defaultMale)
        else:
            doctors_list.extend(defaultFemale)

        return doctors_list



    def cabinets(self, sex: Sex, age: AgePeriodization) -> [Cabinet]:

        defaultCabinet: [Cabinet] = [Cabinet.BloodCollection, Cabinet.FLO, Cabinet.ECG, Cabinet.ClinicalUrineAnalysis]

        problems_to_cabinets = {
            Problem.a1_27: [Cabinet.Audiometry],
            Problem.a1_27_1: [Cabinet.Audiometry],
            Problem.a1_27_2: [Cabinet.Audiometry],
            Problem.a1_36: [Cabinet.Ultrasound],
            Problem.a1_36_1: [Cabinet.Ultrasound],
            Problem.a1_36_2: [Cabinet.Ultrasound],
            Problem.a1_36_3: [Cabinet.Ultrasound],
            Problem.a1_50: [Cabinet.Ultrasound],
            Problem.a2_4_2: [Cabinet.Ultrasound],
            Problem.a4_1: [Cabinet.Ultrasound],
            Problem.a4_3_1: [Cabinet.Audiometry],
            Problem.a4_3_2: [Cabinet.Audiometry],
            Problem.a4_4: [Cabinet.Audiometry],
            Problem.a4_5: [Cabinet.Audiometry],
            Problem.a4_6: [Cabinet.Audiometry],
            Problem.a4_8: [Cabinet.Audiometry],
            Problem.a4_10: [Cabinet.Audiometry],
            Problem.a6: [Cabinet.Audiometry],
            Problem.a6_1: [Cabinet.Audiometry],
            Problem.a6_2: [Cabinet.Audiometry],
            Problem.a7: [Cabinet.Audiometry],
            Problem.a8: [Cabinet.Audiometry],
            Problem.a9: [Cabinet.Audiometry],
            Problem.a10: [Cabinet.Audiometry],
            Problem.a11: [Cabinet.Ultrasound, Cabinet.Audiometry],
            Problem.a11_1: [Cabinet.Ultrasound, Cabinet.Audiometry],
            Problem.a11_2: [Cabinet.Ultrasound, Cabinet.Audiometry],
            Problem.a11_3: [Cabinet.Ultrasound, Cabinet.Audiometry],
            Problem.a11_4: [Cabinet.Ultrasound, Cabinet.Audiometry],
            Problem.a12: [Cabinet.Audiometry],
            Problem.a13: [Cabinet.Audiometry],
            Problem.a14: [Cabinet.Audiometry],
            Problem.a15: [Cabinet.Audiometry],
            Problem.a16: [Cabinet.Audiometry],
            Problem.a17: [Cabinet.Audiometry],
            Problem.a18_1: [Cabinet.Audiometry],
            Problem.a18_2: [Cabinet.Audiometry],
            Problem.a22: [Cabinet.Audiometry],
            Problem.a23: [Cabinet.CollectionBiomaterial],
            Problem.a24: [Cabinet.CollectionBiomaterial],
            Problem.a25: [Cabinet.CollectionBiomaterial],
            Problem.a26: [Cabinet.CollectionBiomaterial],
            Problem.a27: [Cabinet.CollectionBiomaterial]
        }

        cabinets_problems_list: [Cabinet] = problems_to_cabinets.get(self)
        if cabinets_problems_list is None:
            cabinets_problems_list = []

        cabinets_list: [Doctors] = defaultCabinet + cabinets_problems_list

        defaultFemale: [Cabinet] = [Cabinet.UltrasoundSmallTaz]
        defaultOldFemale: [Cabinet] = [Cabinet.Mammography]

        if sex == Sex.Female:
            cabinets_list.extend(defaultFemale)
            if age == AgePeriodization.OldFemale:
                cabinets_list.extend(defaultOldFemale)

        return cabinets_list