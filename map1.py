# //double map[MAP_pointA][2] = { { 0,0 },{ 100,0 },{ 100,100 },{ 0,100 },
# //{ 18,0 },{ 20.5,0 },{ 20.5,20 },{ 18,20 },{ 18,50 },{ 20.5,50 },{ 20.5,100 },{ 18,100 },
# //{ 38.5,0 },{ 41,0 },{ 41,50 },{ 38.5,50 },{ 38.5,80 },{ 41,80 },{ 41,100 },{ 38.5,100 },
# //{ 59,0 },{ 61.5,0 },{ 61.5,20 },{ 59,20 },{ 59,50 },{ 61.5,50 },{ 61.5,100 },{ 59,100 },
# //{ 79.5,0 },{ 82,0 },{ 82,50 },{ 79.5,50 },{ 79.5,80 },{ 82,80 },{ 82,100 },{ 79.5,100 } };
import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig1 = plt.figure()
ax = fig1.add_subplot(111, aspect = 'equal')
ax.add_patch(
    patches.Rectangle(
        (18, 0),
        2.5,
        20,
        color ='#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (18, 50),
        2.5,
        50,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (38.5, 0),
        2.5,
        50,
        color ='#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (38.5, 80),
        2.5,
        20,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (59, 0),
        2.5,
        20,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (59, 50),
        2.5,
        50,
        color = '#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (79.5, 0),
        2.5,
        50,
        color='#000000',
    )
)
ax.add_patch(
    patches.Rectangle(
        (79.5, 80),
        2.5,
        20,
        color='#000000',
    )
)
# ax.add_patch(
#     patches.Circle((44.5, 90.5), 3, color = 'r', alpha = 0.5)
# )
left_array_x = [15, 30, 46]
left_array_y = [45, 51, 53]
right_array_x = [44.5, 50, 42]
right_array_y = [90.5, 43, 46]

right_array_xx = [66, 45]
right_array_yy = [33, 37]

part_x = [5, 15]
part_y = [15, 45]

connect1_x = [46, 44.5]
connect1_y = [53, 90.4]
connect2_x = [46, 50]
connect2_y = [53, 43]
connect3_x = [46, 42]
connect3_y = [53, 46]

# plt.plot(5, 15, '*-', color = 'blue')
# plt.plot(44.5, 90.5, '*-', color = 'blue')
# plt.plot(part_x, part_y, '-', color = 'r')
#
frame_x = [0, 100, 100, 0, 0]
frame_y = [0, 0, 100, 100, 0]
# #'#FFD700''#008000''#FFA500''#FFC0CB''#A52A2A'
# plt.plot(left_array_x, left_array_y, 'o-', color='r')
# plt.plot(right_array_x, right_array_y, '*-', color='#A52A2A')
# plt.plot(right_array_xx, right_array_yy, '*-', color='#A52A2A')


# plt.plot(connect1_x, connect1_y, ':', color='#8A2BE2')
# plt.plot(connect2_x, connect2_y, ':', color='#9400D3')
# plt.plot(connect3_x, connect3_y, ':', color='#800080')
#
# ax.text(3, 8, 'Start', style='italic',color='blue')
# ax.text(47, 90, 'Goal', style='italic',color='blue')
# ax.text(19, 40, 'Forward', style='italic',color='r')
# ax.text(25, 70, 'Backward', style='italic',color='#A52A2A')
#
# ax.text(65, 70, 'BHG termination', style='italic',
#         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 3})
# ax.annotate('UHG', xy=(45, 70),  xycoords='data',
#             xytext=(0.23, 0.9), textcoords='axes fraction',
#             arrowprops=dict(facecolor='#006400', shrink=0.05),
#             horizontalalignment='left', verticalalignment='top',
#             )

plt.plot(frame_x, frame_y, linewidth = '4',linestyle = '-', color='r')
plt.xlim((0, 100))
plt.ylim((0, 100))
plt.show()