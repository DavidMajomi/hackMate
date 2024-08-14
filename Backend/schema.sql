drop TABLE if EXISTS posts;
    CREATE TABLE posts (
        id integer primary key autoincrement,
        author text not null,
        content text not null,
        postdate text not null
    );


drop TABLE if EXISTS users;
    CREATE TABLE users (
        username text primary key,
        displayname text not null,
        bio text,
        dateofcreation text not null
    );