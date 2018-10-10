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
            parity = line[7:8]
            output_file.write(
            str(a) + " " + '$' + str(d) + "\n")

        if line[0:3] == '111':  # add instruction
            op = line[0:3]
            rx = line[3:5]
            ry = line[5:7]
            parity = line[7:8]

            if line[3:5]=='00':
                c = "0"
            elif line[3:5]== '01':
                c="3"
            elif line[3:5]== '10':
                c="6"
            else:
                c = "7"

            if line[5:7] == '00':
                d = "0"
            elif line[5:7] == '01':
                d = "3"
            elif line[5:7] == '10':
                d = "6"
            else:
                d = "7"
            a = "ADD"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '$' + str(d) + "\n")

        if line[0:7] == '0001011':  # AND1 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "SUB"
            output_file.write(                         
                str(a) + "\n")





        if line[0:4] == '0100':  # SLT instruction
            op = line[0:4]
            rx = line[4:5]
            ry = line[5:6]
            rz = line[6:7]
            parity = line[7:8]
            if line[4:5]=='0':
                c = "6"
            else:
                c="7"

            if line[5:6] == '0':
                d = "2"
            else:
                d = "4"

            if line[6:7]=='0':
                e = "3"
            else:
                e = "5"
            a = "SLT"
            output_file.write(str(a) + " "+ '$' + str(c) + "," + " " + '$' + str(d) + "," + " " + '$' + str(e) + "\n")

        if line[0:3] == '101':  #JMPN instruction
            op = line[0:3]
            imm = line[3:7]
            parity = line[7:8]
            if line[3:7]=='0000':
                c = "-8"
            elif line[3:7] == '0001':
                c="-7"
            elif line[3:7] == '0010':
                c="-6"
            elif line[3:7] == '0011':
                c = "-5"
            elif line[3:7] == '0100':
                c = "-4"
            elif line[3:7] == '0101':
                c = "-3"
            elif line[3:7] == '0110':
                c = "-2"
            elif line[3:7] == '0111':
                c = "-1"
            elif line[3:7] == '1000':
                c = "1"
            elif line[3:7] == '1001':
                c = "2"
            elif line[3:7] == '1010':
                c = "3"
            elif line[3:7] == '1011':
                c = "4"
            elif line[3:7] == '1100':
                c = "5"
            elif line[3:7] == '1101':
                c = "6"
            else:
                c = "20"

            a = "JMPN"
            output_file.write(str(a) + " " + str(c) + "\n")
        if line[0:3] == '100':  # BEZR2 instruction
            op = line[0:3]
            imm = line[3:7]
            parity = line[7:8]
            if line[3:7] == '0000':
                c = "4"
            elif line[3:7] == '0001':
                c = "5"
            elif line[3:7] == '0010':
                c = "6"
            elif line[3:7] == '0011':
                c = "7"
            elif line[3:7] == '0100':
                c = "8"
            elif line[3:7] == '0101':
                c = "9"
            elif line[3:7] == '0110':
                c = "10"
            elif line[3:7] == '0111':
                c = "11"
            elif line[3:7] == '1000':
                c = "12"
            elif line[3:7] == '1001':
                c = "13"
            elif line[3:7] == '1010':
                c = "14"
            elif line[3:7] == '1011':
                c = "15"
            elif line[3:7] == '1100':
                c = "16"
            elif line[3:7] == '1101':
                c = "17"
            elif line[3:7] == '1110':
                c = "18"
            else:
                c = "19"

            a = "BEZR2"
            output_file.write(str(a) + " " + str(c) + "\n")


        if line[0:3] == '011':  #BEZR3 instruction
            op = line[0:3]
            imm = line[3:7]
            parity = line[7:8]
            a = "BEZR3"
            d = int(imm, 2)
            output_file.write(
            str(a) + " "+ str(d) + "\n")

            #ask amaan about equal instruction
        if line[0:4] == '0101':  # Equal instruction
            op = line[0:3]
            rx = line[4:6]
            ry = line[6:7]
            parity = line[7:8]

            c= int(rx, 2)
            if line[6:7] == '0':
                d = "6"
            else:
                d = "7"
            a = "EQL"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '$' + str(d)+"\n")



        if line[0:5] == '11011':  # ADD1 instruction
            op = line[0:5]
            rx = line[5:7]
            a = "ADD1"
            d = int(rx, 2)
            parity = line[7:8]
            output_file.write(
                str(a) + " " + "$" + str(d) + "\n")

        if line[0:5] == '00011':  # STORE instruction
            op = line[0:5]
            imm = line[5:7]
            parity = line[7:8]
            if line[5:7] == '00':
                c = "2"
            elif line[5:7] == '01':
                c = "3"
            elif line[5:7] == '10':
                c = "4"
            else:
                c = "5"
            a = "STR"
            output_file.write(str(a) + " " + str(c) + "\n")

        if line[0:7] == '0001010':  # SLR_R3 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "SRL_R3"
            output_file.write(
                str(a) + "\n")

        if line[0:7] == '0001001':  # SLT108 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "SLT108"
            output_file.write(
                str(a) + "\n")

        if line[0:7] == '0001000':  # CNT0 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "CNT0"
            output_file.write(
                str(a) + "\n")

        if line[0:7] == '0000111':  # STR_R4 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "STR_R4"
            output_file.write(
                str(a) + "\n")

        if line[0:7] == '0000110':  # SRL instruction
            op = line[0:7]
            parity = line[7:8]
            a = "SRL"
            output_file.write(
                str(a) + "\n")

        if line[0:7] == '0000010':  # LD_R0 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "LD_R0"
            output_file.write(
                str(a) + "\n")

        if line[0:7] == '0000001':  # XOR instruction
            op = line[0:7]
            parity = line[7:8]
            a = "XOR"
            output_file.write(
                str(a) + "\n")

        if line[0:7] == '0000000':  # AND1 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "AND1"
            output_file.write(
                str(a) + "\n")

        if line[0:5] == '00111':  #LD instruction
              op = line[0:5]
              rx = line[5:6]
              parity = line[7:8]
              imm= line[6:7]
              a = "LD"
              d = int(imm, 2)
              output_file.write(
              str(a) + " "+ str(d) + "\n")

        if line[0:7] == '0000011':  # JR instruction
             op = line[0:7]                                  
             parity = line[7:8]                              
             a = "JR"
             output_file.write(                          
                 str(a) + "\n")

        if line[0:5] == '00011':  # SUB1 instruction
            op = line[0:5]
            imm = line[5:7]
            parity = line[7:8]
            if line[5:7] == '00':
                c = "2"
            elif line[5:7] == '01':
                c = "3"
            elif line[5:7] == '10':
                c = "4"
            else:
                c = "5"
            a = "STR"
            output_file.write(str(a) + " " + str(c) + "\n")




convert_bin_to_asm(p1_input_file, p1_output_file)
convert_bin_to_asm(p2_input_file, p2_output_file)
