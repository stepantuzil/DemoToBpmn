from Parse_DEMO import ActionRuleTypes_arr, TransactionKinds_arr, TransactionProcessStepKinds_arr, AttributeTypes_arr, EntityTypes_arr

class CParameter:
    def __init__(self, entityName, attributeName):
        self.entityName = entityName
        self.attributeName = attributeName

class CActionModel:
    def __init__(self, id, name, transactionKindIdentification, transactionKindName, transactionKindSort,
                 transactionProcessStepKind, parameters_ar, condition, then_action, else_action):
        self.id = id
        self.name = name
        self.transactionKindIdentification = transactionKindIdentification
        self.transactionKindName = transactionKindName
        self.transactionKindSort = transactionKindSort
        self.transactionProcessStepKind = transactionProcessStepKind
        self.parameters_ar = parameters_ar
        self.condition = condition
        self.then_action = then_action
        self.else_action = else_action


ActionModels_arr = []
parameters_ar = []

for x in range(len(ActionRuleTypes_arr)):
    #print("   Id:", ActionRuleTypes_arr[x].id)
    ID = ActionRuleTypes_arr[x].id
    #print("   Name:", ActionRuleTypes_arr[x].name)
    Name = ActionRuleTypes_arr[x].name
    #print("   WHEN:")

    for tran in TransactionKinds_arr:
        if tran.id == ActionRuleTypes_arr[x].transactionKind:
            transactionKindIdentification = tran.identification
            transactionKindName = tran.name
            transactionKindSort = tran.transactionSort
            #print("      TransactionKind:", tran.identification, tran.name, tran.transactionSort)

    for transt in TransactionProcessStepKinds_arr:
        if transt.id == ActionRuleTypes_arr[x].transactionProcessStepKind:
            for tran in TransactionKinds_arr:
                if transt.transactionKind == tran.id:
                    transactionProcessStepKind = transt.stepKind
                    #print("      TransactionProcessStepKind: ", transt.stepKind)

    for y in range(len(ActionRuleTypes_arr[x].parameters)):
        for entity in EntityTypes_arr:
            if entity.id == ActionRuleTypes_arr[x].parameters[y].entity:
                entityName = entity.name
        for attribute in AttributeTypes_arr:
            if attribute.id == ActionRuleTypes_arr[x].parameters[y].attribute:
                attributeName = attribute.name
        parameters_ar.append(CParameter(entityName, attributeName))

    #print("   WHILE:")
    condition = ActionRuleTypes_arr[x].condition
    then_action = ActionRuleTypes_arr[x].then_action
    else_action = ActionRuleTypes_arr[x].else_action

    ActionModels_arr.append(
        CActionModel(ID, Name, transactionKindIdentification, transactionKindName, transactionKindSort,
                 transactionProcessStepKind, parameters_ar, condition, then_action, else_action))

def print_ActionRuleTypes(ActionRuleTypes_arr):
    print("ActionRuleTypes:")
    for x in range(len(ActionRuleTypes_arr)):
        print("   Id:", ActionRuleTypes_arr[x].id)
        print("   Name:", ActionRuleTypes_arr[x].name)
        print("   WHEN:")

        for tran in TransactionKinds_arr:
            if tran.id == ActionRuleTypes_arr[x].transactionKind:
                print("      TransactionKind:", tran.identification, tran.name, tran.transactionSort)

        for transt in TransactionProcessStepKinds_arr:
            if transt.id == ActionRuleTypes_arr[x].transactionProcessStepKind:
                 for tran in TransactionKinds_arr:
                     if transt.transactionKind == tran.id:
                        print("      TransactionProcessStepKind: ",  transt.stepKind)


        print("      WITH:")
        for y in range(len(ActionRuleTypes_arr[x].parameters)):
            for entity in EntityTypes_arr:
                if entity.id == ActionRuleTypes_arr[x].parameters[y].entity:
                    print("        Entity:", entity.name)
            for attribute in AttributeTypes_arr:
                if attribute.id == ActionRuleTypes_arr[x].parameters[y].attribute:
                    print("        Attribute:", attribute.name)
        print("   WHILE:")
        print("        Condition:", ActionRuleTypes_arr[x].condition)
        print("        Then Action:", ActionRuleTypes_arr[x].then_action)
        print("        Else Action:", ActionRuleTypes_arr[x].else_action)
    print("=========================================")

#for x in range(len(ActionModels_arr)):
#    print(ActionModels_arr[x].id)
#    print(ActionModels_arr[x].name)
#    print(ActionModels_arr[x].transactionKindIdentification)
#    print(ActionModels_arr[x].transactionKindName)
#    print(ActionModels_arr[x].transactionKindSort)
#    print(ActionModels_arr[x].transactionProcessStepKind)
#    for y in range(len(ActionModels_arr[x].parameters_ar)):
#        print("      ", ActionModels_arr[x].parameters_ar[y].entityName)
#        print("      ", ActionModels_arr[x].parameters_ar[y].attributeName)
#    print(ActionModels_arr[x].condition)
#    print(ActionModels_arr[x].then_action)
#    print(ActionModels_arr[x].else_action)

#print_ActionRuleTypes(ActionRuleTypes_arr)
