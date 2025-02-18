def caesarCipher(s, k):
    # Write your code here
    s=list(s)
    for i in range(len(s)):
        if not s[i].isalpha():
            continue
        elif 65<=ord(s[i])<=90:
            if ord(s[i])+k<=90:
                s[i]=chr(ord(s[i])+k)
            else:
                s[i]=chr(((ord(s[i]))-65+k)%26+65)
        elif 97<=ord(s[i])<=122:
            if ord(s[i])+k<=122:
                s[i]=chr(ord(s[i])+k)
            else:
                s[i]=chr(((ord(s[i]))-97+k)%26+97)
    s=''.join(i for i in s)
    return s
s="ABCDEF792%$#@qiwfbqfb AFVaifbi"
k=1
print(caesarCipher(s,k))
