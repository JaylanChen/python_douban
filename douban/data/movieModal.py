from peewee import *

db = SqliteDatabase('movie.db')
class BaseModel(Model):
    class Meta:
        database = db # This model uses the "movie.db" database.

class MovieTypeItem(BaseModel):
    id = IntegerField()
    name = TextField()
    url = TextField()

class MovieItem(BaseModel):
    id = IntegerField()
    #名称
    name = TextField()
    #上映时间
    showDate = DateTimeField()
    #别名
    alias = TextField()
    #主演
    leadingRole = TextField()
    #类型
    movieType = ForeignKeyField(MovieTypeItem, related_name='movies')()
    #语言
    language = TextField()
    #时长
    duration = IntegerField()
    #评分
    grade = FloatField()
    #剧情简介
    introduction = TextField()
    #评价数
    comments = IntegerField()