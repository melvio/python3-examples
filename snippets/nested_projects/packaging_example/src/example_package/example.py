#!/usr/bin/env python3
import random


def medical_knowledge():
    result: int = random.randint(1, 3)
    if result == 1:
        print("The spleen is typically between 9 cm and 13 cm long")
        # source: <https://pubs.rsna.org/doi/full/10.1148/radiol.2015150887>
        # quote: 5th–95th interpercentile range: 8.7–13.3 cm

    elif result == 2:
        print("The stethoscope was invented in France in 1816 by Dr. Laennec.")
        # source <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1570491/>
        # quote: Rene Theophile Hyacinthe Laennec (1781–1826) was a French physician who, in 1816, invented the stethoscope
    else:
        print(
            "A disease is considered rare in the EU when fewer than 1 in 2000 people are affected by it."
        )
        # source <https://rarediseases.info.nih.gov/diseases/pages/31/faqs-about-rare-diseases>
        # quote: In the European Union, a disease is defined as rare when it affects fewer than 1 in 2,000 people.
