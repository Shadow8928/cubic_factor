a = int(input('enter X^3 coefficient(Must be Integer)'))
b = float(input('enter X^2 coefficient'))
c = float(input('enter X coefficient'))
d = int(input('enter Constant Value'))

a_fac = []
d_fac = []
z_val = []
t_val = []
if a == 1:
    poly_fact = ''
else:
    poly_fact = str(a)
for i in range(1, a+1):
    if a % i == 0:
        a_fac.append(i)
for i in range(1,d+1):
    if d % i == 0:
        d_fac.append(i)
for i in range(d,0):
    if d % i == 0:
        d_fac.append(i)
for i in range(a,0):
    if a % i == 0:
        a_fac.append(i)
for i in a_fac:
    for j in d_fac:
        z = j/i
        z_val.append(z)
        z = -z
        z_val.append(z)

for s in z_val:
    t = (a*(s**3))+(b*(s**2))+(c*s)+d
    if t == 0:
        t_val.append(s)

for k in t_val:
    if k > 0:
        t = '-'
    else:
        t = '+'
    poly_fact = poly_fact+'(x'+str(t)+str(abs(k))+')'
print(poly_fact)
