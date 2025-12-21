
class WordleSolver:
    def __init__(self):
        self.word_list = []


    def create_word_list(self):
        f = open("valid-wordle-words.txt", "r")
        list_words = []
        for words in f.readlines():
            list_words.append(words.strip())
        f.close()
        self.word_list = list_words

    def get_word_list(self):
        return self.word_list

    def delete_word(self, letter):
        self.word_list = [word for word in self.word_list if letter not in word]

    def in_word(self, letter):
        self.word_list = [word for word in self.word_list if letter in word]

solver = WordleSolver()
solver.create_word_list()
solver.delete_word("a")
solver.delete_word("w")
solver.delete_word("e")
solver.delete_word("t")
solver.delete_word("u")
solver.delete_word("o")
solver.delete_word("p")
solver.delete_word("s")
solver.delete_word("l")
solver.delete_word("c")
solver.delete_word("n")

solver.in_word("r")
solver.in_word("h")

print(solver.get_word_list())

