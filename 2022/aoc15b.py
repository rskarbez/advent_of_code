def read_sensor_data(infile='aoc15_input.txt'):
    with open(infile) as f:
        sensors = {}
        for line in f:
            tokens = line.strip().split()
            sensor_x = int(tokens[2].split('=')[1][:-1])
            sensor_y = int(tokens[3].split('=')[1][:-1])
            beacon_x = int(tokens[-2].split('=')[1][:-1])
            beacon_y = int(tokens[-1].split('=')[1])
            sensors[(sensor_x, sensor_y)] = (beacon_x, beacon_y)
        return sensors

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def compute_coverage_map(sensors, min_x=0, min_y=0, max_x=4000000, max_y=4000000):
    for row in range(max_y+1):
        if row % 100000 == 0:
            print('Row {}'.format(row))
        #print('Row {}'.format(row))
        not_beacons = []
        for k, v in sensors.items():
            dist = manhattan_distance(k, v)
            if row not in range(k[1]-dist, k[1]+dist+1):
                continue
            else:
                y_dist = abs(k[1] - row)
                x_dist = dist - y_dist
                start = k[0] - x_dist
                if start < 0:
                    start = 0
                end = k[0] + x_dist
                if end > max_x:
                    end = max_x
                size = end - start
                if not size:
                    size = 0
                not_beacons.append([start, end, size])
        x = compute_gap(not_beacons)
        if x is not None:
            print('x value found: {}'.format(x))
            print('y value found: {}'.format(row))
            return (x * 4000000) + row

def sort_not_beacons(not_beacons):
    ret_list = []
    sorted_starts = sorted({i for i,_,_ in not_beacons})
    for i in sorted_starts:
        same_start = []
        max_size = -1
        for start, end, size in not_beacons:
            if start == i:
                same_start.append([start, end, size])
        for start, end, size in same_start:
            if size > max_size:
                max_size = size
        ret_list.append([i, i+max_size, max_size])
    return ret_list

def compute_gap(not_beacons):
    range_map = {}
    sorted_not_beacons = sort_not_beacons(not_beacons)
    for start, end, size in sorted_not_beacons:
        if not range_map:
            range_map[start] = size
        for k, v in range_map.items():
            if k == start:
                # Only happens for the first element, break out of the loop
                break
            else:
                # start is always greater than k for any element in range map, by construction
                if start > (k + v + 1):
                    # start is past the end of any existing range, which means we've found the answer
                    print('GAP IDENTIFIED')
                    print(start - 1)
                    return (start - 1)
                elif start <= (k + v + 1):
                    # start is included in an existing range, so there is overlap
                    if end > (k + v):
                        # Only partial overlap, need to extend existing range
                        range_map[k] = end - k
                    else:
                        # Total overlap, nothing needs to change
                        pass
    return None

if __name__ == '__main__':
    #sensors = read_sensor_data('aoc15_sample.txt')
    sensors = read_sensor_data()
    #the_answer = compute_coverage_map(sensors, max_x=20, max_y=20)
    the_answer = compute_coverage_map(sensors)
    print('The answer is {}'.format(the_answer))
