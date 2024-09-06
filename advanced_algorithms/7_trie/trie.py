"""
Trie (Prefix tree)
"""

class TrieNode:
  """Trie node"""

  def __init__(self) -> None:
    self.children = {}
    self.word = False

class Trie:
  """Trie"""

  def __init__(self) -> None:
    self.root = TrieNode()

  def insert(self, word):
    """insert a new node"""
    curr = self.root
    for c in word:
      if c not in curr.children:
        curr.children[c] = TrieNode()
      curr = curr.children[c]
    curr.word = True
  
  def search(self, word):
    """search a node"""
    curr = self.root

    for c in word:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    return curr.word
  
  def starts_with(self, prefix):
    """word start with"""
    curr = self.root

    for c in prefix:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    return True
  

prefix_tree = Trie()
prefix_tree.insert("apple")
prefix_tree.insert("appe")
prefix_tree.insert("nope")

# True
print(prefix_tree.search("apple"))
# False
print(prefix_tree.search("applo"))

# True
print(prefix_tree.starts_with("ap"))

# False
print(prefix_tree.starts_with("na"))