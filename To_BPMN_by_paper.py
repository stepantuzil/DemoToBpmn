from Parse_DEMO import TransactionKinds_arr, ElementaryActorRoles_arr, CompositeActorRoles_arr, \
    TransactionProcessStepKinds_arr, AttributeTypes_arr, EntityTypes_arr, ActionRuleTypes_arr, Connections_arr

Transactions_files = []


def Starting_Transaction():
    T_num = TransactionKinds_arr[0].identification

    if transf_type == 0:
        file_name = 'Start_Tr_' + T_num + '.xml'
        f1 = open('Start_Tr_Tx.xml', 'r')
        f2 = open(file_name, 'w')
    else:
        file_name = 'Start_Tr_HF_' + T_num + '.xml'
        f1 = open('Start_Tr_HF_Tx.xml', 'r')
        f2 = open(file_name, 'w')

    transaction_name = TransactionKinds_arr[0].name
    initiator_name = executor_name = "inic"
    initiator_id = executor_id = "inic"

    # Find Initiator and Executor
    for con in Connections_arr:
        if (TransactionKinds_arr[0].id == con.to_id) | (TransactionKinds_arr[0].id == con.from_id):
            if con.connection_type_name.find("Initiator") != -1:
                initiator_id = con.from_id
            if con.connection_type_name.find("Executor") != -1:
                executor_id = con.to_id

    for eact in ElementaryActorRoles_arr:
        if eact.id == initiator_id:
            initiator_name = eact.identification + ' ' + eact.name
        if eact.id == executor_id:
            executor_name = eact.identification + ' ' + eact.name

    for cact in CompositeActorRoles_arr:
        if cact.id == initiator_id:
            initiator_name = cact.identification + ' ' + cact.name
        if cact.id == executor_id:
            executor_name = cact.identification + ' ' + cact.name

    for line in f1:
        if line.find("Tx+1") == -1:
            if line.find('name="Tx" processRef="Process_Tx"') == -1:
                line = line.replace('Tx', T_num)
            else:
                line = line.replace('name="Tx"', 'name="' + T_num + ' ' + transaction_name + '"')
                line = line.replace('Tx', T_num)
        else:
            line = line.replace('Tx+1', 'T11')
            line = line.replace('Tx', T_num)
            line = line.replace('T11', 'Tx+1')

        if line.find("Executor") != -1:
            line = line.replace("Executor", executor_name + " (Executor)")
        if line.find("Initiator") != -1:
            line = line.replace("Initiator", initiator_name + " (Initiator)")

        f2.write(line)
    ##############################
    f1.close()
    f2.close()
    Transactions_files.append(file_name)


def Middle_Transaction(transaction_number):
    T_num = TransactionKinds_arr[transaction_number].identification

    if transf_type == 0:
        file_name = 'Middle_Tr_' + T_num + '.xml'
        f1 = open('Middle_Tr_Tx.xml', 'r')
        f2 = open(file_name, 'w')
    else:
        file_name = 'Middle_Tr_HF_' + T_num + '.xml'
        f1 = open('Middle_Tr_HF_Tx.xml', 'r')
        f2 = open(file_name, 'w')

    transaction_name = TransactionKinds_arr[transaction_number].name
    initiator_name = executor_name = "inic"
    initiator_id = executor_id = "inic"

    # Find Initiator and Executor
    for con in Connections_arr:
        if (TransactionKinds_arr[transaction_number].id == con.to_id) | (
                TransactionKinds_arr[transaction_number].id == con.from_id):
            if con.connection_type_name.find("Initiator") != -1:
                initiator_id = con.from_id
            if con.connection_type_name.find("Executor") != -1:
                executor_id = con.to_id

    for eact in ElementaryActorRoles_arr:
        if eact.id == initiator_id:
            initiator_name = eact.identification + ' ' + eact.name
        if eact.id == executor_id:
            executor_name = eact.identification + ' ' + eact.name

    for cact in CompositeActorRoles_arr:
        if cact.id == initiator_id:
            initiator_name = cact.identification + ' ' + cact.name
        if cact.id == executor_id:
            executor_name = cact.identification + ' ' + cact.name

    for line in f1:
        if line.find("Tx+1") == -1:
            if line.find('name="Tx" processRef="Process_Tx"') == -1:
                line = line.replace('Tx', T_num)
            else:
                line = line.replace('name="Tx"', 'name="' + T_num + ' ' + transaction_name + '"')
                line = line.replace('Tx', T_num)
        else:
            line = line.replace('Tx+1', 'T11')
            line = line.replace('Tx', T_num)
            line = line.replace('T11', 'Tx+1')

        if line.find("Executor") != -1:
            line = line.replace("Executor", executor_name + " (Executor)")
        if line.find("Initiator") != -1:
            line = line.replace("Initiator", initiator_name + " (Initiator)")

        if line.find("X-1") != -1:
            line = line.replace("X-1", str(transaction_number - 1))
        if line.find("X") != -1:
            line = line.replace("X", str(transaction_number))

        if line.find('x="') != -1:
            for t in line.split():
                if t.find('x="') != -1:
                    t = t[:-1]
                    param, value = t.split('"', 1)
                    x_a = float(value)
                    x_a += transaction_number * 1450
                    # print(str(value), " == ", str(x_a))
                    # print("B ", line)
                    line = line.replace(str(value), str(x_a))
                    # print("A ", line)

        f2.write(line)
    ##############################
    f1.close()
    f2.close()
    Transactions_files.append(file_name)


def End_Transaction(transaction_number):
    T_num = TransactionKinds_arr[transaction_number].identification

    if transf_type == 0:
        file_name = 'End_Tr_' + T_num + '.xml'
        f1 = open('End_Tr_Tx.xml', 'r')
        f2 = open(file_name, 'w')
    else:
        file_name = 'End_Tr_HF_' + T_num + '.xml'
        f1 = open('End_Tr_HF_Tx.xml', 'r')
        f2 = open(file_name, 'w')

    transaction_name = TransactionKinds_arr[transaction_number].name
    initiator_name = executor_name = "inic"
    initiator_id = executor_id = "inic"

    # Find Initiator and Executor
    for con in Connections_arr:
        if (TransactionKinds_arr[transaction_number].id == con.to_id) | (
                TransactionKinds_arr[transaction_number].id == con.from_id):
            if con.connection_type_name.find("Initiator") != -1:
                initiator_id = con.from_id
            if con.connection_type_name.find("Executor") != -1:
                executor_id = con.to_id

    for eact in ElementaryActorRoles_arr:
        if eact.id == initiator_id:
            initiator_name = eact.identification + ' ' + eact.name
        if eact.id == executor_id:
            executor_name = eact.identification + ' ' + eact.name

    for cact in CompositeActorRoles_arr:
        if cact.id == initiator_id:
            initiator_name = cact.identification + ' ' + cact.name
        if cact.id == executor_id:
            executor_name = cact.identification + ' ' + cact.name

    for line in f1:
        if line.find("Tx+1") == -1:
            if line.find('name="Tx" processRef="Process_Tx"') == -1:
                line = line.replace('Tx', T_num)
            else:
                line = line.replace('name="Tx"', 'name="' + T_num + ' ' + transaction_name + '"')
                line = line.replace('Tx', T_num)
        else:
            line = line.replace('Tx+1', 'T11')
            line = line.replace('Tx', T_num)
            line = line.replace('T11', 'Tx+1')

        if line.find("Executor") != -1:
            line = line.replace("Executor", executor_name + " (Executor)")
        if line.find("Initiator") != -1:
            line = line.replace("Initiator", initiator_name + " (Initiator)")

        if line.find("X-1") != -1:
            line = line.replace("X-1", str(transaction_number - 1))

        if line.find('x="') != -1:
            for t in line.split():
                if t.find('x="') != -1:
                    t = t[:-1]
                    param, value = t.split('"', 1)
                    x_a = float(value)
                    x_a += transaction_number * 1450
                    line = line.replace(str(value), str(x_a))

        f2.write(line)
    f1.close()
    f2.close()
    Transactions_files.append(file_name)


def Sub_Transaction(transaction_number):
    T_num = TransactionKinds_arr[transaction_number].identification
    file_name = 'Subprocess_' + T_num + '.xml'
    f1 = open('Subprocess_Tx.xml', 'r')
    f2 = open(file_name, 'w')

    transaction_name = TransactionKinds_arr[transaction_number].name
    next_transaction_name = 'Process_' + TransactionKinds_arr[transaction_number+1].identification

    initiator_name = executor_name = "inic"
    initiator_id = executor_id = "inic"

    # Find Initiator and Executor
    for con in Connections_arr:
        if (TransactionKinds_arr[transaction_number].id == con.to_id) | (
                TransactionKinds_arr[transaction_number].id == con.from_id):
            if con.connection_type_name.find("Initiator") != -1:
                initiator_id = con.from_id
            if con.connection_type_name.find("Executor") != -1:
                executor_id = con.to_id

    for eact in ElementaryActorRoles_arr:
        if eact.id == initiator_id:
            initiator_name = eact.identification + ' ' + eact.name
        if eact.id == executor_id:
            executor_name = eact.identification + ' ' + eact.name

    for cact in CompositeActorRoles_arr:
        if cact.id == initiator_id:
            initiator_name = cact.identification + ' ' + cact.name
        if cact.id == executor_id:
            executor_name = cact.identification + ' ' + cact.name

    for line in f1:
        ################
        if line.find('calledElement="Process_Tx+1"') != -1:
            line = line.replace('calledElement="Process_Tx+1"', 'calledElement="' + next_transaction_name + '"')
        ################
        if line.find("Tx+1") == -1:
            if line.find('name="Tx" processRef="Process_Tx"') == -1:
                line = line.replace('Tx', T_num)
            else:
                line = line.replace('name="Tx"', 'name="' + T_num + ' ' + transaction_name + '"')
                line = line.replace('Tx', T_num)
        else:
            line = line.replace('Tx+1', 'T11')
            line = line.replace('Tx', T_num)
            line = line.replace('T11', 'Tx+1')

        if line.find("Executor") != -1:
            line = line.replace("Executor", executor_name + " (Executor)")
        if line.find("Initiator") != -1:
            line = line.replace("Initiator", initiator_name + " (Initiator)")

        if line.find("X-1") != -1:
            line = line.replace("X-1", str(transaction_number - 1))

        #if line.find('x="') != -1:
        #    for t in line.split():
        #        if t.find('x="') != -1:
        #            t = t[:-1]
        #            param, value = t.split('"', 1)
        #            x_a = float(value)
        #            x_a += transaction_number * 1450
        #            line = line.replace(str(value), str(x_a))

        f2.write(line)
    f1.close()
    f2.close()


def Sub_Transaction_End(transaction_number):
    T_num = TransactionKinds_arr[transaction_number].identification

    file_name = 'Subprocess_' + T_num + '.xml'
    f1 = open('Subprocess_end_Tx.xml', 'r')
    f2 = open(file_name, 'w')

    transaction_name = TransactionKinds_arr[transaction_number].name
    initiator_name = executor_name = "inic"
    initiator_id = executor_id = "inic"

    # Find Initiator and Executor
    for con in Connections_arr:
        if (TransactionKinds_arr[transaction_number].id == con.to_id) | (
                TransactionKinds_arr[transaction_number].id == con.from_id):
            if con.connection_type_name.find("Initiator") != -1:
                initiator_id = con.from_id
            if con.connection_type_name.find("Executor") != -1:
                executor_id = con.to_id

    for eact in ElementaryActorRoles_arr:
        if eact.id == initiator_id:
            initiator_name = eact.identification + ' ' + eact.name
        if eact.id == executor_id:
            executor_name = eact.identification + ' ' + eact.name

    for cact in CompositeActorRoles_arr:
        if cact.id == initiator_id:
            initiator_name = cact.identification + ' ' + cact.name
        if cact.id == executor_id:
            executor_name = cact.identification + ' ' + cact.name

    for line in f1:
        if line.find("Tx+1") == -1:
            if line.find('name="Tx" processRef="Process_Tx"') == -1:
                line = line.replace('Tx', T_num)
            else:
                line = line.replace('name="Tx"', 'name="' + T_num + ' ' + transaction_name + '"')
                line = line.replace('Tx', T_num)
        else:
            line = line.replace('Tx+1', 'T11')
            line = line.replace('Tx', T_num)
            line = line.replace('T11', 'Tx+1')

        if line.find("Executor") != -1:
            line = line.replace("Executor", executor_name + " (Executor)")
        if line.find("Initiator") != -1:
            line = line.replace("Initiator", initiator_name + " (Initiator)")

        if line.find("X-1") != -1:
            line = line.replace("X-1", str(transaction_number - 1))
        if line.find("X") != -1:
            line = line.replace("X", str(transaction_number))

        #if line.find('x="') != -1:
        #    for t in line.split():
        #        if t.find('x="') != -1:
        #            t = t[:-1]
        #            param, value = t.split('"', 1)
        #            x_a = float(value)
        #            x_a += transaction_number * 1450
        #           # print(str(value), " == ", str(x_a))
        #            # print("B ", line)
        #            line = line.replace(str(value), str(x_a))
        #            # print("A ", line)

        f2.write(line)
    ##############################
    f1.close()
    f2.close()


answer = input("Whole transformation, just happy flow or whole with subprocesses?\n"
               "Answer 'all', 'happy' or 'sub'.\n")


if answer == 'all':
    transf_type = 0
elif answer == 'happy':
    transf_type = 1  # happy flow
elif answer == 'sub':
    transf_type = 2
else:
    print('Wrong input.')
    exit(1)

for number_of_transaction in list(range(len(TransactionKinds_arr))):

    if transf_type == 2:
        if number_of_transaction == (len(TransactionKinds_arr) - 1):
            Sub_Transaction_End(number_of_transaction)
        else:
            Sub_Transaction(number_of_transaction)
    else:
        if number_of_transaction == 0:
            Starting_Transaction()

        if (number_of_transaction != 0) & (number_of_transaction != (len(TransactionKinds_arr) - 1)):
            Middle_Transaction(number_of_transaction)

        if number_of_transaction == (len(TransactionKinds_arr) - 1):
            End_Transaction(number_of_transaction)
