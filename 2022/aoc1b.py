if __name__ == '__main__':
    with open('aoc1_input.txt') as f:
        num_lines = 0
        num_elves = 0
        calories_list = []
        running_calories = 0

        for line in f:
            temp_line = line.strip()
            if not temp_line:
                print('Elf {} carries {} calories'.format(num_elves, running_calories))
                calories_list.append(running_calories)
                running_calories = 0
                num_elves += 1
                continue
                #print('New elf!')
            running_calories += int(temp_line)
            #print(temp_line)
            num_lines += 1
        #print('New elf!')
        calories_list.append(running_calories)
        num_elves += 1
        print(num_lines)
        print(num_elves)
        print(max(calories_list))
        print(calories_list)
        sorted_calories_list = sorted(calories_list)
        print(sorted_calories_list)
        print(sorted_calories_list[num_elves-3:num_elves])
        print(sum(sorted_calories_list[num_elves-3:num_elves]))
