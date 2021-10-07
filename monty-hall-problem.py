from random import randint

num_doors = 3
doors = [0] * num_doors

ct_other_door = 0
ct_door_you_picked = 0

for i in range(500000):
    prize = randint(0, 2)
    door_you_pick = 0
    door_revealed = randint(1, 2)
    if prize != door_revealed:
        if prize == door_you_pick:
            ct_door_you_picked += 1
        else:
            ct_other_door += 1

print(ct_door_you_picked, ct_other_door, ct_door_you_picked / ct_other_door)
