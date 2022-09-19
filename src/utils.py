import numpy as np
import matplotlib.pyplot as plt
import math

from . import config

# def calculate_repulsion(point):
#     x, y = point.x, point.y

#     xv = Vector2D(0, 0)
#     yv = Vector2D(0, 0)

#     X_CUTOFF = SIZE * X_SENSITIVITY
#     Y_CUTOFF = SIZE * Y_SENSITIVITY

#     if x < X_CUTOFF or x > SIZE - X_CUTOFF or y < Y_CUTOFF or y > SIZE - Y_CUTOFF:
#         centre = Point2D(SIZE / 2, SIZE / 2)
#         return point - centre
#     else:
#         return None


#     if x < X_CUTOFF:
#         xv = point - Point2D(X_CUTOFF, y)
#     elif x > SIZE - X_CUTOFF:
#         xv = point - Point2D(SIZE - X_CUTOFF, y)
#     if y < Y_CUTOFF:
#         yv = point - Point2D(x, Y_CUTOFF)
#     elif y > SIZE - Y_CUTOFF:
#         yv = point - Point2D(x, SIZE - Y_CUTOFF)
    
#     v = xv + yv
#     return v.unit




# def calculate_repel_force(point, sensitivity):
#     x, y   = point
#     forces = []

#     inf = 0.01
    
#     if x == 0:
#         forces.append((1 / inf, 90))
#         print('A')
#     elif x < sensitivity:
#         forces.append((1 / abs(x), 90))
#     elif x == 1:
#         forces.append((1 / inf, 270))
#     elif x > 1 - sensitivity:
#         forces.append((1 / abs(1 - x), 270))

#     if y == 0:
#         forces.append((1 / inf, 180))
#     elif y < sensitivity:
#         forces.append((1 / abs(y), 180))
#     elif y == 1:
#         forces.append((1 / inf, 0))
#     elif y > 1 - sensitivity:
#         forces.append((1 / abs(1 - y), 0))

#     magnitude = np.sum([force[0] for force in forces]) if len(forces) > 0 else 0
#     direction = np.average([force[1] for force in forces]) if len(forces) > 0 else 0
#     print(f'({x}, {y}): {magnitude}')
#     return magnitude, direction

# def calculate_magnitude(point, sensitivity):
#     x, y = point
#     xd = min(x, abs(1 - x))
#     xm = xd if xd < sensitivity else 1
#     yd = min(y, abs(1 - y))
#     ym = yd if yd < sensitivity else 1
#     m = max((1 - xm), (1 - ym))
#     return m

# def calculate_direction(point, sensitivity):
#     x, y = point
#     dirs = []
#     if x < sensitivity: dirs.append(90)
#     elif x > 1 - sensitivity: dirs.append(270)
#     if y < sensitivity: dirs.append(180)
#     elif y > 1 - sensitivity: dirs.append(0)

#     return None if len(dirs) < 1 else np.average(dirs)

# # fig, ax = plt.subplots(nrows=2, figsize=(4, 8))
# # ax = ax.flatten()

# # size = 100

# # x = np.array(range(size+1))
# # y = np.array(range(size+1))

# # m = np.empty((size+1, size+1))
# # d = np.empty((size+1, size+1))

# # for a in x:
# #     for b in y:
# #         m[b][a] = calculate_magnitude((a / size, b / size), 0.25)
# #         d[b][a] = calculate_direction((a / size, b / size), 0.25)

# # ax[0].set_title('Magnitudes')
# # ax[1].set_title('Direction')

# # # ax[0].scatter(x=x_vals, y=y_vals, c=magnitudes, s=1)
# # ax[0].pcolormesh(m, shading='flat')
# # ax[1].pcolormesh(d, shading='flat')

# # plt.show()
    

    