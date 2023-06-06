class Trie:

    def __init__(self):
        self.trie={}

    def insert(self, word: str) -> None:
        t=self.trie
        for i in word:
            if i not in t : 
                t[i]={}
            t=t[i]
        t['-']=True
        

    def search(self, word: str) -> bool:
        t=self.trie
        for i in word:
            if i not in t: return False
            t=t[i]
        return '-' in t
        

    def startsWith(self, prefix: str) -> bool:
        t=self.trie
        for i in prefix:
            if i not in t :return False
            t=t[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)