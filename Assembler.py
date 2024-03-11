import re
import sys
def Binary_convertor(a,b):
    a=int(a)
    if not(-2147483648<=a<=2147483647):
        print("Immediate out of range")
        exit()
    if a < 0:
        # Convert negative numbers to binary using two's complement
        binary_representation = bin((1 << b) + a)[2:]
    else:
        binary_representation = bin(a)[2:]

    # Ensure the binary representation has the desired number of bits
    binary_representation = binary_representation.zfill(b)

    return binary_representation
    # print(s)

# print(Binary_convertor(-30,32))
def reg_add(register):
    if(register=='zero'):
        return(Binary_convertor(0,5))
    if(register=='ra'):
        return(Binary_convertor(1,5))
    if(register=='sp'):
        return(Binary_convertor(2,5))
    if(register=='gp'):
        return(Binary_convertor(3,5))
    if(register=='tp'):
        return(Binary_convertor(4,5))
    if(register=='t0'):
        return(Binary_convertor(5,5))
    if(register=='t1'):
        return(Binary_convertor(6,5))
    if(register=='t2'):
        return(Binary_convertor(7,5))
    if(register=='s0' or register =='fp'):
        return(Binary_convertor(8,5))
    if(register=='s1'):
        return(Binary_convertor(9,5))
    if(register=='a0'):
        return(Binary_convertor(10,5))
    if(register=='a1'):
        return(Binary_convertor(11,5))
    if(register=='a2'):
        return(Binary_convertor(12,5))
    if(register=='a3'):
        return(Binary_convertor(13,5))
    if(register=='a4'):
        return(Binary_convertor(14,5))
    if(register=='a5'):
        return(Binary_convertor(15,5))
    if(register=='a6'):
        return(Binary_convertor(16,5))
    if(register=='a7'):
        return(Binary_convertor(17,5))
    if(register=='s2'):
        return(Binary_convertor(18,5))
    if(register=='s3'):
        return(Binary_convertor(19,5))
    if(register=='s4'):
        return(Binary_convertor(20,5))
    if(register=='s5'):
        return(Binary_convertor(21,5))
    if(register=='s6'):
        return(Binary_convertor(22,5))
    if(register=='s7'):
        return(Binary_convertor(23,5))
    if(register=='s8'):
        return(Binary_convertor(24,5))
    if(register=='s9'):
        return(Binary_convertor(25,5))
    if(register=='s10'):
        return(Binary_convertor(26,5))
    if(register=='s11'):
        return(Binary_convertor(27,5))
    if(register=='t3'):
        return(Binary_convertor(28,5))
    if(register=='t4'):
        return(Binary_convertor(29,5))
    if(register=='t5'):
        return(Binary_convertor(30,5))
    if(register=='t6'):
        return(Binary_convertor(31,5))
    print("error : invalid register")
def r_type(data,i):
    ans = []
    if(data[0]=='add'):
        ans.append('0110011')  #opcode
        ans.append(reg_add(data[1]))  #rd
        ans.append('000')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        ans.append(reg_add(data[3]))  #rs2
        ans.append('0000000')  #funct7
    if(data[0]=='sub'):
        ans.append('0110011')   #opcode
        ans.append(reg_add(data[1]))   #rd
        ans.append('000')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        ans.append(reg_add(data[3]))  #rs2
        ans.append('0100000')  #funct7
    if(data[0]=='sll'):
        ans.append('0110011')  #opcode
        ans.append(reg_add(data[1]))  #rd
        ans.append('001')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        ans.append(reg_add(data[3]))  #rs2
        ans.append('0000000')  #funct7
    if(data[0]=='slt'):
        ans.append('0110011')  #opcode
        ans.append(reg_add(data[1])) #rd
        ans.append('010')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        ans.append(reg_add(data[3]))  #rs2
        ans.append('0000000')  #funct7
    if(data[0]=='sltu'):
        ans.append('0110011')  #opcode
        ans.append(reg_add(data[1]))  #rd
        ans.append('011')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        ans.append(reg_add(data[3]))  #rs2
        ans.append('0000000')  #funct7
    if(data[0]=='xor'):
        ans.append('0110011')  #opcode
        ans.append(reg_add(data[1]))  #rd
        ans.append('100')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        ans.append(reg_add(data[3]))  #rs2
        ans.append('0000000')  #funct7
    if(data[0]=='srl'):
        ans.append('0110011')  #opcode
        ans.append(reg_add(data[1]))  #rd
        ans.append('101')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        ans.append(reg_add(data[3]))  #rs2
        ans.append('0000000')  #funct7
    if(data[0]=='or'):
        ans.append('0110011')  #opcode
        ans.append(reg_add(data[1]))  #rd
        ans.append('110')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        ans.append(reg_add(data[3]))  #rs2
        ans.append('0000000')  #funct7
    if(data[0]=='and'):
        ans.append('0110011')  #opcode
        ans.append(reg_add(data[1]))  #rd
        ans.append('111')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        ans.append(reg_add(data[3]))  #rs2
        ans.append('0000000')  #funct7
    # while(len(ans)!=0):
    #     print(ans.pop()," ",end="")
    # print("\n")
    return ans
    #[31:25] [24:20] [19:15] [14:12] [11:7] [6:0]
    #funct7 rs2 rs1 funct3 rd opcode
def i_type(data,i):  
    ans=[]  # no [::-1] && [0:12]
    if(data[0]=='lw'):
        ans.append('0000011')  #opcode
        ans.append(reg_add(data[1]))  #rd
        ans.append('010')  #funct3
        ans.append(reg_add(data[3]))  #rs1
        binr = Binary_convertor(data[2],32)
        # binr = binr[::-1]
        ans.append(binr[-12:])  #imm[11:0]
    if(data[0]=='addi'):
        ans.append('0010011')  #opcode
        ans.append(reg_add(data[1]))  #rd
        ans.append('000')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        binr = Binary_convertor(data[3],32)
        # binr = binr[::-1]
        ans.append(binr[-12:])  #imm[11:0]
    if(data[0]=='sltiu'):
        ans.append('0010011')  #opcode
        ans.append(reg_add(data[1]))  #rd
        ans.append('011')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        binr = Binary_convertor(data[3],32)
        # binr = binr[::-1]
        ans.append(binr[-12:])  #imm[11:0]  (0:12)      
    if(data[0]=='jalr'):
        ans.append('1100111')  #opcode
        ans.append(reg_add(data[1]))  #rd
        ans.append('000')  #funct3
        ans.append(reg_add(data[2]))  #rs1
        binr = Binary_convertor(data[3],32)
        # binr = binr[::-1]  #i type
        # print(binr)
        ans.append(binr[-12:])  #imm[11:0] # i type[0:12]
    # while(len(ans)!=0):
    #     print(ans.pop(),end=" ")
    # print("\n")
    return ans
    #[31:20] [19:15] [14:12] [11:7] [6:0]
    #imm[11 : 0] rs1 funct3 rd opcode
def s_type(data,i):  ############################ERROR#########CORRECTED_IG###################
    ans=[]
    if (data[0]=='sw'):
        ans.append('0100011')  #opcode
        binr=Binary_convertor(data[2],32) #imm[0:11]
        # binr=binr[::-1]  #removed
        # print(binr,"\n")
        ans.append(binr[-5:])  #imm[4:0]  #doubt_finish
        ans.append('010')  #funct3
        ans.append(reg_add(data[3]))  #rs1
        ans.append(reg_add(data[1]))  #rs2
        ans.append(binr[-12:-5])  #imm[11:5]
    # while(len(ans)!=0):
    #     print(ans.pop(),end=" ")
    # print("\n")
    return ans
    #imm[11 : 5] rs2 rs1 funct3 imm[4 : 0] opcode S-type
    #[31:25] [24:20] [19:15] [14:12] [11:7] [6:0]
def b_type(data,i):
    if(data[0]=='beq' and data[1]=='zero' and data[2]=='zero' and data[3]=='0'):
        global check
        check=1
    ans=[]
    if(data[0]=='beq'):
        if(data[3].isalpha()):
            temp = (label_dict.get(data[3])-i)*4
            data[3]=temp
        ans.append('1100011')  #opcode
        binr=Binary_convertor(data[3],32)
        # binr=binr[::-1]
        imm1=binr[-5:-1]+binr[-12]
        ans.append(imm1)  #imm[4:1|11]
        ans.append('000') #funct3
        ans.append(reg_add(data[1]))  #rs1
        ans.append(reg_add(data[2]))  #rs2
        imm2=binr[-13]+binr[-11:-5] 
        ans.append(imm2)  #imm[12|10:5]
    if(data[0]=='bne'):
        if(data[3].isalpha()):
            temp = (label_dict.get(data[3])-i)*4
            data[3]=temp
        ans.append('1100011')  #opcode
        binr=Binary_convertor(data[3],32)
        # binr=binr[::-1]
        imm1=binr[-5:-1]+binr[-12]
        ans.append(imm1)  #imm[4:1|11]
        ans.append('001') #funct3
        ans.append(reg_add(data[1]))  #rs1
        ans.append(reg_add(data[2]))  #rs2
        imm2=binr[-13]+binr[-11:-5] 
        ans.append(imm2)  #imm[12|10:5]
    if(data[0]=='blt'):
        if(data[3].isalpha()):
            temp = (label_dict.get(data[3])-i)*4
            data[3]=temp
        ans.append('1100011')  #opcode
        binr=Binary_convertor(data[3],32)
        # binr=binr[::-1] #removed
        # print(binr)
        imm1=binr[-5:-1]+binr[-12]
        ans.append(imm1)  #imm[4:1|11]
        ans.append('100') #funct3
        ans.append(reg_add(data[1]))  #rs1
        ans.append(reg_add(data[2]))  #rs2
        imm2=binr[-13]+binr[-11:-5]  
        ans.append(imm2)  #imm[12|10:5]
    if(data[0]=='bge'):
        if(data[3].isalpha()):
            temp = (label_dict.get(data[3])-i)*4
            data[3]=temp
        ans.append('1100011')  #opcode
        binr=Binary_convertor(data[3],32)
        # binr=binr[::-1]
        imm1=binr[-5:-1]+binr[-12]
        ans.append(imm1)  #imm[4:1|11]
        ans.append('101') #funct3
        ans.append(reg_add(data[1]))  #rs1
        ans.append(reg_add(data[2]))  #rs2
        imm2=binr[-13]+binr[-11:-5] 
        ans.append(imm2)  #imm[12|10:5]
    if(data[0]=='bltu'):
        if(data[3].isalpha()):
            temp = (label_dict.get(data[3])-i)*4
            data[3]=temp
        ans.append('1100011')  #opcode
        binr=Binary_convertor(data[3],32)
        # binr=binr[::-1]
        imm1=binr[-5:-1]+binr[-12]
        ans.append(imm1)  #imm[4:1|11]
        ans.append('110') #funct3
        ans.append(reg_add(data[1]))  #rs1
        ans.append(reg_add(data[2]))  #rs2
        imm2=binr[-13]+binr[-11:-5]  
        ans.append(imm2)  #imm[12|10:5]
    if(data[0]=='bgeu'):
        if(data[3].isalpha()):
            temp = (label_dict.get(data[3])-i)*4
            data[3]=temp
        ans.append('1100011')  #opcode
        binr=Binary_convertor(data[3],32)
        # binr=binr[::-1]
        imm1=binr[-5:-1]+binr[-12]
        ans.append(imm1)  #imm[4:1|11]
        ans.append('111') #funct3
        ans.append(reg_add(data[1]))  #rs1
        ans.append(reg_add(data[2]))  #rs2
        imm2=binr[-13]+binr[-11:-5]  
        ans.append(imm2)  #imm[12|10:5]
    # while(len(ans)!=0):
    #     print(ans.pop(),end=" ")
    # print("\n")
    return ans
    #[31:25] [24:20] [19:15] [14:12] [11:7] [6:0]
    #imm[12|10 : 5] rs2 rs1 funct3 imm[4 : 1|11] opcode
def u_type(data,i):
    ans=[]
    if (data[0]=='lui'):
        ans.append('0110111') #opcode
        ans.append(reg_add(data[1]))  #rd
        binr = Binary_convertor(data[2],32)
        # binr = binr[::-1]
        ans.append(binr[-32:-12])  #imm[31:12]
    if(data[0]=='auipc'):
        ans.append('0010111') #opcode
        ans.append(reg_add(data[1]))  #rd
        binr = Binary_convertor(data[2],32)
        # binr = binr[::-1]
        ans.append(binr[-32:-12])  #imm[31:12]
    # while(len(ans)!=0):
    #     print(ans.pop(),end=" ")
    # print("\n")
    return   ans
    #[31:12] [11:7] [6:0]
    #imm[31:12] rd opcode
    
def j_type(data,i):
    ans=[]
    if (data[0]=='jal'):
        if(data[2].isalpha()):
            temp = (label_dict.get(data[2])-i)*4
            data[2]=temp
        ans.append('1101111')
        ans.append(reg_add(data[1]))
        binr = Binary_convertor(data[2],32)
        # binr=binr[::-1]  removed
        imm= binr[-21]+binr[-11:-1]+binr[-12]+binr[-20:-12]
        ans.append(imm)  #doubt
    # while(len(ans)!=0):
    #     print(ans.pop(),end=" ")
    # print("\n")
    return   ans
    #[31:12] [11:7] [6:0]
    #imm[20|10 : 1|11|19 : 12] rd opcode

def default_case(data,i):
    print("error: ",data[0])
    return
def Switch_case(case_value,data,i):
    switch_dict = {
        'add':r_type,
        'sub':r_type,
        'sll':r_type,
        'slt':r_type,
        'sltu':r_type,
        'xor':r_type,
        'srl':r_type,
        'or':r_type,
        'and':r_type,
        #################
        'lw':i_type,
        'addi':i_type,
        'sltiu':i_type,
        'jalr':i_type,
        #################
        'sw':s_type,
        ################
        'beq':b_type,
        'bne':b_type,
        'blt':b_type,
        'bge':b_type,
        'bltu':b_type,
        'bgeu':b_type,
        ##############
        'lui':u_type,
        'auipc':u_type,
        ##############
        'jal':j_type,
    }
    global output_name
    with open(output_name,'a+') as f:
        s = ""
        l = switch_dict.get(case_value,default_case)(data,i)
        while l:
            s += l.pop()
        s += "\n"
        f.write(s)
            
       
        

final_ans=[]

file_name = sys.argv[1]
output_name = sys.argv[2]
check = 0
label_dict={}
with open(file_name,"+r") as input_file:
    i=-1
    while(True):
        b=input_file.readline()
        if not b:
            break
        if not b.strip():  #for skipping empty lines
            continue
        i=i+1
        if(':' in b):
            label, rest_of_line = b.split(':', 1)
            label=label.strip()
            # data = re.split(r'[,\s()]+', rest_of_line.strip())
            label_dict[label]=i
    input_file.seek(0)
    i=-1        
    while(True):
        a = input_file.readline()
        if not a:
            break
        if not a.strip():  #for skipping empty lines
            continue
        i=i+1
        if(':' in a):
            label, rest_of_line = a.split(':', 1)
            label=label.strip()
            data = re.split(r'[,\s()]+', rest_of_line.strip())

        else:
            pattern = re.compile(r'[,\s()]+')
            data = re.split(pattern,a)
        if(data[0]==''):
            data=data[1:]
        # print(data)
        if (data):
            Switch_case(data[0],data,i)
    if(check == 0):
        print("No Virtual Halt")

        #// if (data[0]==NULL){}   //Empty line
        #// if(len(data[0])==6){}  //instruction
        #// instruction
        # print(data)
# Each line of the
# text file may be of one of two types:
# 1. Empty line: Ignore these lines
# 2. An instruction
# 3. A label


# '0110011': r_type,
#         '0000011': i_type,
#         '0010011': i_type,
#         '1100111': i_type,
#         '0100011': s_type,
#         '1100011': b_type,
#         '0110111': u_type,
#         '1101111': j_type,
    

    # if (data[2]=='000'):  #add / sub
    #     if(data[5]=='0000000'):
    #         #add
    #     if(data[5]=='0100000'):
    #         #sub
    # if (data[2]=='001'):  #sll
    # if (data[2]=='010'):  #slt
    # if (data[2]=='011'):  #stlu
    # if (data[2]=='100'):  #xor
    # if (data[2]=='101'):  #srl
    # if (data[2]=='110'):  #or
    # if (data[2]=='111'):  #and
        
# def Binary_convertor(a,b):
#     a=int(a)
#     if not(-2147483648<=a<=2147483647):
#         print("Immediate out of range")
#         exit()
#     temp = abs(a)
#     s='1'
#     while(temp>0):
#         last_digit = temp%2
#         s = str(int(s)*10+last_digit)
#         temp=temp//2
#     s=s[1:]
#     s=s[::-1]
#     length = len(s)
#     remaining = b-length
#     if(remaining>0):
#         s='0'*remaining+s
#     if(a<0):
#       inverted_bits =''.join('1' if bit == '0' else '0' for bit in s)
#       result = bin(int(inverted_bits, 2) + 1)[2:]
#       s=result.zfill(len(s))
#     return s
#     # print(s)
