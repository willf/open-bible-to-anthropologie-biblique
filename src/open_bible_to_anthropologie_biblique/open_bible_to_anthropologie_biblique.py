from typing import List

from jinja2 import Environment, FileSystemLoader

#from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(loader=FileSystemLoader('templates/'))

class OpenBibleToAnthropologieBiblique:
    def __init__(self):
        self.title_converter = {'Genesis' : 'Gn',  'Exodus' : 'Ex',  'Leviticus' : 'Lv',  'Numbers' : 'Nb',  'Deuteronomy' : 'Dt',  'Joshua' : 'Jos',  'Judges' : 'Jg',  'Ruth' : 'Rt',  '1 Samuel' : '1 S',  '2 Samuel' : '2 S',  '1 Kings' : '1 R',  '2 Kings' : '2 R',  '1 Chronicles' : '1 Ch',  '2 Chronicles' : '2 Ch',  'Ezra' : 'Esd',  'Nehemiah' : 'Ne',  'Esther' : 'Tb',  'Job' : 'Jb',  'Psalm' : 'Ps',  'Proverbs' : 'Pr',  'Ecclesiastes' : 'Qo',  'Song of Solomon' : 'Ct',  'Isaiah' : 'Is',  'Jeremiah' : 'Jr',  'Lamentations' : 'Lm',  'Ezekiel' : 'Ez',  'Daniel' : 'Dn',  'Hosea' : 'Os',  'Joel' : 'Jl',  'Amos' : 'Am',  'Obadiah' : 'Ab',  'Jonah' : 'Jon',  'Micah' : 'Mi',  'Nahum' : 'Na',  'Habakkuk' : 'Ha',  'Zephaniah' : 'So',  'Haggai' : 'Ag',  'Zechariah' : 'Za',  'Malachi' : 'Ml',  'Matthew' : 'Mt',  'Mark' : 'Mc',  'Luke' : 'Lc',  'John' : 'Jn',  'Acts' : 'Ac',  'Romans' : 'Rm',  '1 Corinthians' : '1 Co',  '2 Corinthians' : '2 Co',  'Galatians' : 'Ga',  'Ephesians' : 'Ep',  'Philippians' : 'Ph',  'Colossians' : 'Col',  '1 Thessalonians' : '1 Th',  '2 Thessalonians' : '2 Th',  '1 Timothy' : '1 Tm',  '2 Timothy' : '2 Tm',  'Titus' : 'Tt',  'Philemon' : 'Phm',  'Hebrews' : 'He',  'James' : 'Jc',  '1 Peter' : '1 P',  '2 Peter' : '2 P',  '1 John' : '1 Jn',  '2 John' : '2 Jn',  '3 John' : '3 Jn',  'Jude' : 'Jude',  'Revelation' : 'Ap',  }

    def convert_title(self, title: str) -> str:
        return self.title_converter[title]

class OpenBibleToAnthropologieBibliqueChapter:
    def __init__(self, book: str, bible_keys:List[str], language: str, chapter_number: int, css_class: str, direction: str, verses: List[str]):
        self.book = book
        self.bible_keys = bible_keys
        self.language = language
        self.chapter_number = chapter_number
        self.css_class = css_class
        self.direction = direction
        self.verses = verses

    def render_template(self):
        template_name = "chapter.md.jinja"
        template = env.get_template(template_name)
        tags = []
        for bible_key in self.bible_keys:
            tags.append(f"Bible/{bible_key}/{self.chapter_number}")
        tags.append(self.language)
        return template.render(book=self.book, bible_keys=self.bible_keys, chapter_number=self.chapter_number, css_class=self.css_class, direction=self.direction, verses=self.verses)


def


if __name__ == "__main__":
    import doctest

    doctest.testmod()
