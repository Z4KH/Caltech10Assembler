; Zachary Pestrikov EE/CS10a HW 5
; This routine computes the greatest common divisor of two numbers, a and b 
 ;This routine implements Euclid's Subtraction Algorithm into the Caltech10 CPU
 ;It is an O(2^n) Algorithm
 ;8-bit Values a and b are stored in memory, and the GCD of the two values are returned

 ;Revision History:
  ;  2/10/2024   Zachary Pestrikov   Wrote Code for GCD Computing Program


#code
#org
initialize:
    LDD b
    CMPI 0         ;compare b to 0
    JZ  DONE            ;if b is 0, gcd is just a
    NOP
    LDD a           ; load a
    JMP COMPARISON  ;compare a and b
    NOP

COMPARISON:         ;compares a and b
    CMP b           ;compare a and b
    JGE WHILE       ;if a>=b, go to loop
    JL SWAP     ;swap if a<b
     NOP

WHILE:              ;loop through while b is at most a
    SUB b           ;subtracts b from a
    STD a         ;store a
    JMP COMPARISON  ;jump back to comparison
    NOP

ENDWHILE:           ;determines whether to go back to while loop
    LDD b           ;get b
    CMPI 0       ;compare b to 0
    JZ DONE         ;if b is 0, algorithm done
    NOP
    LDD a           ;load a
    JMP COMPARISON       ;if not 0, continue with loop
    NOP
    

SWAP:              ;swap a and b
	TAX			    ;put a in X temporariliy
	LDD   b 		;gets b
	STD   a		    ;stores b in a
	TXA			    ;get a back
	STD   b	    	;store a in b
  JMP ENDWHILE    ;go to ENDWHILE

DONE:               ;output GCD
    LDD a           ;load a
    RTS             ;return




#data
#byte a
#byte b
;00  ??  a   DB  ?   ;the variable a 
;01  ??  b   DB  ?   ;the variable b 



    

