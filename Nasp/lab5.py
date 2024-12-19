import heapq

TOL_DEC = 3
TOLERANCE = 10**-TOL_DEC


class Node:
    """Node in a Huffman tree
    """

    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob  # probability of symbol
        self.symbol = symbol
        self.left = left
        self.right = right

        # incoming tree direction to node (0/1) - root has ''
        self.code = ''

    def __lt__(self, other: 'Node') -> bool:
        """enables comparisons between objects

        Args:
            other (Node): other object in comparison

        Returns:
            bool: True if self is LESS THAN other,
                  False otherwise
        """
        if roundToDecimals(self.prob, TOL_DEC) == roundToDecimals(other.prob, TOL_DEC):
            return self.symbol < other.symbol
        return roundToDecimals(self.prob, TOL_DEC) < roundToDecimals(other.prob, TOL_DEC)


def Huffman_tree(symbol_with_probs: dict) -> Node:
    """Builds Huffman tree

    Args:
        symbol_with_probs (dict): dictionary symbol-probability that describes the problem

    Returns:
        Node: root of the built Huffman tree
    """
    symbols = symbol_with_probs.keys()  # Get the symbols
    nodes_queue = []
    for symbol in symbols:
        nodes_queue.append(Node(symbol_with_probs[symbol], symbol))  # Nodes for each
    
    heapq.heapify(nodes_queue)  # heap

    while len(nodes_queue) > 1:
        # Two smallest nodes
        left = heapq.heappop(nodes_queue)
        right = heapq.heappop(nodes_queue) # HINT 2

        # Combine nodes into one parent node
        comb_prob = left.prob + right.prob
        comb_symbol = ''.join(sorted(left.symbol + right.symbol))  # HINT 1
        new_node = Node(comb_prob, comb_symbol, left, right)

        left.code = '0'
        right.code = '1'

        heapq.heappush(nodes_queue, new_node) # HINT 2

    return nodes_queue[0]


####################### IT'S BETTER NOT TO MODIFY THE CODE BELOW ##############


def calculate_codes(node: Node, val: str = '', codes=dict()) -> dict:
    # calculates codewords for Huffman subtree starting from node

    newVal = val + str(node.code)

    if(node.left):
        calculate_codes(node.left, newVal, codes)
    if(node.right):
        calculate_codes(node.right, newVal, codes)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal

    return codes


def Huffman_encode(data: str, coding: dict) -> str:
    # encodes
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])
    string = ''.join([str(item) for item in encoding_output])
    return string


def Huffman_decode(encoded_data: str, huffman_tree: Node) -> str:
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right
        elif x == '0':
            huffman_tree = huffman_tree.left
        # check if leaf
        if huffman_tree.left is None and huffman_tree.right is None:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head

    string = ''.join([str(item) for item in decoded_output])
    return string


def roundToDecimals(num: float, decimals: int) -> float:
    """Rounds number to significant decimals

    Args:
        num (float): number to round
        decimals (int): number of significant decimals

    Returns:
        float: rounded number
    """
    return round(num*10**decimals)/10**decimals


symbols_with_probs={'A':0.13,'B':0.21,'C':0.39,'D':0.19,'E':0.08}
print('problem: ', symbols_with_probs)
tree=Huffman_tree(symbols_with_probs)
huffman_code = calculate_codes(tree)
print('encoding:',huffman_code)

data = 'DEBADE'
print('original text: ',data)

print('-------ENCODE--------')
enc=Huffman_encode(data,huffman_code)
print('data encoded: ',enc)

print('-------DECODE--------')
print('data decoded back: ',Huffman_decode(enc,tree))

""" # ispravan izlaz
problem:  {'A': 0.13, 'B': 0.21, 'C': 0.39, 'D': 0.19, 'E': 0.08}
encoding: {'D': '00', 'E': '010', 'A': '011', 'B': '10', 'C': '11'}
original text:  DEBADE
-------ENCODE--------
data encoded:  000101001100010
-------DECODE--------
data decoded back:  DEBADE
"""
    