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

# ------------------------------input & Tokenization---------------------------------------------------------------------

f_input = open('input.txt', 'r') 
tokenized_input = []
i = f_input.read()
data_input_lines = i.split('\n')

for line in data_input_lines:
    tokens = line.split(' ')
    for token in tokens:
        if token in input_headers:
            # identifiers
            tokenized_input.append(token)
tokenized_input.extend('$')
print("\nTokenized input : ", tokenized_input)

# ------------------------------productions---------------------------------------------------------------------

file = open("grammar.txt", "r")  # grammar
productions_array = file.readlines()
productions = []
for i in productions_array:
    key, value = i.split('->')
    newVal = value.rstrip().lstrip()
    newKey = key.strip()
    newArr = [newKey,newVal]
    productions.append(newArr)

# print('\nProduction ===> ', productions)