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

# ------------------------------Logic---------------------------------------------------------------------

stack = ["$","0"]
headerFlag = 0

while headerFlag < len(tokenized_input):
    char = tokenized_input[headerFlag]
    stackindex = stack[-1]
    rowIndex = all_states.index(stackindex)
    columnIndex = table[0].index(char)
    stateAcc = table[rowIndex][columnIndex]
    # print("------>", stateAcc)

    if stateAcc == "acc":
        print("\n!!Parsing Succesfull!!!")
        break

# ------------------------------Shift---------------------------------------------------------------------

    elif stateAcc.startswith("s"):
        print("\n-----------Shif------------")
        stack.append(char)
        print(f"\n{char} => Push Action {stack}")
        headerFlag += 1
        temp = stateAcc[1:]
        stack.append(temp)
        print(f"\n{temp} => Push Action {stack}")


# ------------------------------Reductionn---------------------------------------------------------------------

    elif stateAcc.startswith("r"):
        print("\n-----------Reduction------------")
        temp = int(stateAcc[1:])
        allGrammers = productions
        push_symbol = allGrammers[temp][0]
        temp_grammar = allGrammers[temp][-1]
        len_grammar = len(temp_grammar.split())
            
        for i in range(len_grammar * 2):
            stack.pop()
        stack.append(push_symbol)
        print(f"\n{char} => Push Action {stack}")
        temp_rowIndex = all_states.index(stack[-2])
        temp_columnIndex = table[0].index(stack[-1])
        temp_stateAcc = table[temp_rowIndex][temp_columnIndex]
        stack.append(temp_stateAcc)
        print(f"\n{temp_stateAcc} => Push Action {stack}")

        
# ------------------------------Failed---------------------------------------------------------------------
    
    elif stateAcc == "-":
        print("\n Parsing Failed")
        break

# ------------------------------Non terminals Shift---------------------------------------------------------------------

    else :
        print("\n-----------Simple Shift------------")
        headerFlag += 1
        stack.append(char)
        print(f"\n{char} => Push Action {stack}")
        stack.append(stateAcc)
        print(f"\n{stateAcc} => Push Action {stack}")