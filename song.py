# create your Song class in this file
# Song class interact with song only

class Song:
    def __init__(self,title = "",artist = "",year = 0,status=""):
    #These parameters display the characters of a book should have , should be labeled in order .
        self.artist = artist
        self.title = title
        self.year = year
        self.status= status
    def __str__(self):
        if self.status =="y":
            status= "learned"
            return ("You have learned {} {} ({})".format(self.artist, self.title, self.year))
        else:
            status= ""
            return ("You have not learned {} {} ({})".format(self.artist, self.title, self.year))
    def markSonglearned(self, *args):

        """
        Change the status to the song to learn when user click it
        :return: status
        """
        self.status="n"
        return self.status