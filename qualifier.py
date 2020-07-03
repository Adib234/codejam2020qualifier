"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
from collections import Counter
import itertools
import gc


class ArticleField():
    """The `ArticleField` class for the Advanced Requirements."""


class Article(ArticleField):
    """The `Article` class you need to write for the qualifier."""
    newid = itertools.count()

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content
        self.id = next(self.newid)
        self._last_edited = None

    @property
    def last_edited(self):
        return self._last_edited

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, val):
        self._content = val
        self._last_edited = datetime.datetime.now()

    def __repr__(self):
        return f'<Article title=\"{self.title}\" author=\'{self.author}\' publication_date=\'{ self.publication_date.isoformat()}\'>'

    def __len__(self):
        return len(self.content)

    def __lt__(self, other):
        return self.publication_date < other.publication_date

    def __sorted__(self):
        for passnum in range(len(self)-1, 0, -1):
            for i in range(passnum):
                if self[i].publication_date > self[i+1].publication_date:
                    temp = self[i].publication_date
                    self[i].publication_date = self[i+1].publication_date
                    self[i+1].publication_date = temp
        return repr(self)

    def short_introduction(self, n_characters: int):
        if self.content[n_characters].isalpha() == True:
            start = n_characters-1
            while self.content[start].isalpha() == True:
                start -= 1
            return self.content[:start+1].strip()
        else:
            return self.content[:n_characters].strip()

    def most_common_words(self, n):
        for i in range(len(self.content)):
            if self.content[i].isalpha() == False and self.content[i] != '':
                self.content = self.content.replace(self.content[i], ' ')
        commonList = self.content.replace('\n', ' ').lower().split()
        counter = Counter(commonList).most_common(n)

        order = []
        for i in counter:
            order.append(i[0])

        final = {}

        for i in range(len(counter)):
            final[order[i]] = counter[i][1]
        return final
