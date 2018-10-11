.data
T: .word 0xABCDEF00
best_matching_score: .word -1
best_matching_count: .word -1

Pattern_Array: .word 0, 1, 2, 3, 4, -1, -2, -3, -4, -5,
0xEEEEEEEE, 0x44448888, 0x77777777, 0x33333333, 0xAAAAAAAA,
0xFFFF0000, 0xFFFF, 0xCCCCCCCC, 0x66666666, 0x99999999

.text
lw $t4, 0x2000
lw $t6, 0x2004
lw $s7, 0x2008

# $t7 counter for number of matching bits
# $t6 for best matching score
# $s7 for best matching count

# Outer loop for looping through each value in the array
loop:
slti $t1, $t0, 20
beq $t1, $0, end_loop

add $t7, $0, $0
add $s0, $0, $0
lw $t3, 0x200C($t2)

# Inner loop that will loop through each of the 32 bits
# for the target, and the current value in the array
add $t5, $t4, $0
bit_counter_loop:
slti $s1, $s0, 32
beq $s1, $0, end_bit_counter_loop

andi $s4, $t3, 1
andi $s5, $t5, 1

# If the two bits match, branch to code that 
# will increment number of matching bits
# Else, branch to skip those instructions
beq $s4, $s5, add_to_counter
beq $0, $0, nothing_added

# Add to counter that will increment 
# the number of matching bits
add_to_counter:
addi $t7, $t7, 1

nothing_added:
# Increment counters
srl $t3, $t3, 1
srl $t5, $t5, 1

add $s0, $s0, 1

beq $0, $0, bit_counter_loop

end_bit_counter_loop:

# If the current number of matching bits
# is equal to the global number of matching
# bits, add to that score
# Otherwise, if it greater than the global,
# Set the global to the current, and set
# the count to 1
beq $t6, $t7, add_to_matching_count
slt $s1, $t7, $t6
beq $s1, $0, reset_score
j ignore

add_to_matching_count:
addi $s7, $s7, 1
beq $0, $0, ignore

reset_score:
add $t6, $0, $t7
addi $s7, $0, 1

ignore: 
addi $t0, $t0, 1
addi $t2, $t2, 4

beq $0, $0, loop

end_loop:
# Store value of best matching score and
# count of best matching score in memory
sw $t6, 0x2004($0)
sw $s7, 0x2008($0)
