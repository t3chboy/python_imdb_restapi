from app import db
from marshmallow import Schema, fields


class MoviesGenres(db.Model):
    movie_id = db.Column(db.Integer,primary_key=True)
    genre = db.Column(db.String(255),primary_key=True)


    def getAll(mysql):
        myschema = MoviesGenresSchema(many=True)
        allMovieData = MoviesGenres.query.all()
        result = myschema.dump(allMovieData)
        return result

    def add(movie_id,postmoviedata):
        success=True
        try:
            moviegenredata = []
            for genre in postmoviedata:
                moviegenredata.append(MoviesGenres(movie_id=movie_id,genre=genre))

            db.session.bulk_save_objects(moviegenredata)
            db.session.commit()
            return success
        except Exception as e:
            raise Exception

    def delete(movieid):
            try:
                db.session.query(MoviesGenres).filter(MoviesGenres.movie_id == movieid).delete()
                db.session.commit()
                return [1]
            except Exception as e:
                db.session.rollback()
                raise Exception


# Generate schema for ORM
class MoviesGenresSchema(Schema):
    class Meta:
        model = MoviesGenres
    movie_id = fields.Integer()
    genre = fields.String()