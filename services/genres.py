from dao.genres import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, genre_new):
        return self.dao.create(genre_new)

    def update(self, genre_new):
        self.dao.update(genre_new)
        return self.dao

    def delete(self, gid):
        self.dao.delete(gid)
