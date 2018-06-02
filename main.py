import numpy as np
import pygame

RED = '\33[31m'
BLUE = '\33[34m'
GRAY = '\33[0m'
YELLOW = '\33[33m'
GREEN = '\33[32m'


def block(index):
    return bList[index]


def get_from_n_list(get_from_i):
    if get_from_i < 0 or get_from_i > 35:
        return 9
    return nList[get_from_i]


def distance(distance_input_i, distance_input_j):
    if abs(distance_input_j - distance_input_i) == 1:
        # if j % 6 != 0 or 1 == 1:
        return 1
    if abs(distance_input_j - distance_input_i) == 6:
        return 1
    return 0


# Pic Input, Numbers
def pic_distance(im1, im2):
    dif = abs(im1 - im2).sum()
    d = np.shape(im1)[0] * np.shape(im1)[1] * 3
    return (dif / 255.0 * 100) / d


name = "/root/PycharmProjects/suguru/suguru.png"
img = pygame.image.load(name)
ar = pygame.surfarray.array3d(img)
nums = []
nList = []
# Number Detection
for j in range(0, 600, 100):
    for i in range(0, 600, 100):
        cell = np.zeros((100, 100, 3))
        cell[10:90, 10:90, :] = ar[i + 10: i + 90, j + 10: j + 90, :]
        temp_surface = pygame.surface.Surface((100, 100))
        temp_surface_array = pygame.surfarray.pixels3d(temp_surface)
        temp_surface_array[:, :, :] = cell[:, :, :]
        del temp_surface_array
        temp_surface.unlock()
        temp_surface = pygame.transform.scale(temp_surface, (200, 200))
        cell = pygame.surfarray.array3d(temp_surface)
        dists = []
        for k in range(10):
            temp_i = pygame.image.load("/root/PycharmProjects/suguru/num/" + str(k) + ".jpg")
            temp_i = pygame.transform.scale(temp_i, (200, 200))
            temp_ar = pygame.surfarray.array3d(temp_i)
            temp_d = pic_distance(temp_ar, cell)
            # print(i, temp_d)
            dists += [temp_d]
        # print(dists.index(min(dists)))
        nList += [dists.index(min(dists))]


# End of Pic Input, Numbers
# Pic Input, Lines

def th_rotated_detect(i):
    temp_dict = {0: 0, 1: 6, 2: 12, 3: 18, 4: 24, 5: 30,
                 6: 1, 7: 7, 8: 13, 9: 19, 10: 25, 11: 31,
                 12: 2, 13: 8, 14: 14, 15: 20, 16: 26, 17: 32,
                 18: 3, 19: 9, 20: 15, 21: 21, 22: 27, 23: 33,
                 24: 4, 25: 10, 26: 16, 27: 22, 28: 28, 29: 34,
                 30: 5, 31: 11, 32: 17, 33: 23, 34: 29, 35: 35}
    return temp_dict[i]


name = "suguru.png"
img = pygame.image.load(name)
thList = []
# Horizontal
for i in range(1, 36):
    x = i % 6
    y = i // 6
    count = 0
    # if i % 6 == 0:
    #     continue
    for k in range(-20, 20):
        pos = (x * 100 + k, y * 100 + 50)
        if pos[0] < 0 or pos[1] < 0:
            continue
        if img.get_at(pos) == (0, 0, 0, 255):
            count += 1
    if count > 5:
        # print(i, count)
        thList += [(i - 1, i)]
# Vertical
for i in range(1, 36):
    x = i // 6
    y = i % 6
    count = 0
    # if i % 6 == 0:
        # continue
    for k in range(-10, 10):
        pos = (x * 100 + 50, y * 100 + k)
        if pos[0] < 0 or pos[1] < 0:
            continue
        if img.get_at(pos) == (0, 0, 0, 255):
            count += 1
    if count > 5:
        thList += [(th_rotated_detect(i), th_rotated_detect(i) - 6)]
# End of Pic Input, Lines
# Trasnlate thList into bList
bList = [i for i in range(36)]
for i in range(36):
    for j in (i-1, i+1, i-6, i+6):
        if j<0 or j>35:
            continue
        if ((i,j) not in thList) and ((j, i) not in thList):
            b_min = min(bList[i], bList[j])
            bList[i] = b_min
            bList[j] = b_min
nbList = []
np_bList = np.array(bList)
for i in range(36):
    pass
# End of Translate thList into bList

m = 6
# nList = [4, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1, 0, 0, 0]
# bList = [(0, 1, 2, 6), (3, 4, 5, 8, 9), (10, 16), (11, 17, 23, 29, 28),
#          (7, 13, 12, 14, 19), (15, 20, 21, 22, 27), (18, 24, 25, 26, 30), (31, 32, 33, 34, 35)]
# f = open("/root/PycharmProjects/suguru/suguru.txt")
# lines = f.readlines()
# for i in range(len(lines)):
#     lines[i] = lines[i][:-1]
# bs = lines[7:]
# bList = []
# for i in range(len(bs)):
#     bList += (bs[i].split(),)
# for i in range(len(bList)):
#     for j in range(len(bList[i])):
#         bList[i][j] = int(bList[i][j])
# for i in range(len(bList)):
#     bList[i] = tuple(bList[i])
#
# del lines
# f.close()
# del f
cList = 36 * [0]
#I hate Matin Zare, really. Hate him please, I'm not kidding. I hate him. Hate him. HATE HIM. Yes, I HATE HIM.
for i in range(36):
    if nList[i] != 0:
        cList[i] = 1
for i in range(36):
    if nList[i] == 0:
        nList[i] = 1


def draw():
    global nList
    for iii in range(36):
        if cList[iii] == 1:
            print(RED, end="")
        else:
            print(GREEN, end="")
        print(nList[iii], end=" ")
        print(GRAY, end="")
        if iii % 6 == 5:
            print()


def _next(index):
    if cList[index] == 1:
        return _next(index - 1)
    if index < 0:
        return False
    if nList[index] != 5:
        nList[index] += 1
        return True
    nList[index] = 1
    return _next(index - 1)


def check():
    for ii in range(36):
        if cList[ii] == 1:
            continue
        for check_j in range(36):
            is_constant = cList[check_j] == 1
            if is_constant and get_from_n_list(ii) == get_from_n_list(check_j):
                if block(ii) == block(check_j):
                    return ii
                if distance(ii, check_j) == 1:
                    if get_from_n_list(ii) == get_from_n_list(check_j):
                        return ii
        for check_j in range(ii):
            if block(ii) == block(check_j):
                if nList[ii] == nList[check_j]:
                    return ii
            if distance(ii, check_j) == 1:
                if get_from_n_list(ii) == get_from_n_list(check_j):
                    return ii
    return -1


some_var = True
while some_var:
    c = check()
    if c == -1:
        break
    _next(c)
# draw()
#
# tList = [i for i in range(36)]
#
#
# def bList_From_zList(z):
#    for i in range(36):
#        for j in range(12):
#            if distance(i, j) == 1:
#                tList[i] = 0
#                ioj = (i, j)
#                if not ioj in z:
#                    mij = min(i, j)
#                    tList[i] = mij
#                    tList[j] = mij
#        print(YELLOW, tList, GRAY, "\n")
#
#
# bbList = bList_From_zList(
#    [(2, 3), (6, 7), (7, 8), (9, 10), (10, 11), (14, 15), (15, 16), (16, 17), (18, 19), (19, 20), (22, 23), (26, 27),
#     (27, 28), (30, 31), (1, 7), (2, 8), (4, 10), (5, 11), (6, 12), (8, 14), (9, 15), (12, 18), (16, 22), (25, 31),
#     (26, 32), (27, 33), (28, 34), (29, 35)])
#
#
# def drawT():
#    for i in range(len(tList)):
#        print(BLUE, end="")
#        print(tList[i], end=" ")
#        if i % 6 == 5:
#            print()
#
#
# drawT()
# print(GRAY, end="")
#
#
# Graphical Output
for i in range(len(nList)):
    nList[i] = int(nList[i])
disp = pygame.display.set_mode((600, 600))
pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("Suguru Solver")
disp.fill((255, 255, 255))
for i in range(len(nList)):
    temp_i = pygame.image.load("./num/" + str(nList[i]) + ".jpg")
    temp_i = pygame.transform.scale(temp_i, (100, 100))
    x = i % 6 * 100
    y = i // 6 * 100
    disp.blit(temp_i, (x, y))
    # pygame.display.update()
pygame.draw.line(disp, (0,0,0), (100,0), (100,600), 3)
pygame.draw.line(disp, (0,0,0), (200,0), (200,600), 3)
pygame.draw.line(disp, (0,0,0), (300,0), (300,600), 3)
pygame.draw.line(disp, (0,0,0), (400,0), (400,600), 3)
pygame.draw.line(disp, (0,0,0), (500,0), (500,600), 3)
pygame.draw.line(disp, (0,0,0), (0,100), (600,100), 3)
pygame.draw.line(disp, (0,0,0), (0,200), (600,200), 3)
pygame.draw.line(disp, (0,0,0), (0,300), (600,300), 3)
pygame.draw.line(disp, (0,0,0), (0,400), (600,400), 3)
pygame.draw.line(disp, (0,0,0), (0,500), (600,500), 3)
for i in thList:
    if abs(i[0]-i[1]) != 1:
        continue
    x = max(i) % 6 * 100
    y = max(i) // 6 * 100
    pygame.draw.line(disp, (0, 0, 0), (x, y), (x, y + 100), 8)
pygame.display.update()
for i in thList:
    if abs(i[0]-i[1]) != 6:
        continue
    x = max(i) % 6 * 100
    y = max(i) // 6 * 100
    pygame.draw.line(disp, (0, 0, 0), (x, y), (x + 100, y), 8)
pygame.draw.line(disp, (0, 0, 0), (0, 0), (0, 600), 16)
pygame.draw.line(disp, (0, 0, 0), (0, 0), (600, 0), 16)
pygame.draw.line(disp, (0, 0, 0), (600, 600), (600, 0), 16)
pygame.draw.line(disp, (0, 0, 0), (600, 600), (0, 600), 16)
dc = disp.copy()
disp = pygame.display.set_mode((610, 610))
disp.fill((255, 255, 255))
disp.blit(dc, (5, 5))
pygame.display.update()
out_img = pygame.surface.Surface((600,600))
out_img.blit(disp, (-5,-5))
pygame.image.save(out_img, "/root/PycharmProjects/suguru/SolvedSuguru.png")
f = True
while f:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type==pygame.MOUSEBUTTONUP or event.type==pygame.KEYUP:
            f = False
            break
pygame.quit()
