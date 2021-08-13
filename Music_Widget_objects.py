"""

    Library for the Music Widget to create the objects like the Canvas, where the Songs on

"""


import Ctkinter as Ctk
from lib.encode import Encode_umlauts
import glob


__date__ = '06.08.2021'
__completed__ = '11.08.2021'
__work_time__ = 'about 4 Hours'
__author__ = 'Christof Haidegger'
__version__ = '1.0'
__licence__ = 'Common Licence'
__debugging__ = 'Christof Haidegger'


class ButtonCanvas:
    """

        -> This Button Canvas contain the pause, rewind and next button for the Music Player

    """
    def __init__(self, master, func1, func2, func3):
        """

        :param master: (its the Canvas or root) where the Button should be placed
        :param func1:  function which is to run for the rewind button
        :param func2:  function which is to run for the rewind button
        :param func3:  function which is to run for the next button
        """
        self.Button_Canvas = Ctk.CCanvas(master=master, bg=master['background'], size=(300, 30), corners='angular')

        self.button_list = list()
        self.add_buttons(func1, func2, func3)

    def add_buttons(self, func1, func2, func3):
        """

        :param func1: function which is to run for the rewind button
        :param func2: function which is to run for the rewind button
        :param func3: function which is to run for the next button
            -> function which add the buttons to the Button Canvas
        """
        funcs = [func1, func2, func3]
        button_images = ['images/rewind_button.png', 'images/pause_button.png', 'images/next_button.png']
        x = 0
        for func, image in zip(funcs, button_images):
            button = Ctk.CButton(master=self.Button_Canvas, bg=self.Button_Canvas['background'],
                                 highlight_color=self.Button_Canvas['background'],
                                 pressing_color=self.Button_Canvas['background'], width=90, height=36,
                                 image=(image, 'angular', (42, 15), (25, 25)),
                                 command=lambda ex=func: ex())
            self.button_list.append(button)
            button.place(x=x, y=2)
            x += 100


class ActuallyMusicImageCanvas:
    """

        This function creates the Music Cover image on a Canvas

    """
    def __init__(self, master, song_name) -> None:
        """

        :param master:    master where the music image should be placed
        :param song_name: name of the song to grab the music image
        """
        self.song_path_directory = 'Songs/'
        self.Image_Canvas = Ctk.CCanvas(master=master, bg=master['background'], size=(250, 250), corners='angular')

        self.set_thumbnail_image(song_name)

    def set_thumbnail_image(self, song_name) -> None:
        """

        :param song_name: name of the song
        """
        self.Image_Canvas.create_image(corner='angular', width=240, height=223, pos=(126, 115),
                                       image_path=self.get_image(song_name))

    def set_new_image(self, song_name) -> None:
        """

        :param song_name: name of the song
            -> set the new song image
        """
        self.Image_Canvas.delete('all')
        self.set_thumbnail_image(song_name)

    def get_image(self, song_name) -> str:
        """

        :param song_name: name of the song
        :return: the path of the song cover image
        """
        image_path = self.song_path_directory + song_name + '/song_cover.jpg'

        return image_path


class MusicTitleCanvas:
    """

       Create the tile of the song in form of a Ctkinter Animated Text

    """
    def __init__(self, master, song_name) -> None:
        """

        :param master:    master is the object where the Title should be placed
        :param song_name: name of the song (text of the song label)
        """
        song_name = Encode_umlauts(song_name).headless_encode()
        self.Title_Canvas = Ctk.CCanvas(master=master, bg=master['background'], size=(400, 50), corners='angular')

        self._song_title_label = Ctk.TextAnimation(master=self.Title_Canvas.get_canvas(),
                                                   bg=self.Title_Canvas['background'],
                                                   size=(280, 48), text=song_name, font=('Helvetica', 14), fg='black',
                                                   label_place=(2, 7), text_space=30, test_delay=77)

        self._song_title_label.animated_text.place(x=5, y=1)

    def config_text(self, new_text) -> None:
        """

        :param new_text: change the text to new next (old_text -> new_text)
        :return:
        """
        new_text = Encode_umlauts(new_text).headless_encode()
        self._song_title_label.change_text(new_text)

    def start_animation(self) -> None:
        """

            -> Start the animation when a new song is selected

        """
        self._song_title_label.manual_start()


class MediaObjectCanvas:
    """

        -> Canvas to place the songs on it (it is a CScrollWidget)

    """
    def __init__(self, master, song_control, song_cover_control, title_control, song_directory='Songs/',
                 playlist=None) -> None:
        """

        :param master:             is where the Canvas should be placed
        :param song_control:       control for the song to rewind, pause and next playing
        :param song_cover_control: control to change the song cover image
        :param title_control:      control to change the title of the actually song
        :param song_directory:     directory of the songs to load
        :param playlist:           this is None or a string which contains the path to the text file with the song
                                   directory names
        """
        # this is the path to a text document, where the absolut path of the song directories is stored (line per line)
        self.playlist = playlist
        self.actually_song_index = None
        self.last_song_name_label = None
        self.song_name_label_list = list()
        self.song_control = song_control
        self.song_cover_control = song_cover_control
        self.title_control = title_control

        self.__SONG__DIRECTORY__ = song_directory
        __bg = 'gray25'
        self.song_directories = self._get_all_songs()

        self.media_object_canvas = Ctk.CCanvas(master=master, bg=__bg, size=(310, 310), corners='rounded', max_rad=40)

        # create ScrollCanvas on media_object_canvas
        self._scroll_widget = Ctk.CScrollWidget(master=self.media_object_canvas.get_canvas(), width=295, height=295,
                                                bg=__bg)
        self._scroll_widget.place(x=10, y=10)
        # threading.Thread(target=self._place_songs_on_canvas).start()  # there is some issue
        self._place_songs_on_canvas()

    def _get_all_songs(self) -> list:
        """

        :return: a list with the song directories
        """
        if self.playlist is not None:
            songs = open(self.playlist, 'r')
            song_directories = songs.read().split('\n')
            songs.close()
            return song_directories

        song_directories = glob.glob(self.__SONG__DIRECTORY__ + '*/')

        return song_directories

    def _start_song(self, song_index) -> None:
        """

        :param song_index: index of the song in the song directory list
            -> start the song
        """
        self.song_control.thread_for_next_song_jump(None, None).kill()
        self.actually_song_index = song_index
        if self.last_song_name_label is not None:
            self.last_song_name_label.config(fg='white')
        try:
            song_path = self.song_directories[song_index] + '/' + \
                        Encode_umlauts(self.song_directories[song_index].split('\\')[1]).encode() + '.mp3'
        except IndexError:
            song_index = 0
            self.actually_song_index = song_index
            song_path = self.song_directories[song_index] + '/' + \
                        Encode_umlauts(self.song_directories[song_index].split('\\')[1]).encode() + '.mp3'

        self.last_song_name_label = self.song_name_label_list[song_index]
        self.song_name_label_list[song_index].config(fg='blue2')

        self.song_control.play_music_file(song_path, self.next_song, self.media_object_canvas)
        self.song_cover_control.set_new_image(self.song_directories[song_index].split('\\')[1])
        self.title_control.config_text(self.song_directories[song_index].split('\\')[1])

        self.title_control.start_animation()

    def next_song(self) -> None:
        """

            -> start the next song in the song directory list

        """
        if self.actually_song_index is None:
            return
        index = self.actually_song_index + 1
        self._start_song(index)

    def last_song(self) -> None:
        """

            -> start the rewind song in the song directory list

        """
        if self.actually_song_index is None:
            return
        index = self.actually_song_index - 1
        self._start_song(index)

    def _place_songs_on_canvas(self) -> None:
        """

            -> place the songs on the Ctkinter CScrollWidget

        """
        for song_counter, song_path in enumerate(self.song_directories):
            media_button = Ctk.CButton(master=self._scroll_widget.get_master_for_placing_objects(),
                                       bg='gray20', highlight_color='gray30', pressing_color='gray15', width=285,
                                       height=32, rounded_corners='rounded',
                                       command=lambda cnt=song_counter: self._start_song(cnt))

            song_cover_image_path = Encode_umlauts(song_path + '\\song_cover.jpg').encode()
            song_cover_canvas = Ctk.CCanvas(master=media_button, bg=media_button['background'], size=(25, 25),
                                            corners='angular')
            song_cover_canvas.create_image(corner='round', width=38, height=38, pos=(12, 12),
                                           image_path=song_cover_image_path)
            song_cover_canvas.place(x=10, y=4)
            media_button.set_button_atributes(song_cover_canvas.get_canvas(), song_cover_canvas.outline)
            song_name = song_path.split('\\')[1]
            song_name = Encode_umlauts(song_name).headless_encode()
            song_name_label = Ctk.CLabel(master=media_button, bg=media_button['background'], size=(230, 25),
                                         text=song_name, fg='white', font=('Helvetica', 12, 'bold'), corner='angular',
                                         anchor='NW', text_place=(3, 5))
            song_name_label.place(x=45, y=2)
            self.song_name_label_list.append(song_name_label)
            media_button.set_button_atributes(song_name_label.get_canvas(), song_cover_canvas.outline)

            media_button.grid(column=0, row=song_counter, padx=5, pady=0)
