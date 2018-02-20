use twitter;

select tweets.tweet as kobe_tweets
from users
left join tweets on users.id = tweets.user_id
where users.id = 1;

select first_name, tweet
from users
left join faves on users.id = faves.user_id
left join tweets on faves.tweet_id = tweets.id
where users.id = 2 or users.id = 1;

select users.first_name as followed, users2.first_name as follower
from users
left join follows on users.id = follows.followed_id
left join users as users2 on users2.id = follows.follower_id
where users.id = 1;