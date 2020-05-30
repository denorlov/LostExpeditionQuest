log = '''
Вперед, Вперед, Вперед, Вперед, Вперед, Вперед, Вправо, Вперед, Вперед, Вперед, Вправо, Вперед,
Вправо,

Вперед, Вперед, Влево, Вперед, Вперед, Вперед, Вперед, Вперед, Вперед, Влево, Вперед, Влево,
Вперед, Вперед, Вперед, Вперед, Вперед, Вправо, Вперед, Влево, Вперед, Влево

Вперед, Вперед, Влево, Вперед, Вперед, Вперед, Вперед, Вперед, Вперед, Влево, Вперед, Влево,
Вперед, Вперед, Вперед, Вперед, Вперед, Вправо, Вперед, Влево, Вперед, Влево

Вперед, Вперед, Влево, Вперед, Вперед, Вперед, Вперед, Вперед, Вперед, Влево, Вперед, Влево,
Вперед, Вперед, Вперед, Вперед, Вперед, Вправо, Вперед, Влево, Вперед, Влево

Вправо, Вперед, Вперед, Вперед, Вперед,
Влево, Вперед, Вперед, Вправо, Вперед, Вперед, Вправо, Вперед, Влево,
Вперед, Вправо, Вперед, Вправо,
Вперед, Вперед, Вперед, Вперед, Вперед, Вперед, Вперед,

Вперед, Вперед, Вперед, Вправо, Вперед, Влево,
Вперед, Вперед, Вперед, Вперед, Вперед, Вперед, Вперед,
Влево,
Вперед, Вправо, Вперед, Вправо, Вперед, Вперед, Влево,
Вперед, Вперед,
Вправо, Вперед,
Влево, Вперед,
Влево, Вперед,
Вправо, Вперед,
Вперед, Вправо,
Вперед,
Влево,
Вперед,
Влево, Вперед, Вперед,
Влево, Вперед, Вперед,
Вправо, Вперед,
Влево, Вперед,
Вперед, Вперед, Вперед, Вперед, Вперед, Вперед,
Вперед, Вперед, Вперед, Вперед, Вперед, Вперед,
Вперед, Вперед,

Влево,

Вперед, Вперед, Влево, Вперед, Вперед, Вперед, Вперед, Вперед, Вперед, Влево, Вперед, Влево,
Вперед, Вперед, Вперед, Вперед, Вперед, Вправо, Вперед, Влево, Вперед, Влево

'''
log1=log.replace('\n',' ')
log2=log1.replace(',',' ')
loga=log2.split()

map = ''' 
лхирфбвэзидсэгвйлхфтэйэттмптэчсжыжлч
нмшсбрвъзивжматфьтзсшчжыщэршзбойммпх
лчсниуэтрымчюэлорзюннвючеаычюнхйвмйи
йбсьозпьюэчдгмьмгепьенукхшклтвчиущше
'''

ppos=[0,0]
ddir=[0,0]
ddd=0
day=0

mapmap = map.split('\n')

n = 4
m = 36
ma = [[''] * m for i in range(n)]
for i in range(1,5):
    mama=mapmap[i]
    for j in range(36):
        ma[i-1][j]=mama[j]


def dirdir():
    global ddir
    global ddd
    if ddd==0: ddir=[-1,0]
    elif ddd==1: ddir=[0,1]
    elif ddd==2: ddir=[1,0]
    elif ddd==3: ddir=[0,-1]

def start():
    global ppos
    global ddir
    global ddd
    global day
    ppos=[3,6]
    ddd=3
    dirdir()
    day+=1
    
def forw():
    global ppos
    global ddir
    global day
    ppos[0]=ppos[0]+ddir[0]
    ppos[1]=(ppos[1]+ddir[1])%36
    day+=1

def right():
    global ppos
    global ddir
    global ddd
    ddd=(ddd+1)%4
    dirdir()
    
def left():
    global p0
    global d0
    global ddd
    ddd=(ddd-1)%4
    dirdir()

day=0
start()
res=''
for i in range(len(loga)):
    qq=loga[i]
    if qq=='Старт' : start()
    elif qq=='Вперед' : forw()
    elif qq=='Вправо' : right()
    elif qq=='Влево' : left()
    if (89<=day<89+12) and (qq=='Вперед') :
        res=res+ma[ppos[0]][ppos[1]]

print(res)
    
