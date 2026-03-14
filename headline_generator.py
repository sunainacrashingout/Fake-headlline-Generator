import random

subjects_bollywood = ["Mogambo", "Crime master Gogo", "Manjulika", "Jaadu"]
actions_bollywood = ["danced with a monkey at", "kissed a frog at", "took a selfie with a gorilla", "rode cycle with a crocodile at"]
objects_bollywood = ["Taj Mahal", "at a liquid zoo", "at prime minister's residence", "at film city"]

subjects_politics = ["Modi ji", "Nirmala didi","Mamta ji", "Lalu Preasad Yadav"]
actions_politics = ["was seen stealing ice cream from children", "started screaming 'JUKEGA NAI SAALA'", "was seen shouting and assaulting a reporter"]
objects_polictics = ["at a park", "in a rally", "at republic day parade"]

subjects_tsec = ["Gaurd bhaiya", "A 4st year student" ]
actions_tsec = ["was seen doing break dance", 'was seen crying after his girlfriend dumped him']
objects_tsec = ['at FAISCA', "in boys washroom"]




while(True):
    ch=int(input("Hi! Welcome to 100 percent real news(it's fake).\nPick a topic you are interested in: \n1.Bollywood \n2.Politics \n3.Prestigious TSEC\n4.Exit\n"))
    print("Here's your veryyy real news~~")
    if ch==1:
        headline = random.choice(subjects_bollywood) + " " + random.choice(actions_bollywood) + " " + random.choice(objects_bollywood)
        print("BREAKING NEWS: ",headline)
        print('')
    elif ch==2:
        headline = random.choice(subjects_politics) + " " + random.choice(actions_politics) + " " + random.choice(objects_polictics)
        print("BREAKING NEWS: ",headline)
        print('')
    elif ch==3:
        headline = random.choice(subjects_tsec) + " " + random.choice(actions_tsec) + " " + random.choice(objects_tsec)
        print("BREAKING NEWS: ",headline)
        print('')
    elif ch==4:
        print('Exiting program........')
        break
    else:
        print('Invalid input')