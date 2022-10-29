import dns.resolver

exmp = dns.resolver.app()
file = open("AQUI TU COLOCA O CAMINHO DA SUA WORDLIST EXEMPLO: /root/Desktop/kali.txt", "r")
dom = file.read().splitlines()

x = "O SITE QUE VOCÊ VAI VERIFICAR SE A PORTA ESTA ABERTA"

for x in dom:
try:

	sub_x = x + "." + x
	result = exmp.app(sub_x, "A")
for ip in result:
print(sub_x, "->", ip)
pass 
