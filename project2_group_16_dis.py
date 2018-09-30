# ECE 366 Project 2 Disassembler
# Amaan Baiyat
# Arsalan Babar
# This file disassembles two project files

p1_input_file = open("project2_group_16_p1_bin.txt", "r")
p1_output_file = open("project2_group_16_p1_asm.txt", "w")

p2_input_file = open("project2_group_16_p2_bin.txt", "r")
p2_output_file = open("project2_group_16_p2_asm.txt", "w")


def convert_asm_to_bin(input_file, output_file):
    for line in input_file:
        if (line == "0000"):
            output_file.write("ADD")



convert_asm_to_bin(p1_input_file, p1_output_file)
convert_asm_to_bin(p2_input_file, p2_output_file)



