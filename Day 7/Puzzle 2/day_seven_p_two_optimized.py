def get_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        input_values = [line.strip() for line in lines]
        return input_values, len(input_values), len(input_values[0])


def split_beam_and_count_dp(input_values, width):
    """
    Dynamic Programming approach: Instead of tracking individual timelines,
    we track the COUNT of timelines at each position.
    
    This is much more efficient for large inputs where timelines can grow exponentially.
    
    Mathematical approach:
    - dp[row][col] = number of timelines at position col in row row
    - We only need to store the previous row, so space is O(width) instead of O(timelines)
    - Time complexity is O(height * width) instead of exponential
    """
    # Initialize first row: 1 timeline at each 'S' position, 0 elsewhere
    prev_row = [1 if input_values[0][i] == 'S' else 0 for i in range(width)]
    
    # Process each subsequent row
    for row_idx in range(1, len(input_values)):
        line = input_values[row_idx]
        curr_row = [0] * width  # Initialize current row with zeros
        
        # For each position in the previous row
        for pos in range(width):
            num_timelines = prev_row[pos]  # Number of timelines coming from above
            if num_timelines == 0:  # No timelines at this position
                continue
            
            # Check what's at this position in the current row
            if line[pos] == '^':
                # Splitter: timelines split left and right
                if pos - 1 >= 0:  # Left split (if within bounds)
                    curr_row[pos - 1] += num_timelines
                if pos + 1 < width:  # Right split (if within bounds)
                    curr_row[pos + 1] += num_timelines
            else:
                # Empty space: timelines continue straight down
                curr_row[pos] += num_timelines
        
        prev_row = curr_row
    
    # Total count is the sum of all timelines in the final row
    total_count = sum(prev_row)
    return total_count, prev_row


def main():
    # Test with both inputs
    print("Testing with input.txt (small):")
    input_values, height, width = get_input('input.txt')
    results = split_beam_and_count_dp(input_values, width)
    print(f"Total timelines: {results[0]}")
    
    print("\nTesting with input2.txt (large):")
    input_values, height, width = get_input('input2.txt')
    results = split_beam_and_count_dp(input_values, width)
    print(f"Total timelines: {results[0]} \n {results[1]}")


if __name__ == '__main__':
    main()

