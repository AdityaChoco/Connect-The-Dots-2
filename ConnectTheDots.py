import pgzrun, random, pyautogui
from time import time

WIDTH,HEIGHT=pyautogui.size()
TITLE="Connect The Dots"
fish_points = [
    (100, 400),
    (220, 300),
    (340, 250),
    (460, 300),
    (580, 250),
    (580, 400),
    (580, 550),
    (460, 500),
    (340, 550),
    (220, 520),
    (140, 460),
    (120, 380)
]
# fish_points = [
#     (100, 400),
#     (160, 360),
#     (220, 320),
#     (280, 290),
#     (340, 260),
#     (400, 270),
#     (460, 300),
#     (520, 260),
#     (580, 270),
#     (640, 320),
#     (700, 360),
#     (800, 400),   # tail tip
#     (700, 440),
#     (640, 480),
#     (580, 520),
#     (520, 540),
#     (460, 520),
#     (400, 500),
#     (340, 540),
#     (280, 520),
#     (220, 480),
#     (160, 440),
#     (120, 420),
#     (100, 400)
# ]

next_fish=0
start_time=0
end_time=0
total_time=0
total_fish=len(fish_points)
lines=[]
dots=[]
game_state="start"
for i in range(len(fish_points)):
    fish=Actor("fishy.png")
    fish.pos=fish_points[i]
    dots.append(fish)

def draw():
    global total_time
    screen.clear()
    for i in range(len(dots)):
        dots[i].draw()
        screen.draw.text(str(i+1),(dots[i].pos))
    for line in lines:
        screen.draw.line(line[0],line[1],"White")
    screen.draw.text(f"next fish to connect is {next_fish+1}",(WIDTH*2/3-125,HEIGHT/2-75),fontsize=60)
    if next_fish<total_fish:
        total_time=time()-start_time
    total_time=round(total_time,0)
    screen.draw.text(f"Timer:{total_time}",(20,20))

def update():
    pass
def on_mouse_down(pos):
    global next_fish,lines,start_time,game_state
    if game_state=="start":
        game_state="playing"
        start_time=time()
    if next_fish<total_fish:
        if dots[next_fish].collidepoint(pos):
            if next_fish:
                lines.append((dots[next_fish].pos,dots[next_fish-1].pos))
            next_fish+=1
        else:
            lines=[]
            next_fish=0





pgzrun.go()