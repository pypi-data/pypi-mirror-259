class TextGenerator:
    def __init__(self, input_string):
        self.input_string = input_string

    def convert_string(self):
        uppercase = self.input_string.upper()
        lowercase = self.input_string.lower()
        capital_case = self.input_string.capitalize()
        capital_case_starting_lowercase = self.input_string.title()

        return uppercase, lowercase, capital_case, capital_case_starting_lowercase
    

    def change_to_plural(self, word):
        word = word.lower()
        if word.endswith("y"):
            word = word[:-1]
            word = f"{word}ies"
        elif word.endswith("s"):
            word = f"{word}es"
        else:
            word = f"{word}s"
        return word

    def change_to_singular(self, word):
        word = word.lower()
        if word.endswith("ies"):
            word = word[:-3]
            word = f"{word}y"
        elif word.endswith("es"):
            word = word[:-1]
        elif word.endswith("s"):
            word = word[:-1]
        return word

    def change_to_all_singular(self, word: str, separator: str = '_', font: str = 'lower'):
        trash = []
        words = word.split(separator)
        for _word in words:
            if font == 'lower':
                _word = _word.lower()
            elif font == 'upper':
                _word = _word.upper()
            _word = self.change_to_singular(_word)
            trash.append(_word)
        
        word = separator.join(trash)
        return word
