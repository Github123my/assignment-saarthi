dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]

outputdict = []

for i in range(len(dict_list)):
    if dict_list[i] in outputdict:
        pass
    else:
        outputdict.append(dict_list[i])
    
print(outputdict)
