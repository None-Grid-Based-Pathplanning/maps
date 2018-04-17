import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig1 = plt.figure()
ax = fig1.add_subplot(111, aspect = 'equal')

ax.add_patch(
    patches.Circle((10, 90), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((10, 65), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((10, 40), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((10, 15), 7, color = '#000000')
)

ax.add_patch(
    patches.Circle((30, 80), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((30, 55), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((30, 30), 7, color ='#000000')
)


ax.add_patch(
    patches.Circle((50, 90), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((50, 65), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((50, 40), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((50, 15), 7, color = '#000000')
)

ax.add_patch(
    patches.Circle((70, 80), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((70, 55), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((70, 30), 7, color ='#000000')
)


ax.add_patch(
    patches.Circle((90, 90), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((90, 65), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((90, 40), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((90, 15), 7, color = '#000000')
)


frame_x = [0, 100, 100, 0, 0]
frame_y = [0, 0, 100, 100, 0]


plt.plot(frame_x, frame_y, linewidth = '4',linestyle = '-', color='r')
plt.xlim((0, 100))
plt.ylim((0, 100))
plt.show()