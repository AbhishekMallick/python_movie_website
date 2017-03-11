import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that come to life",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://youtu.be/KYz2wyBy3kc")

# print (toy_story.storyline)

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://youtu.be/d1_JBMrrYw8")

# print (avatar.storyline)
#avatar.show_trailer()

rush = media.Movie("Rush",
	"An epic rivalry",
	"https://upload.wikimedia.org/wikipedia/en/d/d0/Rush_UK_poster.jpeg",
	"https://youtu.be/L_u3FODrenM")

# print (rush.storyline)
# rush.show_trailer()
movies = [toy_story, avatar, rush]
fresh_tomatoes.open_movies_page(movies)
