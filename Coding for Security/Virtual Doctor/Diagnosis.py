# Modules

from sklearn import tree
from time import sleep
import time
import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./30)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ascii Banner

sleep(1./8), print('\033[1;34m'+"\t           __  ___               "+'\033[1;m')
sleep(1./8), print('\033[1;34m'+"\t   \  / | |__)  |  |  |  /\  |   "+'\033[1;m')
sleep(1./8), print('\033[1;34m'+"\t    \/  | |  \  |  \__/ /~~\ |__ "+'\033[1;m')
sleep(1./8), print('\033[1;34m'+"\t    __   __   __  ___  __   __   "+'\033[1;m')
sleep(1./8), print('\033[1;34m'+"\t   |  \ /  \ /  `  |  /  \ |__)  "+'\033[1;m')
sleep(1./8), print('\033[1;34m'+"\t   |__/ \__/ \__,  |  \__/ |  \  \n"+'\033[1;m')
slowprint(('\033[1;30m'"┕━━━━━━━━━━━━━━━━ "'\033[1;m') + ('\033[37m'"Am I healthy?"'\033[0m') + ('\033[1;30m'" ━━━━━━━━━━━━━━━━┙"'\033[1;m\n'))

slowprint('\033[1;36m'+"SELECT AN OPTION:"+'\033[m')
slowprint(('\033[34m'+"[ "+'\033[m') + ('\033[37m'+"1"+'\033[m') + ('\033[34m'+" ]"+'\033[m') + (" Do I have Diabetes?"))
slowprint(('\033[34m'+"[ "+'\033[m') + ('\033[37m'+"2"+'\033[m') + ('\033[34m'+" ]"+'\033[m') + (" Diabetic Symptom Test"))
slowprint(('\033[34m'+"[ "+'\033[m') + ('\033[37m'+"3"+'\033[m') + ('\033[34m'+" ]"+'\033[m') + ('\033[31m'+" Exit"+'\033[1;m\n'))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Code

try:

    act = int(input("➤ "))
    if act == 1:
        
        slowprint(('\033[1;30m'"\n┕━━━━━━━━━━━━━ "'\033[1;m') + ('\033[37m'"Do I have Diabetes?"'\033[0m') + ('\033[1;30m'" ━━━━━━━━━━━━━┙"'\033[1;m\n'))
        slowprint('\033[1;36m'+"ANSWER:"+'\033[m')
        
        features = [                                                                          # [[0],[1],[2]]
            [99, 139, 199], [68, 120, 105], [74, 105, 124], [81, 140, 100], [110, 98, 120],   # [0] - Fasting
            [76, 129, 184], [82, 106, 146], [94, 131, 189], [103, 127, 97], [101, 138, 84],   # [1] - Post-overload
            [90, 120, 132], [55, 110, 129], [100, 50, 120], [80, 130, 140], [70, 140, 112],   # [2] - Daily

            [115, 183, 143], [115, 182, 189], [117, 177, 146], [126, 190, 186], [111, 199, 145],
            [100, 140, 199], [120, 200, 155], [115, 189, 155], [110, 175, 160], [100, 168, 150],
            [101, 145, 156], [110, 160, 189], [120, 180, 135], [119, 187, 173], [108, 174, 149],

            [127, 202, 202], [130, 250, 210], [140, 220, 251], [150, 265, 290], [182, 296, 320],
            [130, 250, 200], [147, 237, 200], [150, 500, 250], [150, 290, 210], [125, 450, 250],
            [200, 200, 200], [200, 250, 200], [130, 179, 251], [127, 201, 201], [182, 200, 320],
            ]

        labels = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   # [0] - Normal Glucose Level
                  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,   # [1] - Decreased Glucose Tolerance
                  2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]   # [2] - Very High Blood Glucose Levels

        classif = tree.DecisionTreeClassifier()
        classif.fit(features, labels)
        a = int(input("• What is your glucose level during fasting? "))
        b = int(input("• What is your post-overload glucose level? "))
        c = int(input("• Normally, what is your glucose level? "))

        if (a or b or c) < 55:
            print('\n'+'\033[1;31m'+"➤"+'\033[m'+' Values are below normal!')
        
        x = classif.predict([[a, b, c]])
        if x == 0:
            print('\n'+'\033[1;32m'+"➤"+'\033[m'+' Your blood glucose level is normal.')
        elif x == 1:
            print('\n'+'\033[1;33m'+"➤"+'\033[m'+' You have decreased glucose tolerance.')
        else:
            print('\n'+'\033[1;31m'+"➤"+'\033[m'+' You have been diagnosed with Diabetes Mellitus.')
        print("\nBe aware that this program does not present the definitive diagnosis!\nConsult a specialist doctor to analyze your health.")

    elif act == 2:

        slowprint(('\033[1;30m'"\n┕━━━━━━━━━━━━ "'\033[1;m') + ('\033[37m'"Diabetic Symptom Test"'\033[0m') + ('\033[1;30m'" ━━━━━━━━━━━━┙"'\033[1;m\n'))
        slowprint('\033[1;36m'+"SELECT THE MATCHING SYMPTOMS:"+'\033[m')

        questions = [" Urinate (pee) a lot, often at night? ", " Are very thirsty? ", " Lose weight without trying? ", " Are very hungry? ", " Have blurry vision? ", " Have numb or tingling hands or feet? ", " Feel very tired? ", " Have very dry skin? ", " Have sores that heal slowly? ", " Have more infections than usual? "]
        positive = ["y", "yes"]
        resultado = 0

        for q in questions:

            answer = input(('\033[34m'+"["+'\033[m') + ('\033[37m'+"+"+'\033[m') + ('\033[34m'+"]"+'\033[m') + (f" {q} "))
            answer = answer.lower()
            if answer in positive:
                resultado+=1

        if resultado <= 3:
            print('\n'+'\033[1;31m'+"➤"+'\033[m'+" Don't worry, it's probably not a diabetes diagnosis.\nBut it's always good to see the doctor!")

        elif resultado <= 4 and resultado > 7:
            print('\n'+'\033[1;31m'+"➤"+'\033[m'+" Your health may be compromised.\nTake proper care and if possible, consult a doctor.")

        elif resultado >= 7:
            print('\n'+'\033[1;31m'+"➤"+'\033[m'+" You may have Diabetes, please consult a doctor!!")

    elif act == 3:
        print("Exiting...")
        quit()

    else:
        print("Please, select a valid option.")

except:
    print("Thanks for using our application, if you want to use it again restart it and insert a valid input value.")
