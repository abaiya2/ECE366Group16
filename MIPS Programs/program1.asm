.data
P: .word 1005
R: .word -1 # R will be stored here
.text
    addi $2, $0, 1
    sw $2, 0x2004   # Save a one in result, useful in case of exponent=0
    addi $6, $0, 6  # load base
    lw $5, 0x2000   # load exponent
    addi $4, $0, 17  # load modulus argument       
loop_1:
    beq $5, $0, end    # we mostly skip most of the steps exponent_zero
    andi $3, $5, 1   # If not: we get the lowest bit value to use and operation between $5 and a constan a previous value 1
    beq  $3, $0, keep_going 
    add $1, $2, $0    
    add $7, $6, $0
    jal mult
    add $2, $8,$0
keep_going:
    add $1, $6, $0   # We elevate the base to the power of two
    add $7, $6, $0
    jal mult
    add $6, $8, $0
    jal mod
    srl $5, $5, 1   # We keep advancing to process the next bits
    j   loop_1        #Jump to keep processing
mult:      
    move $8, $0		     # Can use CLR in ISA
    beq  $1, $0, to_last_address    # if $3=0,  then return since result is 0
loop_2:
    beq  $7, $0, to_last_address    # if $7=0,  then return since result is 0
    add  $8, $8, $1                  
    addi $7, $7, -1       
    j    loop_2              # We keep goint until no more multiplication to be done
mod:
    slt $3, $6, $4  # If we found out that the number is already lower thant seventeen, then we're done
    beq $3, $0, skip_jump
    jr   $31
skip_jump:
    sub $6, $6, $4   
    j   mod           # Keep calculating mod
end:
    add  $6, $2, $0    # To calculate the mod 17 we make succesive substractions
    jal mod
    sw  $6, 0x2004         # We save the result
    j EXIT
to_last_address:
    jr   $31

EXIT:
