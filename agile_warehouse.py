import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig1 = plt.figure()
ax = fig1.add_subplot(111, aspect = 'equal')
ax.add_patch(
    patches.Circle((25, 30), 5, color ='#000000')
)
ax.add_patch(
    patches.Circle((25, 70), 5, color ='#000000')
)
ax.add_patch(
    patches.Circle((50, 30), 5, color ='#000000')
)
ax.add_patch(
    patches.Circle((50, 70), 5, color ='#000000')
)
ax.add_patch(
    patches.Rectangle(
        (70, 10),
        20,
        5,
        color = '#000000'
    )
)
ax.add_patch(
    patches.Rectangle(
        (70, 30),
        20,
        5,
        color = '#000000'
    )
)
ax.add_patch(
    patches.Rectangle(
        (70, 50),
        20,
        5,
        color = '#000000'
    )
)
ax.add_patch(
    patches.Rectangle(
        (70, 70),
        20,
        5,
        color = '#000000'
    )
)
ax.add_patch(
    patches.Rectangle(
        (70, 90),
        20,
        5,
        color = '#000000'
    )
)


frame_x = [0, 100, 100, 0, 0]
frame_y = [0, 0, 100, 100, 0]
plt.plot(frame_x, frame_y, linewidth = '4',linestyle = '-', color='r')

plt.xlim((0, 100))
plt.ylim((0, 100))
plt.show()