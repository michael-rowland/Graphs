def earliest_ancestor(ancestors, start):
    parents = {}
    for parent, child in ancestors:
        if child not in parents:
            parents[child] = set()
        parents[child].add(parent)
    # data stored as dict of child: parents
    # {1: {10}, 3: {1, 2}, 5: {4}, 6: {3, 5}, 7: {5}, 8: {11, 4}, 9: {8}}

    if start not in parents:
        return -1

    visited = set()
    current = parents[start]
    while True:
        gen_lines = set()
        for parent in current:
            if parent in parents:
                # adds to stack if the parent has parents
                gen_lines = gen_lines.union(parents[parent])
            # if there was nothing added to stack, current is oldest ancestor
            if len(gen_lines) == 0:
                return min(current)
            # otherwise rerun loop with parents of parents as new current
            current = gen_lines
