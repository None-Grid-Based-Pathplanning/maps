# //double map[MAP_pointB][2] = { { 0,0 },{ 100,0 },{ 100,100 },{ 0,100 },
# //{ 0,2 },{ MAP_length,2 },{ MAP_length,MAP_width + 2 },{ 0,MAP_width + 2 },{ 30,2 },{ 30 + MAP_length,2 },{ 30 + MAP_length, MAP_width + 2 },{ 30,MAP_width + 2 },{ 60,2 },{ 60 + MAP_length,2 },{ 60 + MAP_length, MAP_width + 2 },{ 60,MAP_width + 2 },
# //{ 100 - MAP_length,11 },{ 100,11 },{ 100,11 + MAP_width },{ 100 - MAP_length,11 + MAP_width },{ 70 - MAP_length,11 },{ 70,11 },{ 70,11 + MAP_width },{ 70 - MAP_length,11 + MAP_width },{ 40 - MAP_length,11 },{ 40,11 },{ 40,11 + MAP_width },{ 40 - MAP_length,11 + MAP_width },
# //{ 0,22 },{ MAP_length,22 },{ MAP_length,MAP_width + 22 },{ 0,MAP_width + 22 },{ 30,22 },{ 30 + MAP_length,22 },{ 30 + MAP_length, MAP_width + 22 },{ 30,MAP_width + 22 },{ 60,22 },{ 60 + MAP_length,22 },{ 60 + MAP_length, MAP_width + 22 },{ 60,MAP_width + 22 },
# //{ 100 - MAP_length,33 },{ 100,33 },{ 100,33 + MAP_width },{ 100 - MAP_length,33 + MAP_width },{ 70 - MAP_length,33 },{ 70,33 },{ 70,33 + MAP_width },{ 70 - MAP_length,33 + MAP_width },{ 40 - MAP_length,33 },{ 40,33 },{ 40,33 + MAP_width },{ 40 - MAP_length,33 + MAP_width },
# //{ 0,44 },{ MAP_length,44 },{ MAP_length,MAP_width + 44 },{ 0,MAP_width + 44 },{ 30,44 },{ 30 + MAP_length,44 },{ 30 + MAP_length, MAP_width + 44 },{ 30,MAP_width + 44 },{ 60,44 },{ 60 + MAP_length,44 },{ 60 + MAP_length, MAP_width + 44 },{ 60,MAP_width + 44 },
# //{ 100 - MAP_length,55 },{ 100,55 },{ 100,55 + MAP_width },{ 100 - MAP_length,55 + MAP_width },{ 70 - MAP_length,55 },{ 70,55 },{ 70,55 + MAP_width },{ 70 - MAP_length,55 + MAP_width },{ 40 - MAP_length,55 },{ 40,55 },{ 40,55 + MAP_width },{ 40 - MAP_length,55 + MAP_width },
# //{ 0,66 },{ MAP_length,66 },{ MAP_length,MAP_width + 66 },{ 0,MAP_width + 66 },{ 30,66 },{ 30 + MAP_length,66 },{ 30 + MAP_length, MAP_width + 66 },{ 30,MAP_width + 66 },{ 60,66 },{ 60 + MAP_length,66 },{ 60 + MAP_length, MAP_width + 66 },{ 60,MAP_width + 66 },
# //{ 100 - MAP_length,77 },{ 100,77 },{ 100,77 + MAP_width },{ 100 - MAP_length,77 + MAP_width },{ 70 - MAP_length,77 },{ 70,77 },{ 70,77 + MAP_width },{ 70 - MAP_length,77 + MAP_width },{ 40 - MAP_length,77 },{ 40,77 },{ 40,77 + MAP_width },{ 40 - MAP_length,77 + MAP_width },
# //{ 0,88 },{ MAP_length,88 },{ MAP_length,MAP_width + 88 },{ 0,MAP_width + 88 },{ 30,88 },{ 30 + MAP_length,88 },{ 30 + MAP_length, MAP_width + 88 },{ 30,MAP_width + 88 },{ 60,88 },{ 60 + MAP_length,88 },{ 60 + MAP_length, MAP_width + 88 },{ 60,MAP_width + 88 },
# //{ 100 - MAP_length,97 },{ 100,97 },{ 100,97 + MAP_width },{ 100 - MAP_length,97 + MAP_width },{ 70 - MAP_length,97 },{ 70,97 },{ 70,97 + MAP_width },{ 70 - MAP_length,97 + MAP_width },{ 40 - MAP_length,97 },{ 40,97 },{ 40,97 + MAP_width },{ 40 - MAP_length,97 + MAP_width },
#define MAP_length 20
#define MAP_width  2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig1 = plt.figure()
ax = fig1.add_subplot(111, aspect = 'equal')
#line1
ax.add_patch(
    patches.Rectangle(
        (0, 2),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (30, 2),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (60, 2),
        20,
        2,
        color = '#000000',
    )
)
#line2
ax.add_patch(
    patches.Rectangle(
        (80, 11),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (50, 11),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (20, 11),
        20,
        2,
        color = '#000000',
    )
)
#line3
ax.add_patch(
    patches.Rectangle(
        (0, 22),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (30, 22),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (60, 22),
        20,
        2,
        color = '#000000',
    )
)
#line4
ax.add_patch(
    patches.Rectangle(
        (80, 33),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (50, 33),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (20, 33),
        20,
        2,
        color = '#000000',
    )
)
#line5
ax.add_patch(
    patches.Rectangle(
        (0, 44),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (30, 44),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (60, 44),
        20,
        2,
        color = '#000000',
    )
)
#line6
ax.add_patch(
    patches.Rectangle(
        (80, 55),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (50, 55),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (20, 55),
        20,
        2,
        color = '#000000',
    )
)
#line7
ax.add_patch(
    patches.Rectangle(
        (0, 66),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (30, 66),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (60, 66),
        20,
        2,
        color = '#000000',
    )
)
#line8
ax.add_patch(
    patches.Rectangle(
        (80, 77),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (50, 77),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (20, 77),
        20,
        2,
        color = '#000000',
    )
)
#line9
ax.add_patch(
    patches.Rectangle(
        (0, 88),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (30, 88),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (60, 88),
        20,
        2,
        color = '#000000',
    )
)
#line10
ax.add_patch(
    patches.Rectangle(
        (80, 97),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (50, 97),
        20,
        2,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (20, 97),
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