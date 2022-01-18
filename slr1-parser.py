# ------------------------------table---------------------------------------------------------------------

file_T = open("table.txt", "r")  # table
tables_array = file_T.readlines()
table = []
for i in tables_array:
    table.append(i.split())
# print('\nTable ===> ',table)
input_headers = table[0]    #columns

all_states = [i[0] for i in table]   #rows
# print("\nall_State ==> ", all_states)