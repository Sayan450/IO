# create your SongList class in this file
from operator import attrgetter
from song  import Song
from operator import itemgetter

class SongList:
    def __init__(self,file = ""):
        """
        initiate the self attribute list_song
        calls the load songs to immediately update the songlist
        :return: None
        """
        self.list_song = [] #Initiate list_song as a list that contains all the songs
        self.load_songs() #Initiate the song_list function
    def get_song(self,text):
        """
        Get through the whole list song , get the title and return it
        :return: each.title
        """
        for each in self.list_song: #Loop through the whole song list
            text2 = ("{} by {} ({}) ({}) ({})".format(each.title,each.artist,each.year,"learned")) #create a new variable called text2 that has the same format to the text in the button
            if text2 == text: #Condition to find the song with same text
                return each.title #Returns the title of that song
        #Comment : This Function supposes to help to update the buttom label whenever user clicks on the song_button so that it reveals the user that song is learnt
                #  But something I could not find that stuck during the process

    def AddSongToSongList(self,title,author,year,status):
        """
        Append new song to the song list
        Sort the song list
        :return: none
        """
        newSong=Song(title,author,year,'y') #Create a new variable called newSong
        self.list_song.append(newSong) #Append new added Song to the list song
        self.sort_songs() #Sort List Song with new Song in the List
    def load_songs(self):
        """
        Load and sort songs , append new format for the song list .
        return the list song for usage
        :return: self.list_song
        """

        self.file=open("songs.csv","r+") #Load files from songs.csv
        list_song = self.file.readlines()#Append list_song list with each lines of csv
        for each in list_song:
            each = each.strip().split(',')#Strip off the comma ',' from the csv line
            formatted_Song = Song(each[0],each[1],int(each[2]),each[3]) #Append title , artist , year to variable formatted_Song , which basically formatted song that would be put to list song to use
            self.list_song.append(formatted_Song) # Append every formatted Song to the list
        self.sort_songs(self)
        return self.list_song
    def save_songs(self):
        """
        Save the song list to csv after closing the kivy demo
        :return: none
        """
        csv_string= "" #Create a new string called csv_string that would fit the format of the new CSV file
        for each in self.list_song: #Loop through the whole list song
            csv_string +="{},{},{},{}\n".format(each.title,each.artist,each.year,each.status) #Define the csv_string with a suitable format for the csv.file with ',' between title , artist and year
        out_file = open("songs.csv",'w')
        out_file.seek(0)
        out_file.truncate()
        out_file.write(csv_string) #Save a newly written out_file to csv.file songs.csv
        out_file.close()
    def sort_songs(self,name):
        """
        Sort the song list based on the spinner selected
        :return: none
        """
        if name=="Title": #If the Spinner text is Title
            self.list_song=sorted(self.list_song,key=attrgetter("title")) #Sort the list_song and temp_button with attrgetter ("title") (Sort by title)
        if name=="Artist":#If the Spinner text is Artist
            self.list_song=sorted(self.list_song,key=attrgetter("artist"))#Sort the list_song and temp_button with attrgetter("artist") (Sort by artist)
        if name=="Year":#If the Spinner text is Year
            self.list_song=sorted(self.list_song,key=attrgetter("year"))#Sort the list_song and temp_button with attrgetter("year") (Sort by year)

