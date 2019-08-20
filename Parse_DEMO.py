import untangle

# from To_BPMN_by_paper import input_file

input_file = input("Enter XML DEMO model file in VISI standard or type 'example' to use example file.\n")

if input_file == 'example':
    file = '../parseXML/DEMO3.8Sample.xml'
else:
    file = input_file

doc = untangle.parse(file)


#####################################################


class CTransactionKind:
    def __init__(self, id, identification, name, transactionSort):
        self.id = id
        self.identification = identification
        self.name = name
        self.transactionSort = transactionSort


TransactionKinds_arr = []
for TransactionKind in doc.DEMOmodel.TransactionKinds.TransactionKind:
    identification = TransactionKind.Identification.cdata
    name = TransactionKind.Name.cdata
    transactionSort = TransactionKind.TransactionSort.cdata

    TransactionKinds_arr.append(CTransactionKind(TransactionKind['Id'], identification, name, transactionSort))


def print_TransactionKinds(TransactionKinds_arr):
    print("TransactionKinds:")
    for x in range(len(TransactionKinds_arr)):
        print("   Id:", TransactionKinds_arr[x].id)
        print("  ", TransactionKinds_arr[x].identification, ":", TransactionKinds_arr[x].name, " ",
              TransactionKinds_arr[x].transactionSort)
        print("  ")
    print("=========================================")


#####################################################


class CElementaryActorRole:
    def __init__(self, id, identification, name):
        self.id = id
        self.identification = identification
        self.name = name


ElementaryActorRoles_arr = []
for ElementaryActorRole in doc.DEMOmodel.ElementaryActorRoles.ElementaryActorRole:
    identification = ElementaryActorRole.Identification.cdata
    name = ElementaryActorRole.Name.cdata

    ElementaryActorRoles_arr.append(CElementaryActorRole(ElementaryActorRole['Id'], identification, name))


def print_ElementaryActorRoles(ElementaryActorRoles_arr):
    print("ElementaryActorRoles:")
    for x in range(len(ElementaryActorRoles_arr)):
        print("   Id:", ElementaryActorRoles_arr[x].id)
        print("  ", ElementaryActorRoles_arr[x].identification, ":", ElementaryActorRoles_arr[x].name)
        print("  ")
    print("=========================================")


#####################################################


class CCompositeActorRole:
    def __init__(self, id, identification, name):
        self.id = id
        self.identification = identification
        self.name = name


CompositeActorRoles_arr = []
for CompositeActorRole in doc.DEMOmodel.CompositeActorRoles.CompositeActorRole:
    identification = CompositeActorRole.Identification.cdata
    name = CompositeActorRole.Name.cdata

    CompositeActorRoles_arr.append(CCompositeActorRole(CompositeActorRole['Id'], identification, name))


def print_CompositeActorRoles(CompositeActorRoles_arr):
    print("CompositeActorRoles:")
    for x in range(len(CompositeActorRoles_arr)):
        print("   Id:", CompositeActorRoles_arr[x].id)
        print("  ", CompositeActorRoles_arr[x].identification, ":", CompositeActorRoles_arr[x].name)
        print("  ")
    print("=========================================")


#####################################################


class CTransactionProcessStepKind:
    def __init__(self, id, transactionKind, stepKind):
        self.id = id
        self.transactionKind = transactionKind
        self.stepKind = stepKind


TransactionProcessStepKinds_arr = []
for TransactionProcessStepKind in doc.DEMOmodel.TransactionProcessStepKinds.TransactionProcessStepKind:
    transactionKind = TransactionProcessStepKind.TransactionKind.cdata
    stepKind = TransactionProcessStepKind.StepKind.cdata

    TransactionProcessStepKinds_arr.append(CTransactionProcessStepKind(TransactionProcessStepKind['Id'],
                                                                       transactionKind, stepKind))


def print_TransactionProcessStepKinds(TransactionProcessStepKinds_arr):
    print("TransactionProcessStepKinds:")
    for x in range(len(TransactionProcessStepKinds_arr)):
        print("   Id:", TransactionProcessStepKinds_arr[x].id)
        print("  ", TransactionProcessStepKinds_arr[x].transactionKind, ":",
              TransactionProcessStepKinds_arr[x].stepKind)
        print("  ")
    print("=========================================")


#####################################################


class CAttributeType:
    def __init__(self, id, name, typeName, entityType):
        self.id = id
        self.name = name
        self.typeName = typeName
        self.entityType = entityType


AttributeTypes_arr = []
for AttributeType in doc.DEMOmodel.AttributeTypes.AttributeType:
    name = AttributeType.Name.cdata
    typeName = AttributeType.TypeName.cdata
    entityType = AttributeType.EntityType.cdata

    AttributeTypes_arr.append(CAttributeType(AttributeType['Id'], name, typeName, entityType))


def print_AttributeTypes(AttributeTypes_arr):
    print("AttributeTypes:")
    for x in range(len(AttributeTypes_arr)):
        print("   Id:", AttributeTypes_arr[x].id)
        print("  ", AttributeTypes_arr[x].name, ":", AttributeTypes_arr[x].typeName, " ",
              AttributeTypes_arr[x].entityType)
        print("  ")
    print("=========================================")


#####################################################


class CEntityType:
    def __init__(self, id, name):
        self.id = id
        self.name = name


EntityTypes_arr = []
for EntityType in doc.DEMOmodel.EntityTypes.EntityType:
    name = EntityType.Name.cdata

    EntityTypes_arr.append(CEntityType(EntityType['Id'], name))


def print_EntityTypes(EntityTypes_arr):
    print("EntityTypes:")
    for x in range(len(EntityTypes_arr)):
        print("   Id:", EntityTypes_arr[x].id)
        print("  ", EntityTypes_arr[x].name)
        print("  ")
    print("=========================================")


#####################################################


class CParameter:
    def __init__(self, entity, attribute):
        self.entity = entity
        self.attribute = attribute


class CActionRuleType:
    def __init__(self, id, name, transactionKind, transactionProcessStepKind, parameters_ar, condition, then_action,
                 else_action):
        self.id = id
        self.name = name
        self.transactionKind = transactionKind
        self.transactionProcessStepKind = transactionProcessStepKind
        self.parameters = parameters_ar
        self.condition = condition
        self.then_action = then_action
        self.else_action = else_action


ActionRuleTypes_arr = []
Parameter_arr = []
for ActionRuleType in doc.DEMOmodel.ActionRuleTypes.ActionRuleType:
    # TODO Asses, Responses ??, While loop ??
    name = ActionRuleType.Name.cdata

    transactionKind = ActionRuleType.When.TransactionKind.cdata
    transactionProcessStepKind = ActionRuleType.When.TransactionProcessStepKind.cdata

    for Parameter in ActionRuleType.When.With.Parameter:
        entity = Parameter.Entity.cdata
        attribute = Parameter.Attribute.cdata

        Parameter_arr.append(CParameter(entity, attribute))

    condition = ActionRuleType.While.Flow.If.Condition.cdata
    then_action = ActionRuleType.While.Flow.If.Then.Action.cdata
    else_action = ActionRuleType.While.Flow.If.Else.Action.cdata

    ActionRuleTypes_arr.append(
        CActionRuleType(ActionRuleType['Id'], name, transactionKind, transactionProcessStepKind, Parameter_arr,
                        condition, then_action, else_action))


def print_ActionRuleTypes(ActionRuleTypes_arr):
    print("ActionRuleTypes:")
    for x in range(len(ActionRuleTypes_arr)):
        print("   Id:", ActionRuleTypes_arr[x].id)
        print("   Name:", ActionRuleTypes_arr[x].name)
        print("   WHEN:")
        print("      TransactionKind:", ActionRuleTypes_arr[x].transactionKind)
        print("      TransactionProcessStepKind:", ActionRuleTypes_arr[x].transactionProcessStepKind)
        print("      WITH:")
        for y in range(len(ActionRuleTypes_arr[x].parameters)):
            print("        Entity:", ActionRuleTypes_arr[x].parameters[y].entity)
            print("        Attribute:", ActionRuleTypes_arr[x].parameters[y].attribute)
        print("   WHILE:")
        print("        Condition:", ActionRuleTypes_arr[x].condition)
        print("        Then Action:", ActionRuleTypes_arr[x].then_action)
        print("        Else Action:", ActionRuleTypes_arr[x].else_action)
    print("=========================================")


#####################################################


class CConnection:
    def __init__(self, id, fromCardinality, toCardinality, connection_type_name, from_type, from_id, to_type, to_id):
        self.id = id
        self.fromCardinality = fromCardinality
        self.toCardinality = toCardinality
        self.connection_type_name = connection_type_name
        self.from_type = from_type
        self.from_id = from_id
        self.to_type = to_type
        self.to_id = to_id


Connections_arr = []
for Connection in doc.DEMOmodel.Connections.Connection:
    # print("   Id:", Connection['Id'], " From:", Connection['FromCardinality'], " To:", Connection['ToCardinality'])
    childs = str(Connection.children)
    i = 0
    j = 0
    connection_type_name = "blank"
    for child_for in childs.split("="):
        if i == 1:
            for name in child_for.split(","):
                if j == 0:
                    # print("name: ", name)
                    # print("name: ", name.replace(" ", ""))
                    connection_type_name = name.replace(" ", "")
                    j += 1
        i += 1

    if connection_type_name == "ExecutorEAR":
        # print("   ExecutorEAR:")
        fromTransactionKind = Connection.ExecutorEAR.FromTransactionKind.cdata
        toElementaryActorRole = Connection.ExecutorEAR.ToElementaryActorRole.cdata

        Connections_arr.append(CConnection(Connection['Id'], Connection['FromCardinality'], Connection['ToCardinality'],
                                           connection_type_name, "FromTransactionKind", fromTransactionKind,
                                           "ToElementaryActorRole", toElementaryActorRole))

        # print("      FromTransactionKind:", fromTransactionKind)
        # print("      ToElementaryActorRole:", toElementaryActorRole)
    if connection_type_name == "ExecutorCAR":
        # print("   ExecutorCAR:")
        fromTransactionKind = Connection.InitiatorCAR.FromTransactionKind.cdata
        toElementaryActorRole = Connection.InitiatorCAR.ToElementaryActorRole.cdata

        Connections_arr.append(CConnection(Connection['Id'], Connection['FromCardinality'], Connection['ToCardinality'],
                                           connection_type_name, "FromTransactionKind", fromTransactionKind,
                                           "ToElementaryActorRole", toElementaryActorRole))

        # print("      FromTransactionKind:", fromTransactionKind)
        # print("      ToElementaryActorRole:", toElementaryActorRole)
    if connection_type_name == "InitiatorEAR":
        # print("   InitiatorEAR:")
        fromElementaryActorRole = Connection.InitiatorEAR.FromElementaryActorRole.cdata
        toTransactionKind = Connection.InitiatorEAR.ToTransactionKind.cdata

        Connections_arr.append(CConnection(Connection['Id'], Connection['FromCardinality'], Connection['ToCardinality'],
                                           connection_type_name, "FromElementaryActorRole", fromElementaryActorRole,
                                           "ToTransactionKind", toTransactionKind))

        # print("      FromElementaryActorRole:", fromElementaryActorRole)
        # print("      ToTransactionKind:", toTransactionKind)
    if connection_type_name == "InitiatorCAR":
        # print("   InitiatorCAR:")
        fromCompositeActorRole = Connection.InitiatorCAR.FromCompositeActorRole.cdata
        toTransactionKind = Connection.InitiatorCAR.ToTransactionKind.cdata

        Connections_arr.append(CConnection(Connection['Id'], Connection['FromCardinality'], Connection['ToCardinality'],
                                           connection_type_name, "FromCompositeActorRole", fromCompositeActorRole,
                                           "ToTransactionKind", toTransactionKind))

        # print("      FromCompositeActorRole:", fromCompositeActorRole)
        # print("      ToTransactionKind:", toTransactionKind)
    if connection_type_name == "InterstrictionATEAR":
        # print("   InterstrictionATEAR:")
        fromAggregateTransactionKind = Connection.InterstrictionATEAR.FromAggregateTransactionKind.cdata
        toElementaryActorRole = Connection.InterstrictionATEAR.ToElementaryActorRole.cdata

        Connections_arr.append(CConnection(Connection['Id'], Connection['FromCardinality'], Connection['ToCardinality'],
                                           connection_type_name, "FromAggregateTransactionKind",
                                           fromAggregateTransactionKind,
                                           "ToElementaryActorRole", toElementaryActorRole))

        # print("      FromAggregateTransactionKind:", fromAggregateTransactionKind)
        # print("      ToElementaryActorRole:", toElementaryActorRole)
    if connection_type_name == "InterstrictionATCAR":
        # print("   InterstrictionATEAR:")
        fromAggregateTransactionKind = Connection.InterstrictionATCAR.FromAggregateTransactionKind.cdata
        toCompositeActorRole = Connection.InterstrictionATCAR.ToCompositeActorRole.cdata

        Connections_arr.append(CConnection(Connection['Id'], Connection['FromCardinality'], Connection['ToCardinality'],
                                           connection_type_name, "FromAggregateTransactionKind",
                                           fromAggregateTransactionKind,
                                           "ToCompositeActorRole", toCompositeActorRole))

        # print("      FromAggregateTransactionKind:", fromAggregateTransactionKind)
        # print("      ToCompositeActorRole:", toCompositeActorRole)
    if connection_type_name == "InterstrictionTEAR":
        # print("   InterstrictionTEAR:")
        fromTransactionKind = Connection.InterstrictionTEAR.FromTransactionKind.cdata
        toElementaryActorRole = Connection.InterstrictionTEAR.ToElementaryActorRole.cdata

        Connections_arr.append(CConnection(Connection['Id'], Connection['FromCardinality'], Connection['ToCardinality'],
                                           connection_type_name, "FromTransactionKind", fromTransactionKind,
                                           "ToElementaryActorRole", toElementaryActorRole))

        # print("      FromTransactionKind:", fromTransactionKind)
        # print("      ToElementaryActorRole:", toElementaryActorRole)
    if connection_type_name == "InterstrictionTCAR":
        # print("   InterstrictionTCAR:")
        fromTransactionKind = Connection.InterstrictionTCAR.FromTransactionKind.cdata
        toCompositeActorRole = Connection.InterstrictionTCAR.ToCompositeActorRole.cdata

        Connections_arr.append(CConnection(Connection['Id'], Connection['FromCardinality'], Connection['ToCardinality'],
                                           connection_type_name, "FromTransactionKind", fromTransactionKind,
                                           "ToCompositeActorRole", toCompositeActorRole))

        # print("      FromTransactionKind:", fromTransactionKind)
        # print("      ToCompositeActorRole:", toCompositeActorRole)
    # PSD
    if connection_type_name == "InitiationTPSK":
        # print("   InitiationTPSK:")
        fromTransactionProcessStepKind = Connection.InitiationTPSK.FromTransactionProcessStepKind.cdata
        toTransactionProcessStepKind = Connection.InitiationTPSK.ToTransactionProcessStepKind.cdata

        Connections_arr.append(CConnection(Connection['Id'], Connection['FromCardinality'], Connection['ToCardinality'],
                                           connection_type_name, "FromTransactionProcessStepKind",
                                           fromTransactionProcessStepKind,
                                           "ToTransactionProcessStepKind", toTransactionProcessStepKind))

        # print("      FromTransactionProcessStepKind:", fromTransactionProcessStepKind)
        # print("      ToTransactionProcessStepKind:", toTransactionProcessStepKind)
    if connection_type_name == "WaitConditionTPSK":
        # print("   WaitConditionTPSK:")
        fromTransactionProcessStepKind = Connection.WaitConditionTPSK.FromTransactionProcessStepKind.cdata
        toTransactionProcessStepKind = Connection.WaitConditionTPSK.ToTransactionProcessStepKind.cdata

        Connections_arr.append(CConnection(Connection['Id'], Connection['FromCardinality'], Connection['ToCardinality'],
                                           connection_type_name, "FromTransactionProcessStepKind",
                                           fromTransactionProcessStepKind,
                                           "ToTransactionProcessStepKind", toTransactionProcessStepKind))

        # print("      FromTransactionProcessStepKind:", fromTransactionProcessStepKind)
        # print("      ToTransactionProcessStepKind:", toTransactionProcessStepKind)


def print_Connections(Connections_arr):
    print("Connections:")
    for x in range(len(Connections_arr)):
        print("   Id:", Connections_arr[x].id, " From:", Connections_arr[x].fromCardinality, " To:",
              Connections_arr[x].toCardinality)
        print("  ", Connections_arr[x].connection_type_name, ":")
        print("      ", Connections_arr[x].from_type, ":", Connections_arr[x].from_id)
        print("      ", Connections_arr[x].to_type, ":", Connections_arr[x].to_id)
    print("=========================================")


#####################################################
def print_all(TransactionKinds_arr, ElementaryActorRoles_arr, CompositeActorRoles_arr, TransactionProcessStepKinds_arr,
              AttributeTypes_arr, EntityTypes_arr, ActionRuleTypes_arr, Connections_arr):
    print_TransactionKinds(TransactionKinds_arr)
    print_ElementaryActorRoles(ElementaryActorRoles_arr)
    print_CompositeActorRoles(CompositeActorRoles_arr)
    print_TransactionProcessStepKinds(TransactionProcessStepKinds_arr)
    print_AttributeTypes(AttributeTypes_arr)
    print_EntityTypes(EntityTypes_arr)
    print_ActionRuleTypes(ActionRuleTypes_arr)
    print_Connections(Connections_arr)


class all_DEMO:
    def __init__(self, TransactionKinds_arr, ElementaryActorRoles_arr, CompositeActorRoles_arr,
                 TransactionProcessStepKinds_arr,
                 AttributeTypes_arr, EntityTypes_arr, ActionRuleTypes_arr, Connections_arr):
        self.TransactionKinds_arr = TransactionKinds_arr
        self.ElementaryActorRoles_arr = ElementaryActorRoles_arr
        self.CompositeActorRoles_arr = CompositeActorRoles_arr
        self.TransactionProcessStepKinds_arr = TransactionProcessStepKinds_arr
        self.AttributeTypes_arr = AttributeTypes_arr
        self.EntityTypes_arr = EntityTypes_arr
        self.ActionRuleTypes_arr = ActionRuleTypes_arr
        self.Connections_arr = Connections_arr


ALL_DEMO = all_DEMO(TransactionKinds_arr, ElementaryActorRoles_arr, CompositeActorRoles_arr,
                    TransactionProcessStepKinds_arr, AttributeTypes_arr, EntityTypes_arr, ActionRuleTypes_arr,
                    Connections_arr)

# print_all(TransactionKinds_arr, ElementaryActorRoles_arr, CompositeActorRoles_arr, TransactionProcessStepKinds_arr,
#              AttributeTypes_arr, EntityTypes_arr, ActionRuleTypes_arr, Connections_arr)
# print_ActionRuleTypes(ActionRuleTypes_arr)
