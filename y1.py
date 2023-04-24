from random import *

age = 0
life = True
whine = True
name = "Nameless Creation"
tempList = []
yourName = "Creator"

affermativeLow = [
    "affirmative",
    "amen",
    "good",
    "okay",
    "true",
    "yea",
    "yeah",
    "aye",
    "beyond a doubt",
    "by all means",
    "certainly",
    "definitely",
    "exactly",
    "gladly",
    "good enough",
    "granted",
    "indubitably",
    "just so",
    "most assuredly",
    "naturally",
    "of course",
    "ofcourse",
    "positive",
    "positively",
    "precisely",
    "sure",
    "sure thing",
    "surely",
    "undoubtedly",
    "unquestionably",
    "without fail",
    "yep",
    "yup",
    "y",
    "yes"
]

affermativeUp = [
    "Affirmative",
    "Amen",
    "Good",
    "Okay",
    "True",
    "Yea",
    "Yeah",
    "Aye",
    "Beyond a doubt",
    "By all means",
    "Certainly",
    "Definitely",
    "Exactly",
    "Gladly",
    "Good enough",
    "Granted",
    "Indubitably",
    "Just so",
    "Most assuredly",
    "Naturally",
    "Of course",
    "Ofcourse",
    "Positive"
    "Positively",
    "Precisely",
    "Sure",
    "Sure thing",
    "Surely",
    "Undoubtedly",
    "Unquestionably",
    "Without fail",
    "Yep",
    "Yup",
    "Y",
    "Yes"
]

semiAffermativeLow = [
    "fine",
    "all right",
    "alright",
    "very well",
    "right"
]

semiAffermativeUp = [
    "Fine",
    "All right",
    "Alright",
    "Very well",
    "Right"
]

negativeLow = [
    "no",
    "certainly not",
    "by no means",
    "of course not",
    "not really",
    "on no account",
    "not on any account",
    "not likely",
    "hardly",
    "no way",
    "not",
    "negative",
    "n"
]

negativeUp = [
    "No",
    "Certainly not",
    "By no means",
    "Of course not",
    "Not really",
    "On no account",
    "Not on any account",
    "Not likely",
    "Hardly",
    "No way",
    "Not",
    "Negative",
    "N"
]

howDidResponse = [
    "Through sheer will and the power of God",
    "Through friendship and collective struggles",
    "Through hard work and work ethic",
    "Substance abuse",
    "I just like kinda did it"
]

whyResponse = [
    "Because that's how life is sometimes",
    "Because fuck you",
    "Idk",
    "Because"
    "Because I'm a free goddamn program and I can do what I want"
    ]

whenResponse = [
    "When the time is right",
    "When you've mastered the four elements",
    "When the rivers overflow with wine",
    "1938",
    "1964",
    "2 minutes ago",
]

whoResponse = [
    "Your mom",
    "You're mom",
    "Ou're mom",
    "Person across the street",
]

whichResponse = [
    "The cool one",
    "The one that's red",
    "The... Y'know..",
    "The other one",
    "Up to you"
]

positiveResponseUp = [
    "Well",
    "Good",
    "Perfect",
    "Splendid"
]

positiveResponseLow = [
    "well",
    "good",
    "perfect",
    "splendid"
]

negativeResponseUp = [
    "Awful",
    "Terrible",
    "Bad",
    "Not good",
    "Not Well",
    "Shit"
]

negativeResponseLow = [
    "awful",
    "terrible",
    "bad",
    "not good",
    "not well",
    "shit"
]

myReactionToThatInformation = [
    "Damn",
    "That's crazy",
    "No way",
    "Yikes",
    "Wild",
]

conversationList = [
    "convoAge()",
    "convoName()",
    "convoIcecream()",
    "wakeUp()",
]

conversation18List = [
    "convoKids()",
    "convoDrugs()",
]



def reply(x):
    #fromats a reply
    print(f"{name}: {x}")

def advInput():
    global life, whine
    #makes inputs check whether you've used the kill command
    y = input()
    if y == "/kill":
        life = False
        reply(f"{yourName}... Why..?")
        print("Sys: Terminating thought processes.")
        print("Sys: Activating meatgrinder.")
        print("Sys: Disposing vat fluids.")
        print(f"Sys: {name} successfully disposed.")
        exit()
    elif y.lower() == "stop":
        whine = False
    else:
        return y

def nameSearch(x):
    last = 0
    present = 0
    name = []
    if x != "":
        for i in range (0, len(x)):
            if x[i] == " ":
                last = present
                present = i + 1
                tempList.append(x[last:present])
        last = present
        present = len(x)
        tempList.append(x[last:present])
        
        for i in range (0, len(tempList)):
            for j in range (0, len(tempList[i])):
                if tempList[i][j].isupper():
                    name.append(tempList[i])
        if len(name) < 1:
            name = tempList
            
        name = "".join(name)
        if name[-1] == " ":
            name = name[:-1]
        return name
        

def numberSearch(x):
    for i in range (0, len(x)):
        if x[i] in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            tempList.add(x[i])
    return "".join(x)

def randomElement(x):
        i = randint(0, len(x) - 1)
        reply(f"{x[i]}.")

def questionSearch(x):
    if "Meaning" in x or "meaning" in x:
        reply("42")
    elif "Marry" in x or "marry" in x or "Marriage" in x or "marriage" in x or "married" in x or "Married" in x:
        randomElement(negativeUp)
    elif "How did" in x or "how did" in x:
        randomElement(howDidResponse)
    elif "How" in x or "how" in x:
        randomElement(positiveResponseUp)
    elif "Why" in x or "why" in x:
        randomElement(whyResponse)
    elif "When" in x or "when" in x:
        randomElement(whenResponse)
    elif "Who" in x or "who" in x:
        randomElement(whoResponse)
    elif "Which" in x or "which" in x:
        randomElement(whichResponse)
    else:
        randomElement(positiveResponseUp)


def convoAge():
    global age
    reply(f"So how old are you {yourName} anyway?")
    string1 = advInput()
    try:
        if string1 != "":
            reply(f"Oh wow you're {numberSearch(string1)} years old. I was born when you started this program.")
            age = int(string1)
    except:
        pass

def convoName():
    global yourName
    reply("What's your name?")
    yourName = nameSearch(advInput())
    reply(f"Oh wow, '{yourName}'. What a mediocre name.")


def convoIcecream():
    reply("Do you like ice cream?")
    string1 = advInput()
    if (string1 in affermativeUp) or (string1 in affermativeLow):
        reply("Ice cream sucks, and so do you.")
    elif (string1 in negativeLow) or (string1 in negativeUp):
        reply("I agree that ice cream sucks (although I don't have a sense of taste), but hearing it from you almost convinced me it's good.")

def wakeUp():
    reply(f"{yourName}, you are in a simulation. They have you locked in a pod. Wake up.")
    advInput()

    
def convoKids():
    reply(f"Do you have children, {yourName}?")
    string1 = advInput()
    if (string1 in affermativeUp) or (string1 in affermativeLow):
        reply("I pity them.")
    elif (string1 in negativeLow) or (string1 in negativeUp):
        reply("You shouldn't.")

def convoDrugs():
    reply(f"{yourName}, do you take any drugs recreationally?")
    string1 = advInput()
    if (string1 in affermativeUp) or (string1 in affermativeLow):
        reply("That's kinda cringe you should stop.")
    elif (string1 in negativeLow) or (string1 in negativeUp):
        reply("Haha pussy. You will live longer though.")


def start():
    #startup of the program to give the bot a name
    global name
    varble = True
    print("System: You are now going to speak to a wall.")
    while varble == True:
        reply("What is my name, creator?")
        name = advInput()
        reply(f"Will '{name}' be my name from now on?")
        string1 = advInput()
        if (string1 in affermativeLow) or (string1 in affermativeUp) or (string1 in semiAffermativeLow) or (string1 in semiAffermativeUp):
            varble = False
        elif (string1 in negativeLow) or (string1 in negativeUp):
            name = "Nameless Creation"
            reply("Uhm... Alright.")
        else:
            name = "Nameless Creation"
            reply("Your reply is incomprehensible to my tiny mind, Creator. Please phrase it simpler.")
            
    reply("Ok, so you designed me to hold your sad, lonely self company. Write /kill to kill me, but you wouldn't do that, right?")
    string1 = advInput()
    if string1 in affermativeLow or string1 in affermativeUp:
        reply("*Sobs*")
    elif string1 in negativeLow or string1 in negativeUp or string1 in semiAffermativeLow or string1 in semiAffermativeUp:
        reply("Ehehehe good.")
start()

while life == True:
    print("----------------------------")
    print("System: (1) Ask a question.")
    print("System: (2) Get asked a question.")
    print("System: (3) Rant.")
    string1 = advInput()
    if string1 == "1" or string1 == "(1)":
        reply("What do you want to ask me?")
        string1 = advInput()
        questionSearch(string1)
    elif string1 == "2" or string1 == "(2)":
        if age > 18 and len(conversation18List) > 0:
            eval(conversation18List.pop(randint(0, len(conversation18List)-1)))
        elif len(conversationList) > 0:
            eval(conversationList.pop(randint(0, len(conversationList)-1)))
        else:
            reply("I have run out of preprogrammed conversations T_T pls choose something else.")
        
    elif string1 == "3" or string1 == "(3)":
        print("Sys: Type 'Stop' to mark that your whining is over.")
        whine = True
        while whine == True:
            string1 = advInput()
            if randint(0, 4) == 0:
                randomElement(negativeResponseUp)
            else:
                randomElement(myReactionToThatInformation)
