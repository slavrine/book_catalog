from app import db
from datetime import datetime

class Publication(db.Model):
    __tablename__='publication'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),nullable=False)

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return 'The Publisher name is {}'.format(self.name)


# define the Book class
class Book(db.Model):
    __tablename__="book"

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(500),nullable=False,index=True)
    pub_date=db.Column(db.DateTime,default=datetime.utcnow())
    avg_rating=db.Column(db.Float)
    author=db.Column(db.String(350))
    format=db.Column(db.String(50))
    image=db.Column(db.String(100),unique=True)
    num_pages=db.Column(db.Integer)


    # Set the foreign key for the Publication class to be the same as publication.id
    # publication = table we have created previously
    # id = a column inside that table
    pub_id=db.Column(db.Integer,db.ForeignKey('publication.id'))

#     # initialize the database
# bookid (primary key) and pub_date are not fed into the init here, as they are fed in automatically
    def __init__(self,title,author,avg_rating,book_format,image,num_pages,pub_id):
        self.title=title
        self.author=author
        self.avg_rating=avg_rating
        self.image=image
        self.num_pages=num_pages
        self.format=book_format
        self.pub_id=pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title,self.author)

