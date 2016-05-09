# class FLAGS():


# 	def __init__(self, name, salary):
# 		jal ="0"  # 0
# 		ns = "0000"
# 		# ns0= "0"  # 1
# 		# ns1 = "0"  # 2
# 		# ns2 = "0"  # 3
# 		# ns3 = "0"  # 4
# 		pcSource = "00"
# 		# pcSource0 = "0"  # 5
# 		# pcSource1 = "0" # 6
# 		aluOp = "0000"
# 		# aluOp0 = "0" # 7
# 		# aluOp1 = "0" # 8
# 		# aluOp2 = "0" # 9 
# 		# aluOp3 = "0" # 10
# 		aluSrcB = "00"
# 		# aluSrcB0 = "0" # 11
# 		# aluSrcB1 = "0" # 12
# 		aluSrcA = "0" # 13
# 		regWrite = "0" # 14
# 		regDest = "0" # 15
# 		irWrite = "0" # 16
# 		memToReg = "0" # 17
# 		memWrite = "0" # 18
# 		memRead = "0" #19
# 		iOrD = "0" # 20
# 		pcWrite = "0" # 21
# 		pcWriteCond = "0" # 22
# 		ifBranch = "0"


#returns a string
def intToBit(myInt):
	return "{:010b}".format(myInt)

def bitToInt(myString):
	return int(myString, 2)

def rev(myString):
	return myString[::-1]

def main():

	swtype= "101011"
	lwtype = "100011"
	rtype = "000000"
	itype = ("001000", "001100", "001101")
	beqtype = "000100"
	jtype="000010"
	jaltype = "000011"
	jrtype = "001000"
	print("v2.0 raw")
	for i in range(0,2**10):

		jal ="0"  # 0
		jr = "0"
		ns = "0000"
		pcSource = "00"
		aluOp = "0000"
		aluSrcB = "00"
		aluSrcA = "0" # 13
		regWrite = "0" # 14
		regDest = "0" # 15
		irWrite = "0" # 16
		memToReg = "0" # 17
		memWrite = "0" # 18
		memRead = "0" #19
		iOrD = "0" # 20
		pcWrite = "0" # 21
		ifBranch = "0"

		opAndState = intToBit(i)
		#opAndState = "1000110001"
		opcode = opAndState[:6] #the 6 most siginificant bits are opcode
		currentState = opAndState[-4:] # the 4 least signifcant bits are currejt
		currentStateInt = bitToInt(currentState)
		if currentStateInt == 0: #fetch
			memRead = "1"
			aluSrcA = "0"
			iOrD = "0"
			irWrite = "1"
			aluSrcB = "01"
			aluOp = "0011"
			pcWrite = "1"
			pcSrc = "00"
			jal = "0"
			jr = "0"
			ifBranch = "0"
		elif currentStateInt == 1: #decode
			aluSrcA = "0"
			aluSrcB = "11"
			aluOp = "0000"
		elif currentStateInt == 2:
			aluSrcA = "1"
			aluSrcB = "10"
			aluOp = "0011"
			
		elif currentStateInt == 3:
			memRead = "1"
			iOrD = "1"

		elif currentStateInt == 4:
			regDest = "1"
			regWrite = "1"
			memToReg = "0"
		elif currentStateInt == 5:
			memWrite = "1"
			iOrD = "1"
		elif currentStateInt == 6:#R TYPE second layer
			aluSrcA ="1"
			aluSrcB = "00"
			aluOp = "1000"
		elif currentStateInt == 7:#R TYPE third layer
			regDest = "1"
			regWrite = "1"
			memToReg = "0"
		elif currentStateInt == 8:# I TYPE second layer
			aluSrcA = "1"
			aluSrcB = "10"
			if opcode == "001000": #addi
				aluOp="0011"
			elif opcode == "001100":#andi
				aluOp = "0110"
			elif opcode == "001101":#ori
				aluOp = "0000"

		elif currentStateInt == 9:# I TYPE third layer
			regDest = "1"
			regWrite = "1"
		elif currentStateInt == 10: #BEQ
			aluSrcA = "1"
			aluSrcB = "00"
			aluOp = "0100"
			ifBranch = "1"
			pcSrc = "01"
		elif currentStateInt == 11: #J
			pcWrite = "1"
			pcSrc = "10"
		elif currentStateInt == 12:#jal
			pcSrc = "10"
			pcWrite = "1"
			jal = "1"
		elif currentStateInt == 13:#jr
			pcSrc = "11"
			pcWrite = "1"
			jr = "1"


		#based on current state, change next state flags
		if currentStateInt == 0: #fetch
			ns = "0001"
		elif currentStateInt == 1: #decode
			if opcode == swtype or opcode == lwtype:
				ns = "0010"
			elif opcode == rtype:
				ns = "0110"
			elif opcode in itype:
				ns="1000"
			elif opcode == beqtype:
				ns="1010"
			elif opcode == jtype:
				ns="1011"
			elif opcode== jaltype:
				ns="1100"
			elif opcode == jrtype:
				ns="1101"

		elif currentStateInt == 2:
			if opcode == lwtype:
				ns = "0011"
			elif opcode == swtype:
				ns="0101"
			
		elif currentStateInt == 3:
			ns = "0100"
		elif currentStateInt == 6:#R TYPE second layer
			ns="0111"
		elif currentStateInt == 8:# I TYPE second layer
			ns="1001"




		beforeHex = jal + jr + ns + pcSource + \
		aluOp + aluSrcB + aluSrcA + regWrite + \
		regDest + irWrite + memToReg + memWrite + \
		memRead+ iOrD + pcWrite + ifBranch

		HexFormat = format(int(beforeHex,2), 'x')
		#print(beforeHex)
		print(HexFormat)

main()