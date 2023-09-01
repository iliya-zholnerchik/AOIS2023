import random


class AssociativeMemory:

    random = random.Random()

    def __init__(self, word_size=8, size=8, randomized=False):
        if not randomized:
            self._array = [[0 for _ in range(word_size)] for _ in range(size)]
        else:
            self._array = [[random.randint(0, 1) for _ in range(word_size)] for _ in range(size)]

    def __repr__(self):
        return str(self._array)

    @staticmethod
    def word_to_int(word):
        return int("".join(str(bit) for bit in word), 2)

    def find(self, min, max):
        min = self.word_to_int(min)
        max = self.word_to_int(max)

        res = []
        for word in self._array:
            iword = self.word_to_int(word)
            if min <= iword <= max:
                res.append(word)

        return res

    @staticmethod
    def _distance(first, second):
        res = 0
        for i, bit in enumerate(first):
            if bit != second[i]:
                res += 1
        return res

    def find_nearest(self, pattern):
        sorted_by_distance = sorted(self._array, key=lambda x: self._distance(x, pattern))
        return sorted_by_distance[0]

    def sort_asc(self):
        return sorted(self._array)

    def sort_desc(self):
        return sorted(self._array, reverse=True)

    def _find_logical(self, pattern, func):
        for word in self._array:
            for i, bit in enumerate(word):
                if pattern[i] is None:
                    if i == len(word) - 1:
                        return word
                    continue
                if not func(pattern[i], bit):
                    break
                if i == len(word) - 1:
                    return word
        return None

    def find_or(self, pattern):
        return self._find_logical(pattern, lambda x, y: bool(x) or bool(y))

    def find_and(self, pattern):
        return self._find_logical(pattern, lambda x, y: bool(x) and bool(y))

    def find_xor(self, pattern):
        return self._find_logical(pattern, lambda x, y: int(x) != int(y))

    def find_equ(self, pattern):
        return self._find_logical(pattern, lambda x, y: int(x) == int(y))

if __name__ == '__main__':
    memory = AssociativeMemory(randomized=True)
    print(f"Your memory: {memory}")

    cmd = ""
    while cmd != "quit":
        cmd = input(" > ")

        if cmd == "sortasc":
            print(memory.sort_asc())
        elif cmd == "sortdesc":
            print(memory.sort_desc())
        elif cmd == "nearest":
            pattern = [ch for ch in input()]
            print(memory.find_nearest(pattern))
        elif cmd == "find":
            min = [ch for ch in input()]
            max = [ch for ch in input()]
            print(memory.find(min, max))
        elif cmd == "or":
            pattern = [ch if ch != "*" else None for ch in input()]
            print(memory.find_or(pattern))
        elif cmd == "and":
            pattern = [ch if ch != "*" else None for ch in input()]
            print(memory.find_and(pattern))
        elif cmd == "xor":
            pattern = [ch if ch != "*" else None for ch in input()]
            print(memory.find_xor(pattern))
        elif cmd == "equ":
            pattern = [ch if ch != "*" else None for ch in input()]
            print(memory.find_equ(pattern))