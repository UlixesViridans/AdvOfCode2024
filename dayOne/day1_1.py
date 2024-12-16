import pdb

def main():
   print("Day 1_1")
   
   
   doubleList = []
   with open("input1.txt") as f:
      for line in f:
         doubleList.append(line)
   
   listOne = list()
   listTwo = list()
   
   for line in doubleList:
      part1,part2=line.split()
      listOne.append(int(part1))
      listTwo.append(int(part2))
   listOne.sort()
   listTwo.sort()
   hammingSum = 0
   
   for L1, L2 in zip(listOne, listTwo):
      hammingSum+=abs(L1-L2)
   print("Hamming Sum is:")
   print(hammingSum)
   
   #create a dict and count how many times numbers in the second list
   #appear in the first list
   def genFreqDict(rawL=list()):
      freqDict = dict()
      for item in rawL:
         if not item in freqDict:
            freqDict[item] = 1
         else:
            freqDict[item] +=1
      return freqDict
   
   L1DictOfL2Simili = dict.fromkeys(listOne, 0)
   L2FreqDict = genFreqDict(listTwo)
   
   similiScore = 0
   for key in L1DictOfL2Simili:
      if key in L2FreqDict:
         L1DictOfL2Simili[key] = key*L2FreqDict[key]
   
   for item in listOne:
      similiScore+=L1DictOfL2Simili[item]
   print(similiScore)
   pdb.set_trace()

if __name__ == '__main__':
   main()