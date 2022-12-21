class Lanternfish():
    def __init__(self, timer):
        self.timer = timer

    def __str__(self):
        return self.timer

    def age(self):
        self.timer -= 1

class LanternfishSchool():
    def __init__(self, fishes):
        self.fishes = fishes
        self.fish_count = len(fishes)

    def __str__(self):
        return 'School of {} lanternfish'.format(self.fish_count)

    def age(self):
        birth_count = 0
        for fish in self.fishes:
            fish.age()
            if fish.timer < 0:
                fish.timer = 6
                birth_count += 1
        for i in range(birth_count):
            self.fishes.append(Lanternfish(8))
            self.fish_count += 1

def read_fishes(infile='aoc6_input.txt'):
    with open(infile) as f:
        fishes = []
        for line in f:
            split_line = line.strip().split(',')
            for fish in split_line:
                fishes.append(Lanternfish(int(fish)))
        return fishes

if __name__ == '__main__':
    #fishes = read_fishes('aoc6_sample.txt')
    fishes = read_fishes()
    school = LanternfishSchool(fishes)
    for i in range(1, 81):
        school.age()
        print('After {} days, we have a {}'.format(i, school))
