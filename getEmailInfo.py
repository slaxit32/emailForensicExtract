#!/usr/bin/python

#made with python 2

import email,csv,os
from emaildata.metadata import MetaData

print("\nDigital Forensics Email Extractor by")

print("""
 ____  ____  __    __  __  ___  _   _    __   
(  _ \(_  _)(  )  (  )( ) / __)( )_( )  /__\  
 )(_) )_)(_  )(__  )(__)( \__ \ ) _ (  /(__)\ 
(____/(____)(____)(______)(___/(_) (_)(__)(__)
\n\n""")

flag=0

for file in os.listdir(os.getcwd()):
	if file.endswith(".eml"):
		file_name=str(os.getcwd()+"/"+file)

		message = email.message_from_file(open(file_name))
		extractor = MetaData(message)

		data = extractor.to_dict()
		
		data['file_name']=file
		
		print (file)

		with open('email_list_stat.csv', 'a') as f:
			w = csv.DictWriter(f, data.keys())
			if(flag==0):
				w.writeheader()
				flag=1
			w.writerow(data)


print("\n\nDone..........\n\n")
