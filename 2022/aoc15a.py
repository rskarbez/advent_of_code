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

dist_map = {}

def manhattan_distance(p1, p2):
    if (p1, p2) in dist_map:
        return dist_map[(p1, p2)]
    dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    dist_map[(p1, p2)] = dist
    return dist

def compute_coverage_map(sensors, row=2000000):
#    temp_sensors = {}
    beacons = []
    not_beacons = []
    for k, v in sensors.items():
        if k[1] == row:
            beacons.append([k[0], k[0]])
        if v[1] == row:
            beacons.append([v[0], v[0]])
#        if k not in temp_sensors:
#            temp_sensors[k] = 'S'
#        if v not in temp_sensors:
#            temp_sensors[v] = 'B'
        dist = manhattan_distance(k, v)
        print('{}, {}: {}'.format(k, v, dist))
        # x_dist = dist
        # => y = 0
        # x_dist = dist-1
        # => y = 1
        # x_dist = dist-2
        # => y = 2
        if row not in range(k[1]-dist, k[1]+dist+1):
            continue
        else:
            y_dist = abs(k[1] - row)
            x_dist = dist - y_dist
            not_beacons.append([k[0] - x_dist, k[0] + x_dist])
#            points = [(x, 2000000) for x in range(k[0]-x_dist, k[0]+x_dist+1)]
#        for x_dist in range(dist+1):
#            y_dist = dist - x_dist
#            if 2000000 not in range(k[1]-y_dist, k[1]+y_dist+1):
#                continue
#            points = [(x, y) for x in range(k[0]-x_dist, k[0]+x_dist+1) for y in range(k[1]-y_dist, k[1]+y_dist+1)]
#        for x in range(k[0]-dist, k[0]+dist+1):
#            for y in range(k[1]-dist, k[1]+dist+1):
#                point = x, y
#            for point in points:
#                if manhattan_distance(point, k) > dist:
#                    continue
#                if point[1] != 2000000:
#                    continue
#                if point not in temp_sensors:
#                    temp_sensors[point] = 'N'
#    return temp_sensors
    return beacons, not_beacons

def compute_answer(beacons, not_beacons):
    master_set = set()
    for min_x, max_x in not_beacons:
        master_set |= set(range(min_x, max_x+1))
    #print(master_set)
    for min_x, _ in beacons:
        master_set -= {min_x}
    #print(master_set)
    return len(master_set)

#    count = 0
#    for k, v in coverage_map.items():
#        x, y = k
#        if y == row and v == 'N':
#            count += 1
#    return count

if __name__ == '__main__':
    #sensors = read_sensor_data('aoc15_sample.txt')
    sensors = read_sensor_data()
    #coverage_map = compute_coverage_map(sensors)
    #beacons, not_beacons = compute_coverage_map(sensors, row=10)
    beacons, not_beacons = compute_coverage_map(sensors)
    #print(coverage_map)
    #print('The answer is {}'.format(compute_answer(coverage_map, row=10)))
    print(not_beacons)
    print('The answer is {}'.format(compute_answer(beacons, not_beacons)))

