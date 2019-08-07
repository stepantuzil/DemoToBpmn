# from Parse_DEMO import TransactionKinds_arr, ElementaryActorRoles_arr, CompositeActorRoles_arr, TransactionProcessStepKinds_arr, AttributeTypes_arr, EntityTypes_arr, ActionRuleTypes_arr, Connections_arr


from Parse_DEMO import CTransactionKind, CElementaryActorRole, CCompositeActorRole, CConnection


##Krmeni prikladu
def Inicialization():
    TransactionKinds_arr = []
    # identification
    # name
    # transactionSort
    TransactionKinds_arr.append(CTransactionKind('00', 'T-1', 'delivery placement', 'original'))
    TransactionKinds_arr.append(CTransactionKind('01', 'T-2', 'delivery completation', 'original'))
    TransactionKinds_arr.append(CTransactionKind('02', 'T-3', 'order delivery', 'original'))
    TransactionKinds_arr.append(CTransactionKind('03', 'T-4', 'order pickup', 'original'))
    TransactionKinds_arr.append(CTransactionKind('04', 'T-5', 'order delivery', 'original'))
    TransactionKinds_arr.append(CTransactionKind('05', 'T-6', 'order payment', 'original'))

    ElementaryActorRoles_arr = []
    # identification
    # name
    ElementaryActorRoles_arr.append(CElementaryActorRole('06', 'A-1', 'Call assistance'))
    ElementaryActorRoles_arr.append(CElementaryActorRole('07', 'A-2', 'Operator'))
    ElementaryActorRoles_arr.append(CElementaryActorRole('08', 'A-3', 'Courier'))

    CompositeActorRoles_arr = []
    # identification
    # name
    CompositeActorRoles_arr.append(CCompositeActorRole('09', 'CA-1', 'customer'))
    CompositeActorRoles_arr.append(CCompositeActorRole('10', 'CA-2', 'pickup person'))
    CompositeActorRoles_arr.append(CCompositeActorRole('11', 'CA-3', 'delivery person'))
    CompositeActorRoles_arr.append(CCompositeActorRole('12', 'CA-4', 'payer'))

    Connections_arr = []
    # id, fromCardinality, toCardinality, connection_type_name, from_type, from_id, to_type, to_id
    Connections_arr.append(CConnection('12', '1', '1', 'Initiator', 'From', '09', 'To', '00'))
    Connections_arr.append(CConnection('13', '1', '1', 'Executor', 'From', '00', 'To', '06'))
    Connections_arr.append(CConnection('14', '1', '1', 'Initiator', 'From', '07', 'To', '01'))
    Connections_arr.append(CConnection('15', '1', '1', 'Initiator', 'From', '01', 'To', '07'))
    Connections_arr.append(CConnection('16', '1', '1', 'Initiator', 'From', '07', 'To', '02'))
    Connections_arr.append(CConnection('17', '1', '1', 'Initiator', 'From', '02', 'To', '08'))
    Connections_arr.append(CConnection('18', '1', '1', 'Initiator', 'From', '08', 'To', '03'))
    Connections_arr.append(CConnection('19', '1', '1', 'Initiator', 'From', '03', 'To', '10'))
    Connections_arr.append(CConnection('20', '1', '1', 'Initiator', 'From', '08', 'To', '04'))
    Connections_arr.append(CConnection('21', '1', '1', 'Initiator', 'From', '04', 'To', '11'))
    Connections_arr.append(CConnection('22', '1', '1', 'Initiator', 'From', '08', 'To', '05'))
    Connections_arr.append(CConnection('22', '1', '1', 'Initiator', 'From', '05', 'To', '12'))

    # FindLoop(Connections_arr)
    Preparation(TransactionKinds_arr, ElementaryActorRoles_arr, CompositeActorRoles_arr, Connections_arr,
                FindLoop(Connections_arr, TransactionKinds_arr))


def FindLoop(Connections_arr, TransactionKinds_arr):
    from1 = from2 = to1 = to2 = 'B'

    Connections_arr_ret = []
    for i in list(range(len(Connections_arr))):
        if i == (len(Connections_arr) - 1):
            break
        from1 = Connections_arr[i].from_id
        to1 = Connections_arr[i].to_id
        to2 = Connections_arr[i + 1].to_id
        if from1 == to2:
            Connections_arr_ret.append(to1)

    TransactionKinds_arr_ret = []

    for i in Connections_arr_ret:
        for j in TransactionKinds_arr:
            if i == j.id:
                TransactionKinds_arr_ret.append(j.identification)

    return TransactionKinds_arr_ret


class CPairs:
    def __init__(self, Mfrom, Mto):
        self.Mfrom = Mfrom
        self.Mto = Mto


def Preparation(TransactionKinds_arr, ElementaryActorRoles_arr, CompositeActorRoles_arr, Connections_arr,
                LoopConnections):
    #####lines
    lanes = []
    lanes.append('    <bpmn:laneSet id="LaneSet_1qs1doz">\n')

    lane = '      <bpmn:lane id="Lane_'
    lane_nr = 0
    for ElActorRole in ElementaryActorRoles_arr:
        lane_ins = lane + str(lane_nr) + '" name="' + ElActorRole.identification + '">\n'
        lanes.append(lane_ins)
        if ElActorRole.id == ElementaryActorRoles_arr[0].id:
            lanes.append('        <bpmn:flowNodeRef>StartEvent_0</bpmn:flowNodeRef>\n')
        lanes.append('      </bpmn:lane>\n')
        lane_nr += 1

    lanes.append('    </bpmn:laneSet>\n')
    ######################################
    # navazujici pary
    Pairs = []
    Pairs_index = 0
    Pairs_order = 0

    Pairs.append(CPairs('F', 'T'))
    # tasks
    tasks = []
    task_num = 0

    start = '    <bpmn:startEvent id="StartEvent_0" name="(' + TransactionKinds_arr[0].identification + '/rq)>\n'
    tasks.append(start)
    tasks.append('    </bpmn:startEvent>\n')

    Pairs[Pairs_index].Mfrom = 'StartEvent_0'
    Pairs_index += 1

    # najit vsechny jak jdou posobe
    for conn in list(range(len(Connections_arr))):  # vsechny connection
        for tr_name in list(range(len(TransactionKinds_arr))):  # transakce
            if Connections_arr[conn].to_id == TransactionKinds_arr[tr_name].id:  # kdyz najdu transakci v connection
                for elAcRo in ElementaryActorRoles_arr:  # najdu ElementaryActor, ktery tam figuruje
                    if Connections_arr[conn].from_id == elAcRo.id:
                        break
                    if Connections_arr[conn].to_id == elAcRo.id:
                        break
                    if conn == (len(Connections_arr) - 1):
                        break
                    if Connections_arr[conn + 1].from_id == elAcRo.id:
                        break
                    if Connections_arr[conn + 1].to_id == elAcRo.id:
                        break
                # udelam Task
                line_to_insert = '        <bpmn:flowNodeRef>Task_' + str(task_num) + '</bpmn:flowNodeRef>\n'
                task_num += 1
                index = 1
                for line in lanes:
                    # print(line, '||', TransactionKinds_arr[tr_name].identification)
                    if line.find(elAcRo.identification) != -1:
                        lanes.insert(index, line_to_insert)
                        # print(line_to_insert, "--", index)
                        break
                    index += 1
                # TODO UserTask??
                tasks_to_insert = '    <bpmn:task id="Task_' + str(task_num) + '" name="' + TransactionKinds_arr[
                    tr_name].name + '">\n'
                tasks.append(tasks_to_insert)
                tasks.append('    </bpmn:task>\n')
                ################################################################
                if Pairs_index % 2 == 1:
                    Pairs[Pairs_order].Mto = TransactionKinds_arr[tr_name].identification
                    Pairs_order += 1
                else:
                    Pairs.append(CPairs('F', 'T'))
                    Pairs[Pairs_order].Mfrom = TransactionKinds_arr[tr_name].identification
                Pairs_index += 1

        # end_transakce
    # end connections

    # for line in lanes:
    #    print(line, end='')
    # for line in tasks:
    #    print(line, end='')

    for i in list(range(len(Pairs) - 1)):
        for j in list(range(len(LoopConnections))):
            if (Pairs[i].Mto != LoopConnections[j]):
                print(Pairs[i].Mfrom, " > ", Pairs[i].Mto)
                print(Pairs[i].Mto, " > ", Pairs[i + 1].Mfrom)


def Making():
    f1 = open("BPMN.xml", 'w')

    f1.write('<?xml version="1.0" encoding="utf-8"?>\n')
    f1.write(
        '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="Definitions_08avh23" targetNamespace="http://bpmn.io/schema/bpmn" exporter="Camunda Modeler" exporterVersion="2.2.4">\n')
    f1.write(
        '  <bpmn:collaboration id="Collaboration_0jzxcrg">\n    <bpmn:participant id="Participant_1cl50va" processRef="Process_1" />\n  </bpmn:collaboration>')

    ##Process


Inicialization()
