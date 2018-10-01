# ECE 366 Project 2 Disassembler
# Amaan Baiyat
# Arsalan Babar
# This file disassembles two project files

p1_input_file = open("project2_group_16_p1_bin.txt", "r")
p1_output_file = open("project2_group_16_p1_asm.txt", "w")

p2_input_file = open("project2_group_16_p2_bin.txt", "r")
p2_output_file = open("project2_group_16_p2_asm.txt", "w")



def convert_bin_to_asm(input_file, output_file):
    for line in input_file:

        if line == "\n":  # empty lines ignored
            continue
        line = line.replace("\n", "")  # remove 'endline' character
        print("Machine Instr: ", line)  # show the asm instruction to screen

        if (line == "0000"):
            output_file.write("ADD"+"\n")
        if (line == "0100"):
            output_file.write("SUB"+"\n")

convert_bin_to_asm(p1_input_file, p1_output_file)
convert_bin_to_asm(p2_input_file, p2_output_file)
