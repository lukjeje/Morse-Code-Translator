MORSE_CODE_DICT = { 'a':'.- ', 'b':'-... ',
                    'c':'-.-. ', 'd':'-.. ', 'e':'. ',
                    'f':'..-. ', 'g':'--. ', 'h':'.... ',
                    'i':'.. ', 'j':'.--- ', 'k':'-.- ',
                    'l':'.-.. ', 'm':'-- ', 'n':'-. ',
                    'o':'--- ', 'p':'.--. ', 'q':'--.- ',
                    'r':'.-. ', 's':'... ', 't':'- ',
                    'u':'..- ', 'v':'...- ', 'w':'.-- ',
                    'x':'-..- ', 'y':'-.-- ', 'z':'--.. ',
                    '1':'.---- ', '2':'..--- ', '3':'...-- ',
                    '4':'....- ', '5':'..... ', '6':'-.... ',
                    '7':'--... ', '8':'---.. ', '9':'----. ',
                    '0':'----- ', ', ':'--..-- ', '.':'.-.-.- ',
                    '?':'..--.. ', '/':'-..-. ', '-':'-....- ',
                    '(':'-.--. ', ')':'-.--.- ', ' ':' / '}

MORSE_CODE_DICT_2 = { '.-':'a', '-...':'b',
                    '-.-.':'c', '-..':'d', '.':'e',
                    '..-.':'f', '--.':'g', '....':'h',
                    '..':'i', '.---':'j', '-.-':'k',
                    '.-..':'l', '--':'m', '-.':'n',
                    '---':'o', '.--.':'p', '--.-':'q',
                    '.-.':'r', '...':'s', '-':'t',
                    '..-':'u', '...-':'v', '.--':'w',
                    '-..-':'x', '-.--':'y', '--..':'z',
                    '.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':', ', '.-.-.-':'.',
                    '..--..':'?', '-..-.':'/', '-....-':'-',
                    '-.--.':'(', '-.--.-':')', '/':' '}                    

def z():

 print("")

 print("Morse Code Translator")
 print("---------------------")

 print("")

 print("translete text to morse 'M' / translete morse to text 'T'")
 print("---------------------------------------------------------")

 print("")

 x = input("(M or T)>>> ")

 print("")



 if x == "M":
    print("write text")
    print("----------")

    print("")

    txt = input("(text)>>> ")
    lowtxt = txt.lower()
    print("")

    print("------")
    print("start")
    print("------")
    print("")

    for x in lowtxt:
        print(MORSE_CODE_DICT[x], end=" ")  
     
    print("")  
    print("")    
    print("------")
    print(" end")
    print("------")
    
    print("")

    cont = input("do you want to continue y/n: ")

    if cont == "y":
        z()
    else:
        print("")
        print("exit")    
   
 if x == "T":
    print("write morse")
    print("-----------")

    print ("")

    y = input("(morse)>>> ")
    splits = y.split()
    
    print("------")
    print("start")
    print("------")
    print("")    


    for x in splits:
       print(MORSE_CODE_DICT_2[x], end=" ")
    

    print("")  
    print("")    
    print("------")
    print(" end")
    print("------")
    
    cont2 = input("do you want to continue y/n: ")

    if cont2 == "y":
        z()
    else:
        print("")
        print("EXIT!") 

 print("")

z()
