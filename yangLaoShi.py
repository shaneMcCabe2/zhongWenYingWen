# view the README markdown file for script details and documentation

# import googletrans module
# Installed alpha version to use translator
from googletrans import Translator


# main function for easy script execution from command line
def __main__():

    # ask for phrase to be reverse translated
    userInput = input('Reverse Translate: ')
    # call reverse translate function and pass in the translated phrase
    reverseTranslate(translateToZhongWen(userInput))

# this function will translate the inputed phrase to Chinese (simplified)
def translateToZhongWen(inputText):

    # translate() function translates text from source language to destination language
    translation = Translator().translate(text=inputText, dest='zh-cn', src='en')
    # output translation text(characters) and pronunciation(pinyin)
    print(translation.text + " " + translation.pronunciation)
    # return the translated text(characters)
    return translation.text


# takes in the translated phrase in Chinese and translates back to English
def reverseTranslate(inputTranslation):

    # reverse translate the passed in translation
    revTranslation = Translator().translate(text=inputTranslation, dest='en', src='zh-cn')
    # output text
    print(revTranslation.text)

# conditional to execute main function and enable easy importing/scripting of this file
if __name__ == '__main__':
    __main__()
