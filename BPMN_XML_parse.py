import Parse_DEMO

from Parse_DEMO import TransactionKinds_arr, ElementaryActorRoles_arr, CompositeActorRoles_arr, \
    TransactionProcessStepKinds_arr, AttributeTypes_arr, EntityTypes_arr, ActionRuleTypes_arr, Connections_arr
# from Parse_DEMO import print_all

# TODO: Maybe all arrays to one

from lxml import etree
from lxml.builder import ElementMaker

definitions_s = '<bpmn:definitions ' \
                'xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" ' \
                'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" ' \
                'xmlns:di="http://www.omg.org/spec/DD/20100524/DI" ' \
                'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" ' \
                'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ' \
                'id="Definitions_08avh23" targetNamespace="http://bpmn.io/schema/bpmn" exporter="Camunda Modeler" exporterVersion="2.2.4">'
definitions_k = '</bpmn:definitions>'

E = ElementMaker(namespace="http://www.omg.org/spec/BPMN/20100524/MODEL",
                 nsmap={'bpmn': "http://www.omg.org/spec/BPMN/20100524/MODEL"})

DEFINITIONS = E.definitions
COLLABORATION = E.collaboration
PARTICIPANT = E.participant
MESSAGEFLOW = E.messageFlow
PROCESS = E.process

Tx = 'Tx-RV-PM'

# bpmn_xml = DEFINITIONS(
#            COLLABORATION(
#                PARTICIPANT(id="ParticipantID", name=Tx, processRef="Process_"+Tx),
#               MESSAGEFLOW(id="MessageFlow_0_Tx")
#        ,id="Collaboration_1abef2q"),#Colaboration
#            PROCESS(id="Process_Tx", isExecutable="false")
#
#        )
tree = etree.parse('Start_Tr_Tx.xml')
root = tree.getroot()

# children = list(root)
# for child in root:
#    print(child.tag)

str_tx = "Tx"

# print(etree.iselement(root))

#####Change number of Transaction
i = 1
Tx_num = "T" + str(i)


def change_str(name):
    str_tmp = name
    a = str_tmp.find("\n")
    if a != -1:
        str_tmp = str_tmp.replace("\n", " ")

    a = str_tmp.find("Tx")
    b = str_tmp.find("Tx+1")
    if a != -1 & b == -1:
        return str_tmp.replace("Tx", str(Tx_num))
    else:
        return name


# name = "EndEvent_2_Tx-RV-ST"
# name=change_str(name)
# print(name)

i = 3
for child in root.getchildren():
    print('tag child 1: ', child.tag)
    for atr in child.items():
        print('   ', atr[0], ':', change_str(str(atr[1])))
        child.set(atr[1], change_str(str(atr[1])))
    for child2 in child.getchildren():
        print('  tag child 2:', child2.tag)
        for atr2 in child2.items():
            print('B1      ', atr2[0], ':', atr2[1])
            if atr2[1].find("Tx") != -1 & atr2[1].find("Tx+1") == -1:
                child2.set(atr2[1], change_str(str(atr2[1])))
            print('A1      ', atr2[0], ':', change_str(str(atr2[1])))
        print("  ----------------------------------")
        child_w = child2
        #######################################################################################################################
        while len(child_w.getchildren()) != 0:
            for child_w2 in child_w.getchildren():
                print('  tag childi ', i, ':', child_w2.tag)
                for atr_w in child_w2.items():
                    print('B2      ', atr_w[0], ':', atr_w[1])
                    if atr_w[1].find("Tx") != -1 & atr_w[1].find("Tx+1") == -1:
                        child_w2.set(str(atr_w[0]), str(change_str(str(atr_w[1]))))
                    print('A2      ', atr_w[0], ':', atr_w[1])
                #######################################################################################################################
                j = i + 1
                while len(child_w2.getchildren()) != 0:
                    for child_w3 in child_w2.getchildren():

                        print('  tag childj ', j, ':', child_w3.tag)
                        for atr_w in child_w3.items():
                            print('B3      ', atr_w[0], ':', atr_w[1])
                            if atr_w[1].find("Tx") != -1 & atr_w[1].find("Tx+1") == -1:
                                child_w3.set(str(atr_w[1]), change_str(str(atr_w[1])))
                            print('A3      ', atr_w[0], ':', atr_w[1])
                    child_w2 = child_w3
                    j = i + 1
            child_w = child_w3
            i = i + 1
            print('i:', i)
        i = 3
    print("====================================")
