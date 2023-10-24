"""
Problem 1: Read and parse a large CSV
Below is example code that will print the first ten lines of the movies_metadata.csv file.
Write a loop to read the entire movies_metadata.csv file and create a dictionary that indexes each movie by ID.

Next, read in the entire credits.csv file

The third field in the CSV, 'id', is the ID of the movie they're in, so it will match your movies_index
As you create a credits index, also attach each cast & crew member to it's movie, by adding it to the "credits" array from the movie dict within the movie index. Each credit has a field, "id", which is unique to the actor or crewmember- that way if you encounter a sound engineer named "Tom Hanks", you can distinguish between them.
"""






"""
Problem 2: Find All Sci-Fi actors
Now that we know which Actors and Crew (all credits) appeared in which films, we want to

find all actors and crew that appeared in "Science Fiction" genre films, and display their names next to how many Science Fiction films they appeared in, from most to least
find all movies that Tom Hanks has appeared in
find all movies where both Tom Hanks and Tim Allen have appeared
(Copy and paste the above code into a this cell to keep your solutions separated (if desired))
"""


"""
Problem 3: Six Degrees of Kevin Bacon
There's a game, called Six Degrees of Kevin Bason. It goes like this: Pick any actor, and you can find within 6 degrees of separation, a movie featuring Kevin Bacon.
In order to solve it with an algorithm, we'll need to use either Breadth First Search or Depth First Search.

Oh by the way you already learned to use graphs in the first question, surprise! They're not as scary as they seem. It's just the idea that "things have relationships".
When you added every cast to it's movie, and every movie to it's cast, you created what's called an edge list.
An edge list is a fancy graph-search term meaning "a list of the relationships between every thing and every other thing indexed by the name of the thing". Every relationship table in SQL is an edge list. Sometimes it looks like this:
"""