var daysUntilMyBirthday = 29;

if (daysUntilMyBirthday <= 5 && daysUntilMyBirthday > 0){
        console.log(daysUntilMyBirthday + " days until my birthday!!!");
}
else if (daysUntilMyBirthday > 30){
        console.log(daysUntilMyBirthday + " days until my birthday. Such a long time...");
}
else if (daysUntilMyBirthday < 30 && daysUntilMyBirthday > 0){
        console.log(daysUntilMyBirthday + " days until my birthday. Almost there!");
}
else {
        console.log("HAPPY BIRTHDAY!!!");
}