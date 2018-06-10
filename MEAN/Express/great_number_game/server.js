var express = require("express");
var bodyParser = require("body-parser");
var session = require("express-session");
var app = express();

app.set("views", __dirname + "/views");
app.set("view engine", "ejs");

app.use(express.static(__dirname + "/static"));
app.use(bodyParser.urlencoded({extended: true}));
app.use(session({secret: "codingdojorocks"}));

// Render the index page
app.get("/", function (request, response) {
    console.log("hit index route");

    // If session does not exist, then generate the random number
    if (!request.session.number) {
        request.session.number = Math.floor(Math.random() * 101);
        request.session.guess = 0;
        request.session.result = "";
        console.log(request.session.number);
    } else {
        console.log(request.session.number);
    }
    response.render("index", { result: request.session.result });
})

app.post("/process", function (request, response) {
    console.log("hit process route");

    // If the user's guess is less than the random number, then display a message.
    if (request.body.guess < request.session.number) {
        console.log(`You guessed ${request.body.guess}. Too low!`);
        request.session.result = "Too low!";

    // If the user's guess is greater than the random number, then display a message.
    } else if (request.body.guess > request.session.number) {
        console.log(`You guessed ${request.body.guess}. Too high!`);
        request.session.result = "Too high!";

    // If the user's guess matches the random number, then display a message.
    } else {
        console.log(`You guessed ${request.body.guess}. Correct!`);
        request.session.result = "Correct!";
    }
    response.redirect("/");
})

// Reset the session and redirect to the index route
app.get("/reset", function (request, response) {
    request.session.destroy();
    response.redirect("/");
})

app.listen(8000, function() {
    console.log("listening on port 8000")
})