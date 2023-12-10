#!/bin/python3

import sys


class TrieNode:
    def __init__(self):
        self.children = {}
        self.failure_link = None
        self.output = []


def build_ac_table(genes):
    root = TrieNode()

    # Build the Trie
    for i, pattern in enumerate(genes):
        node = root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.output.append((pattern, i))

    # Build failure links using BFS
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        for key, child_node in current_node.children.items():
            queue.append(child_node)

            if current_node == root:
                child_node.failure_link = root
            else:
                failure_node = current_node.failure_link
                while failure_node and key not in failure_node.children:
                    failure_node = failure_node.failure_link
                child_node.failure_link = failure_node.children[key] if failure_node else root

            child_node.output += child_node.failure_link.output

    return root


def search_ac_table(text, ac_table, health, first, last):
    current_state = ac_table  # Start at the root of the Aho-Corasick Trie
    # results = []
    total_health = 0

    for i, char in enumerate(text):
        while current_state != ac_table and char not in current_state.children:
            current_state = current_state.failure_link

        if char in current_state.children:
            current_state = current_state.children[char]
        else:
            current_state = ac_table

        for o in current_state.output:
            gene_index = o[1]
            if first <= gene_index <= last:
                # pattern = o[0]
                # position = i - len(pattern) + 1
                # results.append((position, pattern, gene_index))
                total_health += health[gene_index]

    return total_health


if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input().strip())

    ac_table = build_ac_table(genes)

    unhealthiest, healthiest = sys.maxsize, 0
    for s_itr in range(s):

        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]

        d_total_ghealth = search_ac_table(d, ac_table, health, first, last)

        # d_total_ghealth = 0
        # matches = search_ac_table(d, ac_table, first, last)
        # for position, pattern, gene_index in matches:
        #     d_total_ghealth += health[gene_index]

        unhealthiest = min(d_total_ghealth, unhealthiest)
        healthiest = max(d_total_ghealth, healthiest)

    print(unhealthiest, healthiest)
