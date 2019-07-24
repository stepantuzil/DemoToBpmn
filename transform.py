f = open("Start_Tr_Tx.xml", 'r')
f2 = open("Start_Tr_Tx2.xml", 'w')

for line in f:
    #line = '<bpmndi:BPMNShape id="StartEvent_0q98cyn_di" bpmnElement="StartEvent_Tx_RV-ST">'
    if line.find('<bpmndi:BPMNShape id="') != -1 & line.find('isMarkerVisible') == -1:
        line2 = '      <bpmndi:BPMNShape id="'
        x = line.split('=')
        y = x[2][:-2]
        param, value = y.split('"', 1)
        value = value[:-1]
        line2 = line2 + value + '_di' + '"'

        param, value = line.split('"', 1)
        param, value = value.split('"', 1)
        line2 = line2 + value
        #print(line2)
        f2.write(line2)
    # <bpmndi:BPMNEdge id="SequenceFlow_0jxoz50_di" bpmnElement="SequenceFlow_B_23_Tx">
    elif line.find('<bpmndi:BPMNEdge id="') != -1 & line.find('isMarkerVisible') == -1:
        line2 = '      <bpmndi:BPMNEdge id="'
        x = line.split('=')
        y = x[2][:-2]
        param, value = y.split('"', 1)
        value = value[:-1]
        line2 = line2 + value + '_di' + '"'

        param, value = line.split('"', 1)
        param, value = value.split('"', 1)
        line2 = line2 + value
        # print(line2)
        f2.write(line2)
    else:
        f2.write(line)

f.close()
f2.close()