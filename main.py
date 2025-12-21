
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

    def at_pos(self, letter, pos):
        self.word_list = [word for word in self.word_list if letter is word[pos]]

    def not_at_pos(self, letter, pos):
        self.in_word(letter)
        self.word_list = [word for word in self.word_list if letter is not word[pos]]

solver = WordleSolver()
solver.create_word_list()

solver.at_pos("a", 0)
solver.at_pos("e", 4)
solver.not_at_pos("d", 2)
print(solver.get_word_list())

