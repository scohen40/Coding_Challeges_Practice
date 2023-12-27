"""
Problem 1: Read and parse a large CSV
Below is example code that will print the first ten lines of the movies_metadata.csv file.
Write a loop to read the entire movies_metadata.csv file and create a dictionary that indexes each movie by ID.

Next, read in the entire credits.csv file

The third field in the CSV, 'id', is the ID of the movie they're in, so it will match your movies_index
As you create a credits index, also attach each cast & crew member to it's movie, by adding it to the "credits" array from the movie dict within the movie index. Each credit has a field, "id", which is unique to the actor or crewmember- that way if you encounter a sound engineer named "Tom Hanks", you can distinguish between them.
"""

import csv
import pprint
pp = pprint.pprint


counter = 0
columns = []
movies_index = {}
credits_index = {}
with open('../input/the-movies-dataset/movies_metadata.csv', newline='') as f:
    reader = csv.reader(f)
    
    for row in reader:
        # print("Raw row", row)
        movie = {}
        if counter == 0: ## header row
            columns = row
        else:
            column_index = 0
            if len(row) == len(columns):
                for column in columns:
                    movie[column] = row[column_index]
                    if column == "genres":
                        movie[column] = eval(row[column_index])
                    column_index += 1
        ##pp(movie)
        movie["credits"] = []
        #print("New Row ------------------")
        if movie.get('id', False):
            movies_index[movie["id"]] = movie
        counter += 1
        
        if counter > 10:
            break
# pp(movies_index)

counter = 0
with open('../input/the-movies-dataset/credits.csv', newline='') as f:
    reader = csv.reader(f)
    
    for row in reader:
        # print("Raw row", row)
        credit = {}
        if counter == 0: ## header row
            columns = row
        else:
            column_index = 0
            if len(row) == len(columns):
                for column in columns:
                    credit[column] = eval(row[column_index])
                    column_index += 1
            
        if counter > 0:
            cast = credit.get("cast",[])
            crew = credit.get("crew", [])
            cast_and_crew = cast + crew
            print(len(cast_and_crew))
            for crewmember in cast_and_crew:
                if crewmember.get('id', False):
                    existing_crewmember = credits_index.get(crewmember["id"], {})
                    
                    credits_index[crewmember["id"]] = existing_crewmember
        
        counter += 1
        if counter > 500: ## limited to 500 movies for testing, but you'll want to completely index all credits by movie when you do the next exercises
            break

## Above is a loop to read the entire movies_metadata.csv file and create a dictionary that indexes each movie by ID.
## example (with just one movie):

# movies_index = {
#     "862": {
#         "original_title": "Toy Story",
#         "credits": []
#     }
# }

## so that you can find movies by their ID like so:

print(movies_index.get("862"))

## next, read in the entire credits.csv file
## create a similar dictionary for credits, like so:

# credits_index = {
#     "31": {
#         'movie_id': '862',
#         'cast_id': 14, 
#         'character': 'Woody (voice)', 
#         'credit_id': '52fe4284c3a36847f8024f95', 
#         'gender': 2, 
#         'id': 31, 
#         'name': 'Tom Hanks', 
#         'order': 0, 
#         'profile_path': '/pQFoyx7rp09CJTAb932F2g8Nlho.jpg',
#         'movies': [movie_ids go here]
#     }
# }

## The third field in the CSV, 'id', is the ID of the movie they're in, so it will match your movies_index above
## As you create a credits index, also attach each cast & crew member to it's movie, 
## by adding it to the "credits" array from the movie dict above

"""
Problem 2: Find All Sci-Fi actors
Now that we know which Actors and Crew (all credits) appeared in which films, we want to

find all actors and crew that appeared in "Science Fiction" genre films, and display their names next to how many Science Fiction films they appeared in, from most to least
find all movies that Tom Hanks has appeared in
find all movies where both Tom Hanks and Tim Allen have appeared
(Copy and paste the above code into a this cell to keep your solutions separated (if desired))

The top 10 crew in decending order are: 

Roger Corman 70
Stan Lee 69
Steven Spielberg 55
Jerry Goldsmith 55
John Carpenter 48
James Cameron 47
Charles Band 46
Phil Tippett 46
George Lucas  44
Roland Emmerich 41
"""

import csv
import pprint
pp = pprint.pprint
## Solution

counter = 0
columns = []
movies_index = {}
credits_index = {}
genre_index = {} ## Add a genre index

with open('../input/the-movies-dataset/movies_metadata.csv', newline='') as f:
    reader = csv.reader(f)
    
    for row in reader:
        # print("Raw row", row)
        movie = {}
        if counter == 0: ## header row
            columns = row
        else:
            column_index = 0
            if len(row) == len(columns):
                for column in columns:
                    movie[column] = row[column_index]
                    if column == "genres":
                        movie[column] = eval(row[column_index])
                        
                    column_index += 1
        
        movie["credits"] = []
#         print(movie)
        
        
        if movie.get('id', False):
            movies_index[movie["id"]] = movie
            
            ## Here's where we created a list of movies by genre, so that we can find "Science Fiction" movies later
            for genre in movie.get("genres"):
                movies_by_genre = genre_index.get(genre.get("name"),[])
                movies_by_genre.append(movie.get("id"))
                genre_index[genre.get("name")] = movies_by_genre
                
        counter += 1
        
#         if counter > 5000:
#             break
print(counter, " movies loaded")
print(genre_index.keys())

"""
Output:
45467  movies loaded
dict_keys(['Animation', 'Comedy', 'Family', 'Adventure', 'Fantasy', 'Romance', 'Drama', 'Action', 'Crime', 'Thriller', 'Horror', 'History', 'Science Fiction', 'Mystery', 'War', 'Foreign', 'Music', 'Documentary', 'Western', 'TV Movie'])
"""

counter = 0
with open('../input/the-movies-dataset/credits.csv', newline='') as f:
    reader = csv.reader(f)
    
    for row in reader:
        # print("Raw row", row)
        credit = {}
        if counter == 0: ## header row
            columns = row
        else:
            column_index = 0
            if len(row) == len(columns):
                for column in columns:
                    credit[column] = eval(row[column_index])
                    column_index += 1
            
        if counter > 0:
            cast = credit.get("cast",[])
            crew = credit.get("crew", [])
            cast_and_crew = cast + crew
            for crewmember in cast_and_crew:
                
                if crewmember.get('id', False):
                    existing_crewmember = credits_index.get(crewmember["id"])
                    if existing_crewmember:
                        if not existing_crewmember.get("movies"):
                            existing_crewmember["movies"] = []
                        existing_crewmember["movies"].append(credit.get("id"))
                        movie = movies_index.get(str(credit.get("id","0")))
                    else:
                        credits_index[crewmember.get("id")] = crewmember
                    if movie:
                        movie_credits = movie.get("credits",[])
                        movie_credits.append(crewmember)
                        movie["credits"] = movie_credits
                    else: 
                        pass
                        #print("movie not found", credit.get("id"))
        counter += 1
#         if counter > 5000: ## limited to 5000 credits for testing, but you'll want to completely index all credits by movie when you do the next exercises
#             break
            
print(counter, "cast loaded")

"""
Output:
45477 cast loaded
"""

## Splitting the cells like this allows us to run the expensive "load into memory" code one time, then run this smaller subset of code for subsequent runs
print("go")
# print(len(credits_index.keys()))
## Now that we've attached Credits to Films we can look through all the Science Fiction films
sci_fi_movie_count = {}
print(len(genre_index.get("Science Fiction",[])))
for movie_id in genre_index.get("Science Fiction",[]):
    movie = movies_index.get(movie_id,{})
#     print(movie.get("title"))
    ## get the credits
    movie_credits = movie.get("credits",[])
    ## loop over them
    for credit in movie_credits:
#         print(credit)
        ## we'll mark down each time we see each crewmember
        sci_fi_movie_count[credit["id"]] = sci_fi_movie_count.get(credit["id"],0) + 1

score_list = [{"crew": credits_index.get(key), "score": value} for key, value in sci_fi_movie_count.items()]
def get_score(item):
    return item.get("score",0)
sorted_list = reversed(sorted(score_list, key=get_score))

count = 0
for score in sorted_list:
    crew = score.get("crew",{})
    print(crew.get("name"), "(", crew.get("id"), ")", score.get("score",0))
    count += 1
    if count > 10:
        break
    
print("done")
print(credits_index[7624])

"""
Output: 
go
3047
Stan Lee ( 7624 ) 68
Roger Corman ( 102429 ) 61
Charles Band ( 19707 ) 44
Steven Spielberg ( 488 ) 38
Tomoyuki Tanaka ( 18604 ) 33
James Cameron ( 2710 ) 32
Jerry Goldsmith ( 1760 ) 32
Bert I. Gordon ( 101225 ) 31
George Lucas ( 1 ) 31
David Cronenberg ( 224 ) 30
Roland Emmerich ( 6046 ) 30
done
{'cast_id': 26, 'character': 'Himself', 'credit_id': '52fe434bc3a36847f8049347', 'gender': 2, 'id': 7624, 'name': 'Stan Lee', 'order': 12, 'profile_path': '/dTr2gJPL7jELKVkcjtoNx80uVKR.jpg', 'movies': [36647, 36657, 36586, 557, 557, 557, 557, 9480, 9480, 1927, 1927, 1927, 7220, 27601, 558, 558, 558, 36648, 40844, 25757, 9947, 9738, 9738, 9738, 18882, 36668, 36668, 559, 559, 559, 1979, 1979, 1979, 1726, 1726, 1726, 1724, 1724, 1724, 79509, 10138, 10138, 10138, 10195, 10195, 1771, 1771, 24428, 24428, 24428, 71676, 91356, 91356, 1930, 1930, 1930, 22059, 40572, 55327, 24479, 26883, 63686, 169934, 169934, 68721, 68721, 68721, 86843, 76170, 76338, 76338, 100402, 100402, 257346, 257346, 102382, 102382, 127585, 118340, 118340, 177572, 14830, 99861, 99861, 99861, 102899, 102899, 102899, 166424, 166424, 293660, 284053, 284053, 284053, 283995, 283995, 271110, 271110, 284052, 284052, 284052, 246655, 246655, 179267, 230896, 372631, 136585, 207680, 290825, 413279, 299969, 268771, 263115, 263115, 22154, 22154, 14611, 376391]}
"""



"""
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

print(credits_index[7624])

def the_bacon_path(target_actor_id,movies_index,credits_index):
    return the_bacon_path_dfs(target_actor_id,movies_index,credits_index)
    


def the_bacon_path_dfs(target_actor_id,movies_index,credits_index):
    target_actor = credits_index[target_actor_id]
    output = ""
    visited_crew = set()
    def visit_movie(movie):
        
        print(movie)
        
        ## check all crew to see if they're kevin bacon
        for crew in movie.get("credits",[]):
            if crew.get("id") not in visited_crew: ## don't check people twice, or your DFS will grow out of control!
                if crew.get("name") == "Kevin Bacon": ## if we find Bacon, 
                    print("target actor found")
                    return "-> Kevin Bacon"
                else:
                    visited_crew.add(crew.get("id"))
                    for movie_id in crew.get("movies", []):
                        movie = movies_index.get(movie_id)
                        found_bacon = visit_movie(movie)
                        if found_bacon:
                            return "->" + crew.get("name") + found_bacon

    
    target_actor_movies = target_actor.get("movies",[])
    movie = movies_index.get(target_actor_movies[0])
    if movie:
        visit_movie(movie)

def the_bacon_path_bfs(target_actor_id,movies_index,credits_index):
    target_actor = credits_index[target_actor_id]
    output = ""
    visited_crew = set()
    queue_to_visit = [target_actor]
    current_path = []
    kevin = False
    
    while len(queue_to_visit) > 0:
        #print(len(queue_to_visit), len(visited_crew))
        ## get the next crew in line from the queue
        next_crew = queue_to_visit.pop(0)
        visited_crew.add(next_crew.get("id")) ## mark it as visited to save us from entering an infinite loop
        
        ## check all crew to see if they're kevin bacon
        if next_crew.get("name") == "Kevin Bacon":
            print("Found kevin")
            ## found kevin bacon!!
            kevin = next_crew
            break 
        else:
            ## go through the list of their movies
            for movie_id in next_crew.get("movies",[]):
                movie = movies_index.get(str(movie_id))
                if movie:
                    #print("visiting ", movie.get("id"))
                    ## add everyone from their movies to the queue of people to process
                    for crew in movie.get("credits"):
                        if crew.get("id") not in visited_crew:
                            #print("adding ", crew.get("name"))
                            queue_to_visit.append(crew)
                            crew["parent"] = next_crew ## save how we got to this path
    
    
    
    
    if kevin:
        ## work backwards from having found Kevin bacon until the node is the target actor (backwards linked list traversal)
        current_node = kevin
        while current_node != target_actor:
            current_path.append(current_node.get("name"))
            current_node = current_node["parent"]
        current_path.append(target_actor.get("name"))
        print(current_path)
        return " -> ".join(reversed(current_path))
    else:
        return "no path to kevin? seems sus"

    



## the bacon path from Stan Lee
print(the_bacon_path(7624,movies_index,credits_index))

"""
Output:
{'cast_id': 26, 'character': 'Himself', 'credit_id': '52fe434bc3a36847f8049347', 'gender': 2, 'id': 7624, 'name': 'Stan Lee', 'order': 12, 'profile_path': '/dTr2gJPL7jELKVkcjtoNx80uVKR.jpg', 'movies': [36647, 36657, 36586, 557, 557, 557, 557, 9480, 9480, 1927, 1927, 1927, 7220, 27601, 558, 558, 558, 36648, 40844, 25757, 9947, 9738, 9738, 9738, 18882, 36668, 36668, 559, 559, 559, 1979, 1979, 1979, 1726, 1726, 1726, 1724, 1724, 1724, 79509, 10138, 10138, 10138, 10195, 10195, 1771, 1771, 24428, 24428, 24428, 71676, 91356, 91356, 1930, 1930, 1930, 22059, 40572, 55327, 24479, 26883, 63686, 169934, 169934, 68721, 68721, 68721, 86843, 76170, 76338, 76338, 100402, 100402, 257346, 257346, 102382, 102382, 127585, 118340, 118340, 177572, 14830, 99861, 99861, 99861, 102899, 102899, 102899, 166424, 166424, 293660, 284053, 284053, 284053, 283995, 283995, 271110, 271110, 284052, 284052, 284052, 246655, 246655, 179267, 230896, 372631, 136585, 207680, 290825, 413279, 299969, 268771, 263115, 263115, 22154, 22154, 14611, 376391]}
None
"""

