from app import db
from marshmallow import Schema, fields
from app.Models.Movies_Genres import MoviesGenres


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    director_name = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rank = db.Column(db.Float)

    def getAll(self):
        myschema = MoviesSchema(many=True)
        allMovieData = Movies.query.all()
        result = myschema.dump(allMovieData)
        return result

    def add(postmoviedata):
        genreresponse=True
        try:
            adddata = Movies(name=postmoviedata['name'],director_name=postmoviedata['director'],year=postmoviedata['year'],rank=postmoviedata['rank'])
            db.session.add(adddata)
            db.session.commit()
            if adddata.id > 0:
                moviegenredata = {'genre':postmoviedata['genre']}
                genreresponse = MoviesGenres.add(adddata.id,moviegenredata['genre'])
            if genreresponse is not True:
                raise Exception('Failed To Insert Data')
        except Exception as e:
            print("Exception",e)
            db.session.rollback()
            return [-1]
        finally:
            db.session.close()
        return [1]

    def delete(movieid):
        deletemovie = 0
        deletemovie = db.session.query(Movies).get(movieid)

        if deletemovie is not None:
            try:
                db.session.delete(deletemovie)
                db.session.commit()
                genredelete = MoviesGenres.delete(movieid)
                if genredelete[0] is 1:
                    return [1]
            except Exception as e:
                print("Exception",e)
                return [-1,e]
            finally:
                db.session.close()
        else:
            return [0]

class MoviesSchema(Schema):
    class Meta:
        model = Movies
    id = fields.Integer()
    name = fields.String()
    director_name = fields.String()
    year = fields.Integer()
    rank = fields.Float()
