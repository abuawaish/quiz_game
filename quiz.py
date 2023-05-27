def quize_game():
    print("\nwelcome to quiz  game!!")
    user = input("\nDo you wanna play? ")
    score = 0
    if user.lower() not in ["yes","y"] or user.lower() in ["no","n"]:
        print("please tap \"yes\" or \"y\" to play ! ")
        exit()
    print("\nLet's play!")
    q = input("\nwhat CPU stand for? ")
    if q.lower() == "central processing unit":
        print("correct!")
        score += 1
    else:
        print("not correct!")
    q2 = input("\nwhat URL stand for? ")
    if q2.lower() == "uniform resource locator":
        print("correct!")
        score += 1
    else:
        print("not correct!")
    q3 = input("\nwhat ALU stand for? ")
    if q3.lower() == "arithmetic logic unit":
        print("correct!")
        score += 1
    else:
        print("not correct!")
    q4 = input("\nwhat RAM stand for? ")
    if q4.lower() == "random access memory":
        print("correct!")
        score += 1
    else:
        print("not correct!")
    q5 = input("\nwhat BIOS stand for? ")
    if q5.lower() == "basic input output system":
        print("correct!")
        score += 1
    else:
        print("not correct!")
    q6 = input("\nwhat MAC stand for? ")
    if q6.lower() == "media access control":
        print("correct!")
        score += 1
    else:
        print("not correct!")
    print("\nyou got {} score".format(score),end="\n")
    print("\nAnd your total percentage is {}%".format(int(score/6*100)),end="\n")

if __name__=="__main__":
    quize_game()
