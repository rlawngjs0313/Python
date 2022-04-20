#202210904_김주헌_rlawngjs

def getNextPeriodPos(txt, startPos):
    txt = txt[startPos:]
    endPos = txt.find(".")
    if endPos == -1:
        return -1
    else:
        return endPos
def getNextLine(txt, startPos):
    if len(txt) <= startPos:
        return ""
    else:
        txt = txt[startPos:txt.find(".")]
        txt = txt.strip()
        return txt
def countWordsInLine(line):
    words = 0
    print(line)
    if line == "":
        return words
    for i in range(0, len(line)):
        if line.find("\n") != -1 or line.find("\t") != -1 or line.find(" ") != -1:
            if line.find("\n") != -1:
                line = line[line.find("\n"):]
                line = line.strip()
                words += 1
            elif line.find("\t") != -1:
                line = line[line.find("\t"):]
                line = line.strip()
                words += 1
            elif line.find(" ") != -1:
                line = line[line.find("\t"):]
                line = line.strip()
                words += 1
    words += 1
    return words
def main(txt):
    txt = txt.strip()
    startPos = 0
    for i in range(0, len(txt)):
        if txt != "":
            txt = getNextLine(txt, startPos)
            print(i, ": ", txt)
            print("words:", countWordsInLine)
            startPos = getNextPeriodPos(txt, startPos)