#poly.py
#Author: Fatima Khan

#Input
s = input("Enter input such as a=10, b=5, c=1, x=1: \n");
s = s.lower();

#Parse operands
i1 = s.find('a');
i2 = s.find(',');
ai = s[i1+2:i2].strip();
a = float(ai);

o1 = s.find('b');
o2 = s.find(',', i2+1);
bo = s[o1+2:o2].strip();
b = float(bo);

p1 = s.find('c');
p2 = s.find(',', o2+1);
cp = s[p1+2:p2].strip();
c = float(cp);

m1 = s.find('x');
xm = s[m1+2:].strip();
x = float(xm);

#Calculate z using ax^2+bx+c
z = ((a*(x**2)) + (b*x) + c);

#Print output
print("a: ", a);
print("b: ", b);
print("c: ", c);
print("x: ", x);
print("z: ", z);