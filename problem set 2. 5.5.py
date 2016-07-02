def isWordGuessed(secretWord, lettersGuessed):
    if lettersGuessed[0] not in secretWord:
        return False
    if len(lettersGuessed) == 1 and lettersGuessed in secretWord:
        return True
    if len(lettersGuessed) > 1:
        return isWordGuessed(secretWord[1:], lettersGuessed)

def getGuessedWord(secretWord, lettersGuessed):
    x = ''
    while len(secretWord) > 0:
        if secretWord == '':
            break
        elif secretWord[0] not in lettersGuessed:
            x += '_ '
            secretWord = secretWord[1:]
        elif secretWord[0] in lettersGuessed:
            x += str(secretWord[0])
            secretWord = secretWord[1:]
    return x
    
import string
def getAvailableLetters(lettersGuessed):
    x = string.ascii_lowercase
    for i in lettersGuessed:
        if i in x:
            x = x[:x.index(i)] + x[(x.index(i)+1):]
    return x


def hangman(secretWord):
    print 'Welcome to the game, Hangman!'
    print'I am thinking of a word that is %s letters long.' % len(secretWord)
    print '-----------'
    n = 8
    print 'You have %s guesses left' %n
    print 'Available letters: %s' %string.ascii_lowercase
    while n > 0:
        print 'Please guess a letter:',
        lettersGuessed = raw_input()
        isWordGuessed(secretWord, lettersGuessed)
        word = getGuessedWord(secretWord, lettersGuessed)
        if isWordGuessed(secretWord, lettersGuessed) == False:
            print 'Oops! That letter is not in my word:'
            '''
            If the guess was wrong make the number of gueses less
            '''
            n -= 1
            print 'You have %s guesses left' %n
            getAvailableLetters(lettersGuessed)
            print word
                       
        else:
            print 'Good guess: ',
            print word
            print '-----------'
            '''
            If the guess was right show the place of this letter
            '''
            if word == secretWord:
                print 'Congratulations, you won!'
                return None
            print 'You have %s guesses left' %n
    
            
            
        
        
    
    
   
