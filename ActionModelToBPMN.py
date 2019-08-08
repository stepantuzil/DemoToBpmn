from ActionModelDEMO import ActionModels_arr

f1 = open('Condition_X.xml', 'r')
f2 = open('Condition_1.xml', 'w')

ActionModelNumber = 0

#Prepare informations from Action model
formName = ActionModels_arr[ActionModelNumber].name
formName = "TEST"#TODO change


conditionName = ActionModels_arr[ActionModelNumber].condition.replace(" ", "")
thenActionName = ActionModels_arr[ActionModelNumber].then_action.replace(" ", "")
elseActionName = ActionModels_arr[ActionModelNumber].else_action.replace(" ", "")

##
defaultValue = ActionModels_arr[ActionModelNumber].then_action.replace(" ", "") #TODO Ask user
NumberOfAction = 2
#<camunda:formField id="FormField_name" label="FormField_label" type="FormField_type" defaultValue="0" />

for line in f1:
    if line.find("<camunda:formField") != -1:
        line = line.replace('FormField_name', 'FormField_' + formName)
        line = line.replace('FormField_label', 'FormField_' + formName)
    if defaultValue != "No":
        line = line.replace('defaultValue="0"', 'defaultValue="' + defaultValue + '"')
#######################################################
    if line.find('="Task_0_0"') != -1:
        line = line.replace('="Task_0_0"', '="Task_' + thenActionName + '_0"')
    if line.find('name="0"') != -1:
        line = line.replace('name="0"', 'name="' + thenActionName + '"')

    if line.find('="Task_1_0"') != -1:
        line = line.replace('="Task_1_0"', '="Task_' + elseActionName + '_0"')
    if line.find('name="1"') != -1:
        line = line.replace('name="1"', 'name="' + elseActionName + '"')
    #######################################################
    if line.find('="Task_0_0_di"') != -1:
        line = line.replace('="Task_0_0_di"', '="Task_' + thenActionName + '_0_di"')

    if line.find('="Task_1_0_di"') != -1:
        line = line.replace('="Task_1_0_di"', '="Task_' + elseActionName + '_0_di"')
    #######################################################
    if line.find('name="ConditionName"') != -1:
        line = line.replace('name="ConditionName"', 'name="' + conditionName + '"')
    #######################################################
    if (NumberOfAction <= 2) and (line.find('id="Task_2_0"') == -1 or line.find('name="2"') == -1):
        f2.write(line)

##############################
f1.close()
f2.close()