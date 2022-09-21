#Input vragen

age_str = input('What is your age? ')
print(f'Your age is {age_str}')

#Internet verbindingsselectie
connection_choice_str = input('Welke verbindingen witl u gebruiken [4G. 5G, Wifi open]: ')

#Convert answer to upper case
#The user can enter upper, lower or combined casing
connection_choice = connection_choice_str.upper()

if connection_choice == "4G":
    print(f"U bent verbonden via {connection_choice}!")
elif connection_choice == "5G":
    print(f"U bent verbonden via {connection_choice}")
elif connection_choice == "WIFI OPEN":
    print(f"U heeft voor de Wifi open gekozen, wij wjzen erop dat de data door de eigenaar van dit netwerk is te lezen.")
    answer_str = input("Wilt u nog steeds een verbinding maken? [Ja/Nee]: ")
    answer = answer_str.upper()
    if answer == "JA":
        print(f"U bent verbonden via {connection_choice}!")
    else:
            print("U bent niet verbonden!")
else:
        print("Onbekende invoer, er wordt geen verbinding tot stand gebracht")

# Vergelijken met een sub-string
print("Is Hello with a capital 'H' within the string 'Hello, everyone!'")
if "Hello" in "Hello, everyone!":
    print('Yes, hello is within the Hello, everyone! string')

print("Is Hello with a lower case 'h' within the string 'Hello, everyone!'")
if "hello" in "Hello, everyone!":
    print('Yes, hello is within the Hello, everyone! string')
else:
    print('No, hello with small letters is not within the string')

# Flowchart

#Patient exposed to TB [Tuberculoses]
print("Patient exposed to TB")
question_1_str = input("Is the patient an adult or a child? [Adult/Child]: ")
question_1 = question_1_str.upper()
if question_1 == "ADULT":
    # Adult part
    question_2_str = input("Has common TB symptoms? [Yes/No]: ")
    question_2 = question_2_str.upper()
    if question_2 == "YES":
        print("Treat as likely TB patient and perform full TB exam.")
    elif question_2 == "NO":
        print("Have patient report back if unwell, return in 1 month for checkup.")
    else:
        print("Abort, unknown input.")
elif question_1 == "CHILD":
    # Child part
    print("Child")
    question_3_str = input("Can TB test be given [Yes/No]: ")
    question_3 = question_3_str.upper()
    if question_3 == "YES":
        print("Administer TB test.")
        print("Assess TB test results and child's condition.")
    elif question_3 == "NO":
        question_4_str = input("Child well? [Yes/No]: ")
        question_4 = question_4_str.upper()
        if question_4 == "YES":
            print("6 months preventive isoniazid.")
            print("Have parent bring in if child shows symptoms.")
        elif question_4 == "NO":
            print("Take full history.\nExamine for TB.")
            print("If TB likely diagnosis, treat for TB.")
            print("If other diagnosis more likely. treat as needed and watch for TB symptoms.")
        else:
            print("Abort, unknown input.")
    else:
        print("Abort, unknown input.")
else:
    print("Abort, unknown input.")

# Flowchart

# Shopping cart
print("Shopping Cart")
question_1_str = input("Payment method? [Online/Offline]: ")
question_1 = question_1_str.upper()
if question_1 == "ONLINE":
    # Online part
    print("Online, place purchase order")
    question_2_str = input("Admin user? [Yes/No]: ")
    question_2 = question_2_str.upper()
    if question_2 == "YES":
        print("Enter payment detils.")
        print("Place order.")
    elif question_2 == "NO":
        question_3_str = input("Approvel rules? [Approved/Rejected]: ")
        question_3 = question_3_str.upper()
        if question_3 == "APPROVED":
            print("Enter payment details.")
            print("Place order.")
        elif question_3 == "REJECTED":
            print("Purchase order rejected.")
        else:
            print("Abort, uknown input.")
    else:
        print("Abort, unknown inout.")
elif question_1 == "OFFLINE":
    # Offline part
    print("Offline, place order")
    question_4_str = input("Admin user? [Yes/No]: ")
    question_4 = question_4_str.upper()
    if question_4 == "YES":
        print("Order created automatically.")
    elif question_4 == "NO":
        question_5_str = input("Approvel rules? [Approved/Rejected]: ")
        question_5 = question_5_str.upper()
        if question_5 == "APPROVED":            
            print("Order created automatically.")
        elif question_5 == "REJECTED":            
            print("Purchase order rejected.")
        else:            
            print("Abort, unknown input.")
    else:        
        print("Abort, unknown input.")
else:    
    print("Abort, unknown input.")

# Bestellen
#Ordering ar Mac Donald's
eat_in  = False
eat_out = False
aborted = False

print("Welkom bij de Mac Donald's")
question_1_str = input("Hier opeten of meenemen? [Opeten/Meenemen]: ")
question_1 = question_1_str.upper()
if question_1 == "Opeten":
    # Eat in part
    print("Hier opeten")
    eat_in = True
elif question_1 == "Meenemen":
    # Take away part
    print("Meenemen")
    eat_out = True
else:
    aborted = True

if eat_in or eat_out:
    question_2_str = input("Burgers of drankjes? [Burgers/Drankjes]; ")
    question_2 = question_2_str.upper()
    if question_2 == "BURGERS":
        question_3_str = input("Burgers [Hamburger, Cheeseburger, Bic Mac, QuarterPounder]: ")
        question_3 = question_3_str.upper()
        if question_3 == "HAMBURGER":            
            print("Hamburger")
        elif question_3 == "CHEESEBURGER":            
            print("Cheeseburger")
        elif question_3 == "BIC MAC":            
            print("Big Mac")
        elif question_3 == "QUARTER POUNDER":            
            print("Quarter Pounder")
        else:            
            aborted = True
    elif question_2 == "DRANKJES":        
        question_4_str = input("Drankjes [Warme/Koude]: ")        
        question_4 = question_4_str.upper()
        if question_4 == "WARME":            
            question_5_str = input("Warme drank: [Koffie, Cappucino,Chocolademelk]: ")
            question_5 = question_5_str.upper()
            if question_5 == "KOFFIE":                
                print("Koffie")
            elif question_5 == "CAPPUCINO":                
                print("Cappucino")
            elif question_5 == "CHOCOLADEMELK":                
                print("Chocolademelk")
            else:                
                aborted = True
        elif question_4 == "KOUDE":            
            question_6_str = input("Koude drank: [Coca Cola, Cola Zero, 7-Up,Fanta, Fristi]: ")            
            question_6 = question_6_str.upper()
            if question_6 == "COCA COLA":                
                print("Coca Cola")
            elif question_6 == "COLA ZERO":                
                print("Cola Zero")
            elif question_6 == "7-UP":                
                print("7-Up")
            elif question_6 == "FANTA":                
                print("Fanta")
            elif question_6 == "FRISTI":                
                print("Fristi")
            else:                
                aborted = True
        else: 
            aborted = True

    if aborted:    
        print("Abort, unknown input.")
    else:
        if eat_in:        
            print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
        elif eat_out:        
                print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")