var express = require("express");
var bodyParser = require("body-parser");
var session = require("express-session");
var app = express();

app.set("views", __dirname + "/views");
app.set("view engine", "ejs");

app.use(express.static(__dirname + "/static"));
app.use(bodyParser.urlencoded({extended: true}));
app.use(session({secret: "codingdojorocks"}));

// Increment counter by 1
app.get("/", function (request, response) {
    if (!request.session.counter) {
        request.session.counter = 1;
    } else {
        request.session.counter++;
    }
    response.render("index", { counter: request.session.counter});
})

// Increment counter by 2
app.post("/addTwo", function (request, response) {
    if (!request.session.counter) {
        request.session.counter = 1;
    } else {
        request.session.counter++;
    }
    response.redirect("/");
})

// Reset the counter back to 1
app.post("/reset", function (request, response) {
    request.session.destroy();
    response.redirect("/");
})

app.listen(8000, function() {
    console.log("listening on port 8000")
})