import subprocess
a = "alpr /home/parth/Documents/2.jpg"
a = a.split(' ')
z = subprocess.check_output(a)
z=z.split('\n')
print z
print z[1]
