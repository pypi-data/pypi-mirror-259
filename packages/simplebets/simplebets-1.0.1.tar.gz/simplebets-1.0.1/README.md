# Some information

SimpleBets is a library that provides a framework for calculating the odds of a given event based on historical performance

Example 1: 
i want to know the odds Stephen Curry scores 30 points in the next game, 
SimpleBets allows you to make a request and get those odds 

Example 2: 
I want to know the odds GSW wins against Team x,
Again SimpleBets allows this

# The mechanics
The mechanics of a Head to Head Odds Calculation
SimpleBets is effectively a player ranking system
It takes historical performance, and updates a players ranking according to their contribution (weighting) to their teams outcome for a game.
Explicitly, 
if Stephen Curry Performs well (scores x points, gets y rebounds, etc..) and his team wins, his ranking is updated accordingly

Ranking players like this may allow us to imply the team performance based on the players in the team

# GameTeamMetrics
There may be intangibles at the team level that this type of ranking system may miss:
1. Home team advantage
2. Who is the Coach
3. What context is the game being played in (high pressure, low pressure, etc..)
4. 

This may effect head to head type betting

So team level betting may need more information than player ranking system alone can provide,
It may be worth calculating co-efficients for home team advantage
It may be worth assigning context
It may be worth weighting according to a coaches win-lose record

The mechanics of a individual metric Odds Calculation
The mechanics for calculating an individuals likelihood to achieve a particular key metric is based on a probability distribution for that player and that metric.
Ie, If you want to make bets on Stephen Curry scoring 30 or more in the next game, we need to have collected data related to his previous games and built a distribution from it then stored the distribution. 
After that, calculating the odds is simple.

So, There are two types of streams for the engine (at time of writing), 
1. Takes individuals game play, extracts key metrics and build distributions 
2. Takes individuals game play, calculates how their play contributed to their teams outcome, and assigns them a ranking. This combined with GameTeamMetrics may be a good indication for who will win a game given a list of player inclusions.

In both the above cases, we need data.
We need historical data related to game outcomes, and player performances. All the metrics we think should matter:
1. Player:team, gameoutcome, minutes, points, rebounds, etc
2. Away and Home team, Game Context

The engine should be compared with another SportsBetting operator to validate performance

# Plan to test
1. Get Simple Bets Recent (as up to date as possible) NBA data -> test data ✅
2. Get Distributions for Key Metrics for time period -> ✅
3. Get Player Rankings ✅, Get Team co-efficients -> ✅

Head to Head testing
The test only ever needs to predict the "next" game, it is assumed the data will be up to date when live
1. Based on the team, what is the likelihood team x beats team y -> based on player inclusions, whats team ranking, 
2. Does that team ranking provide insight into team v team likelohood -> Check how team rankings predict outcomes
3. How often does team ranking predict the winner? 
2. What price should we offer on that likelihood? 
3. How profitable are we likely to be if we offer those price? 


Individual Metric Testing:
This type of testing should answer these types of questions:
1. What is the likelihood x player achieves y metric? -> Calculate dist
2. What price should we offer on that likelihood? -> 1 / odds + profit margin
3. How profitable are we likely to be if we offer those prices? -> monte carlo


Same Game multi testing:
Same game multi testing




