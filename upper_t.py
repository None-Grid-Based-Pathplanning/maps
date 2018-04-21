import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig1 = plt.figure()
ax = fig1.add_subplot(111, aspect = 'equal')
ax.add_patch(
    patches.Rectangle(
        (50, 30),
        2,
        30,
        color = '#000000'
    )
)
ax.add_patch(
    patches.Rectangle(
        (30, 40),
        2,
        20,
        color = '#000000'
    )
)
ax.add_patch(
    patches.Rectangle(
        (70, 40),
        2,
        22,
        color = '#000000'
    )
)
ax.add_patch(
    patches.Rectangle(
        (30, 60),
        40,
        2,
        color = '#000000'
    )
)

frame_x = [0, 100, 100, 0, 0]
frame_y = [0, 0, 100, 100, 0]
plt.plot(frame_x, frame_y, linewidth = '4',linestyle = '-', color='r')

plt.xlim((0, 100))
plt.ylim((0, 100))
plt.show()