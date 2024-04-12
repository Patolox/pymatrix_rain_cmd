import time
import random
import copy

WIDTH = 203
HEIGHT = 70
DELAY = 0.06
msg = "Wake up, Neo..."



# Creating a grid fo WIDTH*HEIGHT length
matrix = [[" "] * WIDTH for _ in range(HEIGHT)]
    
# Deepcopy to avoid referencing the same memory location
NEW_MATRIX = copy.deepcopy(matrix)

# Some characters may break spacing of the columns
# ALLOWED_CHARS = [chr(i) for i in range(0x30a0, 0x30f0)] + [chr(i) for i in range(0xff09, 0xff50)]

ALLOWED_CHARS = ['0', '1']

def clear_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = " " 

def draw_matrix(m):
    for i in range(len(m)):
        print("".join(m[i][:WIDTH - 1]))

def update_matrix():
    for i in range(len(matrix) - 1):
        for k in range(len(matrix[0])):
            if matrix[i][k] != " ":
                if NEW_MATRIX[i + 1][k] == " ":
                    NEW_MATRIX[i + 1][k] = random.choice(ALLOWED_CHARS)

time.sleep(1)

for c in msg:
    print(c, end="", flush=True)
    time.sleep(0.3)
    if c == 'p':
        time.sleep(0.5)

time.sleep(3)

v_len = 0
while True:
    # Deciding the length of the column with random chars
    v_len = random.randint(8, 16)

    # Updating characters location on the grid
    update_matrix()

    # Populating a column with random chars
    for k in range(v_len//2):
        r_row = random.randint(0, WIDTH - 1)
        for i in range(v_len):
            NEW_MATRIX[i][r_row] = random.choice(ALLOWED_CHARS)

    matrix = copy.deepcopy(NEW_MATRIX)
    draw_matrix(matrix)
    clear_matrix(NEW_MATRIX)
    time.sleep(DELAY)

    
