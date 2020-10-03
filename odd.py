Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> odds = [ 1,  3,  5.  7,  9, 11, 13, 15,17, 19,
	 
SyntaxError: invalid syntax
>>> odds = [ 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
>>> this_minute = datetime.today().minute
>>> if this_minute in odds:
	print("Seems odd")
	else:
		
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> if this_minute in odds:
	print("seems odd");
else:
	print("not odd enough")
