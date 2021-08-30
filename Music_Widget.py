"""

    Class to create a whole Music Player Widget in form of a tkinter Canvas

"""

import Music_Widget_objects
import Ctkinter as Ctk
import tkinter as tk
import play_music


__date__ = '06.08.2021'
__completed__ = '11.08.2021'
__work_time__ = 'about 5 Hours'
__author__ = 'Christof Haidegger'
__version__ = '1.0'
__licence__ = 'Common Licence'
__debugging__ = 'Christof Haidegger'


class MusicPlayerWidget:
    """

        Class to create the Music Player Widget with all of its functionality

    """

    media_object_canvas = None
    music_player_widget = None
    thumbnail_image = None
    last_playlist = None
    song_title = None

    def __init__(self, master):
        """

        :param master:  object, where the MusicPlay is on
        """

        self._music_control = play_music

        if master is not None:
            type(self).music_player_widget = Ctk.CCanvas(master=master, bg='gray30', size=(650, 335), corners='rounded',
                                                         max_rad=40)
            self._place_objects()

    def start_new_playlist(self, playlist_path, shuffle=False):
        """

            -> Start the new Playlist on the Music object

        :param shuffle: if the Playlist should be run in shuffle mode this param would be True
        :param playlist_path: path to the new playlist
        """
        type(self).last_playlist = playlist_path

        if playlist_path is not None:
            play_list_name = playlist_path.split('\\')[-2]
            type(self).song_title.config_text('Playlist: ' + play_list_name)
            cover_path = '/'.join(playlist_path.split('\\')[0: len(playlist_path.split('\\')) - 1]) + '/thump.gif'
            type(self).thumbnail_image.set_new_gif(cover_path)

        else:
            type(self).song_title.config_text('Playlist: ' + 'All Songs')
            type(self).thumbnail_image.set_new_gif('images/fun.gif')

        type(self).media_object_canvas.media_object_canvas.destroy()

        type(self).media_object_canvas = Music_Widget_objects.MediaObjectCanvas(type(self).music_player_widget,
                                                                                self._music_control,
                                                                                type(self).thumbnail_image,
                                                                                type(self).song_title,
                                                                                playlist=playlist_path, _random=shuffle)
        type(self).media_object_canvas.media_object_canvas.place(x=330, y=15)

    def shuffle_playlist_button(self):
        shuffle_button = Ctk.CButton(master=type(self).music_player_widget,
                                     bg=type(self).music_player_widget['background'],
                                     highlight_color=type(self).music_player_widget['background'],
                                     pressing_color=type(self).music_player_widget['background'], width=30, height=30,
                                     image=('images/shuffle.png', 'angular', (15, 15), (30, 30)),
                                     command=lambda: self.start_new_playlist(type(self).last_playlist, True))

        shuffle_button.place(x=290, y=20)

    def _place_objects(self):
        """

        :return: place the objects of the Music Player
        """

        type(self).thumbnail_image = Music_Widget_objects.ActuallyMusicImageCanvas(type(self).music_player_widget, None)
        type(self).thumbnail_image.set_thumbnail_gif('images/fun.gif')
        type(self).thumbnail_image.Image_Canvas.place(x=30, y=20)

        type(self).song_title = Music_Widget_objects.MusicTitleCanvas(type(self).music_player_widget,
                                                                      song_name='Playlist: All Songs', delay=30)
        type(self).song_title.Title_Canvas.place(x=10, y=250)

        type(self).media_object_canvas = Music_Widget_objects.MediaObjectCanvas(type(self).music_player_widget,
                                                                                self._music_control,
                                                                                type(self).thumbnail_image,
                                                                                type(self).song_title,
                                                                                playlist=None)
        type(self).media_object_canvas.media_object_canvas.place(x=330, y=15)

        button_canvas = Music_Widget_objects.ButtonCanvas(type(self).music_player_widget,
                                                          type(self).media_object_canvas.last_song,
                                                          self._music_control.pause_music,
                                                          type(self).media_object_canvas.next_song)
        button_canvas.Button_Canvas.place(x=13, y=292)

        self.shuffle_playlist_button()


def main() -> int:
    """

        -> This is just to test the Media Player Software

    :return: int 0
    """

    root = tk.Tk()
    root.title('Media Player Test')
    media_player = MusicPlayerWidget(root)
    media_player.music_player_widget.pack(pady=20, padx=20)

    root.mainloop()

    return 0


if __name__ == '__main__':
    main()
