#usr/bin/python3.4
import time
import itertools, string

class Wordlist3:
	def createWordlist(self, output, chrs, min_length, max_length):
		if min_length > max_length:
			print("[!] %d<=%d is False"%(min_length,max_length))
		output = open(output, 'w')
		print ("[+] Start Time: ", time.strftime('%H:%M:%S'))
		for n in range(min_length, max_length+1):
			for x in itertools.product(chrs, repeat=n):
				saved = ''.join(x)
				print(saved)
				output.write("%s\n" % saved)
		output.close()
		print ("[-] End Time: ", time.strftime('%H:%M:%S'))

test = Wordlist3()
test.createWordlist("bigtest.txt","adcdefghijklmnopqrstuvwxyz",5,8)
