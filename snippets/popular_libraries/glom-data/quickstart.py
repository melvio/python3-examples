#!/usr/bin/env python3
# <https://glom.readthedocs.io/en/latest/>
import glom

data = {"a": {"b": {"c": "d"}}}
filter_result = glom.glom(data, spec="a.b.c")
print(filter_result)  # d

try:
    glom.glom(data, spec='a.nope')
except glom.core.PathAccessError as e:
    print(e)
# glom.core.PathAccessError: error raised while processing, details below.
# Target-spec trace (most recent last):
# - Target: {'a': {'b': {'c': 'd'}}}
# - Spec: 'a.nope'
# glom.core.PathAccessError: could not access 'nope', part 1 of Path('a', 'nope'), got error: KeyError('nope')


dutch_specialisms = {
    "doctor": {
        "internist": {
            "sub-specialty": "allergologie"
        }
    }
}

result = glom.glom(dutch_specialisms, spec="doctor.internist.sub-specialty")
print(result)  # allergologie"

dutch_specialisms = {
    "doctor": {
        "internist": [
            {"sub-specialty": "allergologie"},
            {"sub-specialty": "bloedtransfusiegeneeskunde"},
            {"sub-specialty": "oncologie"},
        ]
    }
}

result = glom.glom(dutch_specialisms, spec=("doctor.internist", ["sub-specialty"]))
print(result)  # ['allergologie', 'bloedtransfusiegeneeskunde', 'oncologie']
