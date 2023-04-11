class Song:
    # class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(x):
        x.count += 1

    @classmethod
    def add_to_genres(x,genre):
        if genre not in x.genres:
            x.genres.append(genre)

    @classmethod
    def add_to_artists(x,artist):
        if artist not in x.artists:
            x.artists.append(artist)

    @classmethod
    def add_to_genre_count(x,genre):
        if x.genre_count.get(genre) is None:
            x.genre_count[genre] = 1
        else:
            x.genre_count[genre] += 1
    
    @classmethod
    def add_to_artist_count(x,artist):
        if x.artist_count.get(artist) is None:
            x.artist_count[artist] = 1
        else:
            x.artist_count[artist] += 1


    pass
