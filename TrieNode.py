#!/usr/bin/python

class TrieNode():
    def __init__(self):
        self.charMap = {}
        self.stringIndex = set()
        self.is_end_of_word = False


    def add_to_Trie(self, name, index):
        if len(name) <= index:
            return
        if len(name) - 1 == index:
            self.is_end_of_word = True
        char = name[index]
        index += 1
        if char in self.charMap:
            self.charMap.get(char).add_to_Trie(name, index)
        else:
            self.charMap[char] = TrieNode()
            self.charMap.get(char).add_to_Trie(name, index)


    def add_to_Trie_with_index(self, name, index, stringIndex):
        if len(name) <= index:
            return
        if len(name) - 1 == index:
            self.is_end_of_word = True
        char = name[index]
        index += 1
        if char in self.charMap:
            Node = self.charMap.get(char)
            Node.stringIndex.add(stringIndex)
            Node.add_to_Trie_with_index(name, index, stringIndex)
        else:
            self.charMap[char] = TrieNode()
            Node = self.charMap.get(char)
            Node.stringIndex.add(stringIndex)
            Node.add_to_Trie_with_index(name, index, stringIndex)


    def get_the_longest_match(self, search_string, index, output):
        if index >= len(search_string):
            return output

        ch = search_string[index]
        if ch in self.charMap:
            output.append(ch)
            index += 1
            self.charMap.get(ch).get_the_longest_match(search_string, index, output)
        return output


    def get_the_longest_match_with_string(self, search_string, index, output):
        if index >= len(search_string):
            return self.stringIndex

        ch = search_string[index]
        lReturn = self.stringIndex
        if ch in self.charMap:
            output.append(ch)
            index += 1
            lReturn = self.charMap.get(ch).get_the_longest_match_with_string(search_string, index, output)
        return lReturn


if __name__ == "__main__":
    no_of_inputs = int(raw_input())

    tN = TrieNode()
    strings = []
    for _ in xrange(no_of_inputs):
        name = raw_input()
        index = len(strings)
        strings.append(name)
        tN.add_to_Trie_with_index(name, 0, index)

    no_of_inputs = int(raw_input())
    for _ in xrange(no_of_inputs):
        search_string = raw_input("Enter the name to searched: ")
        output = []
        matched_string = tN.get_the_longest_match_with_string(search_string, 0, output)
        # print "".join(matched_string)
        for i in matched_string:
            print strings[i]



