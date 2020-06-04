BEGIN;
--
-- Create model User
--
CREATE TABLE "activities_user" ("id" varchar(9) NOT NULL PRIMARY KEY, "real_name" varchar(200) NOT NULL, "tz" varchar(200) NOT NULL);
--
-- Create model ActivityPeriod
--
CREATE TABLE "activities_activityperiod" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "start_time" datetime NOT NULL, "end_time" datetime NOT NULL, "user_id" varchar(9) NOT NULL REFERENCES "activities_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "activities_activityperiod_user_id_41ad1f70" ON "activities_activityperiod" ("user_id");
COMMIT;