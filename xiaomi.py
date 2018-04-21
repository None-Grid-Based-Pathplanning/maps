import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig1 = plt.figure()
ax = fig1.add_subplot(111, aspect = 'equal')
ax.add_patch(
    patches.Rectangle(
        (40, 20),
        5,
        30,
        color = '#000000'
    )
)
ax.add_patch(
    patches.Rectangle(
        (80, 20),
        5,
        45,
        color = '#000000'
    )
)
ax.add_patch(
    patches.Rectangle(
        (20, 20),
        5,
        40,
        color = '#000000'
    )
)
ax.add_patch(
    patches.Rectangle(
        (60, 20),
        5,
        45,
        color = '#000000'
    )
)
ax.add_patch(
    patches.Rectangle(
        (20, 60),
        40,
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