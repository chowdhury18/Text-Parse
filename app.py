# Importing libraries
from flask import Flask, jsonify, request, Response

# Defining flask application
app = Flask(__name__)

# TextParser class
class TextParser:
    def __init__(self, text):
        """
        Description: 
            This function initializes the text string requested to parse from the client

        Args:
            text (str): text string to be parse.           
        """
        self.text = text

    def getTextLength(self):
        """
        Description: 
            This function calculates the length of the text string withSpace and withoutSpace counting.

        Returns:
            json: length of the text string with space and without space
        """
        withSpace = len(self.text)
        withoutSpace = withSpace - self.text.count(" ")
        return { "withSpaces":withSpace, "withoutSpaces":withoutSpace }

    def getWordCount(self):
        """
        Description: 
            This function calculates the number of word count in the text string.

        Returns:
            json: number of words in the text string.
        """
        wordCount = 0
        words = self.text.split(" ")
        for word in words:
            if len(word) > 0:
                wordCount += 1
        return {"wordCount": wordCount}

    def getCharacterCount(self):
        """
        Description: 
            This function calculates the occurence of characters (only alphabets) in the text string. 

        Returns:
            json: characters (alphabets) occurance in the text string alphabatically.
        """
        text = self.text.lower()
        charCount = []
        for ch in text:
            if ch.isalpha():
                occurence = text.count(ch)
                data = {"char": ch, "count": occurence}
                if data not in charCount:
                    charCount.append(data)
        charCount = sorted(charCount, key=lambda data: data['char'])
        newCharCount = [{x['char']:x['count']} for x in charCount]
        return newCharCount
    
class TextParser_v2:
    def __init__(self, text):
        """
        Description: 
            This function initializes the text string requested to parse from the client

        Args:
            text (str): text string to be parse.           
        """
        self.text = text

    def getTextLength(self):
        """
        Description: 
            This function calculates the length of the text string withSpace and withoutSpace counting.

        Returns:
            json: length of the text string with space and without space
        """
        charCount = 0
        spaceCount = 0
        for ch in self.text:
            if ch == " ":
                charCount += 1
                spaceCount += 1
            else:
                charCount += 1
        withSpace = charCount
        withoutSpace = charCount - spaceCount
        return { "withSpaces":withSpace, "withoutSpaces":withoutSpace }

    def getWordCount(self):
        """
        Description: 
            This function calculates the number of word count in the text string.

        Returns:
            json: number of words in the text string.
        """
        wordCount = 0
        word = ""
        count = 0
        for ch in self.text:
            count += 1
            if ch == " ":
                if len(word) > 0:
                    wordCount += 1
                    word = ""
            else:
                word += str(ch)
                if len(word) > 0 and count == len(self.text):
                    wordCount += 1
                    word = ""
        return {"wordCount": wordCount}


# route
@app.route('/', methods=['GET'])
def welcome():
    """
    Description: 
        A welcome note to TextParse application.

    Returns:
        json: Welcome message and request body.
    """
    output = {"Message": "You are exploring the text parser application. In-order to test it, please install postman/curl and sent POST request to endpoint /analyze. Follow the instruction as given to complete the POST request.", "Request Body": {"text": "This is a valid sentence."}}
    return output, 200


@app.route('/analyze', methods=['POST'])
def analyze_text():
    """
    Description: 
        This function analyze any text string by parsing it. It accepts POST request from clients in application/json format. The endpoint of the POST request is /analyze.

    Returns:
        json: text string length (withSpace and withoutSpace), number of words in the text string and characters (alphabets) occurance in the text string.
    """
    body = request.get_json()
    text = body["text"]

    textParser = TextParser(text) # initialing TextParser
    textLength = textParser.getTextLength() # get textLength
    wordCount = textParser.getWordCount() # get wordCount

    #textParser_v2 = TextParser_v2(text)
    #textLength = textParser_v2.getTextLength()
    #wordCount = textParser_v2.getWordCount()
    
    characterCount = textParser.getCharacterCount() # get characterCount
    output = {"textLength":textLength, "wordCount":wordCount, "characterCount": characterCount}
    return output, 200



if __name__ == '__main__':
    app.run()