from operator import itemgetter
def numPad(str):
    for num in str:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    result = sorted(counter.items(), key=itemgetter(1), reverse=True)
    return result[:3]

counter = {}

num_pad = ('876485374685786457486574685327845678465784562378546978459634615327887146253'
           '91842536765398+856423716789532489653536289496153787845648953768953278451964'
           '783546195479561796489569568854686574784653845678956698536853486453758742145'
           '8761296853896537584185674256465342187546748514751542614253,61568289569868756'
           '4475254214253186689538653428753421687534216853142685342678653724874253165384'
           '21675384216787425316785314628753421687534216875314627853146278531462')

print(numPad(num_pad))