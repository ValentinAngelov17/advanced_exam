ROWS_COUNT = 6
COLUMNS_COUNT = 6
matrix = []

for i in range(ROWS_COUNT):
    matrix.append([str(x) for x in input().split(" ")])

starting_position = input().lstrip("(").rstrip(")").split(", ")
starting_row = int(starting_position[0])
starting_columns = int(starting_position[1])
current_position = [starting_row, starting_columns]
breaking = True
while breaking:
    command = input().split(", ")
    if command[0] == "Stop":
        for row in matrix:
            print(" ".join(row))
        breaking = False

    if command[0] == "Create":
        direction = command[1]
        value = command[2]
        if direction == "down":
            if matrix[current_position[0]+1][current_position[1]] == ".":
                matrix[current_position[0]+1][current_position[1]] = value
                current_position = [current_position[0]+1, starting_columns]
            else:
                pass
        if direction == "up":
            if matrix[current_position[0] - 1][current_position[1]] == ".":
                matrix[current_position[0] - 1][current_position[1]] = value
                current_position = [current_position[0]-1, starting_columns]
            else:
                pass
        if direction == "right":
            if matrix[current_position[0]][current_position[1] + 1] == ".":
                matrix[current_position[0]][current_position[1] + 1] = value
                current_position = [current_position[0], current_position[1] + 1]
            else:
                pass
        if direction == "left":
            if matrix[current_position[0]][current_position[1] - 1] == ".":
                matrix[current_position[0]][current_position[1] - 1] = value
                current_position = [current_position[0], current_position[1] - 1]
            else:
                pass

    if command[0] == "Update":
        direction = command[1]
        value = command[2]

        if direction == "up":
            if matrix[current_position[0]][current_position[1]] != ".":
                matrix[current_position[0] - 1][current_position[1]] = value
                current_position = [current_position[0] - 1, current_position[1]]
        if direction == "down":
            if matrix[current_position[0]][current_position[1]] != ".":
                matrix[current_position[0] + 1][current_position[1]] = value
                current_position = [current_position[0] + 1, current_position[1]]
        if direction == "right":
            if matrix[current_position[0]][current_position[1]] != ".":
                matrix[current_position[0]][current_position[1] + 1] = value
                current_position = [current_position[0], current_position[1] + 1]
        if direction == "left":
            if matrix[current_position[0]][current_position[1]] != ".":
                matrix[current_position[0]][current_position[1] - 1] = value
                current_position = [current_position[0], current_position[1] - 1]
    if command[0] == "Read":
        if command[1] == "up":
            if matrix[current_position[0] - 1][current_position[1]] != ".":
                print(matrix[current_position[0] - 1][current_position[1]])
                current_position = [current_position[0] - 1, current_position[1]]
            else:
                current_position = current_position

        if command[1] == "down":
            if matrix[current_position[0] + 1][current_position[1]] != ".":
                print(matrix[current_position[0] + 1][current_position[1]])
                current_position = [current_position[0] + 1, current_position[1]]
            else:
                current_position = current_position

        if command[1] == "right":
            if matrix[current_position[0]][current_position[1] + 1] != ".":
                print(matrix[current_position[0]][current_position[1] + 1])
                current_position = [current_position[0], current_position[1] + 1]
            else:
                current_position = current_position

        if command[1] == "left":
            if matrix[current_position[0]][current_position[1] - 1] != ".":
                print(matrix[current_position[0]][current_position[1] - 1])
                current_position = [current_position[0], current_position[1] - 1]
            else:
                current_position = current_position

    if command[0] == "Delete":
        if command[1] == "up":
            if matrix[current_position[0] - 1][current_position[1]] != ".":
                matrix[current_position[0] - 1][current_position[1]] = "."
                current_position = [current_position[0] - 1, current_position[1]]
        if command[1] == "down":
            if matrix[current_position[0] + 1][current_position[1]] != ".":
                matrix[current_position[0] + 1][current_position[1]] = "."
                current_position = [current_position[0] + 1, current_position[1]]
        if command[1] == "right":
            if matrix[current_position[0]][current_position[1] + 1] != ".":
                matrix[current_position[0]][current_position[1] + 1] = "."
                current_position = [current_position[0], current_position[1] + 1]
        if command[1] == "left":
            if matrix[current_position[0]][current_position[1] - 1] != ".":
                matrix[current_position[0]][current_position[1] - 1] = "."
                current_position = [current_position[0], current_position[1] - 1]



