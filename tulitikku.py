"""
Tulitikkupeli
"""



def main():

            matchsticks = 21
            losercount=1
            import time

            print("\nGame of sticks\n")
            time.sleep(0.5)
            print(str(matchsticks) + " sticks left")
            time.sleep(1)
            
                            
                               
            while True:  
                    while matchsticks>=1:
                        p1 = input("Player 1 enter how many sticks to remove: \n")
                        if p1 == ("1"):
                            matchsticks = matchsticks - 1
                            losercount = losercount - 1


                            if matchsticks <= 0:
                                break
                            print("There are",matchsticks,"sticks left\n")
                        elif p1 == ("2"):
                            matchsticks = matchsticks - 2
                            losercount = losercount - 1


                            if matchsticks <= 0:
                                break
                            print("There are",matchsticks,"sticks left\n")
                        elif p1 == ("3"):
                            matchsticks = matchsticks - 3
                            losercount = losercount - 1


                            if matchsticks <= 0:
                                break
                            print("There are",matchsticks,"sticks left\n")
                        else:
                            print("Must remove between 1-3 sticks!\n")
                            continue

                        if matchsticks<1:
                            break
                        else:""
        
       
                        while True:

            
                            p2 = input("Player 2 enter how many sticks to remove: \n")
             
             
                            if p2 == ("1"):
                                    matchsticks = matchsticks - 1
                                    losercount = losercount + 1

                                    if matchsticks<=0:
                                        break
                                    print("There are",matchsticks,"sticks left\n")
                                    break
                            elif p2 == ("2"):
                                    matchsticks = matchsticks - 2
                                    losercount = losercount + 1

                                    if matchsticks<=0:
                                        break
                                    print("There are",matchsticks,"sticks left\n")
                                    break
                            elif p2 == ("3"):
                                    matchsticks = matchsticks - 3
                                    losercount = losercount + 1

                                    if matchsticks <= 0:
                                        break
                                    print("There are",matchsticks,"sticks left\n")
                                    break
                            else:
                                    print("Must remove between 1-3 sticks!\n")
                                    continue


                    
                                 
             

                    if losercount==1:
                        print("Player 2 lost the game!\n")
                        new_game = input("Do you want to play again?\n Yes or No")
                        if new_game == "yes" or new_game == "Yes" or new_game == "y":
                            main()
                        else:
                            exit()

                    elif losercount==0:
                        print("Player 1 lost the game!\n")
                        new_game = input("Do you want to play again?\n Yes or No\n\n")
                        if new_game == "yes" or new_game == "Yes" or new_game == "y":
                            main()
                        else:
                            exit()

if __name__=="__main__":
    main()