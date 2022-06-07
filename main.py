# importing the module
import imdb

ia = imdb.IMDb()

# getting top movies
search = ia.get_top250_movies()

# printing top-grossing 10 movies title
for i in range(10):
    print(search[i]['title'])