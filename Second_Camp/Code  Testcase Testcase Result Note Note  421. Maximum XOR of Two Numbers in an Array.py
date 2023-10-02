class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None

class Solution:
    def findMaximumXOR(self, nums):
        root = TrieNode()
        maximumXOR = 0
        self.addBinary(root, self.getBinary(nums[0]))

        for i in range(1, len(nums)):
            binary = self.getBinary(nums[i])
            node = root
            number = 0

            for j in range(len(binary)):
                if binary[j]:
                    if node.zero:
                        node = node.zero
                        number <<= 1
                    else:
                        node = node.one
                        number = (number << 1) + 1
                else:
                    if node.one:
                        node = node.one
                        number = (number << 1) + 1
                    else:
                        node = node.zero
                        number <<= 1

            maximumXOR = max(maximumXOR, nums[i] ^ number)
            self.addBinary(root, binary)

        return maximumXOR

    def addBinary(self, root, binary):
        node = root

        for i in range(len(binary)):
            if binary[i]:
                if not node.one:
                    node.one = TrieNode()
                node = node.one
            else:
                if not node.zero:
                    node.zero = TrieNode()
                node = node.zero

    def getBinary(self, num):
        binary = [False] * 31
        index = 30

        while num > 0:
            binary[index] = (num & 1) == 1
            num >>= 1
            index -= 1

        return binary
