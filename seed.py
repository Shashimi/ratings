import model
import csv
import re
#import DateTime 

def load_users(session):
    # use u.user
    # open the file 
    # use 'with' when opening a file, manipulating file, then closing it 

    with open("seed_data/u.users") as f:
# read the data and tokenize by |
        reader = csv.reader(f, delimiter = "|")
#parse/read line by line 
        for row in reader:
#this tuple is the same as id = row[0], age = row[1], zipcode = row[4]
            id, age, gender, occupation, zipcode = row 
#set as integer 
            id = int(id)
#set as integer 
            age = int(age)
#creating an object 
            u = model.User(id=id, email=None, password=None, age=age, zipcode=zipcode)
#add to the session
            session.add(u) 
#commit 
        session.commit()
        print "Your users have been added to the .db!"   



def load_movies(session):
    # use u.item
    #open the file 
    with open("seed_data/u.item") as f:
#read data and tokenize by |
        reader = csv.reader(f, delimiter = "|")
# looking line by line 
        for line in reader:
#pull out the relevant elements from each line and set to variables
            id = line[0]
            title = line[1]
            release_data = line[2]
            imdb = line[4]
            id = int(id)
# account for accent marks 
            title = title.decode("latin-1")
#remove the year date at the end of the title 
#re.sub performs search and replace across subject,replacing all matches
#of regex in sub with replacement 
            title = re.sub("\d{4}\)","",title)
#ck for release data, if none throw away that data
            if not release_date:
            #will bring you to the beginning of the for loop
                continue 
            #set the release date to the datetime 
            release_date = datetime.datetime.strptime(release_date, "%d-%b-%Y")
            #create the object-sqlalchemy wants explicity when we want to 
            #add to the .db so we add an object to our session 
            m = model.Movies(id=id, name=title, released_at=release_date, 
                                imdb_url=imdb)
            #add to the session 
            session.add(m)
            #commit 
        session.commit()
        print "The movies have been added!"

def load_ratings(session):
    # use u.data
    #open file 

    with open("seed_data/u.data") as f:
        reader = csv.reader(f,delimiter = "\t")
        for line in reader:
            #pull out the relevant elements from line and set to variables
            user_id, movie_id, rating, timestamp = line 
            user_id = int(user_id)
            movie_id = int(movie_id)
            rating = int(rating)

        #create the object
            r=model.Ratings(user_id=user_id, movie_id=movie_id, rating=rating)
            session.add(r)
        session.commit()
        print "The ratings have been added"

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(s)
    load_movies(s)
    load_ratings(s)

if __name__ == "__main__":
    s= model.connect()
    main(s)
