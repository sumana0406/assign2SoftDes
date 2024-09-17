

def charCounter(strInput):
    
    nCharCounter = 0
    
    for char in strInput:
        
        if(char != ' '):
            
            nCharCounter += 1
    
    return nCharCounter



def vowelCounter(strInput):
    
    nVowelCounter = 0
    strInput = strInput.lower()
    
    charVowelArr = ['a', 'e', 'i', 'o', 'u']
    
    for char in strInput:
        
        if( char in charVowelArr):
            
            nVowelCounter += 1
    
    return nVowelCounter



def digitCounter(strInput):
    
    nDigitCounter = 0
    charDigitArr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for char in strInput:
            
        if(char in charDigitArr):
            
            nDigitCounter += 1
    
    return nDigitCounter


def printer():

    strInput = input("Enter the input value whose length you want to find: ")

    print("The total number of characters are:", charCounter(strInput) )
    print("The total number of vowels are:", vowelCounter(strInput) )
    print("The total number of digits are:", digitCounter(strInput) )




printer()

def testChars():
    assert charCounter("this is an assignment in CIS 3196!! @TUJ") == 33, "Test passed"
    
def testChars1():
    try:
        assert charCounter("this is an assignment in CIS 3196!! @TUJ") == 33
        print("Character count test1 passed!")
        
    except AssertionError as e:
        print("Character Test1 failed!")

def testVowels1():
    
    try:
        
        assert vowelCounter("this is an assignment in CIS 3196!! @TUJ") == 9
        print("Vowel count test1 passed!")
        
    except AssertionError as e:
        print("Vowel Test1 failed!")
        
def testDigits1():
    
    try:
        
        assert digitCounter("this is an assignment in CIS 3196!! @TUJ") == 4
        print("Digit count test1 passed!")
        
    except AssertionError as e:
        print("Digit Test1 failed!")
        

testChars1()
testVowels1()
testDigits1()

def testChars2():
    try:
        assert charCounter('\\0354 hiee') == 9
        print("Character count test2 passed!")
        
    except AssertionError as e:
        print("Character Test2 failed!")
        
def testVowels2():
    try:
        assert vowelCounter("\\0354 hiee") == 3
        print("Vowel count test2 passed!")
        
    except AssertionError as e:
        print("Vowel Test2 failed!")
        
def testDigits2():
    try:
        
        assert digitCounter("\\0354 hiee") == 4
        print("Digit count test2 passed!")
        
    except AssertionError as e:
        print("Digit Test2 failed!")

testChars2()
testVowels2()
testDigits2()


def testChars3():
    try:
        assert charCounter('\\-0.354 日ヒతెはHTC') == 15
        print("Character count test3 passed!")
        
    except AssertionError as e:
        print("Character Test3 failed!")
        
def testVowels3():
    try:
        assert vowelCounter('\\-0354 తెはHTC') == 0
        print("Vowel count test3 passed!")
        
    except AssertionError as e:
        print("Vowel Test3 failed!")
        
def testDigits3():
    try:
        
        assert digitCounter('\\-0354 తెはHTC') == 4
        print("Digit count test3 passed!")
        
    except AssertionError as e:
        print("Digit Test3 failed!")
testChars3()
testVowels3()
testDigits3()
#testChars()
