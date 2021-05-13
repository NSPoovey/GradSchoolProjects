class nodeType:
    def __init__(self, data):
        self.Info = data
        self.Link = None

class linkList:
    def __init__(self):
        self.Start = None
    def buildList(self, data):
        curNode = self.Start = nodeType(data[0])
        for i in range(1, len(data)):
            curNode.Link = nodeType(data[i])
            curNode = curNode.Link
    def traverse(self):
        curNode = self.Start
        while curNode:
            print("Current address: "+str(hex(id(curNode)))+" Info: "+str(curNode.Info)+" Link: "+str(hex(id(curNode.Link)) if curNode.Link else "None"))
            curNode = curNode.Link

if __name__=='__main__':
    input = [int(x) for x in input().split()]
    newList = linkList()
    newList.buildList(input)
    newList.traverse()