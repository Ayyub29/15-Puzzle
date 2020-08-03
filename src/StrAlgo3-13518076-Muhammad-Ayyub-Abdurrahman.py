# Muhammad Ayyub Abdurrahman
# 13518076 / K-1 / Tugas Kecil 3 Strategi Algoritma
# Penyelesaian 15-Puzzle dengan Algoritma Branch and Bound

import time
from copy import deepcopy

class Puzzle:
    # def const
    def __init__(self):
        self.data = []
        self.level = 0
        self.number = 1
        self.position = 'root'
        self.parent = 0

    def __eq__(self, puzzle):
        same = True
        for i in range (0,16):
            if (self.data[i] != puzzle.data[i]):
                same = False
        return same

    #setter
    def setData(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
        self.data = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]

    def setLevel(self, Nlevel):
        self.level = Nlevel

    def setNumber(self, NNumber):
        self.number = NNumber

    def setPosition(self, NPosition):
        self.position = NPosition
    
    def setParent(self, NParent):
        self.parent = NParent
    #getter
    def getLevel(self):
        return self.level
    
    def getNumber(self):
        return self.number

    def getPosition(self):
        return self.position

    def getParent(self):
        return self.parent

    def printPuzzle(self):
        print("branch number : " + str(self.getNumber()))
        print("parent : " + str(self.getParent()))
        print("position : " + self.getPosition())
        print("cost : " + str(self.countCost()))
        print("level : " + str(self.getLevel()))
        for i in range (0, 16, 4):
            if (self.data[i] == 0):
                print(" " + "\t" + str(self.data[i + 1]) + "\t" + str(self.data[i + 2]) + "\t" + str(self.data[i + 3]))
            elif(self.data[i+1] == 0):
                print(str(self.data[i]) + "\t" + " " + "\t" + str(self.data[i + 2]) + "\t" + str(self.data[i + 3]))
            elif(self.data[i+2] == 0):
                print(str(self.data[i]) + "\t" + str(self.data[i + 1]) + "\t" + " " + "\t" + str(self.data[i + 3]))
            elif(self.data[i+3] == 0):
                print(str(self.data[i]) + "\t" + str(self.data[i + 1]) + "\t" + str(self.data[i + 2]) + "\t" + " ")
            else:
                print(str(self.data[i]) + "\t" + str(self.data[i + 1]) + "\t" + str(self.data[i + 2]) + "\t" + str(self.data[i + 3]))
        print(" ")

    def posisi(self, x):
        i = 0
        while (self.data[i] != x):
            i += 1
        return i+1

    def fungsiKurang(self, x):
        result = 0
        for j in range(1,x):
            if (self.posisi(j) > self.posisi(x % 16)):
                result += 1
        return result

    def sumFungsiKurang(self):
        result = 0
        for i in range(1,17):
            result += self.fungsiKurang(i)
        return result

    def nilaiX(self):
        if ((self.posisi(0) == 2) or (self.posisi(0) == 4) or (self.posisi(0) == 5) or (self.posisi(0) == 7) or (self.posisi(0) == 10) or (self.posisi(0) == 12) or (self.posisi(0) == 13) or (self.posisi(0) == 15)):
            X = 1
        else:
            X = 0
        return X

    def Solvable(self):
        return (((self.sumFungsiKurang() + self.nilaiX()) % 2) == 0)
    
    def Solved(self):
        return (self.sumFungsiKurang() == 0)

    def countCost(self):
        result = 0
        for i in range(0,16):
            if (self.data[i % 16] != (i + 1)):
                result += 1
        return result + self.getLevel()

    def NilaiPosisiAtas(self):
        if (self.posisi(0) <= 4):
            return -1
        else:
            return self.data[self.posisi(0) - 5]
    
    def NilaiPosisiBawah(self):
        if (self.posisi(0) >= 13):
            return -1
        else:
            return self.data[self.posisi(0) + 3]
    
    def NilaiPosisiKiri(self):
        if ((self.posisi(0) % 4) == 1):
            return -1
        else:
            return self.data[self.posisi(0)-2]

    def NilaiPosisiKanan(self):
        if ((self.posisi(0) % 4) == 0):
            return -1
        else:
            return self.data[self.posisi(0)]

    def tukarPosisi(self, a, b):
        if (b != -1):
            temp = 0
            posA = self.posisi(a) - 1
            posB = self.posisi(b) - 1
            temp = self.data[posA]
            self.data[posA] = self.data[posB]
            self.data[posB] = temp

    def swipe(self, kemana):
        if (kemana == 'a'):
            self.tukarPosisi(0,self.NilaiPosisiKiri())
        elif (kemana == 'w'):
            self.tukarPosisi(0,self.NilaiPosisiAtas())
        elif (kemana == 's'):
            self.tukarPosisi(0,self.NilaiPosisiBawah())
        elif (kemana == 'd'):
            self.tukarPosisi(0,self.NilaiPosisiKanan())

class ListPuzzle:
    def __init__(self):
        self.data = []

    def minCost(self): 
        result = self.data[0]
        x = len(self.data)
        for i in range(0,x):
            if (result.countCost() >= self.data[i].countCost()):
                result = self.data[i]
        return result

    def printPuzzleList(self): 
        i = 1
        for items in self.data:
            print("Langkah ke- " + str(i))
            i += 1
            items.printPuzzle()

def isInside(puzzle,List): 
        result = False
        if any(items == puzzle for items in List.data):
            result = True
        return result

def Solve(puzzle):
    puzzleList = ListPuzzle() #mencatat branch yang aktif
    solutionList = ListPuzzle() #mencatat langkah solusi
    branchActivatedList = ListPuzzle() #mencatat semua branch yang pernah dibangkitkan
    countNumber = 1    
    if (not puzzle.Solvable()):
        print("Puzzle ini tidak dapat diselesaikan \n")
    else:
        print("Puzzle dapat diselesaikan")
        puzzleList.data.append(puzzle)
        branchActivatedList.data.append(puzzle)
        countNumber += 1
        # puzzleList.printPuzzleList()
        while (not (len(puzzleList.data) == 0)):
            temp = puzzleList.minCost()
            # temp.printPuzzle()
            # puzzleList.printPuzzleList()
            if (not temp.Solved()):
                tempUp = deepcopy(temp)
                tempUp.setLevel(temp.level+1)
                tempUp.setParent(temp.getNumber())
                tempUp.swipe('w')
                # print("Hasil Swipe up \n")
                # tempUp.printPuzzle()

                tempRight = deepcopy(temp)
                tempRight.setLevel(temp.level+1)
                tempRight.setParent(temp.getNumber())
                tempRight.swipe('d')
                # print("Hasil Swipe Right \n")
                # tempRight.printPuzzle()

                tempDown = deepcopy(temp)
                tempDown.setLevel(temp.level+1)
                tempDown.setParent(temp.getNumber())
                tempDown.swipe('s')
                # print("Hasil Swipe Down \n")
                # tempDown.printPuzzle()

                tempLeft = deepcopy(temp)
                tempLeft.setLevel(temp.level+1)
                tempLeft.setParent(temp.getNumber())
                tempLeft.swipe('a')
                # print("Hasil Swipe Left \n")
                # tempLeft.printPuzzle()
                
                if ((not isInside(tempUp,branchActivatedList))):
                    puzzleList.data.append(tempUp)
                    branchActivatedList.data.append(tempUp)
                    tempUp.setNumber(countNumber)
                    tempUp.setPosition('Up')
                    countNumber += 1
                if ((not isInside(tempRight,branchActivatedList))):
                    puzzleList.data.append(tempRight)
                    branchActivatedList.data.append(tempRight)
                    tempRight.setNumber(countNumber)
                    tempRight.setPosition('Right')
                    countNumber += 1
                if ((not isInside(tempDown,branchActivatedList))):
                    puzzleList.data.append(tempDown)
                    branchActivatedList.data.append(tempDown)
                    tempDown.setNumber(countNumber)
                    tempDown.setPosition('Down')
                    countNumber += 1
                if ((not isInside(tempLeft,branchActivatedList))):
                    puzzleList.data.append(tempLeft)
                    branchActivatedList.data.append(tempLeft)
                    tempLeft.setNumber(countNumber)
                    tempLeft.setPosition('Left')
                    countNumber += 1
                puzzleList.data.remove(temp)
                # print("Hasil dari pembangkitan dari temp adalah")
                # puzzleList.printPuzzleList()
                # print("List Baru adalah")
                # puzzleList.printPuzzleList()
            else:
                break
                

        if (not (len(puzzleList.data) == 0)):
            print("Untuk menyelesaikan puzzle, Simpul dihidupkan sebanyak " + str(len(branchActivatedList.data)) + " buah")
            print("jadi, solusinya adalah sebagai berikut: \n")
            solutionList.data.append(temp)
            while (temp.getPosition() != 'root'):
                for items in branchActivatedList.data:
                    if (items.getNumber() == temp.getParent()):
                        solutionList.data.append(items)
                        temp = deepcopy(items)
                        break
            solutionList.data.reverse()
            solutionList.printPuzzleList()
            print('Solusi ditemukan!')
        else:
            print('Solusi tidak ditemukan!') 
   
def readPuzzle(text_file_name, puzzle):
    f=open(text_file_name,"r")
    lines=f.read().splitlines()
    input=[]
    for x in lines :
        temp=x.split(  )
        temp1= list(map(int, temp))
        input.append(temp1)
    f.close()
    puzzle.data = input[0] + input[1] + input[2] + input[3]

def main():
    TC1 = Puzzle()

    readPuzzle("testcase1.txt", TC1)

    start_time = time.time()
    print("---Pengujian TC 1---")
    TC1.printPuzzle()
    print("Fungsi Kurang tiap-tiap elemen pada TC 1 adalah")
    for i in range (1,17):
        print(str(i) + " = " + str(TC1.fungsiKurang(i)))
    print(TC1.nilaiX())
    print("SumKurang + X = " + str(TC1.sumFungsiKurang() + TC1.nilaiX()))
    print("\n")
    Solve(TC1)
    print("--- %s ms ---" % ((time.time() - start_time)*1000))
    print('\n')

       
                
#Algoritma Utama
main()
         
            


                            

                            











    







