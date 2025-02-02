from Datasource.Problem import *

def sortStyle():
    return [item.value for item in [
        Doctors.Dermatovenerologist,
        Doctors.Surgeon,
        Doctors.ObstetricianGynecologist,
        Doctors.Otorhinolaryngologist,
        Doctors.Ophthalmologist,
        Cabinet.Mammography,
        Cabinet.FLO,
        Cabinet.BloodCollection,
        Doctors.Dentist,
        Doctors.PsychiatristNarcology,
        Doctors.Neurologist,
        Doctors.Therapist,
        Cabinet.ECG,
        Cabinet.Audiometry,
        Cabinet.UltrasoundSmallTaz,
        Cabinet.CollectionBiomaterial,
        Cabinet.ClinicalUrineAnalysis,
        Cabinet.Ultrasound
    ]]


def sort_specialties(specialties):
    sort_order = {name: index for index, name in enumerate(sortStyle())}
    specialties_sorted = sorted(specialties, key=lambda x: sort_order.get(x[0], float('inf')))
    return specialties_sorted