file = "./puzzle_inputs/day_02_input.txt"
# file = "./puzzle_inputs/day_02_sample.txt"
ranges = [r.split(",") for r in open(file).readlines()][0]

invalid_ids_twice = []
invalid_ids = []
for _range in ranges:
    start, end = _range.split("-")
    range_list = list(range(int(start), int(end) + 1))
    for id in range_list:
        s = str(id)
        l = len(s)
        if s[: int(l / 2)] == s[int(l / 2) :]:
            invalid_ids_twice.append(s)
        for n in range(1, int(l / 2) + 1):
            parts = [s[i : i + n] for i in range(0, l, n)]
            result = all(x == parts[0] for x in parts)
            if result:
                invalid_ids.append(s)

id2_counts = 0
for id in invalid_ids_twice:
    id2_counts += int(id)

id_counts = 0
invalid_ids = list(set(invalid_ids))
for id in invalid_ids:
    id_counts += int(id)

print(f"Invalid IDs listed twice count is: {id2_counts}")
print(f"Invalid IDs listed multiple times count is: {id_counts}")
