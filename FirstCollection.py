'''
author:xiesunsun
date:5-13-9:08
descrption:find all character's First collection
    1. input cannot solve '|'
    2. cannot find  inital alpha automatically
    3. use '#' represent end of file 
    4. use '$' represent xi
'''
from collections import defaultdict
from copy import deepcopy


class Gramma():
    '''store language's gramma production(CFG)'''

    def __init__(self) -> None:
        self.production = defaultdict(list)  # store production
        self.First = defaultdict(set)  # store all char 's first collection
        self.initalAlpha = None
        self.NT = []
        self.T = []
        self.SetIntialAlpha()
        self.AddProduction()
        self.getALLNT()
        self.getAllT()
        self.GetAllFirst()

    def SetIntialAlpha(self):
        S = input('input inital character\n')
        self.initalAlpha = S

    def __str__(self):
        countnum = 1
        restr = []
        for item in self.production:
            for j in self.production[item]:
                restr.append('('+str(countnum)+')'+':  '+item+':'+j+'\n')
                countnum += 1
        return "".join(restr)

    def AddProduction(self):
        data = input()
        tempdata = data.split(' ')
        print(tempdata)
        for tp in tempdata:
            key, value = tp.split('->')
            self.production[key].append(value)

    def getALLNT(self):
        self.NT.extend(list(self.production.keys()))

    def getAllT(self):
        data = list(self.production.values())
        temp = set()
        for item in data:
            for i in "".join(item):
                print(i)
                if i not in self.NT:
                    temp.add(i)
        self.T = list(temp)

    def GetAllFirst(self):
        countnum = 1

        for i in self.T:
            self.First[i].add(i)

        self.First['#'].update(['$', '#'])  # use # represent EOF
        self.First['$'].update(['$', '#'])  # use $ represent \xi
        #？？？？？
        for i in self.NT:
            self.First[i].add('#')  # use $ represent \xi
        old1 = {}
        while old1 != self.First:
            print(f"第{countnum}次运行")
            countnum += 1
            old = deepcopy(self.First)  # 进行每次的迭代处理操作
            old1 = deepcopy(self.First)  # 用来判断是否会退出

            for i in self.production:
                temp = []  # discovery each element
                for j in self.production[i]:  # 别忘了存在一键多值的情况存在的
                    old[j[0]].discard('$')  # 大致完成了 但是这个 old1的判断一点都不完美
                    temp.extend(old[j[0]])

                    n = 0
                    while n <= len(j)-2 and '$' in self.First[j[n]]:
                        old[j[n+1]].discard('$')
                        temp.extend(old[j[n+1]])
                        n += 1
                    if n == len(j)-1 and '$' in self.First[j[n]]:
                        temp.extend(['$'])
                temp.extend(list(self.First[i]))
                self.First[i].update(temp)


if __name__ == '__main__':
    g = Gramma()
    print(g)
    print(g.NT, g.T)
    print(g.First)
