D1 = {"a":"a","b":"b","c":"c","d":"d","e":"e","f":"f","g":"g","h":"h","i":"i","j":"j","k":"k","l":"l","m":"m","n":"n","o":"o","p":"p","q":"q","r":"r","s":"s","t":"t","u":"u","v":"v","w":"w","x":"x","y":"y","z":"z","0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"," ":"\n","A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L","M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z"}
N = int(input())
for i in list(map(str, input().split())):
    D1[i] = "\n"
M = int(input())
for i in list(map(str, input().split())):
    D1[i] = "\n"
K = int(input())
for i in list(map(str, input().split())):
    D1[i] = i
S = int(input())
result = ""
for i, v in enumerate(input()):
    if D1[v] != '\n' or (len(result) != 0 and result[-1] != '\n' and i != S-1):
        result += D1[v]
print(result)