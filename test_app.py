# Import TextParser class
from app import TextParser

# example text string
text = "A solution of Dre@mBroker 2020."
# initializing the class
textParser = TextParser(text)

def test_getTextLength():
    """
    Description: 
        This function tests the text string length

    Returns:
        json: number of words in the text string.           
    """
    response = textParser.getTextLength()
    withSpaces = response['withSpaces']
    withoutSpaces = response['withoutSpaces']
    expected_withSpaces = 31
    expected_withoutSpaces = 27
    assert withSpaces == expected_withSpaces, "Wrong count of withSpaces"
    assert withoutSpaces == expected_withoutSpaces, "Wrong count of withoutSpaces"

def test_getWordCount():
    """
    Description: 
        This function tests the number of word count in the text string.

    Returns:
        json: number of words in the text string.
    """
    response = textParser.getWordCount()
    wordCount = response['wordCount']
    expected_wordCount = 5
    assert  wordCount == expected_wordCount, "Wrong count of words"

def test_getCharacterCount():
    """
    Description: 
        This function tests the occurence of characters (only alphabets) in the text string. 

    Returns:
        json: characters (alphabets) occurance in the text string alphabatically.
    """
    response = textParser.getCharacterCount()
    characters = len(response)
    expected_characters = 15
    assert  characters == expected_characters, "Wrong count of characters"