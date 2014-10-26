BroCode : A Fun Esoteric Programming Language. :D
======
<br><br>
A simple and approximate language, developed as a variant of BrainFuck Language.
Instead of a static array[30,000], initialised with 0, we use a [0]*300 list,
This is a simple List in Python. This helps save memory.<br>

PS: Since the '[]' loop in BrainFuck confuses me a Lot-Lot, ie. the Programming Part<br>
so, i removed that and instead worked on a normal tape and ASCII/Number i/p,o/p. 
It also has a jumping Goto statement. 


Tokens:
[code]
'<' :   Move_Left on tape.
'>' :   Move_Right o tape.
'+' :   Increment_Value_Of_The_Current_Cell by 1
'-' :   Decerement_Value_Of_The_Current_Cell by 1
'![n]' : n=[0,9]. If the current cell is non-zero, jump to the "nth" instruction.
',' :   Take in the Numerical value.
'a' :   Print_The_ASCII_Character
'.' :   Print_The_#_Value
'i' :   Take in the ASCII value and assign it to the cell on the tape.
[/code]<br>
A New Cell Initialisation is initialised with 0 ie. ASCII for NULL.
Since it is a static structure without any loop. Pre Initialised 300*[0] list. 
[code]
ASCII_Codes_Basic: [0->255]
7: 'Bell'
8: 'Backspace'
9: 'Horizontal_Tab'
11: 'Vertical_Tab'
32: 'Space'
{48-57}: [0-9]
{65-90}: [A-Z]
{97-122}: [a-z]
[/code]<br>
For further description of ASCII-Specific decimal values please check:
"http://www.ascii-code.com/"

#To use it, open your command line in the proper directory and 
run "python brocode.py [brocodeplaintext]".

eg: Code for Multipliation: ,>,<->->+>+<<!6>>-<<+>>!16<<<!4>>.
save in: mul.bro 

O/P : "python brocode.py mul.bro"

<br>
<h4>Some Examples can be found in the Example Folder. Quite Straight Forward.</h4.
