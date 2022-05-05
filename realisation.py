from dao.directors import DirectorDAO
from dao.genres import GenreDAO
from dao.movies import MovieDAO
from services.directors import DirectorService
from services.genres import GenreService
from services.movies import MovieService
from database import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
