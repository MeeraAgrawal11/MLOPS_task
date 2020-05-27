file = open('/root/MLOPS/expression_recognition/MLOPS_task/facial_emotion_recognition.py','r')
code = file.read()

if 'keras' or 'tensorflow' in code:			
	if 'Conv2D' in code:				 
		print('OK')
	else:
		print('not OK')
else:
	print('NOT A NEURAL NETWORK')