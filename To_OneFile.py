from To_BPMN_by_paper import Transactions_files, transf_type
from Parse_DEMO import TransactionKinds_arr
import os


def PrepareData():
    f_collaborations = open("collaborations.xml", 'w')
    f_processes = open("processes.xml", 'w')
    f_diagrams = open("diagrams.xml", 'w')

    coll = 0
    proc = 0
    diag = 0

    for file in Transactions_files:
        f_transaction = open(file, 'r')
        for line in f_transaction:
            if line.find("<bpmn:collaboration") != -1:
                coll = 1
            if line.find("</bpmn:collaboration>") != -1:
                f_collaborations.write(line)
                coll = 0

            if line.find("<bpmn:process") != -1:
                proc = 1
            if line.find("</bpmn:process>") != -1:
                f_processes.write(line)
                proc = 0

            if line.find("<bpmndi:BPMNDiagram") != -1:
                diag = 1
            if line.find("</bpmndi:BPMNDiagram>") != -1:
                f_diagrams.write(line)
                diag = 0

            if coll == 1:
                f_collaborations.write(line)

            if proc == 1:
                f_processes.write(line)

            if diag == 1:
                f_diagrams.write(line)
        f_transaction.close()

    f_collaborations.close()
    f_diagrams.close()
    f_processes.close()


def GetItTogether():
    f_collaborations = open("collaborations.xml", 'r')
    f_processes = open("processes.xml", 'r')
    f_diagrams = open("diagrams.xml", 'r')

    if transf_type == 0:
        f_final = open("finalBPMN.xml", "w")
    else:
        f_final = open("finalBPMN_HF.xml", "w")

    f_final.write('<?xml version="1.0" encoding="utf-8"?>\n')
    f_final.write(
        '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="Definitions_08avh23" targetNamespace="http://bpmn.io/schema/bpmn" exporter="Camunda Modeler" exporterVersion="2.2.4">\n')

    # Collaborations
    f_final.write('  <bpmn:collaboration id="Collaboration_A">\n')
    for line in f_collaborations:
        if line.find("<bpmn:collaboration") == -1 & line.find("</bpmn:collaboration") == -1:
            f_final.write(line)
    ###########################################
    for number_of_transaction in list(range(len(TransactionKinds_arr))):
        if number_of_transaction != 0:
            between_message_flow = '     <bpmn:messageFlow id="MessageFlow_F_' + str(number_of_transaction) \
                                   + '" sourceRef="IntermediateThrowEvent_0_' + TransactionKinds_arr[
                                       number_of_transaction - 1].identification \
                                   + '" targetRef="IntermediateCatchEvent_3_' + TransactionKinds_arr[
                                       number_of_transaction].identification + '" />\n'
            f_final.write(between_message_flow)
    ######################################
    f_final.write(' </bpmn:collaboration>\n')

    # Processes
    for line in f_processes:
        f_final.write(line)

    # Diagrams
    f_final.write('  <bpmndi:BPMNDiagram id="BPMNDiagram_1">\n')
    f_final.write('    <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Collaboration_A">\n')
    for line in f_diagrams:
        if line.find("<bpmndi:BPMNDiagram") == -1 & line.find("</bpmndi:BPMNDiagram>") == -1 & line.find(
                "<bpmndi:BPMNPlane") == -1 & line.find("</bpmndi:BPMNPlane") == -1:
            f_final.write(line)

    ###########################################
    for number_of_transaction in list(range(len(TransactionKinds_arr))):
        if number_of_transaction != 0:
            f_final.write('      <bpmndi:BPMNEdge id="MessageFlow_F_' + str(number_of_transaction)
                          + '_di" bpmnElement="MessageFlow_F_' + str(number_of_transaction) + '">\n')

            if transf_type == 0:
                x_a = 1196 + (number_of_transaction - 1) * 1450
                f_final.write('        <di:waypoint x="' + str(x_a) + '" y="1582" />\n')

                x_a = 1757 + (number_of_transaction - 1) * 1450
                f_final.write('        <di:waypoint x="' + str(x_a) + '" y="1582" />\n')
                f_final.write('        <di:waypoint x="' + str(x_a) + '" y="956" />\n')

                x_a = 1871 + (number_of_transaction - 1) * 1450
                f_final.write('        <di:waypoint x="' + str(x_a) + '" y="956" />\n')

                f_final.write('      </bpmndi:BPMNEdge>\n')
            else:
                x_a = 832 + (number_of_transaction - 1) * 1450
                f_final.write('        <di:waypoint x="' + str(x_a) + '" y="494" />\n')

                x_a = 1355 + (number_of_transaction - 1) * 1450
                f_final.write('        <di:waypoint x="' + str(x_a) + '" y="494" />\n')
                f_final.write('        <di:waypoint x="' + str(x_a) + '" y="94" />\n')

                x_a = 1520 + (number_of_transaction - 1) * 1450
                f_final.write('        <di:waypoint x="' + str(x_a) + '" y="94" />\n')

                f_final.write('      </bpmndi:BPMNEdge>\n')
    ######################################

    f_final.write('    </bpmndi:BPMNPlane>\n')
    f_final.write('  </bpmndi:BPMNDiagram>\n')

    f_final.write("</bpmn:definitions>\n")

    f_final.close()

    f_collaborations.close()
    f_diagrams.close()
    f_processes.close()

    os.remove("collaborations.xml")
    os.remove("processes.xml")
    os.remove("diagrams.xml")


def DoTheMagic():
    PrepareData()
    GetItTogether()


DoTheMagic()
