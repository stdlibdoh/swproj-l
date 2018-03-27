def unpackTable(fileName):
    table = open(fileName,"r")
    data = []
    col = 0

    for line in table:
        data.append([])
        for word in line.split():
            data[col].append(int(word))
        col+=1
    return data

# printDemand = (data[-1])

def getDemand():
    print("Demand")
    print(data[-1])
    print("-------")

def getSupply():
    print("Supply")
    for i in range(0,len(data)):
        print(data[i][-1])
    print("-------")

def getCostfig():
    print("Cost Figures")
    for i in range(0, len(data)-1):
        for j in range(0, len(data[i]-1)):
            print(data[i][j])

    print("-------")

def getTable():
    print("Input Table")
    for i in data:
        print(i)
    print("-------")

def printNumbers():
    for i in range(0,len(data)-1):
        for j in range(0, len(data[i])-1):
            print(data[i][j])

# get data and store in 2D array
data = unpackTable("input.dat")

### def nortWest():
#    for i in printTable():
      #[0] = printSupply([0])
##
##def main(fileName):
##    unpackTable()
printNumbers()

#getTable()
#getCostfig()
#getDemand()
#getSupply()
#northWest()

##newtab = [len(data)][len(data[0])]
