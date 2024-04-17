def Binary_convertor(a,b):
    a=int(a)
    temp = abs(a)
    s='1'
    while(temp>0):
        last_digit = temp%2
        s = str(int(s)*10+last_digit)
        temp=temp//2
    s=s[1:]
    s=s[::-1]
    length = len(s)
    remaining = b-length
    if(remaining>0):
        s='0'*remaining+s
    if(a<0):
      inverted_bits =''.join('1' if bit == '0' else '0' for bit in s)
      result = bin(int(inverted_bits, 2) + 1)[2:]
      s=result.zfill(len(s))
    return s

def Decimal_converter(binary):
    # Check if the number is negative
    if binary[0] == '1':
        # Convert the binary number to its decimal value
        decimal = int(binary, 2)
        # Invert the bits
        inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary)
        # Add 1 to get the positive value
        positive_value = int(inverted_bits, 2) + 1
        # Convert to negative by multiplying with -1
        decimal = -positive_value
    else:
        # If the number is positive, convert it directly to decimal
        decimal = int(binary, 2)
    return decimal

def binary_to_decimal(binary_str):
    decimal = 0
    power = len(binary_str) - 1
    for digit in binary_str:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def Binary_xor(bin1, bin2):
    # Make sure both binary strings have the same length
    length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(length)
    bin2 = bin2.zfill(length)
    
    # Perform bitwise XOR
    result = ''
    for i in range(length):
        if bin1[i] != bin2[i]:
            result += '1'
        else:
            result += '0'
    
    return result

def sign_extend(binary_num, num_bits):
    # Check if the number is negative (sign bit is 1)
    if binary_num[0] == '1':
        # Extend with 1s
        extended_num = '1' * (num_bits - len(binary_num)) + binary_num
    else:
        # Extend with 0s
        extended_num = '0' * (num_bits - len(binary_num)) + binary_num
    
    return extended_num

datamemory={'0x00010000':'0b00000000000000000000000000000000',
            '0x00010004':'0b00000000000000000000000000000000',
            '0x00010008':'0b00000000000000000000000000000000',
            '0x0001000c':'0b00000000000000000000000000000000',
            '0x00010010':'0b00000000000000000000000000000000',
            '0x00010014':'0b00000000000000000000000000000000',
            '0x00010018':'0b00000000000000000000000000000000',
            '0x0001001c':'0b00000000000000000000000000000000',
            '0x00010020':'0b00000000000000000000000000000000',
            '0x00010024':'0b00000000000000000000000000000000',
            '0x00010028':'0b00000000000000000000000000000000',
            '0x0001002c':'0b00000000000000000000000000000000',
            '0x00010030':'0b00000000000000000000000000000000',
            '0x00010034':'0b00000000000000000000000000000000',
            '0x00010038':'0b00000000000000000000000000000000',
            '0x0001003c':'0b00000000000000000000000000000000',
            '0x00010040':'0b00000000000000000000000000000000',
            '0x00010044':'0b00000000000000000000000000000000',
            '0x00010048':'0b00000000000000000000000000000000',
            '0x0001004c':'0b00000000000000000000000000000000',
            '0x00010050':'0b00000000000000000000000000000000',
            '0x00010054':'0b00000000000000000000000000000000',
            '0x00010058':'0b00000000000000000000000000000000',
            '0x0001005c':'0b00000000000000000000000000000000',
            '0x00010060':'0b00000000000000000000000000000000',
            '0x00010064':'0b00000000000000000000000000000000',
            '0x00010068':'0b00000000000000000000000000000000',
            '0x0001006c':'0b00000000000000000000000000000000',
            '0x00010070':'0b00000000000000000000000000000000',
            '0x00010074':'0b00000000000000000000000000000000',
            '0x00010078':'0b00000000000000000000000000000000',
            '0x0001007c':'0b00000000000000000000000000000000'}

register_dict = {'00000':'0b00000000000000000000000000000000',
                 '00001':'0b00000000000000000000000000000000',
                 '00010':'0b00000000000000000000000100000000',
                 '00011':'0b00000000000000000000000000000000',
                 '00100':'0b00000000000000000000000000000000',
                 '00101':'0b00000000000000000000000000000000',
                 '00110':'0b00000000000000000000000000000000',
                 '00111':'0b00000000000000000000000000000000',
                 '01000':'0b00000000000000000000000000000000',
                 '01001':'0b00000000000000000000000000000000',
                 '01010':'0b00000000000000000000000000000000',
                 '01011':'0b00000000000000000000000000000000',
                 '01100':'0b00000000000000000000000000000000',
                 '01101':'0b00000000000000000000000000000000',
                 '01110':'0b00000000000000000000000000000000',
                 '01111':'0b00000000000000000000000000000000',
                 '10000':'0b00000000000000000000000000000000',
                 '10001':'0b00000000000000000000000000000000',
                 '10010':'0b00000000000000000000000000000000',
                 '10011':'0b00000000000000000000000000000000',
                 '10100':'0b00000000000000000000000000000000',
                 '10101':'0b00000000000000000000000000000000',
                 '10110':'0b00000000000000000000000000000000',
                 '10111':'0b00000000000000000000000000000000',
                 '11000':'0b00000000000000000000000000000000',
                 '11001':'0b00000000000000000000000000000000',
                 '11010':'0b00000000000000000000000000000000',
                 '11011':'0b00000000000000000000000000000000',
                 '11100':'0b00000000000000000000000000000000',
                 '11101':'0b00000000000000000000000000000000',
                 '11110':'0b00000000000000000000000000000000',
                 '11111':'0b00000000000000000000000000000000'}
def instruction_add(a,b):
    temp1 = Decimal_converter(a) #rs1  # a into decimal
    temp2 = Decimal_converter(b) #rs2  # b into decimal
    ans = temp1 + temp2
    ans_str=Binary_convertor(ans,32)
    return ans_str  # to be stored in rd

def instruction_sub(a,b):
    temp1 = Decimal_converter(a)  # a into decimal
    temp2 = Decimal_converter(b)  # b into decimal
    ans = temp1 - temp2
    ans_str = Binary_convertor(ans,32)
    return ans_str

def instruction_slt(a,b):
    temp1 = Decimal_converter(a)  #rs1
    temp2 = Decimal_converter(b)  #rs2
    ans0=Binary_convertor(0,32)
    ans1=Binary_convertor(1,32)
    if(temp2>temp1):
        return ans1
    else:
        return ans0

def instruction_sltu(a,b):
    temp1 = binary_to_decimal(a)  #rs1
    temp2 = binary_to_decimal(b)  #rs2
    ans0=Binary_convertor(0,32)
    ans1=Binary_convertor(1,32)
    if(temp2>temp1):
        return ans1
    else:
        return ans0
    
def instruction_xor(a,b):
    return Binary_xor(a,b) # to be stored in rd
    
def instruction_sll(a,b):
    #a rs1
    temp_a = int (a,2)
    temp = b[-5:]#b rs2
    num = binary_to_decimal(temp)
    ans = temp_a<<num
    # return ans[-32::]
    return format(ans, '032b')

def instruction_srl(a,b):
    #a rs1
    #b rs2
    temp_a = int (a,2)
    temp = b[-5:]#a rs1
    num = binary_to_decimal(temp)
    ans = temp_a>>num
    # return ans[-32::]
    return format(ans, '032b')
    
def instruction_or(a,b):
    temp1 = int(a,2)  #rs1
    temp2 = int(b,2)  #rs2
    ans = a|b
    final_ans =Binary_convertor(ans,32)
    return final_ans  # to be stored in rd

def instruction_and(a,b):
    temp1 = int(a,2)  #rs1
    temp2 = int(b,2)  #rs2
    ans = a&b
    final_ans =Binary_convertor(ans,32)
    return final_ans # to be stored in rd


def r_type(data):
    global PC
    opcode = data[-7::]
    rd = data[-12:-7]
    funct3 = data[-15:-12]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    funct7 = data[-32:-25]
    
    if (funct3=='000' and funct7=='0000000'): #add
        register_dict[rd] = "0b"+instruction_add(register_dict[rs1][2:],register_dict[rs2][2:])
    if(funct7=='000' and funct7=='0100000'): #sub
        register_dict[rd] ="0b" +instruction_add(register_dict[rs1][2:],register_dict[rs2][2:])
    if(funct3=='001'): #sll
        register_dict[rd] ="0b" +instruction_sll(register_dict[rs1][2:],register_dict[rs2][2:])
    if(funct3=='010'): #slt
        register_dict[rd] ="0b" +instruction_slt(register_dict[rs1][2:],register_dict[rs2][2:])
    if(funct3=='011'): #sltu
        register_dict[rd] ="0b"+instruction_sltu(register_dict[rs1][2:],register_dict[rs2][2:])
    if(funct3=='100'): #xor
        register_dict[rd] ="0b"+instruction_xor(register_dict[rs1][2:],register_dict[rs2][2:])
    if(funct3=='101'): #srl
        register_dict[rd] ="0b"+instruction_srl(register_dict[rs1][2:],register_dict[rs2][2:])
    if(funct3=='110'): #or
        register_dict[rd] ="0b"+instruction_or(register_dict[rs1][2:],register_dict[rs2][2:])
    if(funct3=='111'): #and
        register_dict[rd] ="0b"+instruction_and(register_dict[rs1][2:],register_dict[rs2][2:])
    PC = instruction_add(PC,Binary_convertor(4,32))

PC='0'*32    
def i_type(data):
    global PC
    opcode = data[-7::]
    rd = data[-12:-7]
    funct3 = data[-15:-12]
    rs1 = data[-20:-15]
    imm = data[-32:-20]
    if funct3=='010':
        #lw
        temp=instruction_add(register_dict[rs1][2:],sign_extend(imm,32))
        # temp=hex(int(temp,2))[2:]
        temp1=hex(int(temp,2))[2:].lstrip('0')
        temp1='0x' + temp1.zfill(10- 2)
        register_dict[rd]=datamemory[temp1]
    
    elif funct3 == '000' and opcode=='0010011':  
        #addi
        register_dict[rd]="0b"+instruction_add(register_dict[rs1][2:],sign_extend(imm,32))
    elif funct3 == '011':
        #sltiu
        if binary_to_decimal(register_dict[rs1][2:])<binary_to_decimal(imm):
            register_dict[rd]="0b"+Binary_convertor(1,32)
    else:
        global PC
        register_dict[rd]=instruction_add(PC,Binary_convertor(4,32))
        PC=instruction_add(register_dict[rs1][2:],sign_extend(imm,32))
        PC=PC[:-1]+'0'
    PC = instruction_add(PC,Binary_convertor(4,32))

def s_type(data):
    global PC
    opcode = data[-7::]
    imm1 = data[-12:-7]
    funct3 = data[-15:-12]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    imm2 = data[-32:-25]
    imm =imm2+imm1
    temp=instruction_add(register_dict[rs1][2:],sign_extend(imm,32))
    # temp=hex(int(temp,2)).zfill(8)
    # register_dict[rs2]=datamemory[temp]
    # temp=hex(int(temp,2))[2:]
    temp1=hex(int(temp,2))[2:].lstrip('0')
    temp1='0x' + temp1.zfill(10- 2)
    register_dict[rs2]=datamemory[temp1]
    PC = instruction_add(PC,Binary_convertor(4,32))
def b_type(data):
    global PC
    opcode = data[-7::]
    # imm1 = data[12:-7]
    funct3 = data[-15:-12]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    # imm2 = data[-32:-25]
    imm = data[0] + data[-8] + data[1:7] +data[-12:-8]+"0"
    # imm=  to be done
    temp_PC = Decimal_converter(PC)//4
    temp_imm = Decimal_converter(sign_extend(imm,32))
    ans_PC = (temp_imm+temp_PC) *4
    if(funct3=='000'):
        if(rs1==rs2): #beq
            # PC=instruction_add(PC,sign_extend(imm,32)) # imm 12:1
            PC = Binary_convertor(ans_PC,32)
    if(funct3=='001'):
        if(rs1!=rs2):
            # PC=instruction_add(PC,sign_extend(imm,32)) # imm 12:1
            PC = Binary_convertor(ans_PC,32)
    if(funct3=='100'):
        if(Decimal_converter(rs1)>=Decimal_converter(rs2)):
            # PC=instruction_add(PC,sign_extend(imm,32)) # imm 12:1
            PC = Binary_convertor(ans_PC,32)
    if(funct3=='101'):
        if(binary_to_decimal(rs1)>=binary_to_decimal(rs2)):
            # PC=instruction_add(PC,sign_extend(imm,32)) # imm 12:1
            PC = Binary_convertor(ans_PC,32)
    if(funct3=='110'):
        if(Decimal_converter(rs1)<Decimal_converter(rs2)):
            # PC=instruction_add(PC,sign_extend(imm,32)) # imm 12:1
            PC = Binary_convertor(ans_PC,32)
    if(funct3=='111'):
        if(binary_to_decimal(rs1)<binary_to_decimal(rs2)):
            # PC=instruction_add(PC,sign_extend(imm,32)) # imm 12:1
            PC = Binary_convertor(ans_PC,32)
    # if(rs1==rs2): #ne
    # PC = instruction_add(PC,Binary_convertor(4,32))
def u_type(data):
    global PC
    opcode = data[-7::]
    rd = data[-12:-7]
    imm = data[-32:-12]
    if opcode=="0110111":
        #lui
        register_dict[rd]=imm+("0"*12)
    else:
        #auipe
        register_dict[rd]=instruction_add(PC,imm+("0"*12))
    PC = instruction_add(PC,Binary_convertor(4,32))
def j_type(data):
    global PC
    opcode = data[-7::]
    rd = data[-12:-7]
    imm = data[-32:-12]
    global PC
    register_dict[rd]=instruction_add(PC,Binary_convertor(4,32))
    PC=instruction_add(PC,sign_extend(imm+"0",32))
    PC=PC[:-1]+'0'
    # PC = instruction_add(PC,Binary_convertor(4,32))
def default_case(data):
    print("error: ",data[0],)
    return

def Switch_case(case_value,data):
    switch_dict = {
         '0110011': r_type,
         '0000011': i_type,
         '0010011': i_type,
         '1100111': i_type,
         '0100011': s_type,
         '1100011': b_type,
         '0110111': u_type,
         '0010111': u_type,
         '1101111': j_type,
    }
    switch_dict.get(case_value,default_case)(data)
file_name = input("Enter the file name: ")
with open(file_name,"+r") as input_file:
    lines = [line.rstrip('\n') for line in input_file.readlines()]
    while((Decimal_converter(PC)//4)<=len(lines)):
    # if(True):
        a=lines[Decimal_converter(PC)//4] 
        if not a:
            break
        if not a.strip():  #for skipping empty lines
            continue
        # a=a[::-1]
        Switch_case(a[-7::],a)  #-1:-8:-1
        # break
        print("0b"+PC,end=" ")
        for key,value in register_dict.items():
            print(value,end=" ")
        print('\n')

        if (Decimal_converter(PC)//4 ==11):  # error in line 11
            break
            # print(key,":",value,end=" ")
        #  '0110011': r_type,
        #  '0000011': i_type,
        #  '0010011': i_type,
        #  '1100111': i_type,
        #  '0100011': s_type,
        #  '1100011': b_type,
        #  '0110111': u_type,
        #  '1101111': j_type,
#register_dict = {'00000':'0b0000000000000000000000000000','00001':'0b0000000000000000000000000000','00010':'0b0000000000000000000000000000','00011':'0b0000000000000000000000000000','00100':'0b0000000000000000000000000000','00101':'0b0000000000000000000000000000','00110':'0b0000000000000000000000000000','00111':'0b0000000000000000000000000000','01000':'0b0000000000000000000000000000','01010':'0b0000000000000000000000000000','01011':'0b0000000000000000000000000000','01100':'0b0000000000000000000000000000','01101':'0b0000000000000000000000000000','01110':'0b0000000000000000000000000000','01111':'0b0000000000000000000000000000','10000':'0b0000000000000000000000000000','10001':'0b0000000000000000000000000000','10010':'0b0000000000000000000000000000','10011':'0b0000000000000000000000000000','10100':'0b0000000000000000000000000000','10101':'0b0000000000000000000000000000','10110':'0b0000000000000000000000000000','10111':'0b0000000000000000000000000000','11000':'0b0000000000000000000000000000','11001':'0b0000000000000000000000000000','11010':'0b0000000000000000000000000000','11011':'0b0000000000000000000000000000','11100':'0b0000000000000000000000000000','11101':'0b0000000000000000000000000000','11110':'0b0000000000000000000000000000','11111':'0b0000000000000000000000000000'}
    '''
    
def reg_convertor(register):
    if(Decimal_converter(register)==0):
        return 'zero'
    if(Decimal_converter(register)==1):
        return 'ra'
    if(Decimal_converter(register)==2):
        return 'sp'
    if(Decimal_converter(register)==3):
        return 'gp'
    if(Decimal_converter(register)==4):
        return 'tp'
    if(Decimal_converter(register)==5):
        return 't0'
    if(Decimal_converter(register)==6):
        return 't1'
    if(Decimal_converter(register)==7):
        return 't2'
    if(Decimal_converter(register)==8):
        return 's0'  # assumed s0 can be fp
    if(Decimal_converter(register)==9):
        return 's1'
    if(Decimal_converter(register)==10):
        return 'a0'
    if(Decimal_converter(register)==11):
        return 'a1'
    if(Decimal_converter(register)==12):
        return 'a2'
    if(Decimal_converter(register)==13):
        return 'a3'
    if(Decimal_converter(register)==14):
        return 'a4'
    if(Decimal_converter(register)==15):
        return 'a5'
    if(Decimal_converter(register)==16):
        return 'a6'
    if(Decimal_converter(register)==17):
        return 'a7'
    if(Decimal_converter(register)==18):
        return 's2'
    if(Decimal_converter(register)==19):
        return 's3'
    if(Decimal_converter(register)==20):
        return 's4'
    if(Decimal_converter(register)==21):
        return 's5'
    if(Decimal_converter(register)==22):
        return 's6'
    if(Decimal_converter(register)==23):
        return 's7'    
    if(Decimal_converter(register)==24):
        return 's8'
    if(Decimal_converter(register)==25):
        return 's9'
    if(Decimal_converter(register)==26):
        return 's10'
    if(Decimal_converter(register)==27):
        return 's11'
    if(Decimal_converter(register)==28):
        return 't3'
    if(Decimal_converter(register)==29):
        return 't4'
    if(Decimal_converter(register)==30):
        return 't5'
        '''
# file_name = input("Enter the file name: ")
# with open(file_name,"+r") as input_file:
#     while(True):
#         a = input_file.readline()
#         if not a:
#             break
#         if not a.strip():  #for skipping empty lines
#             continue
#         # a=a[::-1]
#         Switch_case(a[-7::],a)  #-1:-8:-1