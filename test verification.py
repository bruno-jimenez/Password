#[-------------------------------------------]
#   create the list for all input for pwd 
#[-------------------------------------------]

alphabet_min="abcdefghijklmpnopqrstuvwxyz"
alphabet_maj="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres ="1234567890"
caracteres_speciaux ="!@#$%^&*()_-+=[]"

#[-------------------------------------------]
# cretion of all entry for the pwd 
#[-------------------------------------------]

alphabet_min_entry= False
alphabet_maj_entry= False
caracteres_speciaux_entry= False
chiffres_entry= False
psw_entry= False
verification_loop= True

#[-------------------------------------------]
# function for verification pwd 
#[-------------------------------------------]

def verification():

#[-------------------------------------------]
# verification of all entry in the pwd 
#[-------------------------------------------]

    psw_input=list(input("Tape your password , the password must contain 8 caractere minimum , 1 number and 1 upper letter : "))
    psw_input= str(psw_input)
    psw= 0
    psw = len(psw_input)

    if psw >= 7:
        print("your password contain 8 caractere minimum")
        psw_entry= True
    else:
        psw_entry= False
        print("your password no contain 8 caractere minimum")
       
    if psw_input in chiffres: 
        print("your password contain number")
        chiffres_entry= True 
    else:
        chiffres_entry= False
        print("your password no contain number") 

    if psw_input in alphabet_maj:
        print("your password contain upper letter")
        alphabet_maj_entry= True
    else:
        alphabet_maj_entry= False
        print("your password  no contain upper letter")

    if psw_input in alphabet_min: 
        print("your password contain lower letter")
        alphabet_min_entry= True
    else:
        alphabet_min_entry= False
        print("your password no contain lower letter")

    if psw_input in caracteres_speciaux: 
        print("your password contain special caratere")
        caracteres_speciaux_entry= True
    else:
        caracteres_speciaux_entry= False
        print("your password  no contain special caratere")
        
#[-------------------------------------------]
# creation of the encrypting and validation of password or not
#[-------------------------------------------]

    while alphabet_min_entry == True and alphabet_maj_entry == True and psw_entry == True and caracteres_speciaux_entry == True and chiffres_entry == True:
        print("your password is valid encrypting in progress")
    else: 
        if alphabet_min_entry == False or alphabet_maj_entry == False or psw_entry == False or caracteres_speciaux_entry == False or chiffres_entry == False:
            print("invalid password write another password . :)")

verification()