import numpy as np
a = np.array([3,4,5])
b = np.array([6,7,8])
c = np.array([1,2,9])
k = 10

print("(a+b) C = ", np.dot(a+b,c))
print("ac+bc = ", np.dot(a,c)+np.dot(b,c))
print('(ka)b = ', np.dot(k*a,b))
print("k(ab) = ", k*np.dot(a,b))
print("a(kb) = ", np.dot(a,k*b))