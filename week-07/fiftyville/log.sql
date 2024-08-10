-- Keep a log of any SQL queries you execute as you solve the mystery.

-- SELECT description
-- FROM crime_scene_reports
-- WHERE year = 2023 AND month = 7 AND day = 28 AND description LIKE "%duck%";

-- -- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
-- -- * Pista: três testemunhas entrevistadas mencionam the bakery.

-- SELECT transcript FROM interviews
-- WHERE transcript LIKE '%bakery%';

-- | >>> Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot <<< and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
-- | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the >>> ATM on Leggett Street and saw the thief there withdrawing some money. <<<                                                                                                 |
-- | As the thief was leaving the bakery, >>> they called someone who talked to them for less than a minute. <<< In the call, I heard the thief say that they were planning to take >>> the earliest flight out of Fiftyville tomorrow <<<. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

-- SELECT license_plate, activity, hour, minute FROM bakery_security_logs
-- WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25) AND activity = 'exit';

-- *** Selecionar placas do veiculos
-- | license_plate | activity | hour | minute |
-- +---------------+----------+------+--------+
-- | 5P2BI95       | exit     | 10   | 16     |
-- | 94KL13X       | exit     | 10   | 18     |
-- | 6P58WS2       | exit     | 10   | 18     |
-- | 4328GD8       | exit     | 10   | 19     |
-- | G412CB7       | exit     | 10   | 20     |
-- | L93JTIZ       | exit     | 10   | 21     |
-- | 322W7JE       | exit     | 10   | 23     |
-- | 0NTHK55       | exit     | 10   | 23     |

-- *** Selecionar pessoas donas dos carros
-- SELECT id, name FROM people
-- WHERE license_plate IN (
--     SELECT license_plate FROM bakery_security_logs
--     WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25) AND activity = 'exit'
-- );
-- -- |   id   |  name   |
-- -- +--------+---------+
-- -- | 221103 | Vanessa |
-- -- | 243696 | Barry   |
-- -- | 396669 | Iman    |
-- -- | 398010 | Sofia   |
-- -- | 467400 | Luca    |
-- -- | 514354 | Diana   |
-- -- | 560886 | Kelsey  |
-- -- | 686048 | Bruce   |

-- SELECT account_number FROM atm_transactions
-- WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

-- *** Selecionar contas relacionadas ao uso do ATM
-- -- | account_number |
-- -- +----------------+
-- -- | 28500762       |
-- -- | 28296815       |
-- -- | 76054385       |
-- -- | 49610011       |
-- -- | 16153065       |
-- -- | 25506511       |
-- -- | 81061156       |
-- -- | 26013199       |

-- *** Selecionar IDs das contas
-- SELECT person_id FROM bank_accounts
-- WHERE account_number IN (
--     SELECT account_number FROM atm_transactions
--     WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
-- );

-- | person_id |
-- +-----------+
-- | 686048    |
-- | 514354    |
-- | 458378    |
-- | 395717    |
-- | 396669    |
-- | 467400    |
-- | 449774    |
-- | 438727    |

-- *** Selecionar as ligacoes
-- SELECT caller, receiver FROM phone_calls
-- WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60;

-- ** Selecionar quem efetuou a ligacao
-- SELECT id, name FROM people
-- WHERE phone_number IN (
--     SELECT caller FROM phone_calls
--     WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60
--     );

-- -- |   id   |  name   |
-- -- +--------+---------+
-- -- | 395717 | Kenny   |
-- -- | 398010 | Sofia   |
-- -- | 438727 | Benista |
-- -- | 449774 | Taylor  |
-- -- | 514354 | Diana   |
-- -- | 560886 | Kelsey  |
-- -- | 686048 | Bruce   |
-- -- | 907148 | Carina  |

-- *** Selecionar quem recebeu a ligacao
-- SELECT id, name FROM people
-- WHERE phone_number IN (
--     SELECT receiver FROM phone_calls
--     WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60
--     );

-- *** Selecionar o passaporte do caller
-- SELECT passport_number FROM people
-- WHERE phone_number IN (
--     SELECT caller FROM phone_calls
--     WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60
-- );

-- *** Selecionar ID do aeroporto de Fiftyville
-- SELECT id FROM airports
-- WHERE city = 'Fiftyville';

-- *** Selecionar o voo saindo de Fiftyville na data
-- SELECT id, destination_airport_id, hour, minute FROM flights
-- WHERE year = 2023 AND month = 7 AND day = 29
-- AND origin_airport_id = (
--     SELECT id FROM airports
--     WHERE city = 'Fiftyville')
-- ORDER BY hour ASC
-- LIMIT 1;

-- *** Selecionar passaporte dos passageiros do voo
-- SELECT passport_number FROM passengers
-- WHERE flight_id = (
--     SELECT id FROM flights
--     WHERE year = 2023 AND month = 7 AND day = 29
--     AND origin_airport_id = (
--         SELECT id FROM airports
--         WHERE city = 'Fiftyville')
--     ORDER BY hour ASC
--     LIMIT 1
-- );

-- Do LADRAO:
    -- placa
    -- conta
    -- caller

-- Do CUMPLICE

-- SELECT flight_id FROM passengers
-- WHERE passport_number = (
--     SELECT passport_number FROM people
--     WHERE id = (
--         SELECT id FROM people
--         WHERE license_plate IN (
--             SELECT license_plate FROM bakery_security_logs
--             WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25) AND activity = 'exit'
--             )
--     )
-- );

-- selecionar o id voo que tem passageiro com passaporte da pessoa dona da placa


-- SELECT full_name FROM airports
-- WHERE id = (
--     SELECT destination_airport_id FROM flights
--     WHERE id = (
--         SELECT flight_id FROM passengers
--         WHERE passport_number = (
--             SELECT passport_number FROM people
--             WHERE id = (
--                 SELECT id FROM people
--                 WHERE license_plate = (
--                     SELECT license_plate FROM bakery_security_logs
--                     WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25) AND activity = 'exit'
--                 )
--             )
--         )
--     )
-- );

--------------------------------------------------------------------

-- -- ! ! ! ! ! ! What city the thief escaped to: LaGuardia Airport
-- SELECT full_name FROM airports
-- WHERE id = (
--     SELECT destination_airport_id FROM flights
--     WHERE year = 2023 AND month = 7 AND day = 29
--     AND origin_airport_id = (
--         SELECT id FROM airports
--         WHERE city = 'Fiftyville')
--     ORDER BY hour ASC
--     LIMIT 1
-- );

--------------------------------------------------------------------

-- -- ! ! ! ! ! ! The THIEF is : Bruce
-- SELECT name FROM people
-- WHERE license_plate IN (
--     SELECT license_plate FROM bakery_security_logs
--     WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25) AND activity = 'exit'
-- )
-- AND id IN (
--     SELECT person_id FROM bank_accounts
--     WHERE account_number IN (
--         SELECT account_number FROM atm_transactions
--         WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
--     )
-- )
-- AND id IN (
--     SELECT id FROM people
--         WHERE phone_number IN (
--             SELECT caller FROM phone_calls
--             WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60
--         )
-- )
-- AND passport_number IN (
--     SELECT passport_number FROM passengers
--     WHERE flight_id = (
--         SELECT id FROM flights
--         WHERE year = 2023 AND month = 7 AND day = 29
--         AND origin_airport_id = (
--             SELECT id FROM airports
--             WHERE city = 'Fiftyville')
--         ORDER BY hour ASC
--         LIMIT 1
--     )
-- );
--------------------------------------------------------------------

-- -- ! ! ! ! ! ! The ACCOMPLICE is

SELECT name FROM people
WHERE phone_number = (
    SELECT receiver FROM phone_calls
    WHERE caller = (
        SELECT phone_number FROM people
        WHERE license_plate IN (
            SELECT license_plate FROM bakery_security_logs
            WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND (minute >= 15 AND minute <= 25) AND activity = 'exit'
            )
    AND id IN (
        SELECT person_id FROM bank_accounts
        WHERE account_number IN (
            SELECT account_number FROM atm_transactions
            WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
            )
        )
    AND id IN (
        SELECT id FROM people
        WHERE phone_number IN (
            SELECT caller FROM phone_calls
            WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60
        )
    )
    AND passport_number IN (
        SELECT passport_number FROM passengers
        WHERE flight_id = (
            SELECT id FROM flights
            WHERE year = 2023 AND month = 7 AND day = 29
        AND origin_airport_id = (
            SELECT id FROM airports
            WHERE city = 'Fiftyville')
        ORDER BY hour ASC
        LIMIT 1
        )
    )
)
AND day = 28 AND duration < 60
);

