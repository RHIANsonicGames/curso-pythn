import sqlite3

conn = sqlite3.connect("heroes_dragons.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS heroes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                health INTEGER,
                attack INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS dragons
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                health INTEGER,
                attack INTEGER)''')

conn.commit()
conn.close()

class Charater:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Hero(Charater):
    def __str__ (self):
        return f"Hero: {self.name}, Health: {self.health}, Attack {self.attack}"

class Dragon(Charater):
    def __str__ (self):
        return f"Dragon: {self.name}, Health: {self.health}, Attack {self.attack}"

def insert_hero(hero):
    conn = sqlite3.connect("heroes_dragons.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO heroes (name, healt, attack) VALUES (?, ?, ?)",
                   (hero.name, hero.healt. hero.attack))
    conn.commit()
    conn.close()






def insert_dragon(dragon):
    conn = sqlite3.connect("heroes_dragons.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dragons (name, healt, attack) VALUES (?, ?, ?)",
                   (dragon.name, dragon.healt. dragon.attack))
    conn.commit()
    conn.close()

def get_heroes():
    conn = sqlite3.connect("heroes_dragons.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM heroes")
    heroes_data = cursor.fetchall()
    conn.close()

    heroes = [Hero(*data[1:]) for data in heroes_data]
    return heroes

def get_dragons():
    conn = sqlite3.connect("heroes_dragons.db")
    cursor = conn.cursor()
    cursor.execute ("SELECT * FROM dragons")
    dragons_data = cursor.fetchall()
    conn.close()

    dragons = [Dragon(*data[1:]) for data in dragons_data]
    return dragons

def run_tournament():
    heroes = get_heroes()
    dragons = get_dragons()

    for hero in heroes:
        for dragon in dragons:
            if hero.attack > dragon.attack:
                print(f"{hero.name} venceu {dragon.name}!")
            else:
                print(f"{dragon.name} venceu {hero.name}!")


run_tournament()