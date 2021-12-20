import json

from marshmallow import Schema, fields, post_load


class DirectorSchema(Schema):
    name = fields.String()


class MoveInfoSchema(Schema):
    directors = fields.Nested(DirectorSchema, many=True)
    release_date = fields.DateTime()
    rating = fields.Float()
    genres = fields.List(fields.String())
    image_url = fields.Url()
    plot = fields.String()
    rank = fields.Integer()
    running_time_secs = fields.Integer()
    actors = fields.List(fields.String())


class MovieSchema(Schema):
    year = fields.Integer()
    title = fields.String()
    info = fields.Nested(MoveInfoSchema)


class OutputSchema(Schema):
    author = fields.String()


json_path = "../../data/moviedata.json"

with open(json_path, 'rb') as f:
    data_json = json.load(f)
    movie_schema = MovieSchema()
    movies = movie_schema.load(data_json, many=True)
    print(movies)
