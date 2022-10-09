import sys
import time
import pyautogui as pa

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
            break
    pa.click(accept) # 매칭
    time.sleep(610)
    while True:
        L = pa.locateCenterOnScreen('macro/esc.png')
        if L:
            pa.click(L)
            one = pa.locateCenterOnScreen('macro/surrender.png')
        if one:
            pa.click(one)
            break
    while True:
        two = pa.locateCenterOnScreen('macro/surrender_okay.png')
        if two:
            pa.click(two) 
            break #서렌
    while True:
        reset = pa.locateCenterOnScreen('macro/reset.png')
        if reset:
            pa.click(reset)
            break #리셋
    match, accept, timer, reset, one, two = 0, 0, 0, 0, 0, 0
    sys.stdout.write(f"{cnt}번 \n")