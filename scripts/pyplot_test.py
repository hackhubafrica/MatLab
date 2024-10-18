import matplotlib.pyplot as plt 

plt.plot([1,2,3,4],[11,7,8,9],'r^')
plt.xlabel('values 1-4')
plt.ylabel('values 6-9')
# plt.show()

# name = ['joy','vic', 'magneto']
# values = [2,3,4]
# plt.bar(name,values)
# plt.plot(name,values,'gs')
# plt.show()

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
name = ['joy','vic', 'magneto']
values = [6,78,4]
ax.bar(name,values)
plt.show()