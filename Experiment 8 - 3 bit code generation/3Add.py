__author__ = 'Shadab Shaikh, Surajit Karmakar,'
__title__ = 'Three address Code representation'
__date__ = '06-03-2019'
__version__ = '2.0'
__link__ = 'http://www.pracspedia.com/SPCC/3-address-code.html'				#Reference author link

print('Author		: ' + __author__)
print('Title		: ' + __title__)
print('Date		: ' + __date__)
print('Version		: ' + __version__)
print('Reference	: ' + __link__)

precedence=[['/','1'],['*','1'],['+','2'],['-','2'],['^','0'],['=','3']]	#creating a matrix of precedence lowest numbber highest precedence

def precedenceOf(t):														#checking character precedence
	token=t[0]																#assigning string to 1 character variable
	for i in range(len(precedence)):								
		if(token==precedence[i][0]):										#checking if character matches precedence matrix
			return int(precedence[i][1]+"")									#returning its precedence value
	return -1																#or returrning false

opc=0																		#initialization of opc
token=''																	#acting as a pointer to character
operators=[[],[],[],[],[],[],[],[],[],[],[],[]]								#creating 10*2 space for operator
expr=""																		#will store the user input
temp=""																		#used for soring
expr=input("\nEnter the expression\n")
processed=[]																#using to see if literal is already processed
for i in range(len(expr)):
	processed.append(False)													#initializaation of process mat with false

for i in range(len(expr)):
	token=expr[i]															#scanning each character in expr mat
	for j in range(len(precedence)):
		if(token==precedence[j][0]):										#if char matches with precedence mat character
			operators[opc].append(token+"")
			operators[opc].append(str(i)+"")								#appending it to operator matrix
			opc+=1															#incrementing opc for further storing 
			break

print("\nOperators;\nOperator\tLocation")
for i in range(opc):
	print(operators[i][0]+"\t\t"+operators[i][1])							#printing operator found and their location

for i in range(opc-1,0,-1):													#sorting matrix descending based on precedence level of operator
	for j in range(i):
		if(precedenceOf(operators[j][0]) > precedenceOf(operators[j+1][0])):
			temp=operators[j][0]
			operators[j][0]=operators[j+1][0]
			operators[j+1][0]=temp
			temp=operators[j][1]
			operators[j][1]=operators[j+1][1]
			operators[j+1][1]=temp

print("\nOperators sorted in their precedence:\nOperator\tLocation")
for i in range(opc):
	print(operators[i][0]+"\t\t"+operators[i][1])							#displaying sorted result

print("\n")
for i in range(opc):														#running for loop with operator count range
	j=int(operators[i][1]+"")												#stores the number of precedence value
	op1=''
	op2=''																	#will be storing operand 1 and 2
	if(processed[j-1]==True):												#determining if literall is already processseed
		if(precedenceOf(operators[i-1][0])==precedenceOf(operators[i][0])):
			op1="t"+str(i)													#if precedence matches making t# as new operand
		else:
			for x in range(opc):
				if((j-2)==int(operators[x][1])):							
					op1="t"+str((x+1))+""									#making left most t# operand, the middle t# operand
	else:
		op1=expr[j-1]+""													#else mmaking middle character 1st operand
	if(processed[j+1]==True):												#checking if rightmost is already proccessed
		for x in range(opc):
			if((j+2)==int(operators[x][1])):
				op2="t"+str((x+1))+""										#making right most t# operand, the middle t# operand
	else:
		op2=expr[j+1]+""													#else making right most character 2nt operand
	if(operators[i][0]=='='):												#checking if operator matches equal operator
		op2="t"+str((x))+""													#usinng the latest t# variable
		print(op1+operators[i][0]+op2)										#printing only operand with operator
		processed[j]=processed[j-1]=processed[j+1]=True						#updating processed matrix
	else:
		print("t"+str((i+1))+"="+op1+operators[i][0]+op2)					#printing t# with = operand 1 , operator and operand 2
		processed[j]=processed[j-1]=processed[j+1]=True						#updating processed matrix





	
