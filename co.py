
import sys
print("---NOTE: press enter button after each entering each coordinate---")
s_pt_x=float(input("Enter co ordinate sun location x : "))
s_pt_y=float(input("Enter co ordinate sun location y : "))
b1=[]
c1=b1
print("Enter co ordinates for SMALLER building in x1y1 format: ")
for j in range(0,8):
    d=float(input())
    b1.append(d)
b2=[]
c2=b2
print("Enter co ordinates for BIGGERbuilding in x1y1 format: ")
for m in range(0,8):
    g=float(input())
    b2.append(g)

print("This is coordinates of biilding 1"+str(c1))
print("This is coordinates of building 2"+str(c2))
print("Sun coordinates are"+str(s_pt_x) )
print(s_pt_y)

w1=b1[6]-b1[0]
if w1<0:
    w1*=(-1)
else:
    pass
print("this is width of b1")
print(w1)
w2=b2[6]-b2[0]
if w2<0:
    w2*=(-1)
else:
    pass
print("this is width of b2")
print(w2)

h_b1=b1[3]-b1[1]
if h_b1<0:
    h_b1*=(-1)
else:
    pass
print("this is height of b1")
print(h_b1)
h_b2=b2[3]-b2[1]
if h_b2<0:
    h_b2*=(-1)
else:
    pass

print("this is height of b2")
print(h_b2)

h_diff=b2[0]-b1[6]
v_diff=h_b2-h_b1
x_di_sun_edg=b1[6]-s_pt_x
if s_pt_x >=b1[6]:
    print("sun is located next to small building so whole building will be in light this height is :",end=" ")
    print(h_b2+w2)
    sys.exit()
else:
    pass

sun_h_b1=s_pt_y-b1[1]

multiplier=sun_h_b1/x_di_sun_edg

print("this is diffrence in height")
print(v_diff)
lg=((h_diff*multiplier)+v_diff+(w2))
print("TOTAL LIGHTEN LENGTHS of b2 :")
print(lg)
