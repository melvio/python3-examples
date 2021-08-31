from collections import namedtuple

Human = namedtuple(typename="HumanType", field_names=["age", "name"])

human = Human(age=28, name="melvin")

print(human)  # HumanType(age=28, name='melvin')
print(human.age)  # 28
print(human.name)  # melvin
