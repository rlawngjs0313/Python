import sys
import time
import pyautogui as pa
import pydirectinput

cnt = 0

while True:
    while True:
        match = pa.locateCenterOnScreen('macro/matching.png')
        if match:
            pa.click(match)
            break
    while True:
        accept = pa.locateCenterOnScreen('macro/matching_okay.png')
        if accept:
            pa.click(accept) # 매칭
        loading = pa.locateCenterOnScreen('macro/loading.png')
        if loading:
            break
    time.sleep(630)
    while True:
        L = pa.locateCenterOnScreen('macro/esc.png')
        if L:
            pydirectinput.click(L[0], L[1])
        one = pa.locateCenterOnScreen('macro/surrender.png')
        if one:
            pydirectinput.click(one[0], one[1])
            break
    while True:
        two = pa.locateCenterOnScreen('macro/surrender_okay.png')
        if two:
            pydirectinput.click(two[0], two[1]) 
            break #서렌
    while True:
        reset = pa.locateCenterOnScreen('macro/reset.png')
        if reset:
            pa.click(reset)
            break #리셋
    match, accept, timer, reset, one, two, L, loading = 0, 0, 0, 0, 0, 0, 0, 0
    sys.stdout.write(f"{cnt}번 \n")