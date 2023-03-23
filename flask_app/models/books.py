from  flask_app.config.mysqlconnection import connectToMySQL


class Books:
    DB = "books"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.number_of_pages = data['number_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorited_by_author =[]



    @classmethod
    def save(cls, data ):
        query="""
                    INSERT INTO
                    books(title, number_of_pages)
                    VALUES (%(title)s,%(number_of_pages)s)
                    ;"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

    @classmethod
    def get_all_books(cls):
        query="""
                    SELECT * FROM
                    books;
                    """
        result = connectToMySQL(cls.DB).query_db(query)
        all_books =[]
        for row in result:
            all_books.append(cls(row))
        return all_books

    @classmethod
    def get_by_id(cls,data):
        query = """
                    SELECT * FROM
                    books
                    LEFT JOIN favorites 
                    ON
                    books.id = favorites.book_id
                    LEFT JOIN authors
                    ON
                    authors.id = favorites.author_id
                    WHERE
                    book.id =%(id)s
                    ;"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        book = cls(result[0])
        for row in result:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.favorited_by_author.append(author.Author(data))
        return book

    @classmethod
    def unfavorited_books(cls,data):
        query ="""
                    SELECT * FROM
                    books
                    WHERE
                    books.id
                    NOT IN
                    (SELECT
                    book_id
                    FROM
                    favorites
                    WHERE
                    author_id = %(id)s)     
                    ;"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        unfavorited_books =[]
        for row in result:
            # book = cls(result)
            book_info ={
                'id':row['id'],
                'title':row['title'],
                'number_of_pages':row['number_of_pages'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at']
                }
            unfavorited_books.append(cls(book_info))
        return unfavorited_books

