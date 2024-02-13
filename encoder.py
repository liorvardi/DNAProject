from composite_letters import AllCompositeLetters
import random
import math
from utils import *
class Encoder:
    def __init__(self, filename, numCompLetters=defNumCompLetters, numStrings=defNumStrings, stringsLen=defStringsLen):
        self.filename = filename
        self.numCompLetters = numCompLetters
        self.numStrings = numStrings
        self.stringsLen = stringsLen
        self.encodedSegments = self.getAllEncodeOptions()

    def getAllEncodeOptions(self):
        with open(self.filename, 'rb') as file:
            binaryText = file.read().decode('utf-8')

        allLetters = AllCompositeLetters(self.numCompLetters, self.numStrings, self.stringsLen)

        binLen = int(math.log2(self.numCompLetters))
        segments = [binaryText[i:i+binLen] for i in range(0, len(binaryText), binLen)]

        encodedSegments = []
        for segment in segments:
            compLetter = allLetters.getByBinaryIndex(segment)
            encodedSegments.append(compLetter)

        return encodedSegments

    def buildRandomString(self):
        result = ''
        for segment in self.encodedSegments:
            randomString = random.choice(segment.strings)
            result += randomString

        return result
    
    def encode(self, multiplicity, toEncodeFileName):
        with open(toEncodeFileName, 'w') as file:
            for i in range(multiplicity):
                randomString = self.buildRandomString()
                file.write(randomString )


