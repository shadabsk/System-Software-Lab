# Project Title

System Programming Experiments
* Counting the no of words, character, lines,  using lex
* Finding identifiers in C
* Removal of Left Recursion
* Finding the First of a grammar
* Finding the Follow of a grammar
* Implementation of Three Address Code Generation (3AC)

## Getting Started
* Use Python interpreter for left recursion, First, Follow & 3AC to execute the program.
* Use C Compiler to execute the identifier
* Use LEX & gcc to execute the lex experiment.

### Counting the no of words, character, lines,  using lex.
* Requires the lex system software and gcc installed in the system
* The input.txt contains necessary data and is supplied as an input to the program. counter.l is compiled with lex to obtain the lex.yy.c file. syntax is as below
```lex counter.l```
* gcc is used to compile the lex.yy.c file to get the final output. syntax is as below
```gcc lex.yy.c```

### Finding identifiers in C.
* Requires a gcc compiler.
* The program.c acts as an input to the program. Simply compile and run the identifier.c file.

### Removal of Left Recursion.
* Requires python interpreter.
* Follow the on-screen instruction for input syntax, simply run leftrec.py.
*

### Finding the First of a grammar.
* Requires python interpreter.
* Follow the on-screen instruction for input syntax, simply run First.py.

### Finding the Follow of a grammar.
* Requires python interpreter.
* Follow the on-screen instruction for input syntax, simply run Follow.py.

###  Implementation of Three Address Code Generation (3AC).
* Requires python interpreter.
* simply run 3AC.py.

### Prerequisites

* Python 3.* interpreter
* gcc compiler & lex compiler. Refer the following video for windows installation
```
https://www.youtube.com/watch?v=0MUULWzswQE
```

## Demonstrations (Valid set Sample inputs and output)
* Counting the no of words, character, lines,  using lex.
<p align="center">
  <img src="https://i.ibb.co/Dftn85c/Screenshot-at-2019-01-22-13-38-18.png" width="550" height="300"  title="output">
 </p>

* Finding identifiers in C.
<p align="center">
  <img src="https://i.ibb.co/nmVtTBx/output.jpg" width="550" height="300"  title="Output">
 </p>

 * Removal of Left Recursion.
<p align="center">
  ** Sample input 1  
  E->E+T/T
  <img src="https://i.ibb.co/TP0L4Mx/1.png" width="550" height="300"  title="Sample input 1">  
  ** Sample input 2  
  S->(L)/x  
  L->Ls/s  
  <img src="https://i.ibb.co/NCRLvcw/2.png" width="550" height="300"  title="Sample input 2">
 </p>

* Finding the First of a grammar.
<p align="center">
  ** Sample input 1  
  E->TA  
  A->+TA/€  
  T->FB  
  B->\*FB/€  
  F->id(E)  
  <img src="https://i.ibb.co/VQmJsCL/1.png" width="550" height="300" title="Sample input1">  
  ** Sample input 2    
  S->ACB/CbB/Ba  
  A->da/BC  
  B->g/€  
  C->b/€  
  F->id(E)  
  <img src="https://i.ibb.co/QY7KQ99/2.png" width="550" height="300" title="Sample input 2">
 </p>

* Finding the Follow of a grammar.
<p align="center">
 ** Sample input 1  
  E->TA  
  A->+TA/€  
  T->FB  
  B->\*FB/€  
  F->id(E)  
  <img src="https://i.ibb.co/VC5Sw1V/1.png" width="550" height="300" title="Sample input1">  
  ** Sample input 2    
  S->aABb  
  A->C/€  
  B->d/€    
  <img src="https://i.ibb.co/QY7KQ99/2.png" width="550" height="300" title="Sample input 2">
 </p>

 * Implementation of Three Address Code Generation (3AC).
<p align="center">
  <img src="https://i.ibb.co/pbH43vK/1-assignment.jpg" width="550" height="300" title="Sample input">
  <img src="https://i.ibb.co/hdDRzmq/2-non-assignment.jpg" width="550" height="300" title="Sample input 2">
 </p>



## Built With

* [Lex](http://dinosaur.compilertools.net/) - Computer program that generates lexical analyzers..
* [gcc](https://sourceforge.net/projects/tdm-gcc/) - Open source compiler.
* [Geany](https://www.geany.org/download) - IDE.
* [Python 3.\*](https://www.python.org/downloads/) -  Interpreted, high-level, general-purpose programming language.
## Authors

* **Shadab Shaikh** - [shadabsk](https://github.com/shadabsk)

## Acknowledgments

* The template of readme.md was taken from [PurpleBooth](https://github.com/PurpleBooth)
* A sincere thanks to my faculty Asst.Prof Mrs.Apeksha Gopale
* 3AC experiment Python Code has been referenced from JAVA Code available at [pracspedia] http://www.pracspedia.com/SPCC/3-address-code.html

