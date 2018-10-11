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
      <td>CLR</td>
      <td>CLR R0</td>
      <td>1 1 0 1 X X X</td>
      <td>RX = 0</td>
      <td>RX = {R0 - R7}</td>
    </tr>
    <tr>
      <td>ADD</td>
      <td>ADD R0, R1</td>
      <td>1 1 1 X X Y Y</td>
      <td> RX = RX + RY</td>
      <td>RX = {R0  R3, R6,  R7}
       RY = {R0, R2, R6, R7}

</td>
    </tr>
    <tr>
      <td>SUB</td>
      <td>SUB R0, R3</td>
      <td>1 1 0 0 X X Y</td>
      <td>RX = RX - RY</td>
      <td>RX = {R0, R1, R3, R7}
      RY = { R3, R7}
</td>
    </tr>
    <tr>
      <td>SLT</td>
      <td>SLT RX, RY</td>
      <td>0 0 1 X X Y Z</td>
      <td>If X < Y, set Z to 1</td>
      <td>RX = {R4, R7}
      RY = {R2, R3}
      RZ = {R3, R4}
</td>
    </tr>
    <tr>
      <td>JMPN</td>
      <td>JMPN -3</td>
      <td>1 0 1 m m m m</td>
      <td>PC += imm</td>
      <td>Imm = {-8:-1, 20, 1:6}</td>
    </tr>
    <tr>
      <td>BEZR2</td>
      <td>BEZR2 10</td>
      <td>1 0 0 m m m m</td>
      <td>f R2 = 0, PC += imm</td>
      <td>Imm = [4, 19]</td>
    </tr>
    <tr>
      <td>BEZR3</td>
      <td>BEZR3 12</td>
      <td>0 1 1 m m m m</td>
      <td>If R3 = 0, PC += imm</td>
      <td>Imm = {0, 15}</td>
    </tr>
    <tr>
      <td>EQL</td>
      <td>EQL R0, R7</td>
      <td>0 1 0 1 X X Y</td>
      <td>If RX == RY, R3 = 1</td>
      <td>RX={R0:R3} RY={R6,R7}</td>
    </tr>
    <tr>
      <td>ADD1</td>
      <td>ADD1 R1</td>
      <td>0 1 0 0 X X X</td>
      <td>RX = RX + 1</td>
      <td>RX = {R0, R7}</td>
    </tr>
    <tr>
      <td>STR</td>
      <td>STR 5</td>
      <td>0 0 0 1 1  i  i</td>
      <td>M[imm] = R0</td>
      <td>Imm = {2, 3, 4, 5}</td>
    </tr>
    <tr>
      <td>SLT108</td>
      <td>SLT108</td>
      <td>0 0 0 1 0 0 1</td>
      <td>If R1 < 108, R2 = 0</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>SLT16</td>
      <td>SLT16</td>
      <td>0 0 0 1 0 0 0</td>
      <td>If R3 < 16, R4 =  0</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>STR_R1</td>
      <td>STR_R1</td>
      <td>0 0 0 0 1 1 1</td>
      <td>M[R1] = R2</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>SRL</td>
      <td>SRL</td>
      <td>0 0 0 0 1 1 0</td>
      <td>R5 = R5 > 1</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>LD_R0</td>
      <td>LD_R0 R1</td>
      <td>0 0 0 0 0 1 X</td>
      <td>R0 = M[RX]</td>
      <td>RX={R1,R2}</td>
    </tr>
     <tr>
      <td>XOR</td>
      <td>XOR</td>
      <td>0 0 0 0 0 0 1 </td>
      <td>R5 = R6 xor R7</td>
      <td>N/A</td>
    </tr>
     <tr>
      <td>AND1</td>
      <td>AND1</td>
      <td>0 0 0 0 0 0 0</td>
      <td>R3 = R5 & 1</td>
      <td>N/A</td>
    </tr>
    
  </tbody>
</table>