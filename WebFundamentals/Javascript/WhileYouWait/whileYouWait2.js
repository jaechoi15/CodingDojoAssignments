for (var daysUntilMyBirthday = 60; daysUntilMyBirthday > -1; daysUntilMyBirthday -= 1)
{
    if (daysUntilMyBirthday > 29) {
        message = daysUntilMyBirthday + " days until my birthday. Such a long time..."
        console.log(message);
    }
    else if (daysUntilMyBirthday < 30 && daysUntilMyBirthday > 5) {
        message = daysUntilMyBirthday + " days until my birthday. Getting closer."
        console.log(message);
    }
    else if (daysUntilMyBirthday < 6 && daysUntilMyBirthday > 0) {
        message = daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY!!!"
        console.log(message);
    }
    else {
        message = "♪ღ♪HAPPY BIRTHDAY♪ღ♪"
        console.log(message)
    }
}

