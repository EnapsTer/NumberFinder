import sqlite3
from sqlite3 import Error
from numberFinder import PhoneNumberFinder

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def main():
    database = "mainbase.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM urls INNER JOIN url_contact ON urls.url_id = url_contact.parent_id")
        #print child pages
        for row in cur:
            finder = PhoneNumberFinder(row[3])
            for number in finder.get_number():
                print(number + ', parent page %s' %(row[1]))
        #print parent pages
        cur.execute("SELECT * FROM urls")
        for row in cur:
            finder = PhoneNumberFinder(row[1])
            for number in finder.get_number():
                print(number)


if __name__ == '__main__':
    main()




