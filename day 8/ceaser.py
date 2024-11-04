letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shoulcontinue=True
while shoulcontinue:
    dire=input("type 'encode' to encrypt,type 'decode' to decrypt: " ).lower()
    tect=input("type your message: ").lower()
    shiftn=int(input("type the shift number: \n"))

    def encrypt(plain_tect,shift_amount):
        none=""
        for letter in plain_tect:
            if letter in letters:
                position=letters.index(letter)
                newposition=position+shift_amount
                newletter=letters[newposition%26]
                none+=newletter
            else:
                none+=letter
        print(f"the encrypted word is {none}")
    def decrypt(plain_tect,shift_amount):
        none=""
        for letter in plain_tect:
            if letter in letters:
                position=letters.index(letter)
                newposition=position-shift_amount
                newletter=letters[newposition%26]
                none+=newletter
            else:
                none+=letter
        print(f"the decrypted word is {none}")
    if dire=="encrypt":
        encrypt(tect,shiftn)
    elif dire=="decrypt":
        decrypt(tect,shiftn)
    result=input("type 'yes' if you want to go again, otherwise type 'no'.\n").lower()
    if result=="no":
        shoulcontinue=False
        print("Goodbye!")


   