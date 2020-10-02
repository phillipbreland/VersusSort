import csv
import sys
from pathlib import Path

def main():
    ranked_list = []
    print(sys.path[0])
    print("\nEnter input file name:")
    inputFile = input()
    print("\nEnter output file name (will append .csv, will overwrite if file of same name exists):")
    outputFile = input()
    print("\nVote for the better song (1st or 2nd) with '1' or '2':\n")

    with open(Path(sys.path[0])/inputFile) as f:
        ranked_list.append(f.readline().strip())
        for line in f:
            temp = line.strip()
            userInput = ''
            low = 0
            high = len(ranked_list)-1
            currIndex = (low+high)//2

            while high>=low:
                print(temp, "or", ranked_list[currIndex])
                userInput = input()
                if(userInput == '1'):
                    high = currIndex-1
                    if(high<low):
                        break
                    currIndex = (low+high)//2
                elif(userInput == '2'):
                    low = currIndex+1
                    if(high<low):
                        break
                    currIndex = (low+high)//2
            
            ranked_list.insert(low, temp)
            with open(Path(sys.path[0])/(outputFile+'.csv'), 'w', newline ='') as fOut: 
                write = csv.writer(fOut)
                for i, row in enumerate(ranked_list):
                    write.writerow([i+1, row])

    print(ranked_list)
    print("\nOutput written to .csv, press 'Enter' to exit...")
    input()

if __name__=="__main__":
    main()
