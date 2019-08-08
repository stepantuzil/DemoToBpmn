from ActionModelDEMO import ActionModels_arr

from lxml import etree
from lxml.builder import ElementMaker

ActionModelNumber = 0

#Prepare informations from Action model
formName = ActionModels_arr[ActionModelNumber].name
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

def change_str(name):
   # if a != -1 & b == -1:
   #     return str_tmp.replace("Tx", str(Tx_num))
   # else:
   #     return name

   str_tmp = name

   a = str_tmp.find("\n")
   if a != -1:
       str_tmp = str_tmp.replace("\n", " ")

   if name == 'FormField_name':
       print(">>>>>>>>", str_tmp.replace('name', str(formName)))
       return str_tmp.replace('name', str(formName))
   elif name == 'FormField_label':
       print(">>>>>>>>", str_tmp.replace('label', str(formName)))
       return str_tmp.replace('label', str(formName))
   return str_tmp

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
        #######################################################################################################################
        while len(child_w.getchildren()) != 0:
            for child_w2 in child_w.getchildren():
                print('  tag childi ', i, ':', child_w2.tag)
                for atr_w in child_w2.items():
                    print(atr_w[0], ':', atr_w[1])
                #######################################################################################################################
                j = i + 1
                while len(child_w2.getchildren()) != 0:
                    for child_w3 in child_w2.getchildren():

                        print('  tag childj ', j, ':', child_w3.tag)
                        for atr_w in child_w3.items():
                            print('B3      ', atr_w[0], ':', atr_w[1])

                            if atr_w[1] == 'FormField_name':
                                child_w3.set(str(atr_w[1]), change_str(str(atr_w[1])))
                            if atr_w[1] == 'FormField_label':
                                child_w3.set(str(atr_w[1]), change_str(str(atr_w[1])))

                            print('A3      ', atr_w[0], ':', atr_w[1])
                    child_w2 = child_w3
                    j = i + 1
            child_w = child_w3
            i = i + 1
            print('i:', i)
        i = 3
    print("====================================")