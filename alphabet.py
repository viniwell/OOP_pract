import string
class Alphabet:
    def __init__(self,lang, letters):
        self.lang=lang
        self.letters=letters
    def __str__(self):
        ans=self.letters
        return ans
    def letters_num(self):
        ans=len(self.letters)
        return ans
    

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)
    def __str__(self):
        return super().__str__()
    _letters_num=26
    def is_en_letter(self,letter):
        if letter in self.letters:
            return 'True'
        else:
            return 'False'
    def letters_num(self):
        return EngAlphabet._letters_num
    @staticmethod
    def example():
        print('Hello world')
def main():
    alph=EngAlphabet()
    print(alph)
    print(alph._letters_num)
    print(alph.is_en_letter('F'))
    print(alph.is_en_letter('Щ'))
    EngAlphabet.example()
main()
    

