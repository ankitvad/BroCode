BroCode : A Fun Esoteric Programming Language. :D
======
<br>
A simple and approximate language, developed as a variant of BrainFuck Language.
Instead of a static array[30,000], initialised with 0, we use a [0]*300 list,
This is a simple List in Python. This helps save memory.<br>

PS: Since the '[ ]' loop in BrainFuck confuses me a Lot-Lot, ie. the Programming Part<br>
so, i removed that and instead worked on a normal tape and ASCII/Number i/p,o/p. 
It also has a jumping Goto statement. 


Tokens:
<br>
'<' :   Move_Left on tape.<br>
'>' :   Move_Right o tape.<br>
'+' :   Increment_Value_Of_The_Current_Cell by 1<br>
'-' :   Decerement_Value_Of_The_Current_Cell by 1<br>
'![n]' : n=[0,9]. If the current cell is non-zero, jump to the "nth" instruction.<br>
',' :   Take in the Numerical value.<br>
'a' :   Print_The_ASCII_Character<br>
'.' :   Print_The_#_Value<br>
'i' :   Take in the ASCII value and assign it to the cell on the tape.<br>
<br>
A New Cell Initialisation is initialised with 0 ie. ASCII for NULL.
Since it is a static structure without any loop. Pre Initialised 300*[0] list. 
<br>
ASCII_Codes_Basic: [0->255]<br>
7: 'Bell'<br>
8: 'Backspace'<br>
9: 'Horizontal_Tab'<br>
11: 'Vertical_Tab'<br>
32: 'Space'<br>
{48-57}: [0-9]<br>
{65-90}: [A-Z]<br>
{97-122}: [a-z]<br>
<br>
For further description of ASCII-Specific decimal values please check:
"http://www.ascii-code.com/"
<br>
To use it, open your command line in the proper directory and 
run :<br>"python brocode.py [brocodeplaintext]"
<br>
eg: Code for Multipliation: ,>,<->->+>+<<!6>>-<<+>>!16<<<!4>>.
save in: mul.bro 

O/P : "python brocode.py mul.bro"

<br>
Some Examples can be found in the Example Folder. Quite Straight Forward.
