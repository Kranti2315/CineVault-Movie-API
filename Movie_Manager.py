# Database Connectivity
from database import get_connection
conn = get_connection()
cursor = conn.cursor()

class Movie:
    def __init__(self, mid, mname, mgenre, mrating,mavailable):
        self.__movie_id = mid
        self.__name = mname
        self.__genre = mgenre
        self.__rating = mrating
        self.__available=mavailable

    def getId(self):
        return self.__movie_id

    def __str__(self):

        return f"| {self.__movie_id:^5} | {self.__name:^15} | {self.__genre:^12} | {self.__rating:^6} |{self.__available:^6}"

while True:
    print("\n" + "="*55)
    print("              MOVIE COLLECTION MANAGER")
    print("="*55)


    print("1 ➤ Add Movie")
    print("2 ➤ Display Movies")
    print("3 ➤ Update Movie By Id")
    print("4 ➤ Delete Movie")
    print("5 ➤ Search Movie")
    print("6 ➤ Exit")

    print("-"*55)
    choice = int(input("Enter your choice: "))

    # Add Movies

    if choice == 1:
        size = int(input("How Many Movies You Want To Add : "))
        for i in range(size):
            movie_id = int(input("Movie Id : "))
            name = input("Movie Name : ")
            genre = input("Genre : ")
            rating = float(input("Rating : "))
            available=input("Enter Availability: ")
            
            query = """
            INSERT INTO movies
            (movie_id,name,genre,rating,available)
            VALUES(%s,%s,%s,%s,%s)
            """
            values = (
                movie_id,
                name,
                genre,
                rating,
                available
            )

            cursor.execute(query, values)
            conn.commit()

        print("Movie Added Successfully")

    # Display Movies
    elif choice == 2:

        cursor.execute(
            "SELECT * FROM movies"
        )

        movies = cursor.fetchall()
        print("Data received")

        if len(movies) == 0:
            print("Movie Collection Empty")
        else:
            print("\n"+"-"*55)
            print("| ID |  Name  |  Genre  |  Rating  | Available |")
            print("-"*55)
            for movie in movies:
                print(movie)

            print("-"*55)

    # Update Movies
    elif choice == 3:
        ex_id = int(input("Enter existing Movie Id : "))
        name = input("New Movie Name : ")
        genre = input("New Genre : ")
        rating = float(input("New Rating : "))
        available=input("Enter Availability: ")
        query = """

        UPDATE movies

        SET name=%s,
        genre=%s,
        rating=%s,
        available=%s

        WHERE movie_id=%s

        """
        values = (
            name,
            genre,
            rating,
            available,
            ex_id
        )
        cursor.execute(query, values)

        conn.commit()

        if cursor.rowcount > 0:

            print("Movie Updated Successfully")


        else:

            print("Movie Id Not Found")

    # Delete Movies
    elif choice == 4:
        del_id = int(input("Enter Movie Id to delete : "))

        cursor.execute(
            "DELETE FROM movies WHERE movie_id=%s",
            (del_id,)

        )
        conn.commit()

        if cursor.rowcount > 0:
            print("Movie Deleted Successfully")
        else:
            print("Movie Id Not Found")

    # Search Movies
    elif choice == 5:
        search_id = int(input("Enter Movie Id to search : "))
        cursor.execute(

            "SELECT * FROM movies WHERE movie_id=%s",

            (search_id,)

        )

        movie = cursor.fetchone()
        if movie:
            print("\nMovie Found")
            print(movie)
        else:
            print("Movie Id Not Found")

    elif choice==7:
        available=input("Enter Availability")

    

    # Exit
    elif choice == 6:
        print("Thank You For Using Movie Manager")
        conn.close()
        break
    else:
        print("Invalid Choice")


    
        
