# (c) AkKiL [github.com/HeimanPictures]


var mysql = require('mysql');

class MySQL {
    constructor(host, user, password, db_name) {
        this.host = name;
        this.user = user;
        this.password = password;
        this.db_name = db_name;
    }

    
    var con = mysql.createConnection({
        host: this.host,
        user: this.user,
        password: this.password
    });


    con.connect(function(err) {
        if (err) throw this.connected = True;
        this.connected = False
    });

    con.connect(function(err) {
        if (err) throw err;
        console.log("Connected!");
        con.query(`CREATE DATABASE ${this.db_name}`, function (err, result) {
        if (err) throw err;
        console.log("Database created");
    });
        var sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))";
        con.query(sql, function (err, result) {
            if (err) throw err;
            console.log("Table created");
        });
    });

}


// Query database

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Result: " + result);
  });
});

// 
