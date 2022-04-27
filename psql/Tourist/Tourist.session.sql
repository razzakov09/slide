-- #1
-- SELECT * FROM inner_flights;

-- #2
-- SELECT * FROM inner_flights WHERE id > 10;

-- #3
-- SELECT * FROM inner_flights 
-- WHERE to_destination in ('Ош', 'Бишкек');

-- #4
-- SELECT * FROM inner_flights
-- WHERE quantity > 150;

-- #5
-- SELECT company FROM outter_flights
-- WHERE flight_type = 'Пассажирский';

-- #6
-- SELECT * FROM outter_flights
-- WHERE id < 7;

-- #7
-- SELECT * FROM outter_flights
-- WHERE flight_type = 'Грузовой';

-- #8
-- SELECT * FROM outter_flights
-- WHERE neighbors > 3;

-- #9
-- SELECT * FROM outter_flights
-- WHERE neighbors < 3 AND flight_type = 'Пассажирский';

-- #10
-- SELECT company, to_country FROM outter_flights; 