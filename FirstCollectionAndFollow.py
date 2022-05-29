'''
author:xiesunsun
date:5-13-9:08
descrption:find all character's First collection and specific GM's FOLLOW set
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
        self.Follow = defaultdict(set)  # store all char's follow collection
        self.First = defaultdict(set)  # store all char 's first collection
        self.initalAlpha = None
        self.NT = []
        self.T = []
        self.SetIntialAlpha()
        self.AddProduction()
        self.getALLNT()
        self.getAllT()
        self.GetAllFirst()
        self.getAllFollow()

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

    def getAllFollow(self):
        '''这个不动点算法有点东西的'''
        for i in self.NT:
            self.Follow[i].add('#')
        # self.Follow[self.initalAlpha].add('#') #迭代的过程我们会遇到这个东西吗,不会遇到的起始符号，我们只会在相应的production的左侧出现的
        old = {}
        while old != self.Follow:  # 不动点算法的标准起势
            old = deepcopy(self.Follow)
            for key in self.production:
                for j in self.production[key]:  # 一值多键的可能性
                    temp = []
                    temp.extend(self.Follow[key])
                    length = len(j)
                    for i in range(length):  # 注意我们需要的是到倒序
                        if j[length-i-1] in self.NT:
                            # 注意这一段话的逻辑问题
                            self.Follow[j[length-i-1]
                                        ].update(set(temp).union(self.Follow[j[length-i-1]]))
                            if '$' in self.First[j[length-i-1]]:
                                # 修正相应的temp迭代项目
                                temp.extend(
                                    self.First[j[length-i-1]]-set(['$']))
                            else:
                                # 修正相应的temp迭代项目
                                temp = self.First[j[length-i-1]]
                        else:
                            # 终结符号的情况我们直接赋值修原始项目
                            temp = self.First[j[length-i-1]]


if __name__ == '__main__':
    g = Gramma()
    print(g)
    print(g.NT, g.T)
    print(g.First)
    print(g.Follow)
