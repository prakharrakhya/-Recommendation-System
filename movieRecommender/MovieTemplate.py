class MovieTemplateBase:
    def __init__(self , name , year , imdbID , Type , Poster):
        self.name = name
        self.year = year
        self.imdbid = imdbID
        self.type = Type
        self.poster = Poster

class MovieTemplateDetails:
    def __init__(self , name , year , imdbID , Type , Poster , Rated , ReleaseDate , Runtime , Genre , Director , 
                 Writer ,Actor, Plot , Language , Ratings , Metascore , imdbrating , imdbvotes):
        self.name = name
        self.year = year
        self.imdbid = imdbID
        self.type = Type
        self.poster = Poster
        self.releasedate = ReleaseDate
        self.runtime = Runtime
        self.rated = Rated
        self.genre = Genre
        self.director = Director
        self.writer = Writer
        self.actor = Actor
        self.plot = Plot
        self.language = Language
        self.ratings = Ratings
        self.metascore = Metascore
        self.imdbrating = imdbrating
        self.imdbvotes = imdbvotes
        
    
def getMovie(MovieList):
    data = []
    for k in MovieList:
        movie = MovieTemplateBase(k['Title'] , k['Year'] , k['imdbID'] , k['Type'] , k['Poster'])
        data.append(movie)
    return data

def get_movie_area(k):
    movie = MovieTemplateBase(k['Title'] , k['Year'] , k['imdbID'] , k['Type'] , k['Poster'])
    return movie   

def getMovieDetails(MovieData):
    k = MovieData
    movie = MovieTemplateDetails(k['Title'] , k['Year'] , k['imdbID'] , 
                                     k['Type'] , k['Poster'] , k['Rated'] , k['Released'] , 
                                     k['Runtime'] , k['Genre'] , k['Director'] , k['Writer'] , 
                                     k['Actors'] , k['Plot'] , k['Language'] , k['Ratings'] , 
                                     k['Metascore'] , k['imdbRating'] , k['imdbVotes'])
        
    return movie