import random
import string
import math
from utils import defSeed
def totalUniqueCompositeLetters(numStrings, stringsLen):
    totalUniqueStrings = 4 ** stringsLen
    totalUniqueCompositeLetters = math.comb(totalUniqueStrings, numStrings)
    return totalUniqueCompositeLetters

class CompositeLetter:
    def __init__(self, strings):
        self.strings = strings

    def __eq__(self, other):
        if isinstance(other, CompositeLetter):
            return set(self.strings) == set(other.strings)
        return False

    def __hash__(self):
        return hash(set(self.strings))
        
class RandomCompositeLetter(CompositeLetter):
    random.seed(defSeed)
    def __init__(self, numStrings, stringsLen):
        super().__init__(None)
        self.numStrings = numStrings
        self.stringsLen = stringsLen
        self.strings = self.generateStrings()

    def generateStrings(self):
        strings = set()
        while len(strings) < self.numStrings:
            string_ = ''.join(random.choice("ATGC") for _ in range(self.stringsLen))  # Composite string
            if string_ not in strings:
                strings.add(string_)
        return list(strings)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.numStrings:
            result = self.strings[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
    #eq and hash inherited from CompositeLetter
    
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class AllCompositeLetters(metaclass=Singleton):       
    def __init__(self, numCompLetters, numStrings, stringsLen):
        maxCompLetters = totalUniqueCompositeLetters(numStrings, stringsLen)
        if(numCompLetters > maxCompLetters):
            raise ValueError("Number of composite letters can't be reached with the given number of strings and string length.")
        if(numCompLetters == 0):
            numCompLetters = maxCompLetters
        self.numCompLetters = numCompLetters
        self.compositeLetters = self.generateCompositeLetters(numCompLetters, numStrings, stringsLen)
        self.binSeqLen = math.ceil(math.log2(numCompLetters))

    def generateCompositeLetters(self, numCompLetters, numStrings, stringsLen):
        compositeLetters = []
        while len(compositeLetters) < numCompLetters:
            compLetter = RandomCompositeLetter(numStrings=numStrings,stringsLen=stringsLen)
            if compLetter not in compositeLetters:
                compositeLetters.append(compLetter)
        return compositeLetters

    def getByBinaryIndex(self, binaryIndex):
        index = int(binaryIndex, 2)
        if index < self.numCompLetters:
            return self.compositeLetters[index]
        else:
            raise IndexError("Binary index out of range")

    def getBinaryIndex(self, compositeLetter):
        if(compositeLetter not in self.compositeLetters):
            raise ValueError("Composite letter: "+ str(compositeLetter.strings) + " not in the list: " + str([c.strings for c in self.compositeLetters]))
        index = self.compositeLetters.index(compositeLetter)
        return bin(index)[2:].zfill(self.binSeqLen)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.numCompLetters:
            result = self.compositeLetters[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def printAll(self):
        for i in range(self.numCompLetters):
            binaryIndex = bin(i)[2:].zfill(self.binSeqLen)
            print("0b" + binaryIndex)
            letterAtIndex =self.getByBinaryIndex(binaryIndex)
            print(letterAtIndex.strings)
            assert self.getBinaryIndex(letterAtIndex) == binaryIndex
    