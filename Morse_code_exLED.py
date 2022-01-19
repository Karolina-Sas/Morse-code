import machine
import utime

Morse_dictionary={
    "A":"*-",
    "B":"-***",
    "C":"-*-*",
    "D":"-**",
    "E":"*",
    "F":"**-*",
    "G":"--*",
    "H":"****",
    "I":"**",
    "J":"*---",
    "K":"-*-",
    "L":"*-**",
    "M":"--",
    "N":"-*",
    "O":"---",
    "P":"*--*",
    "Q":"--*-",
    "R":"*-*",
    "S":"***",
    "T":"-",
    "U":"**-",
    "V":"***-",
    "W":"*--",
    "X":"-**-",
    "Y":"-*--",
    "Z":"--**",
    " ":" ",         
    }

LED_1=machine.Pin(15,machine.Pin.OUT)
LED_2=machine.Pin(14,machine.Pin.OUT)
LED_3=machine.Pin(12,machine.Pin.OUT)

def text_transformation():
    letters_list=[]
    tekst=input("Write a text: ")
    tekst=tekst.upper()
    for letter in tekst:
        letters_list.append(letter)
    print(letters_list)
    
    for list_letter in letters_list:
        for key,value in Morse_dictionary.items():
            if list_letter==key:
                print(list_letter,Morse_dictionary[key])
#                 print(Morse_dictionary[key])
                for sign in Morse_dictionary[key]:
                    utime.sleep(0.12)
                    if sign=="-":
                        
                        
                        LED_1.value(1)
                        LED_2.value(1)
                        LED_3.value(1)
                        utime.sleep(0.28)
                        LED_1.value(0)
                        LED_2.value(0)
                        LED_3.value(0)
                        utime.sleep(0.28)
                    elif sign=="*":
                        
                        LED_1.value(1)
                        LED_2.value(1)
                        LED_3.value(1)
                        utime.sleep(0.14)
                        LED_1.value(0)
                        LED_2.value(0)
                        LED_3.value(0)
                        utime.sleep(0.14)
                                                          
        
print(text_transformation())

