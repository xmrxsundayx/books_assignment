from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.books import Books

class Authors:
    DB = "books"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.get_authors_favorites =[]


    @classmethod
    def save(cls, data ):
        query=""" 
                    INSERT INTO
                    authors(name)
                    VALUES (%(name)s)
                    ;"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

    @classmethod
    def get_all_authors(cls):
        query ="""
                    SELECT * FROM 
                    authors;
                    """
        result = connectToMySQL(cls.DB).query_db(query)
        all_authors =[]
        for row in result:
            #make an object
            all_authors.append(cls(row))
            #add to list
        return all_authors



    @classmethod
    def add_favorite(cls,data):
        query = """INSERT INTO 
                    favorites (author_id,book_id) 
                    VALUES 
                    (%(author_id)s,%(book_id)s)
                    ;"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

    @classmethod
    def authors_favorites(cls,data):
        query ="""
                    SELECT * FROM
                    authors
                    LEFT JOIN favorites
                    ON
                    authors.id = favorites.author_id
                    LEFT JOIN books
                    ON 
                    books.id = favorites.book_id
                    WHERE
                    authors.id = %(id)s
                    ;"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        author = cls(result[0])
        # print(result)
        for row in result:
            book_info ={
                'id':row['books.id'],
                'title':row['title'],
                'number_of_pages':row['number_of_pages'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at']
            }
            author.get_authors_favorites.append(Books(book_info))
        return author