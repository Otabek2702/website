from abc import ABC, abstractmethod
from .settings import database
import sqlite3


class BaseModel(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def objects():
        pass

    @abstractmethod
    def save(self):
        pass


class Club(BaseModel):
    def save(self):
        sql = sqlite3.connect(database)
        cur = sql.cursor()
        if self.id is None:
            cur.execute("Insert into Club_info (club_name, stadium) "
                        "values (?,?)", (self.club_name, self.stadium))
        else:
            cur.execute("Update Club_info set club_name = ?,"
                        "stadium = ?"
                        "where id = ?", (self.club_name, self.stadium, self.id))
        sql.commit()
        sql.close()

    def update(self):
        pass

    def objects():
        sql = sqlite3.connect(database)
        cursor = sql.execute("SELECT id, Club_name, stadium  from Club_info")
        res = []
        for row in cursor:
            res.append(Club(row[1], row[2], row[0]))
        sql.close()
        return res

    def delete(self):
        sql = sqlite3.connect(database)
        cur = sql.cursor()
        cur.execute(f"Delete from Club_info where id={self.id}")
        sql.commit()
        sql.close()

    def __init__(self, club_name, stadium, id=None):
        super().__init__(id)
        self.club_name = club_name
        self.stadium = stadium

    @property
    def club_name(self):
        return self.__club_name

    @club_name.setter
    def club_name(self, value):
        if isinstance(value, str):
            self.__club_name = value
        else:
            self.__club_name = ''

    @property
    def stadium(self):
        return self.__stadium

    @stadium.setter
    def stadium(self, value):
        if isinstance(value, str):
            self.__stadium = value
        else:
            self.__stadium = ''

    def __str__(self):
        return f"{self.club_name} {self.stadium}"


class Club_Managment(Club):
    def __init__(self, name, surname, nationality,
                 birthday, prestige, id=None, club_name=None, stadium=None):
        super().__init__(club_name, stadium, id)
        self.name = name
        self.surname = surname
        self.nationality = nationality
        self.birthday = birthday
        self.prestige = prestige

    def save(self):
        sql = sqlite3.connect(database)
        cur = sql.cursor()
        if self.id is None:
            cur.execute("Insert into club_managment (name_cm, "
                        "surname_cm, "
                        "nationality, "
                        "Birthday, "
                        "prestige) "
                        "values (?, ?, ?, ?, ?)", (self.name,
                                                   self.surname,
                                                   self.nationality,
                                                   self.birthday,
                                                   self.prestige
                                                   ))
        else:
            cur.execute("Update club_managment set name_cm = ?, "
                        "surname_cm = ?,"
                        "nationality=?,"
                        "Birthday=?,"
                        "prestige=?"
                        " where id = ?;", (self.name, self.surname,
                                           self.nationality, self.birthday,
                                           self.prestige, self.id))
        sql.commit()
        sql.close()

    def objects():
        sql = sqlite3.connect(database)
        cursor = sql.execute("SELECT id, name_cm,"
                             " surname_cm, nationality,"
                             "birthday, prestige "
                             "from club_managment;")
        res = []
        for row in cursor:
            res.append(Club_Managment(row[1], row[2], row[3], row[4], row[5], row[0]))
        sql.close()
        return res

    def delete(self):
        sql = sqlite3.connect(database)
        cur = sql.cursor()
        cur.execute(f"Delete from club_managment where id={self.id}")
        sql.commit()
        sql.close()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            self.__name = ''

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if isinstance(value, str):
            self.__surname = value
        else:
            self.__surname = ''

    @property
    def nationality(self):
        return self.__nationality

    @nationality.setter
    def nationality(self, value):
        if isinstance(value, str):
            self.__nationality = value
        else:
            self.__nationality = ''

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if isinstance(value, str):
            self.__birthday = value
        else:
            self.__birthday = ''

    def __str__(self):
        return f"{self.name} {self.surname} " \
               f"{self.nationality} {self.birthday} {self.prestige}"


class CoachingStuff(Club):
    def __init__(self, name, surname, nationality,
                 specialization, birthday,
                 id=None, club_name=None, stadium=None,
                 ):
        super().__init__(club_name, stadium, id)
        self.name = name
        self.surname = surname
        self.nationality = nationality
        self.specialization = specialization
        self.birthday = birthday

    def save(self):
        sql = sqlite3.connect(database)
        cur = sql.cursor()
        if self.id is None:
            cur.execute("Insert into coaching_stuff (name_cs, "
                        "surname_cs, "
                        "nationality, "
                        "specialization, "
                        "birthday) "
                        "values (?,?,?,?,?)", (self.name,
                                               self.surname,
                                               self.nationality,
                                               self.specialization,
                                               self.birthday
                                               ))
        else:
            cur.execute("Update coaching_stuff set name_cs = ?, "
                        "surname_cs = ?,"
                        "nationality=?,"
                        "specialization=?,"
                        "birthday=?"
                        " where id = ?;", (self.name, self.surname,
                                           self.nationality, self.specialization,
                                           self.birthday, self.id))
        sql.commit()
        sql.close()

    def objects():
        sql = sqlite3.connect(database)
        cursor = sql.execute("SELECT id, name_cs,"
                             " surname_cs, nationality,"
                             " specialization, birthday "
                             "from coaching_stuff;")
        res = []
        for row in cursor:
            res.append(CoachingStuff(row[1], row[2], row[3], row[4], row[5], row[0]))
        sql.close()
        return res

    def delete(self):
        sql = sqlite3.connect(database)
        cur = sql.cursor()
        cur.execute(f"Delete from coaching_stuff where id={self.id}")
        sql.commit()
        sql.close()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if isinstance(value, str):
            self.__surname = value
        else:
            self.__surname = ''

    def __str__(self):
        return f"{self.name} {self.surname} " \
               f"{self.nationality} {self.specialization} " \
               f"{self.birthday}"


class Player(BaseModel):
    def update(self):
        pass

    def __init__(self, name, surname, player_number, birthday_date,
                 age, nationality, number_of_games,
                 height, weight, contract_id, id=None):
        super().__init__(id)
        self.name = name
        self.surname = surname
        self.player_number = player_number
        self.birthday_date = birthday_date
        self.age = age
        self.nationality = nationality
        self.number_of_games = number_of_games
        self.height = height
        self.weight = weight
        self.contract_id = contract_id

    def save(self):
        sql = sqlite3.connect(database)
        cur = sql.cursor()
        if self.id is None:
            cur.execute("Insert into players (name, surname, player_number,"
                        "birthday_date, age, nationality, number_of_games,"
                        "height, weight, contract_id)"
                        " values (?,?,?,?,?,?,?,?,?,?)",
                        (self.name, self.surname,
                         self.player_number, self.birthday_date,
                         self.age, self.nationality,
                         self.number_of_games, self.height,
                         self.weight, self.contract_id))
        else:
            cur.execute("Update players set name = ?, "
                        "surname = ?,"
                        "player_number = ?,"
                        "birthday_date = ?,"
                        "age = ?,"
                        "nationality=?,"
                        "number_of_games=?,"
                        "height=?,"
                        "weight=?,"
                        "contract_id=?"
                        " where id = ?;", (self.name, self.surname,
                                           self.player_number, self.birthday_date,
                                           self.age, self.nationality,
                                           self.number_of_games, self.height,
                                           self.weight, self.contract_id, self.id))
        sql.commit()
        sql.close()

    def objects():
        sql = sqlite3.connect(database)
        cursor = sql.execute("SELECT id, name, "
                             "surname, player_number, "
                             "birthday_date, age, "
                             "nationality, number_of_games, "
                             "height, weight, contract_id  from players")
        res = []
        for row in cursor:
            res.append(Player(row[1], row[2], row[3],
                              row[4], row[5], row[6],
                              row[7], row[8], row[9],
                              row[10], row[0]))
        sql.close()
        return res

    def delete(self):
        sql = sqlite3.connect(database)
        cur = sql.cursor()
        cur.execute(f"Delete from players where id={self.id}")
        sql.commit()
        sql.close()

    def __str__(self):
        return f"{self.name} {self.surname} {self.player_number} " \
               f"{self.birthday_date} {self.age} " \
               f"{self.nationality} {self.number_of_games} " \
               f"{self.height} {self.weight} {self.contract_id}"


class Contract(BaseModel):
    def update(self):
        pass

    def __init__(self, contract_id, expiration_date,
                 salary, signer, id=None):
        super().__init__(id)
        self.contract_id = contract_id
        self.expiration_date = expiration_date
        self.salary = salary
        self.signer = signer

    def save(self):
        sql = sqlite3.connect(database)
        cur = sql.cursor()
        if self.id is None:
            cur.execute("Insert into contracts (contract_id, muddat, salary, signer) "
                        "values (?,?,?,?)", (self.contract_id, self.expiration_date,
                                             self.salary, self.signer))
        else:
            cur.execute("Update contracts set contract_id = ?,"
                        "muddat = ?,"
                        "salary=?,"
                        "signer=?"
                        "where id = ?", (self.contract_id, self.expiration_date,
                                         self.salary, self.signer, self.id))
        sql.commit()
        sql.close()

    def objects():
        sql = sqlite3.connect(database)
        cursor = sql.execute("SELECT id, contract_id, "
                             "muddat, salary, signer  from contracts")
        res = []
        for row in cursor:
            res.append(Contract(row[1], row[2], row[3], row[4], row[0]))
        sql.close()
        return res

    def delete(self):
        sql = sqlite3.connect(database)
        cur = sql.cursor()
        cur.execute(f"Delete from contracts where id={self.id}")
        sql.commit()
        sql.close()

    def __str__(self):
        return f"{self.contract_id} {self.expiration_date} {self.salary} {self.signer}"
