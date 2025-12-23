def get_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        input_values = [line.strip() for line in lines]
        return input_values, len(input_values), len(input_values[0])


def split_beam_and_count(input_values, width):
    timeline_count = 1
    first_line = input_values[0]
    current_ind = [i for i in range(width) if first_line[i] == 'S']
    for line in input_values[1:]:
        new_ind = []
        # print(line, current_ind, timeline_count, end='  ***  ')
        for tl_i in current_ind:

            if line[tl_i] == '^':
                timeline_count += 1
                new_ind.append(tl_i + 1)
                new_ind.append(tl_i - 1)

            else:
                new_ind.append(tl_i)
        current_ind = new_ind

        # print(line, current_ind, timeline_count)

    return timeline_count, current_ind, len(current_ind)

#
# def split_beam_and_count(input_values, width):
#     # Start with timeline positions from the first row (where 'S' is)
#     # We track positions as a list (allowing duplicates for multiple timelines at same position)
#     current_timelines = [i for i in range(width) if input_values[0][i] == 'S']
#
#     # Process each subsequent row
#     for row_idx in range(1, len(input_values)):
#         line = input_values[row_idx]
#         new_timelines = []
#
#         # For each timeline from the previous row
#         for timeline_pos in current_timelines:
#             # Safety check: ensure position is within bounds
#             if timeline_pos < 0 or timeline_pos >= width:
#                 continue
#
#             # Check what's at this position in the current row
#             if line[timeline_pos] == '^':
#                 # Splitter: timeline splits into left and right
#                 if timeline_pos - 1 >= 0:  # Left split (if within bounds)
#                     new_timelines.append(timeline_pos - 1)
#                 if timeline_pos + 1 <= width:  # Right split (if within bounds)
#                     new_timelines.append(timeline_pos + 1)
#             else:
#                 # Empty space: timeline continues straight down
#                 new_timelines.append(timeline_pos)
#
#         current_timelines = new_timelines
#         # Optional: uncomment to see progress (slows down execution)
#         # if row_idx % 10 == 0:
#         #     print(f"Row {row_idx}/{len(input_values)-1}: {len(current_timelines)} timelines")
#
#     # Total count is the number of timelines at the end
#     return len(current_timelines), current_timelines
def main():
    input_values, height, width = get_input('./input2.txt')
    # input_values, height, width = get_input('input.txt')
    # print(input_values, '\n', height, '\n', width)
    results = split_beam_and_count(input_values, width)
    print(results[0])
    # print(results[1])
    # print(results[2])


if __name__ == '__main__':
    main()
