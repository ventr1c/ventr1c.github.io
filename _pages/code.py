# file: time,name,num
# average of nums

# file: name, course, score
# 
import os

def avrFile(path):
    nums = []
    with open(path) as fp:
        # get filePointer for the file
        for f in fp.readlines():
            l=f.split(',')
            nums.append(l[2])
        fp.close()
    avr = sum(nums)/len(nums)
    return avr

select * from file 
group by course having avg(score)

def avrScore(path):
    cDict = dict()
    nDict = dict()# nums of students for each course
    with open(path) as fp:
        for f in fp.readlines():
            l = f.split(',')
            if(l[1] not in cDict):
                cDict[l[1]] = l[2]
                nDict[l[1]] = 1
            else:
                cDict[l[1]] += l[2]
                nDict[l[1]] += 1
        fp.close()
    # get average for every course
    for key, _ in enumerate(cDict):
        cDict[key]/=nDict[key]
    return cDict


def main():
    filePath = ''
    avr = avrFile(filePath)
    
if __name__ == "__main__":
    a = main()
    print(a)
    return 0

# student management system
# lecturer: add score
# student: view score