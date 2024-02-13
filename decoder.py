from composite_letters import AllCompositeLetters, CompositeLetter
from utils import *
import math

class Decoder:
    def __init__(self, inputFileName, numCompLetters=defNumCompLetters, numStrings=defNumStrings, stringsLen=defStringsLen):
        self.inputFileName = inputFileName
        self.numCompLetters = numCompLetters
        self.numStrings = numStrings
        self.stringsLen = stringsLen
        self.allLetters = AllCompositeLetters(numCompLetters, numStrings, stringsLen)

    def decode(self, outputFileName=decodedFileNameBin):
        compOptions = {}
        with open(self.inputFileName, 'rb') as file:
            lines = file.read().decode('utf-8').split('\n')

        for line in lines:
            line = line.strip()  # Remove newline character
            for i in range(0, len(line), self.stringsLen):
                segment = line[i:i+self.stringsLen]
                if i not in compOptions:
                    compOptions[i] = set()
                compOptions[i].add(segment)

        decodedText = ''
        with open(outputFileName, 'w') as file:
            for index, strings in compOptions.items():
                if len(strings) == self.numStrings:
                    compLetter = CompositeLetter(strings)
                    decodedText = self.allLetters.getBinaryIndex(compLetter)
                else:
                    decodedText = '?' * self.allLetters.binSeqLen
                file.write(decodedText)
