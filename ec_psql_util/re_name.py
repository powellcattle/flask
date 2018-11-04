import re

import ec_psql_util

list_streets = ec_psql_util.sql_get_streets()

_add_req = 'MYATT'
list_candidates = list()

for value in list_streets:
    if _add_req not in value["full_name"]:
        continue
    list_candidates.append(value)


print(list_candidates)

