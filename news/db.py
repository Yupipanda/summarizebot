import sqlite3, re, random
from deep_translator import GoogleTranslator
import os

class PostDB:
    def __init__(self):
        path = os.getcwd() + '/.config/database/'
        self.db = sqlite3.connect(path + 'posts.db')
        self.cur = self.db.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS posts (
            link TEXT,
            title TEXT
        )""")
        self.db.commit()
    def _check_post(self, link):
        self.cur.execute("SELECT COUNT(0) FROM posts WHERE link=?", (link,))
        result = self.cur.fetchone()[0]
        if result == 0:
            return False
        else:
            return True
    @staticmethod
    def verify_post(link):
        url_patterns = [re.compile(r'https?://'), re.compile(r'http?://')]
        if url_patterns[0].match(link) or url_patterns[1].match(link):
            return True
        else:
            return False

    def add_post(self, link, title):
        translated_title = ''
        for i in range(0, 4):
            try:
                translated_title = GoogleTranslator(source='auto', target='ru').translate(title)
                if translated_title != '':
                    break
            except Exception:
                print('Пробую еще раз перевести заголовок:\n======\n{title}\n======')
        values = (link, translated_title)
        self.cur.execute("INSERT INTO posts (link, title) VALUES (?, ?)", values)
        self.db.commit()
        self.db.close()
        print(f'Добавленно в базу:\n======\n{link}\n======\n{translated_title}\n======')
    def add_post_ifnexist(self, link, title):
        translated_title = ''
        for i in range(0, 4):
            try:
                translated_title = GoogleTranslator(source='auto', target='ru').translate(title)
                if translated_title != '':
                    break
            except Exception:
                print(f'Пробую еще раз перевести заголовок:\n======\n{title}\n======')
        if not self._check_post(link):
            values = (link, translated_title)
            self.cur.execute("INSERT INTO posts (link, title) VALUES (?, ?)", values)
            self.db.commit()
            self.db.close()
            print(f'Добавленно в базу:\n======\n{link}\n======\n{translated_title}\n======')
        else:
            print(f'Запись:\n======\n{link}\n======\n{translated_title}\n======\nУже есть в базе.')
    def get_items(self, limit):
        self.cur.execute('SELECT * FROM posts')
        items = self.cur.fetchmany(limit)
        random.shuffle(items)
        return items

