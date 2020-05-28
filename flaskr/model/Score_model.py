from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flaskr import db


class Att_Score(db.EmbeddedDocument):
    att_obj = db.StringField(required=True)  # 科目
    att_score = db.StringField(required=True)  # 分数


class Bas_Score(db.EmbeddedDocument):
    bas_obj = db.StringField(required=True)  # 科目
    bas_score = db.StringField(required=True)  # 分数


class Min_Score(db.EmbeddedDocument):
    min_obj = db.StringField(required=True)  # 科目
    min_score = db.StringField(required=True)  # 分数


class Pro_Score(db.EmbeddedDocument):
    pro_obj = db.StringField(required=True)  # 科目
    pro_score = db.StringField(required=True)  # 分数


class Student(db.Document):
    stu_name = db.StringField(required=True)  # 学生姓名
    Stu_id = db.StringField(required=True)  # 学生学号
    stu_coll = db.StringField(required=True)  # 学生所在院系
    stu_Sub = db.StringField(required=True)  # 学生所在专业
    stu_Grad = db.StringField(required=True)  # 学生所在年级
    stu_class = db.StringField(required=True)  # 学生所在班级
    stu_Att_sc = db.EmbeddedDocumentField(Att_Score)  # 学生通识教育课程成绩子文档
    stu_Bas_sc = db.EmbeddedDocumentField(Bas_Score)  # 学生专业基础课程成绩子文档
    stu_Min_sc = db.EmbeddedDocumentField(Min_Score)  # 学生实践课程成绩子文档
    stu_Pro_sc = db.EmbeddedDocumentField(Pro_Score)  # 学生专业课成绩子文档
