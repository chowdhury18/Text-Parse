from flask import Flask, jsonify, request, Response

app = Flask(__name__)

# route
@app.route('/analyze', methods=['POST'])
def analyze_text():
    body = request.get_json()
    text = body["text"]
    textLength = getTextLength(text)
    wordCount = getWordCount(text)
    characterCount = getCharacterCount(text)
    output = {"textLength":textLength, "wordCount":wordCount, "characterCount": characterCount}
    return output, 200

def getTextLength(text):
    withSpace = len(text)
    withoutSpace = withSpace - text.count(" ")
    return { "withSpaces":withSpace, "withoutSpaces":withoutSpace }

def getWordCount(text):
    wordCount = 0
    words = text.split(" ")
    for word in words:
        if len(word) > 0:
            wordCount += 1
    return {"wordCount": wordCount}

def getCharacterCount(text):
    text = text.lower()
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