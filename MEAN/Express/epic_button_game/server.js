var express = require("express");
var bodyParser = require("body-parser");
var session = require("express-session");
var path = require("path");
var app = express();

app.set("views", __dirname + "/views");
app.set("view engine", "ejs");

app.use(express.static(__dirname + "/static"));
app.use(bodyParser.urlencoded({extended: true}));
app.use(session({secret: "codingdojorocks"}));

// Render the index page
app.get("/", function (request, response) {
    // console.log("hit index route")
    response.render("index");
});

var server = app.listen(8000, function() {
    console.log("listening on port 8000")
});

var io = require("socket.io").listen(server);

io.sockets.on('connection', function (socket) {
    console.log("Client/socket is connected!");
    console.log("Client/socket id is: ", socket.id);

    var count;
    
    socket.on("button", function (data) {
        console.log("button clicked. increase count")
        if (count == undefined) {
            count = 0;
        };
        count++;
        socket.emit("main-message", {response: count});
    });

    socket.on("reset", function(data) {
        console.log("reset count");
        count = 1;
        socket.emit("main-message", {response: count});
    })
});