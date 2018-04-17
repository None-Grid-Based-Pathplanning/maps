import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig1 = plt.figure()
ax = fig1.add_subplot(111, aspect = 'equal')

ax.add_patch(plt.Polygon([[16 , 90], [26 , 66], [11 , 80]], color='#000000'))

ax.add_patch(
    patches.Circle((15, 40), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((85, 40), 7, color ='#000000')
)
ax.add_patch(
    patches.Rectangle(
        (20, 11),
        60,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (50, 40),
        10,
        20,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (40, 75),
        20,
        2,
        color = '#000000',
    )
)


frame_x = [0, 100, 100, 0, 0]
frame_y = [0, 0, 100, 100, 0]
plt.plot(frame_x, frame_y, linewidth = '4',linestyle = '-', color='r')
plt.xlim((0, 100))
plt.ylim((0, 100))
plt.show()