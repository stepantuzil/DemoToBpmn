from ActionModelDEMO import ActionModels_arr

from lxml import etree
from lxml.builder import ElementMaker

ActionModelNumber = 0

#Prepare informations from Action model
conditionName = ActionModels_arr[ActionModelNumber].condition
thenActionName = ActionModels_arr[ActionModelNumber].then_action
elseActionName = ActionModels_arr[ActionModelNumber].else_action



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

tree = etree.parse('Condition_X.xml')
root = tree.getroot()

#print(etree.iselement(root))

i = 3
for child in root.getchildren():
    print('tag child 1: ', child.tag)
    for atr in child.items():
        print('   ', atr[0], ':', (str(atr[1])))
        child.set(atr[1], str(atr[1]))
    for child2 in child.getchildren():
        print('  tag child 2:', child2.tag)
        for atr2 in child2.items():
            print(atr2[0], ':', atr2[1])
        print("==========================================")
        child_w = child2
    print('---------------------------------------')