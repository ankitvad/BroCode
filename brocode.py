#BroCode: v0.1...{Initialisation_Phase}
#AnkitVadehra. (ankit-vadehra.co.nr)
#contact: ankitvad@gmail.com
'''A simple and approximate language, developed as a variant of BrainFuck Language.
Instead of a static array[30,000], initialised with 0, we use a [0]*300 list,
This is a simple List in Python. This helps save memory.

Tokens:
'<' :   Move_Left on tape.
'>' :   Move_Right o tape.
'+' :   Increment_Value_Of_The_Current_Cell by 1
'-' :   Decerement_Value_Of_The_Current_Cell by 1
'![n]' : n=[0,9]. If the current cell is non-zero, jump to the "nth" instruction.
',' :   Take in the Numerical value.
'a' :   Print_The_ASCII_Character
'.' :   Print_The_#_Value
'i' :   Take in the ASCII value and assign it to the cell on the tape.

A New Cell Initialisation is initialised with 0 ie. ASCII for NULL.
Since it is a static structure without any loop. Pre Initialised 300*[0] list. 

ASCII_Codes_Basic: [0->255]
7: 'Bell'
8: 'Backspace'
9: 'Horizontal_Tab'
11: 'Vertical_Tab'
32: 'Space'
{48-57}: [0-9]
{65-90}: [A-Z]
{97-122}: [a-z]

For further description of ASCII-Specific decimal values please check:
"http://www.ascii-code.com/"

#To use it, open your command line in the proper directory and 
run "python brocode.py [brocodeplaintext]".

eg: Code for Multipliation: ,>,<->->+>+<<!6>>-<<+>>!16<<<!4>>.
save in: mul.bro 

O/P : "python brocode.py mul.bro"

'''
from sys import stdin, stdout, argv, exit
def modify(token_file):
    """
    Taking the code and handling the !n jumps.
    """
    flag,result,next_step=0,[],'0123456789'
    while flag<len(token_file):
        if token_file[flag] in '><+-.a,i':
            result.append(token_file[flag])
        if token_file[flag]=='!':
            tmpr=''
            flag+=1
            if not token_file[flag] in next_step:
                exit('Parser found ! and expected a number; instead got {0} at instruction {1}'.format(instr[z],z))
            while token_file[flag] in next_step:
                tmpr+=token_file[flag]
                flag+=1
            result.append(int(tmpr))
            flag-=1
        flag+=1
    return result

def run_strip(token_file):
    """
    Code: has the converted value. Current_Pos: holds the current position of the pointer on the
    list. Initially it starts at 300/2 ie. 150. So equal space both ways.
    Index: Well, this is used to handle an index for the code list.
    Result: It stores the final Result. initially NULL.
    """
    code,current_pos,index,result = modify(token_file),150,0,''# Result is initialised as NULL initially.
    TAPE = [0]*300 #A Tape-List with 300 cells. All 0 initially.
    while current_pos<len(TAPE) and current_pos>=0 and index<len(code):# current_pos=[0,300].
        if code[index]=='>':    #Increment Pointer on TAPE..
            current_pos+=1
        if code[index]=='<':    #Decrement Pointer on TAPE..
            current_pos-=1
        if code[index]=='+':    #Increase Value of Cell..    
            TAPE[current_pos]+=1
        if code[index]=='-':     #Decrease Value of Cell..
            TAPE[current_pos]-=1
        if code[index]=='.':
            result+=(str(TAPE[current_pos])+' ')
        if code[index]=='a':
            result+=chr(TAPE[current_pos])
        if code[index]==',':
            stdout.write('#-->')
	    TAPE[current_pos]=int(stdin.readline())	
        if code[index]=='i':
            stdout.write('A-->')
	    TAPE[current_pos]=int(stdin.readline())
        if type(code[index])==int and TAPE[current_pos]!=0:
            index=code[index]
	else:
	    index+=1
    print result

if __name__ == '__main__':
	input_script = open(argv[1], 'r')#r Initialises the 'open' to only read a file. 
	token_file = input_script.read()
    #Any character other than the Tokens are automatically deleted.
	token_file = filter(lambda x:x in '><+-ai.,!0123456789',token_file)
	run_strip(token_file)
	input_script.close()