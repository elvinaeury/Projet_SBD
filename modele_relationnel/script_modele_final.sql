CREATE TABLE "accidents_events" (
  "id_event" serial PRIMARY KEY,
  "week_day" varchar,
  "date" timestamp,
  "type_event" varchar(2),
  "phase" varchar,
  "location" varchar,
  "country" varchar,
  "total_occupants" integer,
  "total_fatalities" integer,
  "aircraft_damage" varchar,
  "aircraft_fate" varchar
);

CREATE TABLE "aircrafts" (
  "id_aircraft" serial PRIMARY KEY,
  "type_aircraft" varchar,
  "year_built" integer,
  "number_engines" integer,
  "type_engines" varchar,
  "first_flight" integer,
  "cycles" integer,
  "total_airframe_hours" integer,
  "registration" varchar,
  "c_n_msn" varchar
);

CREATE TABLE "flight_info" (
  "id_flight" serial PRIMARY KEY,
  "operator" varchar,
  "nature" varchar,
  "flight_number" integer,
  "crew_number" integer,
  "passengers_number" integer
);

CREATE TABLE "fatalities_reports" (
  "id_report" serial PRIMARY KEY,
  "crew_fatalities" integer,
  "passengers_fatalities" integer,
  "collision_casualties" integer,
  "ground_casualties" integer,
  "status" varchar
);

CREATE TABLE "airports" (
  "code_icao" varchar(4) PRIMARY KEY,
  "code_iata" varchar(3),
  "name" varchar,
  "city" varchar,
  "country" varchar,
  "latitude" float,
  "longitude" float,
  "altitude" float
);

CREATE TABLE "departure_airport" (
  "flight" serial,
  "icao" varchar(4),
  PRIMARY KEY ("flight", "icao")
);

CREATE TABLE "destination_airport" (
  "flight" serial,
  "icao" varchar(4),
  PRIMARY KEY ("flight", "icao")
);

ALTER TABLE "aircrafts" ADD FOREIGN KEY ("id_aircraft") REFERENCES "accidents_events" ("id_event");

ALTER TABLE "flight_info" ADD FOREIGN KEY ("id_flight") REFERENCES "accidents_events" ("id_event");

ALTER TABLE "fatalities_reports" ADD FOREIGN KEY ("id_report") REFERENCES "accidents_events" ("id_event");

ALTER TABLE "departure_airport" ADD FOREIGN KEY ("icao") REFERENCES "airports" ("code_icao");

ALTER TABLE "destination_airport" ADD FOREIGN KEY ("icao") REFERENCES "airports" ("code_icao");

ALTER TABLE "destination_airport" ADD FOREIGN KEY ("flight") REFERENCES "flight_info" ("id_flight");

ALTER TABLE "departure_airport" ADD FOREIGN KEY ("flight") REFERENCES "flight_info" ("id_flight");

