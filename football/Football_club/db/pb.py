import sqlite3

sql = sqlite3.connect('football_club.db')
cursor = sql.cursor()

cursor.execute('''CREATE TABLE if not exists club_managment(
    id INTEGER NOT NULL Primary Key autoincrement, 
    name_cm TEXT NOT NULL,
    surname_cm TEXT NOT NULL,
    nationality TEXT NOT NULL,
    birthday text NOT NULL,
    cpecialization TEXT NOT NULL
);''')
sql.commit()

club_data = [
    (1, 'Jaon', 'Laporta', 'Ispaniya', '1974-03-08', 'Prezident'),
    (2, 'Rafael', 'Yuste', 'Ispaniya', '1978-07-05', 'Vitse-prezident'),
    (3, 'Ferran', 'Reverter', 'Ispaniya', '1987-02-15', 'Ijro direktori'),
    (4, 'Mateu', 'Alemani', 'Ispaniya', '1971-05-24', 'Sport direktori'),
    (5, 'Ramon', 'Plames', 'Ispaniya', '1977-12-26', 'Texnik sekretar'),
    (6, 'Xavi', 'Ernandes', 'Ispaniya', '1980-01-25', 'Bosh murabbiy')
]

cursor.execute('''CREATE TABLE IF NOT EXISTS coaching_stuff(
    id INTEGER NOT NULL Primary Key autoincrement,
    name_cs TEXT NOT NULL,
    surname_cs TEXT NOT NULL,
    nationality TEXT NOT NULL,
    specialization TEXT NOT NULL,
    birthday text NOT NULL,
    update_at text NOT NULL        
);''')
sql.commit()

coach_data = [
    (1, 'Xavi', 'Ernandes', 'Ispaniya', 'Bosh murabbiy', '1980-01-25', '2022-06-20'),
    (2, 'Henrik', 'Larsson', 'Shvetsiya', 'Bosh murabbiy assiistenti', '1971-09-20', '2022-06-30'),
    (3, 'Alfred', 'Schreuder', 'Niderlandiya', 'Bosh murabbiy assistenti', '1972-11-02', '2022-06-30'),
    (4, 'José', 'De la Fuente', 'Ispaniya', 'Darvozabon murabbiyi', '1970-12-22', '2022-10-20'),
    (5, 'Jaume', 'Bartres', 'Ispaniya', 'Fitness trener', '1980-01-25', '2022-06-30')
]

cursor.execute('''CREATE TABLE IF NOT EXISTS contracts(
    id INTEGER NOT NULL Primary Key autoincrement,
    contract_id INTEGER NOT NULL,
    muddat text NOT NULL,
    salary REAL NOT NULL,
    signer TEXT NOT NULL  
);''')
sql.commit()

contract_data = [
    (1, 1, '2022-06-30', 580000, 'Jozep Bartameu'),
    (2, 2, '2023-01-01', 150000, 'Joan Laporta'),
    (3, 3, '2023-06-01', 15000, 'Joan Laporta'),
    (4, 4, '2025-06-01', 525000, 'Jozep Bartameu'),
    (5, 5, '2022-06-01', 2339787.76, 'Joan Laporta'),
    (6, 6, '2023-06-01', 300000, 'Jozep Bartameu'),
    (7, 7, '2023-06-01', 411000, 'Jozep Bartameu'),
    (8, 8, '2022-06-01', 867000, 'Sandro Rossel'),
    (9, 9, '2023-06-01', 16500, 'Jozep Bartameu'),
    (10, 10, '2023-06-01', 1200000, 'Jozep Bartameu'),
    (11, 11, '2026-06-01', 294000, 'Joan Laporta')
]

cursor.execute('''CREATE TABLE IF NOT EXISTS fan_club(
    id INTEGER NOT NULL Primary Key autoincrement,
    organization_code INTEGER NOT NULL,
    fun_club_name TEXT NOT NULL,
    odamlar_soni INTEGER NOT NULL
);''')
sql.commit()

fan_club_data = [
    (1, 1007, 'Boixos Nois', 15000000),
    (2, 2384, 'Barsamaniya uz', 42000),
    (3, 3684, 'Barscamaia', 480000),
    (4, 4548, 'Penya Blaugrana Osos Rusos', 150000)
]

cursor.execute('''CREATE TABLE IF NOT EXISTS players(
    id INTEGER NOT NULL Primary Key autoincrement,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    player_number INTEGER NOT NULL,
    birthday_date TEXT NOT NULL,
    age UNSIGNED INTEGER NOT NULL,
    nationality TEXT NOT NULL,
    number_of_games INTEGER NOT NULL,
    height REAL NOT NULL,
    weight REAL NOT NULL,
    contract_id unsigned integer not null 
);''')
sql.commit()

player_data = [
    (1, 'Mark Andre', 'Ter Shtegen', 1, '1992-04-30', 29, 'Germaniya', 284, 187, 85, 1),
    (2, 'Norbertu Murara', 'Neto', 13, '1989-06-19', 32, 'Braziliya', 195, 190, 84, 2),
    (3, 'Inyaki', 'Penya', 26, '1999-03-02', 22, 'Ispaniya', 50, 185, 80, 3),
    (4, 'Serjinyo', 'Dest', 2, '2000-11-03', 21, 'Amerika', 71, 175, 62, 4),
    (5, 'Jerar', 'Pike', 3, '1987-02-02', 34, 'Ispaniya', 721, 194, 85, 5),
    (6, 'Ronald', 'Arauxo', 4, '1999-03-07', 22, 'Urugvay', 122, 191, 80, 6),
    (7, 'Kleman', 'Langle', 15, '1995-05-17', 26, 'Fransiya', 243, 186, 81, 7),
    (8, 'Jordi', 'Alba', 18, '1989-03-21', 32, 'Ispaniya', 455, 170, 68, 8),
    (9, 'Oskar', 'Mingesa', 22, '1999-05-13', 22, 'Ispaniya', 87, 184, 75, 9),
    (10, 'Samuel', 'Imtiti', 23, '1993-11-14', 28, 'Fransiya', 322, 182, 75, 10),
    (11, 'Erik', 'Garsiya', 24, '2001-01-09', 20, 'Ispaniya', 36, 183, 79, 11)
]

cursor.executemany("INSERT OR IGNORE INTO club_managment VALUES (?, ?, ?, ?, ?, ?)", club_data)
cursor.executemany("INSERT OR IGNORE INTO coaching_stuff VALUES (?, ?, ?, ?, ?, ?, ?)", coach_data)
cursor.executemany("INSERT OR IGNORE INTO contracts VALUES (?, ?, ?, ?, ?)", contract_data)
cursor.executemany("INSERT OR IGNORE INTO fan_club VALUES (?, ?, ?, ?)", fan_club_data)
cursor.executemany("INSERT OR IGNORE INTO players VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", player_data)
sql.commit()
sql.close()
