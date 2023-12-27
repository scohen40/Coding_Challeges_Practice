"""
Problem 3: Six Degrees of Kevin Bacon

There's a game, called Six Degrees of Kevin Bacon. It goes like this: Pick any actor, and you can find within 6 degrees of separation, a movie featuring Kevin Bacon.
In order to solve it with an algorithm, we'll need to use either Breadth First Search or Depth First Search.

Oh by the way you already learned to use graphs in the first question, surprise! They're not as scary as they seem. It's just the idea that "things have relationships".
When you added every cast to it's movie, and every movie to it's cast, you created what's called an edge list.
An edge list is a fancy graph-search term meaning "a list of the relationships between every thing and every other thing indexed by the name of the thing". Every relationship table in SQL is an edge list. Sometimes it looks like this:

edge_list = {
    1: [2,3],
    2: [1,3],
    3: [1,2]
}
This would represent some graph where everything in the graph has a relationship with every other thing- 1 has a relationship with 2 and 3, and 2 and 3 have relationships with each other. Here's another, where that isn't the case:

edge_list = {
    1: [2,3,4],
    2: [1,3],
    3: [1,2],
    4: [1]
}
4 only has a relationship with 1, and vice versa, so 2 and 3 "don't know" 4.

In the Six Degrees of Kevin Bacon game, the numbers can represent the IDs of actors that shared a movie with each other. In this case, 4 has only been in a movie with 1, while 2 and 3 haven't. If 3 represents Kevin Bacon, the path from 4 to 3 is 4 -> 1 -> 3.

The Prompt Itself
Write a function building off of the indexes you made above that will take any cast or crew member and output a path to Kevin Bacon, like so:

Stan Lee -> Stephen Norrington -> Paul Curtis -> John C. Stuver -> Guy Adan -> Larry Wallace -> Alex Cameron -> Kevin Bacon
Note: Due to not every movie being in the dataset, the actual kevin bacon number is usually higher than 6
"""


