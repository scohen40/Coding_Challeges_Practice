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

# THIS PART REDOES THE CREDITS LOADING FROM PART 1

#### IMPORTING MOVIES AND CREDITS
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

          for genre in movie.get("genres"):
            movies_by_genre = genre_index.get(genre.get("name"),[])
            movies_by_genre.append(movie.get("id"))
            genre_index[genre.get("name")] = movies_by_genre
        counter += 1

        # if counter > 50:
        #     break
# print("Movies:")
# pp(movies_index)
print(counter, " movies loaded")
print(len(movies_index))
print(genre_index.keys())

credit_counter = 0
total_cast = 0

added_to_movies_credits = 0

columns = []

credits_index = {}
adding_counter = 0
with open('credits.csv', newline='') as credits_file:
  reader = csv.reader(credits_file)

  for row in reader:
    credit = {}
    if credit_counter == 0: ## header row
        columns = row
        # print(columns)

    else:
        column_index = 0
        if len(row) == len(columns):
            for column in columns:
                credit[column] = eval(row[column_index])
                column_index += 1
        # if counter == 1 :
          # print("Raw row", row)
          # pp(credit)


    #add each staff_member to the credits index using the id field
    if credit_counter > 0:
      cast = credit.get("cast", [])
      crew = credit.get("crew", [])
      cast_and_crew = cast + crew

      #go through each staff member to add to the credits index and then add them to their movie
      for staff_member in cast_and_crew:
          total_cast += 1
          #add the staff member to the credits_index and add the current movie to their movies
          #check if the staff member has an id before adding them
          if staff_member.get("id", False):
            staff_member_id = staff_member.get("id")
            #if the staff member is not in the credits_index, add it after creating in it a movies array
            if not credits_index.get(staff_member_id, False):
              staff_member["movies"] = [] #will this work if there's no movie id?
              credits_index[staff_member_id] = staff_member
              adding_counter += 1
            #check if theres a movie id to get the movie, add the movie to the staff member's movies, and add the staff member to that movie
            movie_id = str(credit.get("id","0"))
            if movie_id:
              movie = movies_index.get(movie_id)
              #check if there's a movie with that index
              if movie:
                #add the movie to that staff member's movies
                credits_index[staff_member_id]["movies"].append(movie_id)
                #add the staff member to the movie's credits array
                movie_credits = movie.get("credits", [])
                # if staff_member not in movie_credits:
                movie_credits.append(staff_member)
                movie["credits"] = movie_credits
                added_to_movies_credits += 1

    credit_counter += 1
    # if counter > 50:
    #     break

# print("Credits:")
print(added_to_movies_credits)
# pp(credits_index)
# pp(movies_index)
print("Adding Counter: ", adding_counter)
print(credit_counter, " movies credits loaded", total_cast, " cast")

#####LOAD ALL CAST AND CREW IN SCIENCE FICTION MOVIES
counter = 0
sci_fi_crew = {}

##loop through movie ids within the science fiction genre in the genres_index
for sci_movie_id in genre_index.get("Science Fiction", []):
  ##get the movie of the sci_movie_id from the movies index
  if movies_index.get(sci_movie_id, False):
    ##get the credits for that movie
    movie = movies_index.get(sci_movie_id, {})
    credits = movie.get("credits")
    # print(len(credits))
    # pp(credits)

    ##add all of the crew and counts in that movie to the dictionary
    for crewmember in credits:
      # print(crewmember)
      # print(crewmember.get('id'))
      crew_id = crewmember.get('id')
      # print(crew_id)
      ##if the crewmember isn't in the dict, add them and set count to 1
      ##check if the crewmember is in the dictionary
      if not sci_fi_crew.get(crew_id, False):
        ##if the crewmember is not in the dictionary, add them to the dictionary by their id - save their name and sci-fi movie count of 1
        sci_fi_crew[crew_id] = crewmember
        sci_fi_crew[crew_id]["sci_fi_movie_count"] = 1
        counter += 1
      else:
        ##if the crewmember is in the dictionary increment the count by 1
        sci_fi_crew[crew_id]["sci_fi_movie_count"] += 1
        # print("adding 1 to, ", crew_id , "now: ", sci_fi_crew[crew_id]["sci_fi_movie_count"])

    # if counter > 50:
    #   break
print("Sci-Fi crew added: ", counter)
# print(counter)
print(len(sci_fi_crew))
# pp(sci_fi_crew)
# pp(sci_fi_crew.get(1546172))


##sort from highest count to lowest count
sorted_crew = sorted(sci_fi_crew.items(), key=lambda item: item[1]["sci_fi_movie_count"], reverse=True)
# pp(sorted_list)
##print the names and counts of the actors with the top ten highest counts
for crewmember in sorted_crew[0:11]:
  print(crewmember[1].get("name"), crewmember[1].get("sci_fi_movie_count"))
  # pp(crewmember)
