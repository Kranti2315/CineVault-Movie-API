from flask import Flask,jsonify,request
from database import get_connection
from logger import logger
app=Flask(__name__)

# GET ALL MOVIES

@app.route("/movies",methods=["GET"])
def get_movies():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM movies")
    data=cursor.fetchall()
    logger.info("Movies fetched")
    return jsonify(data)

# ADD MOVIE
@app.route("/movies",methods=["POST"])
def add_movie():
    data=request.json
    conn=get_connection()
    cursor=conn.cursor()

    query="""
    INSERT INTO movies
    VALUES(%s,%s,%s,%s,%s)
    """

    values=(
    data["id"],
    data["name"],
    data["genre"],
    data["rating"],
    data["available"],
    )

    cursor.execute(query,values)
    conn.commit()
    logger.info("Movie Added")
    return jsonify(
    {
    "message":"Movie Added Successfully"
    })

# DELETE MOVIE
@app.route("/movies/<int:id>",
methods=["DELETE"])
def delete_movie(id):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("DELETE FROM movies WHERE movie_id=%s",(id,))
    conn.commit()

    logger.warning("Movie Deleted")
    return jsonify(
    {
    "message":"Deleted"
    })

app.run(debug=True)