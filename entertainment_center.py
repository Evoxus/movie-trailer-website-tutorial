import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", \
    "A story of a boy and his toys coming to life",\
    "http://www.impawards.com/1995/posters/toy_story_ver1.jpg", \
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",\
    "A marine on an alien planet",\
    "http://www.impawards.com/2009/posters/avatar.jpg",\
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

the_matrix = media.Movie("The Matrix",\
    "Follow the white rabbit",\
    "http://www.impawards.com/1999/posters/matrix_ver1.jpg",\
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

the_departed = media.Movie("The Departed",\
    "Irish gangsters",\
    "https://fanart.tv/fanart/movies/1422/movieposter/the-departed-52f9631087322.jpg",\
    "https://www.youtube.com/watch?v=SGWvwjZ0eDc")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",\
    "A man is wrongly accused of murder",\
    "http://static.rogerebert.com/uploads/movie/movie_poster/the-shawshank-redemption-1994/large_9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg",\
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

inception = media.Movie("Inception",\
    "Dreams within dreams",\
    "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg",\
    "https://www.youtube.com/watch?v=66TuSJo4dZM")

lord_of_the_rings = media.Movie("The Lord of the Rings: The Fellowship of the Ring",\
    "Mixed race group wanders through the woods",\
    "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=Pki6jbSbXIY")

movies = [toy_story, avatar, the_matrix, the_departed, the_shawshank_redemption, inception, lord_of_the_rings]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)
