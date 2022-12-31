create DOMAIN global_loc VARCHAR(15) not NULL

CREATE TABLE game_status
(
    id           SERIAL PRIMARY KEY,
    world_height smallint,
    world_width  smallint,
    user_loc     global_loc,
    dragon_loc   global_loc,
    dungeon_loc  global_loc,
    reward_level smallint,
    difficulty   global_loc,
    last_save    TIMESTAMP
);