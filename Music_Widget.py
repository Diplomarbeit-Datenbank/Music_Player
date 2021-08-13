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
    def __init__(self, master):
        """

        :param master:  object, where the MusicPlay is on
        """

        self._music_control = play_music
        self.music_player_widget = Ctk.CCanvas(master=master, bg='gray30', size=(650, 335), corners='rounded',
                                               max_rad=40)

        self._place_objects()

    def _place_objects(self):
        """

        :return: place the objects of the Music Player
        """
        thumbnail_image = Music_Widget_objects.\
            ActuallyMusicImageCanvas(self.music_player_widget,
                                     song_name='Ava Max - Sweet but Psycho (Lyrics)')
        thumbnail_image.Image_Canvas.place(x=30, y=20)

        song_title = Music_Widget_objects.MusicTitleCanvas(self.music_player_widget,
                                                           song_name='Ava Max - Sweet but Psycho (Lyrics)')
        song_title.Title_Canvas.place(x=10, y=250)

        media_object_canvas = Music_Widget_objects.MediaObjectCanvas(self.music_player_widget, self._music_control,
                                                                     thumbnail_image, song_title)
        media_object_canvas.media_object_canvas.place(x=330, y=15)

        button_canvas = Music_Widget_objects.ButtonCanvas(self.music_player_widget,
                                                          media_object_canvas.last_song,
                                                          self._music_control.pause_music,
                                                          media_object_canvas.next_song)
        button_canvas.Button_Canvas.place(x=13, y=292)


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
