-- Keep a log of any SQL queries you execute as you solve the mystery.
-- In order to research the crime scene, we open the table
.schema crime_scene_reports

-- And retrieve the items on it
.schema crime_scene_reports
SELECT * FROM crime_scene_reports;

-- As the list is massive, we narrow it to the ones with "duck"
SELECT * FROM crime_scene_reports WHERE description LIKE "%duck%";

-- We know that the theft occured in the Humphrey Street bakery at 10:15am on 28/7/2021, 3 witnesses mention the bakery
-- Let's dedlve into the interviews table
-- ### Interviews
-- Ruth: Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot, you might want to look for cars that left the parking

-- Eugene: I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at
-- Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money

-- Raymond: As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
-- The thief then asked the person on the other end of the phone to purchase the flight ticket
.schema interviews
SELECT * FROM interviews WHERE transcript LIKE "%bakery%";

-- One of the people interviewed mentioned that they saw the thief asking for the first flight on the next day
-- So we query the flights for the 29/7/2021
.schema flights
SELECT * FROM flights WHERE day == 29 ORDER BY hour, minute;

-- The first flight on the morning on the 29th is at 8am, let's see where it's headed to (flight: 36, airport destination: 4)
.schema airports
SELECT full_name, city FROM airports WHERE id = 4;

-- We know now that the city of destination is [New York City]

-- Let's get information from the first interview, via bakery secury logs [1]
SELECT name FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25
AND activity = "exit";
-- Suspects: Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, Kelsey

-- Let's observe who was withdrawing money on the correct time and place [2]
SELECT DISTINCT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_location = "Leggett Street" AND transaction_type = "withdraw" AND month = 7 AND day = 28;
-- Suspects: Luca, Kenny, Taylow, Bruce, Brooke, Iman, Benista, Diana

-- Let's extract the passenger list from the first question, we already know the flight number [3]
SELECT name FROM people
JOIN  passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = 36;
-- Suspects: Doris, Sofia, Bruce, Edward, Kelsey, Taylor, Kenny, Luca

-- Checking the phone logs
.schema phone_calls
SELECT DISTINCT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE month = 7 AND day = 28 ANd duration < 60;
-- Suspects: Sofia, Kelsey, Bruce, Taylor, Diana, Carina, Kenny, Benista

-- The only common suspect is [Bruce]
-- In order to find the accomplice, we register Bruce's phone call
SELECT DISTINCT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE month = 7 AND day = 28 ANd duration < 60 AND caller = "(367) 555-5533";
-- The suspect is [Robin]
