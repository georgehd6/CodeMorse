#global var
#dict morse
dict_morse_code = {
        'a' : '.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-',
        'l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-',
        'w':'.--','x':'-..-','y':'-.--','z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
        '6':'-....','7':'--...','8':'---..','9':'----.','0':'-----', '/': ' ',
    }

#func to pass text to morse code
def text_to_Morse_Code(text):
    morse_code = ""
    for letter in text:
        if letter == " ":
            morse_code += "/ "
        else:
            morse_code += dict_morse_code[letter]
            morse_code += " "
    return morse_code

#func to pass code morse to text
def Morse_code_to_text(morse):
    new_text = ""
    morse_letter = ""
    for letter in morse:
        if letter == ' ':
            if morse_letter == '/':
                new_text += " "
                morse_letter = ""
            else:
                new_text += list(dict_morse_code.keys())[list(dict_morse_code.values()).index(morse_letter)]
                morse_letter = ""
        else:
            morse_letter += letter
    return new_text



text = input("Type text taht you want to pass to Morse Code: ")
morse_text = text_to_Morse_Code(text)
print(morse_text)
text = Morse_code_to_text(morse_text)
print(text)