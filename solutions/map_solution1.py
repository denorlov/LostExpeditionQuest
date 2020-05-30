map = '''
лхирфбвэзидсэгвйлхфтэйэттмптэчсжыжлч
нмшсбрвъзивжматфьтзсшчжыщэршзбойммпх
лчсниуэтрымчюэлорзюннвючеаычюнхйвмйи
йбсьозпьюэчдгмьмгепьенукхшклтвчиущше
'''
map = map.strip().split("\n")
map1 = [list(row) for row in map]
print(map1)

log = '''
Вперед, Вперед, Вперед, Вперед, Вперед, Вперед, Вправо, Вперед, Вперед, Вперед, Вправо, Вперед, 
Вправо,

Вперед, Вперед, Влево, Вперед, Вперед, Вперед, Вперед, Вперед, Вперед, Влево, Вперед, Влево,
Вперед, Вперед, Вперед, Вперед, Вперед, Вправо, Вперед, Влево, Вперед, Влево
'''
log = log.replace(",", "")
log = log.strip().split()
log = [w.strip() for w in log]

direction = "лево"
x, y = 6, 3
day = 1

print(f"день: {day}, x,y={(x, y)}, direction={direction}, letter={map1[y][x]}")

for command in log:
    if "Вперед" == command:
        if direction == "верх":
            y -= 1
        elif direction == "лево":
            x -= 1
            if x < 0:
                x = len(map1[0]) - 1
        elif direction == "право":
            x += 1
            if x == len(map1[0]):
                x = 0
        elif direction == "низ":
            y += 1

        day += 1
        print(f"день: {day}, cmd={command}, x,y={(x, y)}, \tdirection: {direction}, letter={map1[y][x]}")
    else:
        print(f"день: {day}, cmd={command}, \t\t\t\tdirection: {direction} ->", end="")

        if "Влево" == command:
            if direction == "верх":
                direction = "лево"
            elif direction == "лево":
                direction = "низ"
            elif direction == "право":
                direction = "верх"
            elif direction == "низ":
                direction = "право"

        if "Вправо" == command:
            if direction == "верх":
                direction = "право"
            elif direction == "лево":
                direction = "верх"
            elif direction == "право":
                direction = "низ"
            elif direction == "низ":
                direction = "лево"

        print(f" {direction}")


