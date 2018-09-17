def hangman(word):
    rletters = list(word)
    board = "_"*len(word)
    print("Slovo: ", " ".join(board))
    wrong = 0
    stages= ["________ ",
             "        | ",
             "|       | ",
             "|       0 ",
             "|      /|\ ",
             "|      / \ "]
    while len(rletters)>0 and wrong<6:
        bukva=input("                     Vvedite bukvu:")
        if bukva in rletters and bukva!="":
            ind=rletters.index(bukva)
            board[ind]=bukva
            print("Verno, vy ugadali bukvu "," ".join(board))
            rletters.remove(bukva)
        else:
            print(stages[wrong])
            wrong+=1
    if len(rletters)==0:
        print("----- You win! ------")
    else:
        print("----- You loose------")

print("Rastet v lesu:")
hangman("trava")






