from dao.models.movies import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre_id(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, yid):
        return self.session.query(Movie).filter(Movie.year == yid).all()

    def create(self, movie_new):
        result = Movie(**movie_new)
        self.session.add(result)
        self.session.commit()
        return result

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_mid):
        movie = self.get_one(movie_mid.get("id"))
        movie.title = movie_mid.get("title")
        movie.description = movie_mid.get("description")
        movie.trailer = movie_mid.get("trailer")
        movie.year = movie_mid.get("year")
        movie.rating = movie_mid.get("rating")
        movie.genre_id = movie_mid.get("genre_id")
        movie.director_id = movie_mid.get("director_id")

        self.session.add(movie)
        self.session.commit()
