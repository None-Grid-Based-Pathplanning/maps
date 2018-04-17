import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig1 = plt.figure()
ax = fig1.add_subplot(111, aspect = 'equal')
for i in range(6):
    ax.add_patch(plt.Polygon([[6 + i*16, 96], [16 + i*16, 96], [11 + i*16, 88]], color='#000000'))
for i in range(5):
    ax.add_patch(plt.Polygon([[14 + i*16, 86], [24 + i*16, 86], [19 + i*16, 78]], color='#000000'))
for i in range(6):
    ax.add_patch(plt.Polygon([[6 + i*16, 76], [16 + i*16, 76], [11 + i*16, 68]], color='#000000'))

for i in range(5):
    ax.add_patch(plt.Polygon([[14 + i*16, 66], [24 + i*16, 66], [19 + i*16, 58]], color='#000000'))
for i in range(6):
    ax.add_patch(plt.Polygon([[6 + i*16, 56], [16 + i*16, 56], [11 + i*16, 48]], color='#000000'))

for i in range(5):
    ax.add_patch(plt.Polygon([[14 + i*16, 46], [24 + i*16, 46], [19 + i*16, 38]], color='#000000'))
for i in range(6):
    ax.add_patch(plt.Polygon([[6 + i*16, 36], [16 + i*16, 36], [11 + i*16, 28]], color='#000000'))

for i in range(5):
    ax.add_patch(plt.Polygon([[14 + i*16, 26], [24 + i*16, 26], [19 + i*16, 18]], color='#000000'))

for i in range(6):
    ax.add_patch(plt.Polygon([[6 + i*16, 16], [16 + i*16, 16], [11 + i*16, 8]], color='#000000'))






frame_x = [0, 100, 100, 0, 0]
frame_y = [0, 0, 100, 100, 0]


plt.plot(frame_x, frame_y, linewidth = '4',linestyle = '-', color='r')
plt.xlim((0, 100))
plt.ylim((0, 100))
plt.show()