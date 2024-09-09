def minion_game(string):
    stuart_scr=0
    kevin_scr=0
    len_str=len(string)
    for i in range(len_str):
        if string[i] not in ['A','E','I','O','U']:
            stuart_scr+=int(len(string[i:]))
        else:
            kevin_scr+=int(len(string[i:]))
    if kevin_scr>stuart_scr:
        print("Kevin",kevin_scr)
    elif kevin_scr<stuart_scr:
        print("Stuart",stuart_scr)
    else:
        print("Draw")
                
u_in=input("Enter the word\n")
minion_game(u_in)