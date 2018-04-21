import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy.random as rnd
fig1 = plt.figure()
ax = fig1.add_subplot(111, aspect = 'equal')

ax.add_patch(plt.Polygon([[16 , 85], [36 , 70], [25 , 65]], color='#000000'))
ax.add_patch(plt.Polygon([[84 , 85], [66 , 70], [75 , 65]], color='#000000'))
ax.add_patch(plt.Polygon([[50 , 55], [50 , 45], [45 , 48]], color='#000000'))
ax.add_patch(plt.Polygon([[35 , 40], [65 , 40], [50 , 35]], color='#000000'))

ax.add_patch(patches.Ellipse(xy=(40, 60), width=10, height=15, angle=90,  color='#000000'))

ax.add_patch(patches.Ellipse(xy=(60, 60), width=10, height=15, angle=90,  color='#000000'))

ax.add_patch(
    patches.Rectangle(
        (10, 50),
        20,
        1,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (70, 50),
        20,
        1,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (5, 40),
        20,
        1,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (75, 40),
        20,
        1,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (10, 30),
        20,
        1,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (70, 30),
        20,
        1,
        color = '#000000',
    )
)

frame_x = [0, 100, 100, 0, 0]
frame_y = [0, 0, 100, 100, 0]
plt.plot(frame_x, frame_y, linewidth = '4',linestyle = '-', color='r')
plt.xlim((0, 100))
plt.ylim((0, 100))
plt.show()