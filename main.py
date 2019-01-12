"""
Name: Sayan Das
Date: 10/01/2019
Brief Project Description: This project opens the song list using kivy app of the song list , help the user interacts with the song list .
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from songlist import SongList
class SongsToLearnApp(App):
    """
    Main program - Kivy app to demo song list system
    """
    status_text = StringProperty()
    status_text2 = StringProperty()
    def __init__(self, **kwargs):
        """
        :Parameter:**kwargs
        Initiate the self.song_list to SongList() class
        :return:None
        """
        super(SongsToLearnApp, self).__init__(**kwargs)
        self.song_list = SongList()
    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Vaibhav Jain - Song List"
        self.root = Builder.load_file('app.kv')
        self.create_entry_buttons() #Display the entry at start

        return self.root

    def create_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        num_song=0
        learned_num=0
        self.root.ids.entriesBox.clear_widgets()
        for each in self.song_list.list_song:
            # create a button for each song entry
            num_song+=1 #Add up the number of song for every song looped in the list

            if each.status == "n":
                temp_button = Button(text="{} by {} ({}) ({})".format(each.title,each.artist,each.year,"learned"))#Format the text for learned song in temp_button
            else:
                temp_button = Button(text="{} by {} ({}) ".format(each.title,each.artist,each.year))
                temp_button.bind(on_release=self.press_entry)
                temp_button.bind(on_release=each.markSonglearned)#Mark the song chosen from the temp_button by clicking it learnt #Also note , by clicking refresh it will help
            self.root.ids.entriesBox.add_widget(temp_button)
            if each.status =="n":
                temp_button.background_color = [1,0,0,1] #turn background color into red
                learned_num+=1
            else :
                temp_button.background_color = [2,1,1,2] #turn background color button into pink
        self.status_text = "To learn:{} learned :{}".format(num_song-learned_num,learned_num)
    def press_entry(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        name = instance.text

        self.status_text2 = "You have not learned {}".format((self.song_list.get_song(name))) # This would update the bottom label if the user press on the temp_button
        instance.state = 'normal'
        #Note that I failed to update the bottom label text.

    def clear_text(self):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        # use the .children attribute to access all widgets that are "in" another widget
        self.root.ids.Title.text = ""
        self.root.ids.Artist.text = ""              #Empty the text boxes
        self.root.ids.Year.text = ""
        for instance in self.root.ids.entriesBox.children:    #Normalise the button state
            instance.state = 'normal'
        self.root.ids.statusLabel2.text="" #Empty the status label text box

    def add_song(self):
        """
        Handler for pressing the add button
        :return: None
        """

        if self.root.ids.Title.text == "" or self.root.ids.Artist.text == "" or self.root.ids.Year.text == "":
            self.root.ids.statusLabel.text = "All fields must be required"                                      #Displayed when user does not fill in all the field and press Add Song
            return
        try:
            YEAR = int(self.root.ids.Year.text) #Make sure the year text is a number
            self.song_list.AddSongToSongList(self.root.ids.Title.text,self.root.ids.Artist.text,self.root.ids.Year.text,"n")#Return to function from songlist
            temp_button = Button(text="{} by {} ({}) ({})".format(self.root.ids.Title.text,self.root.ids.Artist.text,self.root.ids.Year.text,"y"))
            temp_button.bind(on_release=self.press_entry)
            temp_button.background_color = [1,0,0,2]        #Append the new temp button with color pink
            self.root.ids.entriesBox.add_widget(temp_button)#Adding widget temp_button
            self.root.ids.Title.text = ""
            self.root.ids.Artist.text = "" #Empty the text boxes
            self.root.ids.Year.text = ""
        except ValueError:
            self.status_text2="Please enter a valid number"#Display status label at the buttom

    def on_stop(self):
        """
        Saves the songs to the csv file by calling the save_songs
        :return: None
        """
        self.song_list.save_songs()
    def press_refresh(self):
        """
        Refresh the page whether the user learn songs or choose to sort by title or artist or year from the spinner
        :return: None
        """
        self.song_list.sort_songs(self.root.ids.spinner.text) #Sort_songs based on the text on the spinner
        self.create_entry_buttons() #Recreate the entry button whenever you click
        #Note & Comment : This Button supposes not to be included in the Gui layout and could be worked independently for each temp button and for the spinner , it does not undo the songs that have been learned.
        #Keeping button helps a more convenient way to show the result after pressing it .

    def clear_fields(self):
        """
        Clear the Title , Artist , Year boxes
        :return: None
        """
        self.root.ids.Title.text = ""
        self.root.ids.Artist.text = ""
        self.root.ids.Year.text = ""


SongsToLearnApp().run()
