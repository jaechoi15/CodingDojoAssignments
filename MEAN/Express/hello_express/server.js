// Load the express module
var express = require("express");

// require body-parser
var bodyParser = require('body-parser');

var session = require('express-session');

// invoke var express and store the resulting application in var app to create the server itself
var app = express();

// lets handle the base route "/" and respond with "Hello Express"
app.get('/', function(request, response) {
    response.render("index", {title: "my Express project"});
})

// this is the line that tells our server to use the "/static" folder for static content
app.use(express.static(__dirname + "/static"));

app.use(bodyParser.urlencoded({extended: true}));

app.use(session({secret: "codingdojorocks"}));

// This sets the location where express will look for the ejs views
app.set('views', __dirname + '/views');

// Now lets set the view engine itself so that express knows that we are using ejs
app.set('view engine', 'ejs');

// app.get("/users", function (request, response) {
//     var users_array = [
//         {name: "Michael", email: "michael@codingdojo.com"}, 
//         {name: "Jay", email: "jay@codingdojo.com"}, 
//         {name: "Brendan", email: "brendan@codingdojo.com"}, 
//         {name: "Andrew", email: "andrew@codingdojo.com"}
//     ];
//     response.render("users", {users: users_array});
// })

// app.get("/index", function (request, response) {
//     response.render("index");
// })

app.post("/users", function (request, response) {
    console.log("POST DATA \n\n", request.body)
    request.session.name = request.body.name;
    console.log("request session: " + request.session.name);
    response.redirect("/")
});

app.get("/users/:id", function (request, response) {
    console.log("The user id requested is:", request.params.id);
    response.send("You requested the user with id: " + request.params.id);
})

// Tell the express app to listen on port 8000
// this line will almost always be at the end of your server.js file
app.listen(8000, function() {
    console.log("listening on port 8000")
})