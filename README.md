# ECE 366 Group 16 
### Members: 
* Arsalan Babar 
* Amaan Baiyat
## FLUX ISA

#### Registers:
 * General Purpose Registers:
    * $0, $1, $2, $3, $4, $5, $6, $7
 * Special Registers:
    * $RA - Used for JAL and JR commands

<table>
  <thead>
    <tr>
      <th>Instructions</th>
      <th>Examples</th>
      <th>Machine Code </th>
      <th> Functionality </th>
      <th> Range </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AND1</td>
      <td>AND1</td>
      <td>0 0 0 0 0 0 0</td>
      <td>R3 = R5 & 1</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>XOR</td>
      <td>XOR</td>
      <td>0 0 0 0 0 0 1</td>
      <td>R0 = R6 XOR R0</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>LD_R0</td>
      <td>LD_R0</td>
      <td>0 0 0 0 0 1 0</td>
      <td>R0 = M[R1]</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>JR</td>
      <td>JR</td>
      <td>0 0 0 0 0 1 1</td>
      <td>PC = $RA</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>SRL</td>
      <td>SRL</td>
      <td>0 0 0 0 1 1 0</td>
      <td>R5 = R5 >> 1</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>STR_R4</td>
      <td>STR_R4</td>
      <td>0 0 0 0 1 1 1</td>
      <td>M[R1] = R4</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>CNT0</td>
      <td>CNT0</td>
      <td>0 0 0 1 0 0 0</td>
      <td>R4 = #0s in R0</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>SLT108</td>
      <td>SLT108</td>
      <td>0 0 0 1 0 0 1</td>
      <td>If R1 < 108, R2 = 1</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>SRL_R3</td>
      <td>SRL_R3</td>
      <td>0 0 0 1 0 1 0</td>
      <td>R3 = R3 >> 1</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>SUB</td>
      <td>SUB</td>
      <td>0 0 0 1 0 1 1</td>
      <td>R6 = R6 - R4</td>
      <td>n/a</td>
    </tr>            
    <tr>
      <td>SUB1</td>
      <td>SUB1</td>
      <td>0 0 0 1 1 0 0</td>
      <td>R7 = R7 - 1</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>ADD_R0</td>
      <td>ADD_R0</td>
      <td>0 0 0 1 1 0 1</td>
      <td>R0 = R0 + R1</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>MOV</td>
      <td>MOV R1, R2</td>
      <td>0 0 1 X X Y Y</td>
      <td>RX = RY</td>
      <td>RX = 
      {R1, R2, R6, R7}

RY = {R0, R2, R6, R7}
</td>
    </tr>
    <tr>
      <td>SLT</td>
      <td>SLT RX, RY, RZ
      
SLT R6, R2, R3
</td>
      <td>0 1 0 0 X Y Z</td>
      <td>If X < Y, set Z to 1</td>
<td>RX = {R6,  R7}

RY = {R2, R4}

RZ = {R3, R5}
</td>
    </tr>          
    <tr>
      <td>EQL</td>
      <td>EQL R1, R7</td>
      <td>0 1 0 1 0 X Y</td>
      <td>If RX == RY, R3 = 1</td>
      <td>RX = {R0, R1}
      
RY = {R6, R7}
</td>
    </tr>
    <tr>
      <td>LD</td>
      <td>LD R4, 1</td>
      <td>0 1 0 1 1 X i</td>
      <td>RX = M[i]</td>
      <td>RX = {R4, R5}
      
Imm = {0, 1}
</td>
    </tr>
    <tr>
      <td>BEZU</td>
      <td>BEZU R3, 12</td>
      <td>0 1 1 X X m m</td>
      <td>If RX = 0, PC += imm</td>
      <td>RX = {R2, R3, R5, R7}
      
Imm = {2, 7, 10, 11} 
</td>
    </tr>
    <tr>
      <td>BEZ</td>
      <td>BEZ R1, 5</td>
      <td>1 0 0 X X m m</td>
      <td>If RX = 0, PC += imm</td>
      <td>RX ={R1, R3, R5, R7}  
      
Imm = {5, 13, 14, 25}
</td>
    </tr>
    <tr>
      <td>JMPN</td>
      <td>JMPN -3</td>
      <td>1 0 1 0 m m m</td>
      <td>PC += imm</td>
      <td>Imm = {-13, -10, -7, -4
                  
  -3, 2, 3, 4 }
</td>
    </tr>
    <tr>
      <td>STR</td>
      <td>STR R6, 5</td>
      <td>1 1 0 0 X i i</td>
      <td>M[i] = RX</td>
      <td>RX = {R0, R6}
      
Imm = {2, 3, 4, 5}
</td>
    </tr>
    <tr>
      <td>CLR</td>
      <td>CLR R0</td>
      <td>1 1 0 1 0 X X</td>
      <td>RX = 0</td>
      <td>RX = {R0, R1, R6,  R7}</td>
    </tr>
    <tr>
      <td>ADD1</td>
      <td>ADD1 R1</td>
      <td>1 1 0 1 1 X X</td>
      <td>RX = RX + 1</td>
      <td>RX = {R0, R1, R2, R6}</td>
    </tr>            
    <tr>
      <td>JAL</td>
      <td>JAL -6</td>
      <td>1 1 1 0 0 i i</td>
      <td>$ra = PC

PC += imm
</td>
      <td>imm = {-6, 5, 8, 9}</td>
    </tr>
  </tbody>
</table>