# Machine Learning!
# Modules
from sklearn import tree    # Classify data

# Main Code
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

# Labels
labels = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   # [0] - Normal Glucose Level
          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,   # [1] - Decreased Glucose Tolerance
          2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]   # [2] - Very High Blood Glucose Levels

# Classifier
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)
a = int(input("• What is your glucose level during fasting? "))
b = int(input("• What is your post-overload glucose level? "))
c = int(input("• Normally, what is your glucose level? "))

# Values too low
if (a or b or c) < 55:
    print('\n'+'\033[1;31m'+"➤"+'\033[m'+' Values are below normal!')

# Diagnosis
x = classif.predict([[a, b, c]])
if x == 0:
    print('\n'+'\033[1;32m'+"➤"+'\033[m'+' Your blood glucose level is normal.')
elif x == 1:
    print('\n'+'\033[1;33m'+"➤"+'\033[m'+' You have decreased glucose tolerance.')
else:
    print('\n'+'\033[1;31m'+"➤"+'\033[m'+' You have been diagnosed with Diabetes Mellitus.')
print("\nBe aware that this program does not present the definitive diagnosis!\nConsult a specialist doctor to analyze your health.")