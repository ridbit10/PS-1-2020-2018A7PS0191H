with open("text.txt",'r',encoding='utf-8') as f:
    s=f.read()
    ss = set(s.split())
    wrd = input()
    if wrd in ss:
        print("Word found")
    else:
        print("Word not found")
