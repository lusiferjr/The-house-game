class room:
    def __init__(self,n,e,w,s,i,nam):
        self.north=n
        self.east=e
        self.west=w
        self.south=s
        self.item=i
        self.name=nam
    def drop(self,i):
        temp=-1
        for k in self.item:
            temp += 1
            if k==i:
                break
        del self.item[temp]
    def add(self,i):
        self.item.append(i)




class man:
    def __init__(self,m):
        self.current_room=m
        self.item=[]


    def look(self):
        print('North:',end='')
        if d[self.current_room].north is not None:
            print('\t',d[self.current_room].north)
        else:
            print('\t','wall')
        print('South:',end='')
        if d[self.current_room].south is not None:
            print('\t',d[self.current_room].south)
        else:
            print('\t','wall')
        print('East:',end='')
        if d[self.current_room].east is not None:
            print('\t',d[self.current_room].east)
        else:
            print('\t','wall')
        print('West:',end='')
        if d[self.current_room].west is not None:
            print('\t',d[self.current_room].west)
        else:
            print('\t','wall')
        print("Item in room:",end='')
        print('\t',*d[self.current_room].item)
        print('\n\n')

    def pick(self,i):
        temp=d[self.current_room].item[i]
        self.item.append(temp)
        d[self.current_room].drop(i)

    def drop(self,i):
        temp=self.item[i]
        del self.item[i]
        d[self.current_room].add(temp)


    def move(self,i):
            if i=='north' and d[self.current_room].north!=None:
                self.current_room=d[self.current_room].north
            elif i=='east' and d[self.current_room].east!=None:
                self.current_room = d[self.current_room].east
            elif i=='west' and d[self.current_room].west!=None:
                self.current_room = d[self.current_room].west
            elif i=='south' and d[self.current_room].south!=None:
                self.current_room = d[self.current_room].south
    def show_item(self):
        print('item in bag:')
        print(*self.item)
    def show(self):
        print(*d[self.current_room].item)


d={'road':room('park', None, None, None, [], 'road'),
   'park':room('study',None,None,'road',['key','frog','football'],'park'),
   'study':room('bed',None,'draw','park',['book','pen','notebook','notes'],'study'),
   'kitchen':room('bed',None,'draw','park',['knife','apple'],'study'),
   'train':room(None,'bed',None,'draw',['boxing bag','chess'],'train'),
   'draw':room('train','study',None,None,['bottel','sofa'],'draw'),
   'bed':room(None,'kitchen','train','study',['pillow','charger'],'bed'),
   'road':room('park', None, None, None, [], 'road')}

r=man('road')
def move():
    print("""which direction u want to move:
north
south
east
west""")
    x=input()
    r.move(x)
def pick():
    print('dont want to pick a item pass -1')
    print("list of item u can pick")
    r.show()
    x=int(input())
    if x!=-1:
        r.pick(i)
def drop():
    print('dont want to pick a item pass -1')
    print("list of item man has:")
    for i in range(r.item.__len__()):
        print(i,sep='')
        print(r.item[i])
    x=int(input())
    if x!=-1:
        r.drop(x)

while 1:
    print("""enter your choice:
1:look
2:move
3:show item
4:pick
5:drop""")
    x=int(input())
    if x==1:
        r.look()
    elif x==2:
        move()
    elif x==3:
        r.show_item()
    elif x==4:
        pick()
    elif x==5:
        drop()
    else:
        break




    



