This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' #define the variable symbols
MAX_KEY_SIZE = len(SYMBOLS) #get the length of symbols

def getMode(): #defines the function
    while True: #loop
        print('Do you wish to encrypt or decrypt a message?') #print the message
        mode = input().lower() #set mode as the input from lower
        if mode in ['encrypt', 'e', 'decrypt', 'd']: #if the user inputs encrypt, decrypt, e, or d
            return mode #return the variable mode
        else: #else do the following
            print('Enter either "encrypt" or "e" or "decrypt" or "d".') #print the message

def getMessage(): #defines getMessage
    print('Enter your message: ') #print the message
    return input() #return the input

def getKey(): #defines getKey
    key = 0 #sets key as 0
    while True: #do the following while it is true
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE)) #print the statement
        key = int(input()) #setting key as the input
        if (key >= 1 and key <= MAX_KEY_SIZE): #if the key is greater than or equal to 1 and less the the max key size
            return key #return the key

def getTranslatedMessage(mode, message, key): #define getTransltedMessage
    if mode[0] == 'd': #if the first element of mode is d
        key = -key #key equals negative key
    translated = '' #translated equals nothing

    for symbol in message: #for every symbol in message
        symbolIndex = SYMBOLS.find(symbol) #the symbolindex equals the SYMBOLS found in symbol
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol #add the symbol to translated
        else: #otherwise
            #Encrypt or decrypt
            symbolIndex += key #add the key
        if symbolIndex >= len(SYMBOLS): #if the symbolindex is greater than the length of symbols, the shift starts happening here depending on the length of SYMBOl list and the key
            symbolIndex -= len(SYMBOLS) #subtract the length of symbols
        elif symbolIndex < 0: #else if the symbolIndex is greater than 0
            symbolIndex += len(SYMBOLS) #add the length of symbols

        translated += SYMBOLS[symbolIndex] #add SYMBOLS[symbolIndex] to translated
    return translated #return the variable translated

mode = getMode() #mode will equal the output of the function defined above (call functions)
message = getMessage() #message will equal the output of the function defined above
key = getKey() #key will equal the output of the function defined above
print('Your translated text is: ') #print the message
print(getTranslatedMessage(mode, message, key)) #print the mode, message, and key