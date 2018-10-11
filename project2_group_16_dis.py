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

        if line[0:5] == '11010':  # clear instruction
            op = line[0:5]
            rx = line[5:7]
            a = "CLR"
            if line[5:7]== '00':
                d='0'
            elif line[5:7]=='01':
                d='1'
            elif line[5:7]=='10':
                d='6'
            else:
                d='7'
            parity = line[7:8]
            output_file.write(
            str(a) + " " + '$' + str(d) + "\n")
            #FUNCTIONALITY: RX=0         EXAMPLE OUTPUT: CLR R6
            #RANGE FOR RX {$0, $1, $6, $7}  00= $0 01=$1 10=$6 11=$7

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
            #FUNCTIONALITY: RX= RX+RY  EXAMPLE OUTPUT: ADD R0, R1
            #RANGE OF RX AND RY {$0,$3,$6,$7} 00=$0 01=$3 10=$6 11=$7
        if line[0:7] == '0001011':  # SUB instruction
            op = line[0:7]
            parity = line[7:8]
            a = "SUB"
            output_file.write(                         
                str(a) + "\n")
            #FUNCTIONALITY: R6 = R6 - R4   EXAMPLE OF OUTPUT: SUB


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
         #FUNCTIONALITY: If X < Y, SET Z TO 1    EXAMPLE OF OUTPUT: SLT RX, RY, RZ
         #RANGE FOR RX {$6,$7}  0=$6 1=$7                           SLT R6, R4, R3
         #RANGE FOR RY {$2,$4)  0=$2 1=$4
         #RANGE FOR RZ ($3,$5)  0=$3 1=$5

        if line[0:4] == '1010':  #JMPN instruction
            op = line[0:4]
            imm = line[4:7]
            parity = line[7:8]
            if line[4:7]=='000':
                c = "-13"
            elif line[3:7] == '001':
                c="-10"
            elif line[3:7] == '010':
                c="-7"
            elif line[3:7] == '011':
                c = "-4"
            elif line[3:7] == '100':
                c = "-3"
            elif line[3:7] == '101':
                c = "2"
            elif line[3:7] == '110':
                c = "3"
            else:
                c = "4"
            a = "JMPN"
            output_file.write(str(a) + " " + str(c) + "\n")
            #FUNCTIONALITY:PC += imm        EXAMPLE OUTPUT: JMPN -13
            #RANGE OF Imm {-13,-10, -7, -4, -3, 2, 3, 4}
            #000=-13 001=-10 010=-7 011=-4 100=-3 101=2 110=3 111=4

        if line[0:5] == '01010':  # Equal instruction
            op = line[0:5]
            rx = line[5:6]
            ry = line[6:7]
            parity = line[7:8]

            c= int(rx, 2)
            if line[6:7] == '0':
                d = "6"
            else:
                d = "7"
            a = "EQL"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '$' + str(d)+"\n")
             #FUNCTIONALITY: If RX == RY, R3 = 1    EXAMPLE OF OUTPUT: EQL R1, R7
             #RANGE FOR RX FROM $0-$3
             #RANGE FOR RY {$6,$7)

        if line[0:5] == '11011':  # ADD1 instruction
            op = line[0:5]
            rx = line[5:7]

            if line[5:7]=='00':
                 c = "0"
            elif line[5:7]== '01':
                 c="1"
            elif line[5:7]== '10':
                 c="2"
            else:
                 c = "6"
            parity = line[7:8]
            a = "ADD1"
            output_file.write(
                str(a) + " " + "$" + str(c) + "\n")
            #FUNCTIONALITY: RX = RX + 1   EXAMPLE OUTPUT: ADD1 R1
            #RANGE OF RX  {$0,$1,$2,$6)
        if line[0:4] == '1100':  # STORE instruction
            op = line[0:4]
            RX = line[4:5]
            imm = line[5:7]
            parity = line[7:8]
            if line [4:5]== '0':
                d='0'
            else:
                d='6'
            if line[5:7] == '00':
                c = "2"
            elif line[5:7] == '01':
                c = "3"
            elif line[5:7] == '10':
                c = "4"
            else:
                c = "5"
            a = "STR"
            output_file.write(str(a) + " " + "$"+ str(d) + "," +" "+ str(c) + "\n")
            #FUNCTION: M[imm] = RX     EXAMPLE OUTPUT: STR R6,5
            #RANGE OF RX {$0,$6} 0=$0 1=$6
            #RANGE OF IMM {2,3,4,5} 00=2 01=3 10=4 11=5

        if line[0:7] == '0001010':  # SLR_R3 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "SRL_R3"
            output_file.write(
                str(a) + "\n")
            #FUNCTIONALITY: R3 = R3 >> 1   EXAMPLE OF OUTPUT: SRL_R3

        if line[0:7] == '0001001':  # SLT108 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "SLT108"
            output_file.write(
                str(a) + "\n")
            #FUNCTIONALITY: If R1 < 108, R2 = 0    EXAMPLE OF OUTPUT: SLT108

        if line[0:7] == '0001000':  # CNT0 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "CNT0"
            output_file.write(
                str(a) + "\n")
             #FUNCTIONALITY: R4 = #0s in R0     EXAMPLE OF OUTPUT: CNT0

        if line[0:7] == '0000111':  # STR_R4 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "STR_R4"
            output_file.write(
                str(a) + "\n")
             #FUNCTIONALITY: M[R1] = R4    EXAMPLE OF OUTPUT: STR_R4

        if line[0:7] == '0000110':  # SRL instruction
            op = line[0:7]
            parity = line[7:8]
            a = "SRL"
            output_file.write(
                str(a) + "\n")
            #FUNCTIONALITY: R5 = R5 > 1    EXAMPLE OF OUTPUT: SRL


        if line[0:7] == '0000010':  # LD_R0 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "LD_R0"
            output_file.write(
                str(a) + "\n")
             #FUNCTIONALITY: R0 = M[R1]   EXAMPLE OF OUTPUT: LD_R0

        if line[0:7] == '0000001':  # XOR instruction
            op = line[0:7]
            parity = line[7:8]
            a = "XOR"
            output_file.write(
                str(a) + "\n")
            #FUNCTIONALITY: R0 = R6 xor R0   EXAMPLE OF OUTPUT: XOR

        if line[0:7] == '0000000':  # AND1 instruction
            op = line[0:7]
            parity = line[7:8]
            a = "AND1"
            output_file.write(
                str(a) + "\n")
            #FUNCTIONALITY: R3 = R5 & 1    EXAMPLE OF OUTPUT: AND1

        if line[0:5] == '01011':  #LD instruction
              op = line[0:5]
              rx = line[5:6]
              parity = line[7:8]
              imm= line[6:7]
              if line[5:6]== '0':
                  c="4"
              else:
                  c="5"
              d = int(imm, 2)
              
              a = "LD"

              output_file.write(
              str(a) + " "+ "$" + str(c)+ ","+ " "+  str(d) + "\n")
             #FUNCTIONALITY: R5 = M[i]    EXAMPLE OF OUTPUT: LD R4, 1
             #RANGE OF RX {$4,$5) 0=$4 1=$5  RANGE OF IMM {0,1}

        if line[0:7] == '0000011':  # JR instruction
             op = line[0:7]                                  
             parity = line[7:8]                              
             a = "JR"
             output_file.write(                          
                 str(a) + "\n")

            #FUNCTIONALITY: PC = $RA    EXAMPLE OF OUTPUT: JR


        if line[0:5] == '00011':  # SUB1 instruction
            op = line[0:5]
            imm = line[5:7]
            parity = line[7:8]
            if line[5:7] == '00':
                c = "4"
            elif line[5:7] == '01':
                c = "5"
            elif line[5:7] == '10':
                c = "6"
            else:
                c = "7"
            a = "SUB1"
            output_file.write(str(a) + " " + "$"+ str(c) + "\n")
            #FUNCTIONALITY: RX = RX - 1    EXAMPLE OF OUTPUT: SUB1 $7
            #RANGE FOR RX FROM $4-$7  00=$4 01=$5 10=$6 11=$7

        if line[0:3] == '001':  #MOV instruction
            op = line[0:3]
            RX = line[3:5]
            RY = line[5:7]
            parity = line[7:8]                                           
            if line[3:5] == '00':
                c = "1"
            elif line[3:5] == '01':
                c = "2"
            elif line[3:5] == '10':
                c = "6"
            else:
                c = "7"
            if line[5:7] == '00':
                d= "0"
            elif line[5:7] == '01':
                d = "2"
            elif line[5:7] == '10':
                d = "6"
            else:
                d = "7"
            a = "MOV"
            output_file.write(str(a) + " " + "$"+ str(c) + "," + " " + "$" + str(d) + "\n")
            #FUNCTIONALITY: RX = RY    EXAMPLE OF OUTPUT: MOV R1,R2
            #RANGE FOR RX {$1,$2,$6,$7}  00=$1 01=$2 10=$6 11=$7
            #RANGE FOR RY {$0,$2,$6,$7)  00=$0 01=$2 10=$6 11=$7

        if line[0:3] == '011':  # BEZU instruction
             op = line[0:3]
             RX = line[3:5]
             imm= line[5:7]
             parity = line[7:8]
             if line[3:5] == '00':
                 c = "2"
             elif line[3:5] == '01':
                 c = "3"
             elif line[3:5] == '10':
                 c = "5"
             else:
                 c = "7"

             if line[5:7] == '00':
                  d = "2"
             elif line[5:7] == '01':
                  d = "7"
             elif line[5:7] == '10':
                  d = "10"
             else:
                  d = "11"
             a = "BEZU"
             output_file.write(str(a) + " " + "$"+ str(c) + ","+" " + str(d) + "\n")
             #FUNCTIONALITY: If R3 = 0, PC += imm   EXAMPLE OF OUTPUT: BEZU R3, 12
             #RANGE FOR RX {$2,$3,$5,$7}  00=$2 01=$3 10=$5 11=$7
             #RANGE FOR Imm {2,7,10,11}
             #00=2 01=7 10=10 11=11
        if line[0:3] == '100':  # BEZ instruction
           op = line[0:3]
           RX = line[3:5]
           imm= line[5:7]
           parity = line[7:8]
           if line[3:5] == '00':
               c = "1"
           elif line[3:5] == '01':
               c = "3"                                                             
           elif line[3:5] == '10':
               c = "5"
           else:
               c = "7"

           if line[5:7] == '00':
                d = "5"
           elif line[5:7] == '01':
                d = "13"
           elif line[5:7] == '10':
                d = "14"
           else:
                d = "25"
           a = "BEZ"
           output_file.write(str(a) + " " + "$"+ str(c) + ","+" " + str(d) + "\n")
           #FUNCTIONALITY: If RX = 0, PC += imm    EXAMPLE OF OUTPUT: BEZ R2, 10
           #RANGE FOR RX {$1,$3,$5,$7} 00=$1 01=$3 10=$5 11=$5
           #RANGE FOR Imm {5,13,14,25} 00=5 01=13 10=14 11=25
        if line[0:5] == '00110':  # JAL instruction
           op = line[0:5]
           imm= line[5:7]
           parity = line[7:8]
           if line[5:7] == '00':
               c = "-6"
           elif line[5:7] == '01':
               c = "5"
           elif line[5:7] == '10':
               c = "8"
           else:
               c = "9"
           a = "JAL"
           output_file.write(str(a) + " " + str(c) + "\n")
           #FUNCTIONALITY:$ra = PC     EXAMPLE OF OUTPUT: JAL 10
           #              PC += imm
           #RANGE OF Imm {-6,5,8,9}
           # 00=-6 01=5 10=8 11=9








convert_bin_to_asm(p1_input_file, p1_output_file)
convert_bin_to_asm(p2_input_file, p2_output_file)
