import numpy as np


vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

indices = [(0, 2, 3), (0, 1, 2),
           (1, 7, 2), (1, 6, 7),
           (6, 5, 4), (4, 7, 6),
           (3, 4, 5), (3, 5, 0),
           (3, 7, 4), (3, 2, 7),
           (0, 6, 1), (0, 5, 6)]

tex_coord = [(0, 0), (1, 0), (1, 1), (0, 1)]
tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                     (0, 2, 3), (0, 1, 2),
                     (0, 1, 2), (2, 3, 0),
                     (2, 3, 0), (2, 0, 1),
                     (0, 2, 3), (0, 1, 2),
                     (3, 1, 2), (3, 0, 1)]




def get_data(vertices, indices):
    data = [vertices[ind] for triangle in indices for ind in triangle]
    return np.array(data, dtype='f4')

colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0),
                             (1, 1, 0), (1, 0, 1), (1, 1, 1), (0, 1, 1),
                             (0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 0, 0)]
vertex_color_data = get_data(colors, indices)


# vertex_data = get_data(vertices, indices)
# tex_coord_data = get_data(tex_coord, tex_coord_indices)
# data = np.hstack([tex_coord_data, vertex_data])
# print(data)

print(vertex_color_data)