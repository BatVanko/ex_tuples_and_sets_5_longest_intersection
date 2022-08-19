# ex_tuples_and_sets_5_longest_intersection
Write a program that finds the longest intersection. You will be given a number N. On each of the next N lines you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive. 
Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its length in the format: "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"

Input

3
0,3-1,2
2,10-3,5
6,15-3,10

Output

Longest intersection is [6, 7, 8, 9, 10] with length 5
