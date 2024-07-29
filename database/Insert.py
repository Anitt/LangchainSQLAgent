# Insert into HR database .

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('../hr_database.db')
cursor = conn.cursor()

# Insert data into the regions table
regions_data = [
    (1, 'Europe'),
    (2, 'Americas'),
    (3, 'Asia'),
    (4, 'Middle East and Africa')
]

cursor.executemany("INSERT INTO regions (region_id, region_name) VALUES (?, ?)", regions_data)

# Insert data into the countries table
countries_data = [
    ('AR', 'Argentina', 2),
    ('AU', 'Australia', 3),
    ('BE', 'Belgium', 1),
    ('BR', 'Brazil', 2),
    ('CA', 'Canada', 2),
    ('CH', 'Switzerland', 1),
    ('CN', 'China', 3),
    ('DE', 'Germany', 1),
    ('DK', 'Denmark', 1),
    ('EG', 'Egypt', 4),
    ('FR', 'France', 1),
    ('HK', 'HongKong', 3),
    ('IL', 'Israel', 4),
    ('IN', 'India', 3),
    ('IT', 'Italy', 1),
    ('JP', 'Japan', 3),
    ('KW', 'Kuwait', 4),
    ('MX', 'Mexico', 2),
    ('NG', 'Nigeria', 4),
    ('NL', 'Netherlands', 1),
    ('SG', 'Singapore', 3),
    ('UK', 'United Kingdom', 1),
    ('US', 'United States of America', 2),
    ('ZM', 'Zambia', 4),
    ('ZW', 'Zimbabwe', 4)
]

cursor.executemany("INSERT INTO countries (country_id, country_name, region_id) VALUES (?, ?, ?)", countries_data)

# Insert data into the locations table
locations_data = [
    (1400, '2014 Jabberwocky Rd', '26192', 'Southlake', 'Texas', 'US'),
    (1500, '2011 Interiors Blvd', '99236', 'South San Francisco', 'California', 'US'),
    (1700, '2004 Charade Rd', '98199', 'Seattle', 'Washington', 'US'),
    (1800, '147 Spadina Ave', 'M5V 2L7', 'Toronto', 'Ontario', 'CA'),
    (2400, '8204 Arthur St', None, 'London', None, 'UK'),
    (2500, 'Magdalen Centre, The Oxford Science Park', 'OX9 9ZB', 'Oxford', 'Oxford', 'UK'),
    (2700, 'Schwanthalerstr. 7031', '80925', 'Munich', 'Bavaria', 'DE')
]

cursor.executemany("INSERT INTO locations (location_id, street_address, postal_code, city, state_province, country_id) VALUES (?, ?, ?, ?, ?, ?)", locations_data)

# Insert data into the jobs table
jobs_data = [
    (1, 'Public Accountant', 4200.00, 9000.00),
    (2, 'Accounting Manager', 8200.00, 16000.00),
    (3, 'Administration Assistant', 3000.00, 6000.00),
    (4, 'President', 20000.00, 40000.00),
    (5, 'Administration Vice President', 15000.00, 30000.00),
    (6, 'Accountant', 4200.00, 9000.00),
    (7, 'Finance Manager', 8200.00, 16000.00),
    (8, 'Human Resources Representative', 4000.00, 9000.00),
    (9, 'Programmer', 4000.00, 10000.00),
    (10, 'Marketing Manager', 9000.00, 15000.00),
    (11, 'Marketing Representative', 4000.00, 9000.00),
    (12, 'Public Relations Representative', 4500.00, 10500.00),
    (13, 'Purchasing Clerk', 2500.00, 5500.00),
    (14, 'Purchasing Manager', 8000.00, 15000.00),
    (15, 'Sales Manager', 10000.00, 20000.00),
    (16, 'Sales Representative', 6000.00, 12000.00),
    (17, 'Shipping Clerk', 2500.00, 5500.00),
    (18, 'Stock Clerk', 2000.00, 5000.00),
    (19, 'Stock Manager', 5500.00, 8500.00)
]

cursor.executemany("INSERT INTO jobs (job_id, job_title, min_salary, max_salary) VALUES (?, ?, ?, ?)", jobs_data)

# Insert data into the departments table
departments_data = [
    (1, 'Administration', 1700),
    (2, 'Marketing', 1800),
    (3, 'Purchasing', 1700),
    (4, 'Human Resources', 2400),
    (5, 'Shipping', 1500),
    (6, 'IT', 1400),
    (7, 'Public Relations', 2700),
    (8, 'Sales', 2500),
    (9, 'Executive', 1700),
    (10, 'Finance', 1700),
    (11, 'Accounting', 1700)
]

cursor.executemany("INSERT INTO departments (department_id, department_name, location_id) VALUES (?, ?, ?)", departments_data)

# Insert data into the employees table
employees_data = [
    (100, 'Steven', 'King', 'steven.king@sqltutorial.org', '515.123.4567', '1987-06-17', 4, 24000.00, None, 9),
    (101, 'Neena', 'Kochhar', 'neena.kochhar@sqltutorial.org', '515.123.4568', '1989-09-21', 5, 17000.00, 100, 9),
    (102, 'Lex', 'De Haan', 'lex.dehaan@sqltutorial.org', '515.123.4569', '1993-01-13', 5, 17000.00, 100, 9),
    (103, 'Alexander', 'Hunold', 'alexander.hunold@sqltutorial.org', '590.423.4567', '1990-01-03', 9, 9000.00, 102, 6),
    (104, 'Bruce', 'Ernst', 'bruce.ernst@sqltutorial.org', '590.423.4568', '1991-05-21', 9, 6000.00, 103, 6),
    (105, 'David', 'Austin', 'david.austin@sqltutorial.org', '590.423.4569', '1997-06-25', 9, 4800.00, 103, 6),
    (106, 'Valli', 'Pataballa', 'valli.pataballa@sqltutorial.org', '590.423.4560', '1998-02-05', 9, 4800.00, 103, 6),
    (107, 'Diana', 'Lorentz', 'diana.lorentz@sqltutorial.org', '590.423.5567', '1999-02-07', 9, 4200.00, 103, 6),
    (108, 'Nancy', 'Greenberg', 'nancy.greenberg@sqltutorial.org', '515.124.4569', '1994-08-17', 7, 12000.00, 101, 10),
    (109, 'Daniel', 'Faviet', 'daniel.faviet@sqltutorial.org', '515.124.4169', '1994-08-16', 6, 9000.00, 108, 10),
    (110, 'John', 'Chen', 'john.chen@sqltutorial.org', '515.124.4269', '1997-09-28', 6, 8200.00, 108, 10),
    (111, 'Ismael', 'Sciarra', 'ismael.sciarra@sqltutorial.org', '515.124.4369', '1997-09-30', 6, 7700.00, 108, 10),
    (112, 'Jose Manuel', 'Urman', 'josemanuel.urman@sqltutorial.org', '515.124.4469', '1998-03-07', 6, 7800.00, 108, 10),
    (113, 'Luis', 'Popp', 'luis.popp@sqltutorial.org', '515.124.4567', '1999-12-07', 6, 6900.00, 108, 10),
    (114, 'Den', 'Raphaely', 'den.raphaely@sqltutorial.org', '515.127.4561', '1994-12-07', 15, 11000.00, 100, 8),
    (115, 'Alexander', 'Khoo', 'alexander.khoo@sqltutorial.org', '515.127.4562', '1995-05-18', 16, 3100.00, 114, 8),
    (116, 'Shelli', 'Baida', 'shelli.baida@sqltutorial.org', '515.127.4563', '1997-12-24', 16, 2900.00, 114, 8),
    (117, 'Sigal', 'Tobias', 'sigal.tobias@sqltutorial.org', '515.127.4564', '1997-07-24', 16, 2800.00, 114, 8),
    (118, 'Guy', 'Himuro', 'guy.himuro@sqltutorial.org', '515.127.4565', '1998-11-15', 16, 2600.00, 114, 8),
    (119, 'Karen', 'Colmenares', 'karen.colmenares@sqltutorial.org', '515.127.4566', '1999-08-10', 16, 2500.00, 114, 8),
    (120, 'Matthew', 'Weiss', 'matthew.weiss@sqltutorial.org', '650.123.1234', '1996-07-18', 9, 8000.00, 100, 6),
    (121, 'Adam', 'Fripp', 'adam.fripp@sqltutorial.org', '650.123.2234', '1999-04-10', 9, 8200.00, 120, 6),
    (122, 'Payam', 'Kaufling', 'payam.kaufling@sqltutorial.org', '650.123.3234', '1995-05-01', 9, 7900.00, 121, 6),
    (123, 'Shanta', 'Vollman', 'shanta.vollman@sqltutorial.org', '650.123.4234', '1997-10-10', 9, 6500.00, 121, 6),
    (124, 'Kevin', 'Mourgos', 'kevin.mourgos@sqltutorial.org', '650.123.5234', '1999-11-16', 9, 5800.00, 121, 6),
    (125, 'Julia', 'Nayer', 'julia.nayer@sqltutorial.org', '650.124.1214', '1997-07-16', 10, 3200.00, 100, 7),
    (126, 'Irene', 'Mikkilineni', 'irene.mikkilineni@sqltutorial.org', '650.124.1224', '1998-09-28', 10, 2700.00, 125, 7),
    (127, 'James', 'Landry', 'james.landry@sqltutorial.org', '650.124.1334', '1999-01-14', 10, 2400.00, 125, 7),
    (128, 'Steven', 'Markle', 'steven.markle@sqltutorial.org', '650.124.1434', '1998-03-08', 10, 2200.00, 125, 7),
    (129, 'Laura', 'Bissot', 'laura.bissot@sqltutorial.org', '650.124.5234', '1997-08-20', 9, 3300.00, 120, 6),
    (130, 'Mozhe', 'Atkinson', 'mozhe.atkinson@sqltutorial.org', '650.124.6234', '1997-10-30', 9, 2800.00, 120, 6),
    (131, 'James', 'Marquez', 'james.marquez@sqltutorial.org', '650.124.7234', '1998-01-05', 9, 2500.00, 120, 6),
    (132, 'TJ', 'Olson', 'tj.olson@sqltutorial.org', '650.124.8234', '1999-04-10', 9, 2100.00, 120, 6),
    (133, 'Jason', 'Mallin', 'jason.mallin@sqltutorial.org', '650.127.1934', '1996-06-14', 9, 3300.00, 121, 6),
    (134, 'Michael', 'Rogers', 'michael.rogers@sqltutorial.org', '650.127.1935', '1998-08-26', 9, 2900.00, 121, 6),
    (135, 'Ki', 'Gee', 'ki.gee@sqltutorial.org', '650.127.1936', '1999-12-12', 9, 2400.00, 121, 6),
    (136, 'Hazel', 'Philtanker', 'hazel.philtanker@sqltutorial.org', '650.127.1937', '2000-02-06', 9, 2200.00, 121, 6),
    (137, 'Renske', 'Ladwig', 'renske.ladwig@sqltutorial.org', '650.121.1234', '1995-07-14', 9, 3600.00, 121, 6),
    (138, 'Stephen', 'Stiles', 'stephen.stiles@sqltutorial.org', '650.121.2034', '1995-10-26', 9, 3200.00, 121, 6),
    (139, 'John', 'Seo', 'john.seo@sqltutorial.org', '650.121.2019', '1997-02-12', 9, 2700.00, 121, 6),
    (140, 'Joshua', 'Patel', 'joshua.patel@sqltutorial.org', '650.121.2020', '1998-04-06', 9, 2500.00, 121, 6),
    (141, 'Trenna', 'Rajs', 'trenna.rajs@sqltutorial.org', '650.121.2004', '1998-10-17', 9, 2900.00, 121, 6),
    (142, 'Curtis', 'Davies', 'curtis.davies@sqltutorial.org', '650.121.2990', '1999-01-29', 9, 3100.00, 121, 6),
    (143, 'Randall', 'Matos', 'randall.matos@sqltutorial.org', '650.121.2877', '1998-03-15', 9, 2600.00, 121, 6),
    (144, 'Peter', 'Vargas', 'peter.vargas@sqltutorial.org', '650.121.2298', '1998-07-09', 9, 2500.00, 121, 6),
    (145, 'John', 'Russell', 'john.russell@sqltutorial.org', '011.44.1344.429268', '1996-10-01', 9, 14000.00, 100, 8),
    (146, 'Karen', 'Partners', 'karen.partners@sqltutorial.org', '011.44.1344.429278', '1997-01-05', 9, 13500.00, 100, 8),
    (147, 'Alberto', 'Errazuriz', 'alberto.errazuriz@sqltutorial.org', '011.44.1344.429268', '1997-03-10', 9, 12000.00, 145, 8),
    (148, 'Gerald', 'Cambrault', 'gerald.cambrault@sqltutorial.org', '011.44.1344.429267', '1999-10-15', 9, 11000.00, 147, 8),
    (149, 'Eleni', 'Zlotkey', 'eleni.zlotkey@sqltutorial.org', '011.44.1344.429266', '2000-01-29', 9, 10500.00, 148, 8),
    (150, 'Peter', 'Tucker', 'peter.tucker@sqltutorial.org', '011.44.1344.429265', '2000-01-30', 9, 10000.00, 147, 8),
    (151, 'David', 'Bernstein', 'david.bernstein@sqltutorial.org', '011.44.1344.429264', '2000-03-24', 9, 9500.00, 147, 8),
    (152, 'Peter', 'Hall', 'peter.hall@sqltutorial.org', '011.44.1344.429263', '2000-03-24', 9, 9000.00, 147, 8),
    (153, 'Christopher', 'Olsen', 'christopher.olsen@sqltutorial.org', '650.123.8234', '1996-03-30', 9, 8000.00, 100, 7),
    (154, 'Nanette', 'Cambrault', 'nanette.cambrault@sqltutorial.org', '650.123.9234', '1998-12-09', 9, 7500.00, 153, 7),
    (155, 'Oliver', 'Tuvault', 'oliver.tuvault@sqltutorial.org', '650.124.6234', '1999-11-23', 9, 7000.00, 153, 7),
    (156, 'Janette', 'King', 'janette.king@sqltutorial.org', '650.124.7234', '2000-01-30', 9, 6500.00, 154, 7),
    (157, 'Patrick', 'Sully', 'patrick.sully@sqltutorial.org', '650.124.8234', '2000-03-04', 9, 6000.00, 154, 7),
    (158, 'Allan', 'Mccain', 'allan.mccain@sqltutorial.org', '650.124.9234', '2000-03-04', 9, 5500.00, 154, 7),
    (159, 'Lindsey', 'Smith', 'lindsey.smith@sqltutorial.org', '650.127.4234', '2000-03-10', 9, 5000.00, 154, 7),
    (160, 'Louise', 'Doran', 'louise.doran@sqltutorial.org', '650.127.5234', '2000-03-10', 9, 4500.00, 154, 7),
    (161, 'Sarath', 'Sewall', 'sarath.sewall@sqltutorial.org', '650.127.6234', '2000-03-10', 9, 4000.00, 154, 7),
    (162, 'Clara', 'Vishney', 'clara.vishney@sqltutorial.org', '650.127.7234', '2000-03-10', 9, 3500.00, 154, 7),
    (163, 'Danielle', 'Greene', 'danielle.greene@sqltutorial.org', '650.127.8234', '2000-03-10', 9, 3000.00, 154, 7),
    (164, 'Mattea', 'Marvins', 'mattea.marvins@sqltutorial.org', '650.127.9234', '2000-03-10', 9, 2500.00, 154, 7),
    (165, 'David', 'Lee', 'david.lee@sqltutorial.org', '650.121.1234', '2000-03-24', 9, 2000.00, 100, 7),
    (166, 'Sundar', 'Ande', 'sundar.ande@sqltutorial.org', '650.121.2234', '2000-03-24', 9, 1500.00, 100, 7),
    (167, 'Amit', 'Banda', 'amit.banda@sqltutorial.org', '650.121.3234', '2000-03-24', 9, 1100.00, 100, 7),
    (168, 'Lisa', 'Salos', 'lisa.salos@sqltutorial.org', '650.121.4234', '2000-03-24', 9, 900.00, 100, 7)
]

cursor.executemany("INSERT INTO employees (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", employees_data)



# Commit the changes and close the connection
conn.commit()
conn.close()



import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('../hr_database.db')
cursor = conn.cursor()

# Data for the table dependents
dependents_data = [
    (1, 'Penelope', 'Gietz', 'Child', 206),
    (2, 'Nick', 'Higgins', 'Child', 205),
    (3, 'Ed', 'Whalen', 'Child', 200),
    (4, 'Jennifer', 'King', 'Child', 100),
    (5, 'Johnny', 'Kochhar', 'Child', 101),
    (6, 'Bette', 'De Haan', 'Child', 102),
    (7, 'Grace', 'Faviet', 'Child', 109),
    (8, 'Matthew', 'Chen', 'Child', 110),
    (9, 'Joe', 'Sciarra', 'Child', 111),
    (10, 'Christian', 'Urman', 'Child', 112),
    (11, 'Zero', 'Popp', 'Child', 113),
    (12, 'Karl', 'Greenberg', 'Child', 108),
    (13, 'Uma', 'Mavris', 'Child', 203),
    (14, 'Vivien', 'Hunold', 'Child', 103),
    (15, 'Cuba', 'Ernst', 'Child', 104),
    (16, 'Fred', 'Austin', 'Child', 105),
    (17, 'Helen', 'Pataballa', 'Child', 106),
    (18, 'Dan', 'Lorentz', 'Child', 107),
    (19, 'Bob', 'Hartstein', 'Child', 201),
    (20, 'Lucille', 'Fay', 'Child', 202),
    (21, 'Kirsten', 'Baer', 'Child', 204),
    (22, 'Elvis', 'Khoo', 'Child', 115),
    (23, 'Sandra', 'Baida', 'Child', 116),
    (24, 'Cameron', 'Tobias', 'Child', 117),
    (25, 'Kevin', 'Himuro', 'Child', 118),
    (26, 'Rip', 'Colmenares', 'Child', 119),
    (27, 'Julia', 'Raphaely', 'Child', 114),
    (28, 'Woody', 'Russell', 'Child', 145),
    (29, 'Alec', 'Partners', 'Child', 146),
    (30, 'Sandra', 'Taylor', 'Child', 176)
]

# Insert data into the dependents table
cursor.executemany('INSERT INTO dependents (dependent_id, first_name, last_name, relationship, employee_id) VALUES (?, ?, ?, ?, ?)', dependents_data)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully into the dependents table!")
