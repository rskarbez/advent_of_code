class LanternfishSchool():
    def __init__(self, fishes):
        self.init_fishes = fishes
        self.fish_count = len(fishes)
        self.fish_spawn_in_X_days = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for fish in self.init_fishes:
            self.fish_spawn_in_X_days[fish] += 1

    def __str__(self):
        return 'School of {} lanternfish'.format(self.fish_count)

    def age(self):
        birth_count = self.fish_spawn_in_X_days.pop(0)
        self.fish_spawn_in_X_days.append(birth_count)
        self.fish_spawn_in_X_days[6] += birth_count
        self.fish_count += birth_count

def read_fishes(infile='aoc6_input.txt'):
    with open(infile) as f:
        fishes = []
        for line in f:
            split_line = line.strip().split(',')
            for fish in split_line:
                fishes.append(int(fish))
        return fishes

if __name__ == '__main__':
    #fishes = read_fishes('aoc6_sample.txt')
    fishes = read_fishes()
    school = LanternfishSchool(fishes)
    for i in range(1, 257):
        school.age()
        print('After {} days, we have a {}'.format(i, school))
