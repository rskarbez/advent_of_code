if __name__ == '__main__':
    with open('aoc1_input.txt') as f:
        num_lines = 0
        num_elves = 0
        calories_list = []
        running_calories = 0

        for line in f:
            temp_line = line.strip()
            if not temp_line:
                # not temp_line is true if and only if temp_line is empty
                # use this to detect blank lines between elves
                print('Elf {} carries {} calories'.format(num_elves, running_calories))
                calories_list.append(running_calories)
                running_calories = 0
                # Reset to 0 each time an elf is "recorded"
                # Gives us a fresh slate for the next elf
                num_elves += 1
                continue
            running_calories += int(temp_line)
            num_lines += 1
        # Due to the fact there is NOT an extra blank line at file end,
        # we have an extra elf in temporary storage!
        #
        # Add that elf and the associated calorie count to our list
        calories_list.append(running_calories)
        num_elves += 1
        print(num_lines)
        print(num_elves)
        print(max(calories_list))
