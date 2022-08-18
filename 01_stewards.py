from collections import deque
matches = [str(x) for x in input().split(", ")]
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])
seat_matches = []

rotations = 0
sum_of_chars = 0


while first_sequence and second_sequence:
    if rotations == 10:
        break
    if len(seat_matches) == 3:
        break
    first = first_sequence.popleft()
    second = second_sequence.pop()
    sum_of_chars = sum((first, second))
    ascii_table = chr(sum_of_chars)
    first_try = str(first) + ascii_table
    second_try = str(second) + ascii_table
    if (first_try or second_try) not in seat_matches:
        if first_try in matches:
            seat_matches.append(first_try)
        else:
            first_sequence.append(first)
            second_sequence.appendleft(second)
        if second_try in matches:
            seat_matches.append(second_try)
        else:
            first_sequence.append(first)
            second_sequence.appendleft(second)
    rotations += 1

final = ", ".join(seat_matches)

print(f"Seat matches: {final}")
print(f"Rotations count: {rotations}")