# SQL Murder Mystery
## Disclaimer
This SQL tutorial is based on content from the NUKnightLab GitHub repository [sql-mysteries](https://github.com/NUKnightLab/sql-mysteries). It has been forked and adapted for a browser-based version of SQLite. All original rights remain with NUKnightLab, and State Library Victoria (SLV) does not claim ownership of the original content.

## Introduction
> ***Note:*** _This can be a pair programming activity or done independently._

#### Use SQL to Solve a Murder Mystery!
There's been a Murder in SQL City! The SQL Murder Mystery is designed to be both a self-directed lesson to learn SQL concepts and commands and a fun game for experienced SQL users to solve an intriguing crime.

Please feel free to consult a [SQL Tutorial](https://www.w3schools.com/sql/) or [GenAI](https://chatgpt.com/) to assist your efforts.

## Exercise
#### Requirements & Setup
Navigate to this URL in your preferred web browser:
https://sqliteonline.com/#urldb=https://raw.githubusercontent.com/StateLibraryVictoria/code-club/main/session-resources/sql-murder-mystery/sql-murder-mystery.db

If the above URL didn't work, please follow these steps:
1. Download the sqlite database file and save to your local machine: [sql-murder-mystery.db](sql-murder-mystery.db)
2. Navigate to [https://sqliteonline.com/](https://sqliteonline.com/) . This site will be used as a free online SQLite database environment. No account/signup is necessary.
3. Load the SQLite database by clicking on `File` --> `Open DB` and selecting the `sql-murder-mystery.db` file
4. Confirm that you can see nine table objects on the left hand pane.
5. Use the clues and Entity Relationship Diagram (ERD) below to solve the case!

#### Entity Relationship Diagram
Please refer to the ERD diagram below for table relationships.
![Entity Relationship Diagram](sql-murder-mystery-erd.png "Entity Relationship Diagram")


#### Initial Clue
A crime has taken place and the detective needs your help. The detective gave you the
crime scene report, but you somehow lost it. You vaguely remember that the crime
was a **murder​** that occurred sometime on **January 15, 2018** and that it took place in **SQL City​**.
All the clues to this mystery are buried in a huge database, and you need to use
SQL to navigate through this vast network of information. Your first step to solving the
mystery is to retrieve the corresponding **crime scene report** from the police
department’s database. From there, you can use your SQL skills to find the murderer.


#### Getting Started
* **For SQL beginners**: Refer to the initial clue above, and use the hints below.

* **For experienced SQL users**: The initial clue and ERD is all you need! Try not to refer to the walkthrough.


## Hints
<details>
<summary>Hint 1: Query the crime_scene_report table.</summary>

Filter by using a <b>WHERE</b> clause on the <i>date</i>, <i>city</i>, and <i>type</i> columns.
<br />
<br />

<details>
<summary>Hint 2: Query the person table to identify the names of the two witnesses.</summary>

Use <b>ORDER BY address_number DESC</b> to sort in descending order. <b>LIMIT</b> can be used to only return the desired number of rows (e.g. LIMIT 1).
Use <b>LIKE</b> for pattern matching.
<br />
<br />

<details>
<summary>Hint 3: Query the interview table to read the transcripts of the witnesses.</summary>

Morty Schapiro (14887) & Annabel Miller (16371).
Use <b>WHERE person_id IN (14887,16371)</b> to filter for the two witnesses.
<br />
<br />

<details>

<summary>Hint 4: Witness Clues.</summary>

<i>I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started with "48Z". Only gold members have those bags. The man got into a car with a plate that included "H42W".</i>

<i>I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.</i>

Inspect the following tables given the above clues: <b>get_fit_now_member</b>, <b>drivers_license</b>, <b>get_fit_now_check_in</b>
<br />
<br />

<details>

<summary>Final Hint: Use an INNER JOIN to join the tables together based on the related/matching columns.</summary>

Tables: <b>person</b>, <b>drivers_license</b>, <b>get_fit_now_member</b>, <b>get_fit_now_check_in</b>

WHERE get_fit_now_member.id LIKE '48Z%'
AND drivers_license.plate_number LIKE '%H42W%'
AND get_fit_now_check_in.check_in_date = 20180109;

You should have the answer now!
</details>
</details>
</details>
</details>
</details>


## Checking the Solution
Run the following in your SQL environment to check whether you've found the right murderer:

```sql
INSERT INTO solution VALUES (1, 'Insert the name of the person you found here');

SELECT value FROM solution;
```


## Solution Walkthrough
<details>
<summary>Click here to see the full walkthrough!</summary>
  
```sql
-- 1. Querying the crime_scene_report table
SELECT description 
FROM crime_scene_report
WHERE date = 20180115 
AND city = 'SQL City' 
AND type = 'murder';

-- Security footage shows that there were 2 witnesses.
-- The first witness lives at the last house on "Northwestern Dr".
SELECT * 
FROM person 
WHERE address_street_name = 'Northwestern Dr' 
ORDER BY address_number desc
LIMIT 1;

-- The second witness, named Annabel, lives somewhere on "Franklin Ave".
SELECT * 
FROM person
WHERE name LIKE 'Annabel%' 
AND address_street_name = 'Franklin Ave';

--  Query the interview table to read the transcript of the witnesses.
-- 14887 : Morty Schapiro
-- 16371 : Annabel Miller
SELECT transcript 
FROM interview 
WHERE person_id IN (14887,16371);

-- I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started
-- with "48Z". Only gold members have those bags. The man got into a car with a plate that included "H42W".
SELECT * 
FROM get_fit_now_member 
WHERE id LIKE '48Z%'
AND membership_status = 'gold';

SELECT * 
FROM drivers_license 
WHERE plate_number LIKE '%H42W%';

-- I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.
SELECT * 
FROM get_fit_now_check_in 
WHERE check_in_date = 20180109;

-- Use an INNER JOIN to join the tables together based on the related/matching columns.
SELECT person.name
FROM person
INNER JOIN drivers_license 
 ON person.license_id = drivers_license.id
INNER JOIN get_fit_now_member 
 ON person.id = get_fit_now_member.person_id
INNER JOIN get_fit_now_check_in 
 ON get_fit_now_member.id = get_fit_now_check_in.membership_id
WHERE get_fit_now_member.id LIKE '48Z%'
AND drivers_license.plate_number LIKE '%H42W%'
AND get_fit_now_check_in.check_in_date = 20180109;

-- Jeremy Bowers
INSERT INTO solution VALUES (1, 'Jeremy Bowers');
SELECT value FROM solution;

-- Congrats, you found the murderer! But wait, theres more... If you think you are re up for a challenge,
-- try querying the interview transcript of the murderer to find the real villain behind this crime.
-- If you feel especially confident in your SQL skills, try to complete this final step with
-- no more than 2 queries. Use this same INSERT statement with your new suspect to check your answer.

-- Check Jeremy Bowers' interview transcript (person_id = 67318)
SELECT transcript 
FROM interview 
WHERE person_id = 67318;

-- I was hired by a woman with a lot of money. I don't know her name but I know she's around
-- 5'5" (65") or 5'7" (67"). She has red hair AND she drives a Tesla Model S. I know that she
--  attended the SQL Symphony Concert 3 times in December 2017.

-- Use an INNER JOIN to join the tables together based on the related/matching columns.

SELECT person.name
FROM person
INNER JOIN drivers_license 
 ON person.license_id = drivers_license.id
INNER JOIN facebook_event_checkin
 ON person.id = facebook_event_checkin.person_id 
WHERE drivers_license.car_make = 'Tesla'
AND drivers_license.car_model = 'Model S'
AND drivers_license.hair_color = 'red'
AND drivers_license.height between 65 AND 67
AND drivers_license.gender = 'female'
AND facebook_event_checkin.event_name = 'SQL Symphony Concert'
AND facebook_event_checkin.date LIKE '201712%'
GROUP BY person.name
HAVING COUNT(person.name) =3;

-- Miranda Priestly
INSERT INTO solution VALUES (1, 'Miranda Priestly');
SELECT value FROM solution;

-- Congrats, you found the brains behind the murder! Everyone in SQL City hails you as the greatest
-- SQL detective of all time. Time to break out the champagne!

```
 </details>



## Additional Resources
- [W3 Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [Codecademy SQL Reference](https://www.codecademy.com/article/sql-commands)
