import sqlite3

SELECT SUM(character_id)
FROM charactercreator_character 

SELECT SUM(item_id)
FROM armory_item armory_item

SELECT SUM(item_ptr_id)
FROM armory_weapon aw

SELECT * FROM charactercreator_character_inventory 
LIMIT 20;

SELECT AVG(item_id)
FROM charactercreator_character_inventory cci