def read_patterns(infile='aoc8_input.txt'):
    with open(infile) as f:
        signals = []
        outputs = []
        for line in f:
            sig_patterns, out_patterns = line.split('|')
            s = sig_patterns.strip().split()
            o = out_patterns.strip().split()
            signals.append(s)
            outputs.append(o)
        return signals, outputs


if __name__ == '__main__':
    #signals, outputs = read_patterns('aoc8_sample.txt')
    signals, outputs = read_patterns()

    digit_counts = {i:0 for i in range(10)}
    for value in outputs:
        for digit in value:
            wires = len(digit)
            match wires:
                case 2:
                    digit_counts[1] += 1
                case 3:
                    digit_counts[7] += 1
                case 4:
                    digit_counts[4] += 1
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    digit_counts[8] += 1
                case _:
                    print('ERROR')

    print('The answer is {}'.format(sum(digit_counts.values())))

