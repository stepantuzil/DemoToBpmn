from ActionModelDEMO import ActionModels_arr

f1 = open('Condition_X.xml', 'r')
f2 = open('Condition_1.xml', 'w')

ActionModelNumber = 0

#Prepare informations from Action model
formName = ActionModels_arr[ActionModelNumber].name
formName = "TEST"#TODO change

conditionName = ActionModels_arr[ActionModelNumber].condition
thenActionName = ActionModels_arr[ActionModelNumber].then_action
elseActionName = ActionModels_arr[ActionModelNumber].else_action
##
defaultValue = ActionModels_arr[ActionModelNumber].then_action #TODO Ask user
NumberOfAction = 2
#<camunda:formField id="FormField_name" label="FormField_label" type="FormField_type" defaultValue="0" />

for line in f1:
    if line.find("<camunda:formField") != -1:

        line = line.replace('FormField_name', 'FormField_' + formName)
        line = line.replace('FormField_label', 'FormField_' + formName)
        if defaultValue != "No":
            line = line.replace('defaultValue="0"', 'defaultValue="' + defaultValue + '"')

    if line.find('id="Task_0_0"') != -1:
        line = line.replace('id="Task_0_0"', 'id="Task_' + thenActionName + '_0"')
    if line.find('name="0"') != -1:
        line = line.replace('name="0""', 'name="' + thenActionName + '"')

    if line.find('id="Task_1_0"') != -1:
        line = line.replace('id="Task_1_0"', 'id="Task_' + thenActionName + '_0"')
    if line.find('name="1"') != -1:
        line = line.replace('name="1""', 'name="1"' + thenActionName + '"')

    if (NumberOfAction <= 2) and (line.find('id="Task_2_0"') == -1 or line.find('name="2"') == -1):
        f2.write(line)

##############################
f1.close()
f2.close()