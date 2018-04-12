# //double map[MAP_pointA][2] = { { 0,0 },{ 100,0 },{ 100,100 },{ 0,100 },
# //{ 18,0 },{ 20.5,0 },{ 20.5,20 },{ 18,20 },{ 18,50 },{ 20.5,50 },{ 20.5,100 },{ 18,100 },
# //{ 38.5,0 },{ 41,0 },{ 41,50 },{ 38.5,50 },{ 38.5,80 },{ 41,80 },{ 41,100 },{ 38.5,100 },
# //{ 59,0 },{ 61.5,0 },{ 61.5,20 },{ 59,20 },{ 59,50 },{ 61.5,50 },{ 61.5,100 },{ 59,100 },
# //{ 79.5,0 },{ 82,0 },{ 82,50 },{ 79.5,50 },{ 79.5,80 },{ 82,80 },{ 82,100 },{ 79.5,100 } };
import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig1 = plt.figure()


ax = fig1.add_subplot(111, aspect = 'equal')
# ax.add_patch(
#     patches.Rectangle(
#         (18, 0),
#         2.5,
#         20,
#         color ='#000000',
#     )
# )

ax.add_patch(
    patches.Circle((14, 90), 6, color ='#000000')
)
ax.add_patch(plt.Polygon([[14, 47], [13, 33], [26, 41]], color= '#000000'))
ax.add_patch(plt.Polygon([[47, 57], [44, 68], [59, 75]], color= '#000000'))
ax.add_patch(plt.Polygon([[40, 7], [51, 8], [58, 21]], color= '#000000'))
ax.add_patch(plt.Polygon([[63, 89], [66, 80], [80, 90]], color='#000000'))


ax.add_patch(
    patches.Circle((24, 63), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((24, 15), 6, color = '#000000')
)
ax.add_patch(
    patches.Circle((60, 40), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((37, 42), 5, color = '#000000')
)
ax.add_patch(
    patches.Circle((40, 82), 6, color ='#000000')
)
ax.add_patch(
    patches.Circle((80, 20), 7, color ='#000000')
)
ax.add_patch(
    patches.Circle((80, 50), 6, color ='#000000')
)

ax.add_patch(
    patches.Circle((85, 75), 5, color ='#000000')
)
# ax.add_patch(
#     patches.Circle((70, 60), 5, color ='#000000')
# )
# ax.add_patch(
#     patches.Circle((85, 40), 5, color = '#000000')
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


frame_x = [0, 100, 100, 0, 0]
frame_y = [0, 0, 100, 100, 0]


plt.plot(frame_x, frame_y, linewidth = '4',linestyle = '-', color='r')
plt.xlim((0, 100))
plt.ylim((0, 100))
plt.show()