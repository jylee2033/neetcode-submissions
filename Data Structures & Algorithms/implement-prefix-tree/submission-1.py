class PrefixNode:
    def __init__(self) -> None:
        self.children = {}
        self.endNone = False


class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = PrefixNode()

            cur = cur.children[w]

        cur.endNone = True

    def search(self, word: str) -> bool:
        cur = self.root

        for w in word:
            if w not in cur.children:
                return False

            cur = cur.children[w]

        return cur.endNone
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for w in prefix:
            if w not in cur.children:
                return False

            cur = cur.children[w]

        return True
        
        