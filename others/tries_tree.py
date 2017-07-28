class TrieNode():
	def __init__(self,):
		self.next = {}


class Trie():
	def __init__(self,):
		self.root = TrieNode()

	def Add(self,word):
		node = self.root
		for w in word:
			if w not in node.next:
				node.next[w] = TrieNode()
			node = node.next[w]
		return True;

	def search(self,word):
		node = self.root
		for w in word:
			if w not in node.next:
				return False 
			node = node.next[w]
		return True


t = Trie()



t.Add('liu')
print t.search('liu')
t.Add('te')
print t.search('te')

print t.search('zhou')

