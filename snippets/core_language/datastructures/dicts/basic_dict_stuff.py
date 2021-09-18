#!/usr/bin/env python3


complaint_specialist = {
    "Sore Knee": "Orthopedic Surgeon",
    "Breast Lump": "Oncologist",
    "Red Eye": "Ophthalmologist"
}
print(complaint_specialist)
# {'Sore Knee': 'Orthopedic Surgeon', 'Breast Lump': 'Oncologist', 'Red Eye': 'Ophthalmologist'}

for complaint in complaint_specialist:
    print(f"{complaint=}, {complaint_specialist[complaint]=}")

complaint_generalist = dict.fromkeys(complaint_specialist, "GP")
print(complaint_generalist)
# {'Sore Knee': 'GP', 'Breast Lump': 'GP', 'Red Eye': 'GP'}
