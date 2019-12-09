SELECT COUNT(*)
FROM "buddymove_holidayiq.sqlite3" bhs

SELECT COUNT("User Id")
FROM "buddymove_holidayiq.sqlite3" bhs
WHERE "User Id" IN (Nature, Shopping)
/* got that one wrong */