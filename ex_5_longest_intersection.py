n = int(input())
longest_intersection = set()
for _ in range(n):
    first_range, second_range = input().split('-')
    first_set = set()
    first_start, first_end = [int(x) for x in first_range.split(',')]
    for i in range(first_start, first_end+1):
        first_set.add(i)
    second_set = set()
    second_start, second_end = [int(x) for x in second_range.split(',')]
    for i in range(second_start, second_end + 1):
        second_set.add(i)
    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')




