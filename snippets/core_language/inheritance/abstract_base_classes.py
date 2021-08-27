import abc
from abc import ABC


class Doctor(ABC):
    def __init__(self, specialty):
        self.specialty = specialty

    def __str__(self):
        return self.__class__.__name__ + "(" + f"specialty={self.specialty}" + ")"

    @abc.abstractmethod
    def get_relevant_dutch_knmg_url(self):
        pass

    @abc.abstractmethod
    def is_surgical(self):
        pass


class Internist(Doctor):

    def __init__(self):
        super().__init__("internist")

    def get_relevant_dutch_knmg_url(self):
        return "https://www.knmg.nl/opleiding-herregistratie-carriere/geneeskundestudie/overzicht-opleidingen-1/beroepskeuze-interne-geneeskunde/interne-geneeskunde-1.htm"

    def is_surgical(self):
        return False


class Oncologist(Internist):
    def __init__(self):
        super(Oncologist, self).__init__()
        self.sub_specialty = self.__class__.__name__


if __name__ == "__main__":
    internist = Internist()
    print(internist)  # Internist(specialty=internist)
    print(internist.is_surgical())  # False

    oncologist = Oncologist()
    print(oncologist)  # Oncologist(specialty=internist)
    print(oncologist.is_surgical())  # False
    print(oncologist.sub_specialty)  # Oncologist
