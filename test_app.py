from app import getTextLength, getWordCount, getCharacterCount

def test_getTextLength():
    text = "A solution of Dre@mBroker 2020."
    response = getTextLength(text)
    withSpaces = response['withSpaces']
    withoutSpaces = response['withoutSpaces']
    expected_withSpaces = 31
    expected_withoutSpaces = 27
    assert withSpaces == expected_withSpaces, "Wrong count of withSpaces"
    assert withoutSpaces == expected_withoutSpaces, "Wrong count of withoutSpaces"

def test_getWordCount():
    text = "A solution of Dre@mBroker 2020."
    response = getWordCount(text)
    wordCount = response['wordCount']
    expected_wordCount = 5
    assert  wordCount == expected_wordCount, "Wrong count of words"

def test_getCharacterCount():
    text = "A solution of Dre@mBroker 2020."
    response = getCharacterCount(text)
    characters = len(response)
    expected_characters = 15
    assert  characters == expected_characters, "Wrong count of characters"