#How much time do you think you spent on this lab?           I think I probably spent around 2ish hours total on this lab
#What part of this program was the most challenging?         The most challenging part was definitely just wrapping my head around all of the different outputs and creating the chunks and everything
#How did you overcome the challenge?                         Writing things out helped a lot plus just imagining different code workflows
#What part of this program was the MOST FUN?                 I loved testing it! It was so satisfying to see everything work and the outputs be correct
#What do you plan to add to your program in the future?      I plan to make it usable for 6 letter words ranging to 12 letter words and maybe make the output a bit prettier


"""
need to (optional):
- "guess again!" for wrong answers
- make output prettier
- game header/intro
"""

import random

words = []
hints = []
wordGuessed = [False,False,False,False,False,False,False]
chunks = []

def getWords():
    file = open("words SHELBY.txt","r")
    fileData = file.readlines()

    # CREATE LISTS OF WORDS AND HINTS
    for line in fileData:
        lineSplit = line.split(",")
        
        word = lineSplit[0]
        words.append(lineSplit[0])

        hint = lineSplit[1]
        hints.append(hint[:-1])

# FUNCTION FOR STRIKING
def striken(text):
    return ''.join(chr(822)+t for t in text)

# "FORMULA" FOR CREATING CHUNKS
def chunkIt(word):
    length = len(word)

    if (length == 6):    #if 6 letters     AVENUE -> AVE NUE
        chunks.append(word[:3])
        chunks.append(word[3:])

    if (length == 7):    #if 7 letters     ICEBERG -> ICE BERG    or     ICEB ERG
        rando = random.randint(3,4)
        chunks.append(word[:rando])
        chunks.append(word[rando:])

    if (length == 8):    #if 8 letters     ACADEMIC -> ACA DEM IC
        chunks.append(word[:3])
        chunks.append(word[3:6])
        chunks.append(word[6:])

    if (length == 9):    #if 9 letters     BAMBOOZLE -> BAM BOO ZLE
        chunks.append(word[:3])
        chunks.append(word[3:6])
        chunks.append(word[6:])

    if (length == 10):   #if 10 letters    APPRECIATE -> APP REC IATE     or      APP RECI ATE      or       APPR ECI ATE
        rando = random.randint(1,3)  #which chunk (1, 2, or 3) will have 4

        if (rando == 1):             #if first chunk is 4
            chunks.append(word[:4])
            chunks.append(word[4:7])
            chunks.append(word[7:])

        if (rando == 2):             #if second chunk is 4
            chunks.append(word[:3])
            chunks.append(word[3:7])
            chunks.append(word[7:])

        if (rando == 3):             #if third chunk is 4
            chunks.append(word[:3])
            chunks.append(word[3:6])
            chunks.append(word[6:])

    if (length == 11):   #if 11 letters    ABOLISHMENT -> ABO LIS HME NT
        chunks.append(word[:3])
        chunks.append(word[3:6])
        chunks.append(word[6:9])
        chunks.append(word[9:])

    if (length == 12):   #if 12 letters    RELATIONSHIP -> REL ATI ONS HIP 
        chunks.append(word[:3])
        chunks.append(word[3:6])
        chunks.append(word[6:9])
        chunks.append(word[9:])
    
# ADDING ALL CHUNKS TO "CHUNK"
def addChunks():
    for word in words:
        chunkIt(word)

# FOR PRINTING ALL HINTS + WORD LENGTHS + CHUNK BANK
def display():
    listLength = len(words)

    # PRINTING HINTS + WORDS
    for i in range (listLength):    #go through all 7 words
        endPart = ""
        if (wordGuessed[i]==False):  #if word has NOT been guessed yet
            length = len(words[i])
            endPart = (str(length) + " letters")
        else:
            endPart = (words[i].upper())
        
        spacesNeeded = (55 - (len(hints[i])+len(endPart)))
        output = (hints[i] + (spacesNeeded*" ") + endPart)
        print(output)
    
    print("")

    # PRINTING CHUNKS       ----> 7 per row for now!
    chunksShuffle = random.sample(chunks,len(chunks))   #makes new list of shuffled chunks

    numChunks = len(chunksShuffle)  #number of chunks
    numChunksSplit = numChunks//3
    chunksLineOne = chunksShuffle[:numChunksSplit]
    chunksLineTwo = chunksShuffle[numChunksSplit:(numChunksSplit*2)]
    chunksLineThree = chunksShuffle[(numChunksSplit*2):]

    line1 = "         "
    line2 = "       "
    line3 = "        "
    
    for chunkSingle in chunksLineOne:
        line1 = line1 + chunkSingle.upper() + "    "
    for chunkSingle in chunksLineTwo:
        line2 = line2 + "    " + chunkSingle.upper()
    for chunk in chunksLineThree:
        line3 = line3 + chunk.upper() + "    "
    
    print(line1 + "\n" + line2 + "\n" + line3)

# FUNCTION FOR INPUTTING GUESSES
def guessing():
    print("")
    guess = input("Enter a guess: ")

    for m in range (len(words)):          #go through every word
        if (guess==words[m]):              #if guess is in word list
            wordGuessed[m] = True          #then... set wordGuessed to 'true'
            
    if((len(guess))==6):   #if guess length is 6 or 7 (meaning there would be 2 chunks)
        guess1 = guess[:3]
        guess2 = guess[3:]

        for i in range (len(chunks)):         #go through every chunk
            if (guess1==chunks[i]):           #if guess1 = chunk... strike it
                chunks[i] = striken(chunks[i])

        for v in range (len(chunks)):         #go through every chunk
            if (guess2==chunks[v]):           #if guess2 = chunk... strike it
                chunks[v] = striken(chunks[v])

    if((len(guess))==7):  #if 7 letters     ICEBERG -> ICE BERG    or     ICEB ERG
        guess1 = guess[:3]   # ICE
        guess2 = guess[3:]   # BERG
        guess3 = guess[:4]   # ICEB
        guess4 = guess[4:]   # ERG

        for i in range (len(chunks)):         
            if (guess1==chunks[i]):           
                chunks[i] = striken(chunks[i])

        for v in range (len(chunks)):         
            if (guess2==chunks[v]):          
                chunks[v] = striken(chunks[v])
        
        for m in range (len(chunks)):         
            if (guess3==chunks[m]):           
                chunks[m] = striken(chunks[m])
        
        for p in range (len(chunks)):         
            if (guess4==chunks[p]):           
                chunks[p] = striken(chunks[p])

    if((len(guess))==8 or (len(guess))==9):
        guess1 = guess[:3]
        guess2 = guess[3:6]
        guess3 = guess[6:]

        for i in range (len(chunks)):         
            if (guess1==chunks[i]):          
                chunks[i] = striken(chunks[i])

        for v in range (len(chunks)):         
            if (guess2==chunks[v]):           
                chunks[v] = striken(chunks[v])
        
        for m in range (len(chunks)):         
            if (guess3==chunks[m]):           
                chunks[m] = striken(chunks[m])

    if((len(guess))==10):  #if 10 letters    APPRECIATE -> APP REC IATE     or      APP RECI ATE      or       APPR ECI ATE
        guess1 = guess[:3]   # APP
        guess2 = guess[3:6]  # REC
        guess3 = guess[6:]   # IATE
        guess4 = guess[3:7]  # RECI
        guess5 = guess[7:]   # ATE
        guess6 = guess[:4]   # APPR
        guess7 = guess[4:7]  # ECI

        for i in range (len(chunks)):         
            if (guess1==chunks[i]):           
                chunks[i] = striken(chunks[i])

        for v in range (len(chunks)):         
            if (guess2==chunks[v]):          
                chunks[v] = striken(chunks[v])
        
        for m in range (len(chunks)):         
            if (guess3==chunks[m]):           
                chunks[m] = striken(chunks[m])
        
        for p in range (len(chunks)):         
            if (guess4==chunks[p]):           
                chunks[p] = striken(chunks[p])

        for g in range (len(chunks)):         
            if (guess5==chunks[g]):           
                chunks[g] = striken(chunks[g])

        for w in range (len(chunks)):         
            if (guess6==chunks[w]):           
                chunks[w] = striken(chunks[w])
        
        for z in range (len(chunks)):         
            if (guess7==chunks[z]):           
                chunks[z] = striken(chunks[z])
        
    if((len(guess))==11 or (len(guess))==12):
        guess1 = guess[:3]
        guess2 = guess[3:6]
        guess3 = guess[6:9]
        guess4 = guess[9:]


        for i in range (len(chunks)):        
            if (guess1==chunks[i]):           
                chunks[i] = striken(chunks[i])

        for v in range (len(chunks)):        
            if (guess2==chunks[v]):          
                chunks[v] = striken(chunks[v])
        
        for m in range (len(chunks)):         
            if (guess3==chunks[m]):           
                chunks[m] = striken(chunks[m])
        
        for p in range (len(chunks)):         
            if (guess4==chunks[p]):           
                chunks[p] = striken(chunks[p])


# GET WORDS FROM OUTSIDE FILE
getWords()

# MAKE LIST OF CHUNKS
addChunks()

# PRINTING EVERYTHING
print("")
print("*******************************************************") #55 characters
print("")

# REPEATING GAME UNTIL ALL 7 WORDS GUESSED
while not (wordGuessed==[True,True,True,True,True,True,True]):
    display()
    guessing()
    print("")

# FINAL 'CONGRATULATIONS' LINE
if (wordGuessed==[True,True,True,True,True,True,True]):
    display()
    print("")
    print("Congratulations, you got all 7 words!")
    print("*******************************************************") #55 characters