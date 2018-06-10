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
})

// Display the submitted form
// app.post("/result", function (request, response) {
//     // console.log("hit result route")
//     response.render("result", { name: request.body.name, location: request.body.location, language: request.body.language, comment: request.body.comment });
// })

var server = app.listen(8000, function() {
    console.log("listening on port 8000")
})

var io = require("socket.io").listen(server);

io.sockets.on('connection', function (socket) {
    console.log("Client/socket is connected!");
    console.log("Client/socket id is: ", socket.id);

    socket.on("posting_form", function (data) {
        var random_number = Math.floor((Math.random() * 1000) + 1);
        socket.emit("updated_message", {response: data});
        socket.emit("random_number", {response: random_number});
    })
})