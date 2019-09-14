string="I am a programmer. I love sharing knowledge."
sentsplit=string.split('. ')
for i in range(len(sentsplit)):
	sentsplit[i] = sentsplit[i].split()
print(sentsplit)

print("hello")