from collections import deque


def get_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        light_diagram = []
        buttons = []
        joltage = []
        for line in lines:
            new_line = line.split(' ')
            light_diagram.append(new_line[0])
            buttons.append(new_line[1:-1])
            joltage.append(new_line[-1])
        return light_diagram, buttons, joltage


def get_light_diagram(light_diagram):
    return [ld[1:-1] for ld in light_diagram]


def get_buttons(buttons_all):
    buttons = []
    for btn_list in buttons_all:
        buttons_mach_str = []
        for btn in btn_list:
            new_btn = btn.strip('()')
            buttons_mach_str.append(new_btn)
        buttons_mach_int = []
        # print(buttons_mach_str)
        for btn in buttons_mach_str:
            btn = btn.split(',')
            new_btn = tuple(map(int, btn))
            buttons_mach_int.append(new_btn)
        buttons.append(buttons_mach_int)
    return buttons


def get_btn_combo_set(btn_combo_set):
    # print(btn_combo_set)
    total_presses = 0
    for btn_combo in btn_combo_set:
        light_diagram = btn_combo[0]
        buttons = btn_combo[1]
        # print('this', light_diagram, buttons)
        min_presses = calc_button_combo(light_diagram, buttons)
        total_presses += min_presses
        print(f"Target: {light_diagram}, Minimum presses: {min_presses}")
    return total_presses


def calc_button_combo(light_diagram, buttons):
    light_diagram = list(light_diagram)
    min_presses = find_minimum_presses(light_diagram, buttons)
    return min_presses


def find_minimum_presses(target_state, buttons):
    """
    Use BFS to find the minimum number of button presses needed
    to reach the target state from the initial state (all '.').
    """
    target_state = list(target_state)
    initial_state = ['.'] * len(target_state)

    # If already at target, return 0
    if initial_state == target_state:
        return 0

    print(f'buttons: {buttons}')
    print(f'initial state: {initial_state}')
    print(f'target state: {target_state}')

    # BFS: (current_state, num_presses)
    queue = deque([(tuple(initial_state), 0)])
    visited = {tuple(initial_state)}
    # print(type(visited))

    while queue:
        current_state, num_presses = queue.popleft()
        # print(f'current_state: {current_state}')
        current_state = list(current_state)
        # print(f'current_state: {current_state}')

        # Try pressing each button
        for button in buttons:
            # print(f'current_state: {current_state}, num_presses: {num_presses}, visited: {visited}')
            # print(f'current_state: {current_state}')
            new_state = press_single_button(current_state, button)
            new_state_tuple = tuple(new_state)

            # Check if we reached the target
            if new_state == target_state:
                # print(f'queue: {queue}, visited: {visited}')
                return num_presses + 1

            # If we haven't seen this state before, add it to the queue
            if new_state_tuple not in visited:
                # print(f'queue: {queue}, visited: {visited}')
                visited.add(new_state_tuple)
                queue.append((new_state_tuple, num_presses + 1))

    # If we can't reach the target, return -1 (or handle as needed)
    return -1


def press_single_button(current_state, button):
    """
    Press a single button and return the new state.
    """
    new_state = current_state.copy()
    for idx in button:
        if new_state[idx] == '.':
            new_state[idx] = '#'
        elif new_state[idx] == '#':
            new_state[idx] = '.'
    return new_state


def main():
    light_diagram, buttons, joltage = get_input('./input2.txt')
    # print(f'light dia: {light_diagram}, \nbuttons: {buttons}, \n{joltage}')
    light_diagram = get_light_diagram(light_diagram)
    buttons = get_buttons(buttons)

    # print(f'light dia: {light_diagram}, \nbuttons: {buttons}')
    light_dia_and_all_buttons = zip(light_diagram, buttons)

    total_presses = get_btn_combo_set(tuple(light_dia_and_all_buttons))
    print(f"\nTotal minimum button presses: {total_presses}")


if __name__ == '__main__':
    main()
