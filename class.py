while True:
    full_name  = input ("Please insert your full name : ")
    if full_name == 'exit':
        break
    split_person = full_name.split()
    print ( "Your first name : ", split_person [0])
    try :
        print ( "Your last name : ", split_person [1])
    except IndexError:
        print("you didnt enter last name for this person, please enter again ")

