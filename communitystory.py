def start_game():
    print("WELCOME TO THE WALKING BREAD------>You are in AMC'S hit television series The Walking Dead, Season 1 Episode 1 'Days Gone Bye', you see Rick make it out of the hospital and then look down and see you have been bitten, you have hours to live. You can choose to 1->follow him or 2->to go your own way. Pick your choice as the number it corresponds to...")
    startchoices = input("1. Follow the sheriff man Rick | 2. Find your own sick, cool, original path > ")
    print(startchoices)
    if startchoices == "1":
        forest()
    else:
        highway()
def forest():
    print("Rick Grimes is a bad boy, he tears the trail up leaving you half-winded and in his dust. After hours of following him, you see he has made it to a survival camp full of other civilian survivors. You know your wound is only further infecting you. Do you 1->seek medical attention or 2->be tough cookie and keep your mouth shut. ")
    forestchoices = input("1. Bandaids, please! | 2. I am a hard nut to crack > ")
    print(forestchoices)
    if forestchoices == "1":
        print("The survivors all clamor and freak out. They unanimously decide it is more humane to exile you from the camp than to kill you in daylight, so before you leave you cut all of the RV breaklines and puncture holes in the water supplies to inconvinience the people. While in process of exile, before you die you find out you have the killed the entire cast of AMC's The Walking Dead and you sued by the producers for millions of dollars. Luckily you won't be around long enough to pay up ;). Fin. (GAME OVER) ")
        start_game()
    elif forestchoices == "2":
        becomecarldad()
def highway():
    print("HIGHWAY YOU'RE ON A HIGHWAY, ZOMBIES E'RYWERE MON, FIGHT OR FLIGHT,YOUNG BRAVE PROTAGONIST?????")
    livingroomchoices = input("1. Kick zombie butt | 2. No way José! (I don't know that many José's now that I think of it, the ones that I do personally know are actually quite nice and amenable) > ")
    print(livingroomchoices)
    if livingroomchoices == "1":
       print("You cannot ward of the zombies, as you breathe your dying breaths you go to IMBD.com and give AMC's 'The Walking Dead' a 2.4/10 rating along with a snobby review and you pass on the to fabric of the universe. GAME OVER")
       start_game()
    elif livingroomchoices == "2":
        print("You not that guy u died brah GAME OVER")
        start_game()
def killthecast():
    print("The survivors all clamor and freak out. They unanimously decide it is more humane to exile you from the camp than to kill you in daylight, so before you leave you cut all of the RV breaklines and puncture holes in the water supplies to inconvinience the people. While in process of exile, before you die you find out you have the killed the entire cast of AMC's The Walking Dead and you sued by the producers for millions of dollars. Luckily you won't be around long enough to pay up ;). Fin. (GAME OVER)")
def becomecarldad():
    print("You thug it out like a tough cookie. Over the next following hours you feel more ill and Rick's wife has been talking to you for hours. She is unhappy because she is married to Rick, Married because she is lonely and lonely because she is unhappy. She wants you to foster and raise Carl as your own. Rick's time has long sinced passed. I f lines of text I'd prolly say smth abt Shane too. What do you think about them apples? ")
    carldadchoices = input("1. I can raise CARL as one of my own and I will rename him Buffert (he is 14 years of age) | 2. No no no, how could I do something so horrific, so abhorrent, so atrocious, so terribel to the man, the myth and the legend, Rick Grimes himself? Besides he'll probably shoot me if he found out--->")
    print(carldadchoices)
    if carldadchoices == "1":
        print("Yeah, you were shot and killed by Rick.... moron. GAME OVER")
        start_game()
    elif carldadchoices == "2":
        print("Passed up the offer, Rick's wife was very displeased and cried a little and then a lot. You sat at the campfire with Rick hours afraid that he had suspected something and before you can open your mouth to defend yourself, he hands you a cooked hot dog. You then uncontrllabley tremble, vomit, and even release gas and before you can say the phrase: 'it's a zombie outbreak' you bit into Rick's face, killing him. Hey, maybe being a ghoul isn't so bad, at least now you aren't expected to smell good or have nice inviting words for having a cup of tea with your bro or girlie. GAME OVER")
    start_game()


start_game()