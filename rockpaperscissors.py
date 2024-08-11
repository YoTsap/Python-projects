with open('rockpapsci.txt') as f:
    lines = f.read().splitlines()


def is_draw(yo,elf):
    if elf== "A" and yo=="X":
        return True
    elif elf=="B" and yo== "Y":
        return True
    elif elf== "C" and yo=="Z":
        return True
    else:
        return False

def is_win(yo,elf):
    if elf == "A" and yo == "Y":
        return True
    elif elf== "B" and yo == "Z":
        return True
    elif elf=="C" and yo== "X":
        return True
    else:
        return False


def is_win(result):
    return result == "Z"


def is_draw(result):
    return result == "Y"


def calculate_tool_score(tool):
    if tool=="X":
        return 1
    elif tool== "Y":
        return 2
    elif tool =="Z":
        return 3

def calculate_yo_for_draw(elf):
    if elf == "C":
        return "Z"
    elif elf == "B":
        return "Y"
    else:
        return "X"


def calculate_yo_for_win(elf):
    if elf == "C":
        return "X"
    elif elf == "B":
        return "Z"
    else:
        return "Y"


def calculate_yo_for_lose(elf):
    if elf == "C":
        return "Y"
    elif elf == "B":
        return "X"
    else:
        return "Z"


def calculate_yo_selection(elf,result):
    if is_draw(result):
        return calculate_yo_for_draw(elf)
    if is_win(result):
        return calculate_yo_for_win(elf)
    else:
        return calculate_yo_for_lose(elf)



score=0
for game in lines:

    elf,result = game.split(" ")

    if is_draw(result):
        score+=3
    elif is_win(result):
        score+=6
    score= score + calculate_tool_score(calculate_yo_selection(elf,result))

print(score)


