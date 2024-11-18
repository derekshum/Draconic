import csv
from datetime import datetime
from random import randint

DIE_SIZES = [4, 6, 8, 10, 12]
MAX_DICE = 30
TRIALS = 100000

def find_average(dice_num: int, die_size: int):
    return (die_size/2 + 0.5) * dice_num

def find_savage_average(dice_num: int, die_size: int) -> float:
    total: int = 0
    for i in range(TRIALS):
        roll_1: int = 0
        roll_2: int = 0
        for i in range(dice_num):
            roll_1 += randint(1, die_size)
            roll_2 += randint(1, die_size)
        total += max(roll_1, roll_2)
    return total/TRIALS

def main():
    results: list[list] = []

    # set titles
    title_row: list = ['Number of Dice']
    for die_size in DIE_SIZES:
        title_row.extend([
            f'average of d{die_size}',
            f'savage of d{die_size}',
            f'damage increase of d{die_size}'
            f'% increase of d{die_size}'
        ])
    results.append(title_row)

    # set data rows
    for dice_num in range(1, MAX_DICE + 1):
        print(f'Starting dice_num {dice_num}.')
        dice_num_row = [dice_num]
        for die_size in DIE_SIZES:
            print(f'Starting die_size {die_size}.')
            average = find_average(dice_num, die_size)
            savage_average = round(find_savage_average(dice_num, die_size), 2)
            damage_increase = round(savage_average - average, 2)
            percent_increase = round((savage_average / average - 1) * 100, 1)
            dice_num_row.extend([average, savage_average, damage_increase, f'{percent_increase}%'])
        results.append(dice_num_row)

    with open(
            f'savage_attacker_comparison_{datetime.now().strftime("%Y-%m-%dT%H-%M-%S")}.csv',
            'w',
            newline=''
    ) as f:
        write = csv.writer(f)
        write.writerows(results)


if __name__ == '__main__':
    main()

