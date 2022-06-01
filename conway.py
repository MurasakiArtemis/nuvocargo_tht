
automata_size = 5
maximum_time = 3

cellular_automaton = [
    [False, False, False, False, False],
    [True, True, True, False, False], 
    [False, False, False, False, False],
    [False, False, False, True, True],
    [False, False, False, True, True]
]

next_cellular_automaton = [
    [False, False, False, False, False],
    [False, False, False, False, False], 
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False]
]

def print_cellular_automaton(automaton):
    for i in range(0, automata_size):
        line = '|'
        for j in range(0, automata_size):
            if automaton[i][j]:
                line = line + "*"
            else:
                line = line + " "
            line = line + "|"
        print(line)

for time in range(0, maximum_time):
    print_cellular_automaton(cellular_automaton)
    print()
    # I don't quite like accessing list items by index
    for i in range(0, automata_size):
        for j in range(0, automata_size):
            current_cell = cellular_automaton[i][j]
            neighbors = []
            # Can be done as list comprehension, but it looks ugly
            for x in range(max(0, i-1), min(i+2, automata_size)):
                for y in range(max(0, j-1), min(j+2, automata_size)):
                    if x != i or y != j:
                        neighbors.append(cellular_automaton[x][y])
            alive_neighbors = [element for element in neighbors if element]
            lives_next_gen = False
            # Gets whether this cell will keep active next cycle
            if current_cell and len(alive_neighbors) > 1 and len(alive_neighbors) < 4:
                lives_next_gen = True
            # Gets whether this cell will activate next cycle
            if not current_cell and len(alive_neighbors) == 3:
                lives_next_gen = True
            # Sets value for next cycle
            if lives_next_gen:
                next_cellular_automaton[i][j] = True
            else:
                next_cellular_automaton[i][j] = False

    cellular_automaton = next_cellular_automaton
    next_cellular_automaton = [
        [False, False, False, False, False],
        [False, False, False, False, False], 
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]
    ]
            