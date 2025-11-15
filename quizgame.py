import pgzrun

WIDTH = 600
HEIGHT = 600

mbox = Rect(0,0,600,60)
qbox = Rect(0,0,450,110)
tbox = Rect(0,0,70,70)
a1box = Rect(0,0,200,100)
a2box = Rect(0,0,200,100)
a3box = Rect(0,0,200,100)
a4box = Rect(0,0,200,100)
sbox = Rect(0,0,70,140)

score = 0
time_left = 10
qfile_name = "C:\\Users\\Hp\\Desktop\\Game Development\\images\\quizgame.txt"
message = ""

game_over = False

abox = [a1box,a2box,a3box,a4box]
ques = []
count = 0
index = 0 
mbox.move_ip(0,0)
qbox.move_ip(20,70)
tbox.move_ip(500,70)
a1box.move_ip(20,200)
a2box.move_ip(300,200)
a3box.move_ip(20,380)
a4box.move_ip(300,380)
sbox.move_ip(500,170)
def draw():
    global message 
    screen.clear()
    screen.fill("orange")
    screen.draw.filled_rect(mbox,"blue")
    screen.draw.filled_rect(qbox,"black")
    screen.draw.filled_rect(tbox,"green")
    screen.draw.filled_rect(sbox,"white")
    for i in abox:
        screen.draw.filled_rect(i,"black")
    message="welcome to quiz master"
    message=message+f"q:{index}of{count}"
    screen.draw.textbox(message,mbox,color="purple")
    screen.draw.textbox(str(time_left),tbox,color="yellow")
    screen.draw.textbox("skip",sbox,color="blue")
    screen.draw.textbox(q[0].strip(),qbox,color="red")
    ix=1
    for i in abox:
        screen.draw.textbox(q[ix].strip(),i,color="yellow")
        ix+=1
def update():
    movem()

def movem():
    mbox.x=mbox.x-2
    if mbox.right < 0:
        mbox.left=WIDTH
        
def readquestion():
    global count, ques
    qfile = open(qfile_name,"r")
    for i in qfile:
        ques.append(i)
        count+=1
    qfile.close()

def next_question():
    global index 
    index+=1 
    return ques.pop(0).split(",")
    
def on_mouse_down(pos):
    ix=1
    for i in abox:
        if i.collidepoint(pos):
            if ix is int(q[5]):     
                correct_answer()
            else:
                gameover()
        ix+=1
    if sbox.collidepoint(pos):
        skipquestion()

def correct_answer():
    global score, q, time_left, ques
    score+=1
    if ques:
        q=next_question()
        time_left=10
    else:
        gameover()

def skipquestion():
    global q, time_left
    if ques and not game_over:
        q= next_question()  
        time_left=10
    else:
        gameover()
        
def gameover():
    global q, time_left, game_over
    message = f"game over you got {score} questions correct" 
    q = [message,"-","-","-","-",5]
    time_left=0
    game_over= True

def updatetimeleft():
    global time_left
    if time_left:
        time_left-=1
    else:
        gameover()

readquestion()
q = next_question()
clock.schedule_interval(updatetimeleft,1)

pgzrun.go()