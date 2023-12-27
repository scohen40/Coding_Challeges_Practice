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
genre_index = {}

with open('movies_metadata.csv', newline='') as movies_metadata_file:
    reader = csv.reader(movies_metadata_file)

    for row in reader:
#         print("Raw row", row)
        movie = {}
        if counter == 0: ## header row
            columns = row
#             print(columns)
        else:
            column_index = 0
            if len(row) == len(columns):
                for column in columns:
                    movie[column] = row[column_index]
                    if column == "genres":
                        movie[column] = eval(row[column_index])
                    column_index += 1
#         pp(movie)

        movie["credits"] = []
        #print("New Row ------------------")
        if movie.get('id', False):
          movies_index[movie["id"]] = movie

        counter += 1

        # if counter > 50:
        #     break
# print("Movies:")
# pp(movies_index)
print(counter, " movies loaded")
print(len(movies_index))
# print(genre_index.keys())


## Above is a loop to read the entire movies_metadata.csv file and create a dictionary that indexes each movie by ID.
## example (with just one movie):

# movies_index = {
#     "862": {
#         "original_title": "Toy Story",
#         "credits": []
#     }
# }

## so that you can find movies by their ID like so:

# pp(movies_index.get("862"))
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

"""
Output:
45467  movies loaded
45430
"""

###LOADING CREDITS AND NOT ADDING MOVIE DOUBLES TO CREDITS

counter = 0
columns = []

credits_index = {}

with open('credits.csv', newline='') as credits_file:
    reader = csv.reader(credits_file)

    for row in reader:
#         print("Raw row", row)
        credit = {}
        if counter == 0: ## header row
            columns = row
#             print(columns)

        else:
            column_index = 0
            if len(row) == len(columns):
                for column in columns:
                    credit[column] = eval(row[column_index])
                    column_index += 1
#         pp(credit)

#         print("New Row ------------------")

        ## add each staff_member to the credits index using the id field
        if counter > 0:
            cast = credit.get("cast", [])
            crew = credit.get("crew", [])
            cast_and_crew = cast + crew
            movie_id = str(credit.get("id"))
#             pp(cast_and_crew)
            ##go through each staff member to add them to their movie and then add to the credits index
            for staff_member in cast_and_crew:
                staff_id = staff_member.get("id")
#                 pp(staff_member)
                ##add the staff_member to the credit_index dictionary by the id, if it isn't already in there, and add the movie to the staff's movie list
                if not credits_index.get(staff_id, False):
#                     print('adding')
                    staff_member["movies"] = [movie_id]
                    staff_member["movie_id"] = movie_id
#                     pp(staff_member)
                    credits_index[staff_id] = staff_member
                else:
            ##ISSUE WITH THIS PART: If we are just adding movies for every time the same id comes up, the credit info is lost by not adding the individual credits by the credit id's. Each person might play different roles in different movies.
                    if movie_id not in credits_index[staff_id]['movies']:
                        credits_index[staff_id]['movies'].append(movie_id)
                ##add the staff_member to the credits array in the movies index using the movie id in the credit
                if movies_index.get(movie_id, False):
#                     print('adding to movie credits')
                    movies_index[movie_id]["credits"].append(staff_id)
                    # pp(movies_index[movie_id])




#         if movies_index.get(id, False):

#             movies_index[id]["credits"] = movies_index[id].get("credits", []).append(credit)
#             pp(movies_index.get(id).get("credits"))


        counter += 1

        # if counter > 50:
        #     break

# print("Credits:")
# pp(credits_index.get("31"))
# pp(credits_index)
# pp(movies_index)
        
print(counter)
print(len(movies_index))
print(len(credits_index))
        
"""
Output:
45477
45430
353343
"""