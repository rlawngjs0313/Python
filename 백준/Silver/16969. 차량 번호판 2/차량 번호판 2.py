s=input()
if  s[0]=='d': ans=10
if s[0]=='c' : ans=26
for i in range(1, len(s)) :
    if s[i] == 'd' :
        if s[i-1]==s[i]: ans*=9 ;ans%=1000000009
        else: ans*=10 ;ans%=1000000009
    elif s[i] == 'c' :
        if s[i - 1] == s[i]: ans *= 25 ;ans%=1000000009
        else: ans*=26 ;ans%=1000000009
print(ans)