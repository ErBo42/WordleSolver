
class WordleSolver:
    def __init__(self):
        self.__word_list = []
        self.__letter_total_dict = {}
        self.__letter_freq_dict = {}
        self.create_word_list()


    def create_word_list(self):
        f = open("valid-wordle-words.txt", "r")
        list_words = []
        for words in f.readlines():
            list_words.append(words.strip())
        f.close()
        self.__word_list = list_words

    def get_word_list(self):
        return self.__word_list

    def delete_word(self, letter):
        self.__word_list = [word for word in self.__word_list if letter not in word]

    def in_word(self, letter):
        self.__word_list = [word for word in self.__word_list if letter in word]

    def at_pos(self, letter, pos):
        self.__word_list = [word for word in self.__word_list if letter is word[pos-1]]

    def not_at_pos(self, letter, pos):
        self.in_word(letter)
        self.__word_list = [word for word in self.__word_list if letter is not word[pos-1]]

    def create_letter_freq(self):
        for word in self.__word_list:
            for i in word:
                x = self.__letter_total_dict.get(i)
                if x is None:
                    self.__letter_total_dict.update({i: 1})
                else:
                    self.__letter_total_dict.update({i: x + 1})

        total_letters = len(self.__word_list) * 5

        for key in self.__letter_total_dict:
            self.__letter_freq_dict[key] = (self.__letter_total_dict[key]/total_letters)

    def get_letter_freq(self):
        return self.__letter_freq_dict

    def get_letter_total(self):
        return self.__letter_total_dict

    def get_word_rec(self):
        self.create_letter_freq()
        best_word = ""
        best_value = 0
        for word in self.__word_list:
            current_value = 0
            current_word = word
            used_letters = []
            for letter in current_word:
                if letter not in used_letters:
                    used_letters.append(letter)
                    current_value += self.__letter_freq_dict[letter]

            if current_value > best_value:
                best_value = current_value
                best_word = current_word
        return best_word



