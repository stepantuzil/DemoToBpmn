from ActionModelDEMO import ActionModels_arr

numberActionModels = len(ActionModels_arr) - 1

file_name = 'Condition_' + str(numberActionModels) + '.xml'
f1 = open('Condition_X.xml', 'r')
f2 = open(file_name, 'w')

conditionName = ActionModels_arr[numberActionModels].name
conditionName = conditionName.replace('<', '_')
conditionName = conditionName.replace('>', '_')


condition = ActionModels_arr[numberActionModels].condition
condition = condition.replace(" ", "_")
thenAction = ActionModels_arr[numberActionModels].then_action
thenAction = thenAction.replace(" ", "_")
elseAction = ActionModels_arr[numberActionModels].else_action
elseAction = elseAction.replace(" ", "_")

defaultValue = thenAction #TODO ask user

for line in f1:
    if line.find('<camunda:formField') != -1:
        line = line.replace('id="FormField_name"', 'id="FormField_' + conditionName + '"')
        line = line.replace('label="FormField_label"', 'label="FormField_' + conditionName + '"')

    if line.find('<bpmn:exclusiveGateway') != -1:
        line = line.replace('name="ConditionName"', 'name="' + condition + '"')
        #TODO default SequenceFlow

    #####################################################

    if line.find('="Task_0_X"') != -1:
        line = line.replace('="Task_0_X"', '="Task_' + thenAction + '_X"')

    if line.find('="Task_1_X"') != -1:
        line = line.replace('="Task_1_X"', '="Task_' + elseAction + '_X"')

    if line.find('="Task_0_X_di"') != -1:
        line = line.replace('="Task_0_X_di"', '="Task_' + thenAction + '_X_di"')

    if line.find('="Task_1_X_di"') != -1:
        line = line.replace('="Task_1_X_di"', '="Task_' + elseAction + '_X_di"')

    #####################################################

    if line.find('name="0"') != -1:
        line = line.replace('name="0"', 'name="' + thenAction + '"')

    if line.find('name="1"') != -1:
        line = line.replace('name="1"', 'name="' + elseAction + '"')

    if line.find('_X') != -1:
        line = line.replace('_X', '_' + str(numberActionModels))
    if line.find('_X_di') != -1:
        line = line.replace('_X_di"', '_' + str(numberActionModels) + '_di')

    print(line)
    f2.write(line)
###############################
f1.close()
f2.close()
