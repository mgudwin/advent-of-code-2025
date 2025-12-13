import math


def read_file(file):
    coordinates = tuple(
        [
            tuple([int(i.split(",")[0]), int(i.split(",")[1]), int(i.split(",")[2])])
            for i in [r.split("\n")[0] for r in open(file).readlines()]
        ]
    )
    return coordinates


def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def get_all_distances_sorted(coordinates):
    distance = {}
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            if i == j:
                continue
            key = tuple([i, j])
            if key not in list[distance.items()]:
                distance[key] = calculate_distance(coordinates[i], coordinates[j])
    # Sorting using sorted() method
    distance = {
        key: value for key, value in sorted(distance.items(), key=lambda item: item[1])
    }
    return distance


def group_first_x_items(distances, num_of_connections_needed):
    group_dict = {}
    group_num = 0
    connection_keys = list(distances.keys())[:num_of_connections_needed]

    for key in connection_keys:
        jb1 = key[0]
        jb2 = key[1]

        jb1_groups = [k for k, v in group_dict.items() if jb1 in v]
        jb2_groups = [k for k, v in group_dict.items() if jb2 in v]
        combined_groups = list(set(jb1_groups + jb2_groups))

        if len(jb1_groups) > 1:
            print(f"{jb1} found in multiple groups {jb1_groups}")
        if len(jb2_groups) > 1:
            print(f"{jb2} found in multiple groups {jb2_groups}")

        # if not in a group already
        if len(combined_groups) == 0:
            group_dict[group_num] = set([jb1, jb2])
            group_num += 1

        # If jb 1 or jb 2 are already in a single group
        elif len(combined_groups) == 1:
            group_dict[combined_groups[0]] |= set([jb1, jb2])

        elif len(combined_groups) == 2:
            circuit1 = set(group_dict[combined_groups[0]])
            circuit2 = set(group_dict[combined_groups[1]])
            group_dict[combined_groups[0]] = circuit1 | circuit2
            group_dict.pop(combined_groups[1], None)

    return group_dict


def group_all_items(distances, coordinates, jb_count):
    group_dict = {}
    group_num = 0
    connection_keys = list(distances.keys())

    for key in connection_keys:

        group_keys = [key for key in group_dict]
        if len(group_keys) == 1:
            jbs_in_group = len(group_dict[group_keys[0]])
            if jbs_in_group == jb_count:
                coord1 = coordinates[jb1]
                coord2 = coordinates[jb2]
                dist_from_wall = coord1[0] * coord2[0]
                return dist_from_wall

        # 172294
        jb1 = key[0]
        jb2 = key[1]

        jb1_groups = [k for k, v in group_dict.items() if jb1 in v]
        jb2_groups = [k for k, v in group_dict.items() if jb2 in v]
        combined_groups = list(set(jb1_groups + jb2_groups))

        if len(jb1_groups) > 1:
            print(f"{jb1} found in multiple groups {jb1_groups}")
        if len(jb2_groups) > 1:
            print(f"{jb2} found in multiple groups {jb2_groups}")

        # if not in a group already
        if len(combined_groups) == 0:
            group_dict[group_num] = set([jb1, jb2])
            group_num += 1

        # If jb 1 or jb 2 are already in a single group
        elif len(combined_groups) == 1:
            group_dict[combined_groups[0]] |= set([jb1, jb2])

        elif len(combined_groups) == 2:
            circuit1 = set(group_dict[combined_groups[0]])
            circuit2 = set(group_dict[combined_groups[1]])
            group_dict[combined_groups[0]] = circuit1 | circuit2
            group_dict.pop(combined_groups[1], None)

    return group_dict


def calculate_sizes(group_dict, top_x_sizes):
    # calculate circuit size
    group_size = []
    for key, value in group_dict.items():
        group_size.append(tuple([key, len(value)]))

    size_sorted = tuple(sorted(group_size, key=lambda i: i[1], reverse=True))
    product = math.prod([i[1] for i in size_sorted[:top_x_sizes]])
    return product


def main():
    file = "./puzzle_inputs/day_08_input.txt"
    # file = "./puzzle_inputs/day_08_sample.txt"

    # Part 1
    coordinates = read_file(file)
    distances = get_all_distances_sorted(coordinates)
    num_of_connections_needed = 1000
    group_dict = group_first_x_items(distances, num_of_connections_needed)
    product = calculate_sizes(group_dict, 3)
    print(f"The sorted sizes are {product}")

    # Part 2
    jb_count = len(coordinates)
    dist_from_wall = group_all_items(distances, coordinates, jb_count)
    print(f"Distance from the wall is {dist_from_wall}")


if __name__ == "__main__":
    main()
