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

        if line[0:4] == '1101':  # clear instruction
            op = line[0:4]
            rx = line[4:7]
            a = "CLR"
            d = int(rx, 2)
            output_file.write(
            str(a) + " " + '$' + str(d) + "\n")

        if line[0:3] == '111':  # add instruction
            op = line[0:3]
            rx = line[3:5]
            ry = line[5:7]

            if line[3:5]=='00':
                c = "R0"
            elif line[3:5]== '01':
                c="R3"
            elif line[3:5]== '10':
                c="R6"
            else:
                c = "$R7"

            if line[5:7] == '00':
                d = "R0"
            elif line[5:7] == '01':
                d = "R3"
            elif line[5:7] == '10':
                d = "R6"
            else:
                d = "R7"
            a = "ADD"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '$' + str(d) + "\n")

        if line[0:4] == '1100':  # Sub instruction
            op = line[0:4]
            rx = line[4:6]
            ry = line[6:7]

            if line[4:6]=='00':
                c = "R0"
            elif line[4:5]== '01':
                c="R3"
            elif line[4:6]== '10':
                c="R6"
            else:
                c = "R7"

            if line[6:7] == '0':
                d = "R3"
            else:
                d = "R7"
            a = "SUB"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '$' + str(d) + "\n")

        if line[0:3] == '001':  # SLT instruction
            op = line[0:3]
            rx = line[3:5]
            ry = line[5:6]
            rz = line[6:7]
            if line[3:5]=='00':
                c = "R4"
            else:
                c="R7"

            if line[5:6] == '0':
                d = "R2"
            else:
                d = "R3"
            a = "SLT"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '$' + str(d) + "\n")





convert_bin_to_asm(p1_input_file, p1_output_file)
convert_bin_to_asm(p2_input_file, p2_output_file)
