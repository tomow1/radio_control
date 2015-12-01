drop table if exists stations;
create table stations (
  id integer primary key autoincrement,
  display_name text not null,
  name text not null
);
