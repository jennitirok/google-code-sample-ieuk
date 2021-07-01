"""A video player class."""

from .video_library import VideoLibrary
from random import randint


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.is_playing = False
        self.currently_playing = ""
        self.currently_playing_id = ""
        self.is_paused = False
        self.playlists = []

    def get_video_details(self, id):
        video = self._video_library.get_video(id)
        # Formatting how the tags needs to be displayed
        tags = "["
        for tag in video.tags:
            tags += tag + " "
        tags += "]"

        # Check if there are tags available
        if tags != "[]":
            tags = tags[0:len(tags) - 2] + "]"

        details = video.title + " (" + video.video_id + ") " + tags
        return details

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        video_list = []
        all_videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")

        for video in all_videos:
            detail = self.get_video_details(video.video_id)
            video_list += [detail]

        # Sort the titles
        video_list.sort()
        for video in video_list:
            print(video)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        all_videos = self._video_library.get_all_videos()
        ids = []
        for video in all_videos:
            ids.append(video.video_id)

        # Check if the video exists
        if video_id not in ids:
            print("Cannot play video: Video does not exist")
        else:
            for video in all_videos:
                if video_id == video.video_id:
                    # Check if there is a video playing
                    if self.is_playing == False:
                        print("Playing video: {}".format(video.title))
                        self.currently_playing = video.title
                        self.currently_playing_id = video.video_id
                        self.is_playing = True
                    elif self.is_playing == True:
                        print("Stopping video: {}".format(self.currently_playing))
                        print("Playing video: {}".format(video.title))
                        self.currently_playing = video.title
                        self.currently_playing_id = video.video_id
                        self.is_paused = False

    def stop_video(self):
        """Stops the current video."""

        # Check if there is a video playing
        if self.is_playing == True:
            print("Stopping video: {}".format(self.currently_playing))
            self.is_playing = False
            self.currently_playing = ""
            self.currently_playing_id = ""
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        all_videos = self._video_library.get_all_videos()
        ids = []
        for video in all_videos:
            ids.append(video.video_id)

        # Generate random integer for random video to be played
        random_video_id = ids[randint(0,4)]
        random_video = self._video_library.get_video(random_video_id)
        if self.is_playing == False:
            print("Playing video: {}".format(random_video.title))
            self.currently_playing = random_video.title
            self.currently_playing_id = random_video_id
            self.is_playing = True
        elif self.is_playing == True:
            print("Stopping video: {}".format(self.currently_playing))
            print("Playing video: {}".format(random_video.title))
            self.currently_playing = random_video.title
            self.currently_playing_id = random_video_id

    def pause_video(self):
        """Pauses the current video."""

        if (self.is_paused == False) and (self.is_playing == False):
            print("Cannot pause video: No video is currently playing")
        elif (self.is_paused == False):
            print("Pausing video: {}".format(self.currently_playing))
            self.is_paused = True
        elif (self.is_paused == True):
            print("Video already paused: {}".format(self.currently_playing))

    def continue_video(self):
        """Resumes playing the current video."""

        if (self.is_paused == False) and (self.is_playing == False):
            print("Cannot continue video: No video is currently playing")
        elif (self.is_paused == False):
            print("Cannot continue video: Video is not paused")
        elif (self.is_paused == True):
            print("Continuing video: {}".format(self.currently_playing))
            self.is_paused = False

    def show_playing(self):
        """Displays video currently playing."""

        if (self.is_paused == False) and (self.is_playing == True):
            video_detail = self.get_video_details(self.currently_playing_id)
            print("Currently playing: {}".format(video_detail))
        elif (self.is_paused == True) and (self.is_playing == True):
            video_detail = self.get_video_details(self.currently_playing_id)
            print("Currently playing: {} - PAUSED".format(video_detail))
        elif (self.is_playing == False):
            print("No video is currently playing")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        name = playlist_name
        list_lower = []
        for i in range(len(self.playlists)):
            list_lower.append(self.playlists[i][0].lower)

        if playlist_name.lower() in list_lower:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlists.append([name])
            print("Successfully created new playlist: {}".format(name))

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        # lists = []
        # for i in range(len(self.playlists)):
        #     lists.append(self.playlists[i][0])
        #
        # if playlist_name not in lists:
        #     print("Cannot add video to {}: Playlist does not exist".format(playlist_name))
        # elif playlist_name in lists:
        #     video = self._video_library.get_video(video_id)
        #     # Check if video exists
        #     if video == None
        #         print("Cannot add video to {}: Video does not exist")
        #         # Check if the video has already been added
        #     else:
                index = self.playlists

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        video_list = []
        titles = []
        ids = []
        term = search_term.lower()
        all_videos = self._video_library.get_all_videos()
        for video in all_videos:
            if term in video.title.lower():
                detail = self.get_video_details(video.video_id)
                video_list += [detail]
                titles.append(video.title)
                ids.append(video.video_id)

        if video_list == []:
            print("No search results for {}".format(search_term))
        elif video_list != []:
            video_list.sort()
            titles.sort()
            print("Here are the results for {}:".format(search_term))
            for i in range(len(video_list)):
                print(str(i+1) + ") " + video_list[i])
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            ans = input("If your answer is not a valid number, we will assume it's a no.\n")
            try:
                ans_int = int(ans)
                if (ans_int >= 1) and (ans_int <= len(video_list)):
                    print("Playing video: {}".format(titles[ans_int - 1]))
                    self.is_playing = True
                    self.currently_playing = titles[ans_int - 1]
                    self.currently_playing_id = ids[ans_int - 1]
            except ValueError:
                # Handle the exception
                return

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        video_list = []
        titles = []
        ids = []
        strip_tag = video_tag.lstrip("#")
        tag = "#" + strip_tag.lower()
        all_videos = self._video_library.get_all_videos()
        for video in all_videos:
            if tag in video.tags:
                detail = self.get_video_details(video.video_id)
                video_list += [detail]
                titles.append(video.title)
                ids.append(video.video_id)

        if video_list == []:
            print("No search results for {}".format(video_tag))
        elif video_list != []:
            video_list.sort()
            titles.sort()
            print("Here are the results for {}:".format(video_tag))
            for i in range(len(video_list)):
                print(str(i + 1) + ") " + video_list[i])
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            ans = input("If your answer is not a valid number, we will assume it's a no.\n")
            try:
                ans_int = int(ans)
                if (ans_int >= 1) and (ans_int <= len(video_list)):
                    print("Playing video: {}".format(titles[ans_int - 1]))
                    self.is_playing = True
                    self.currently_playing = titles[ans_int - 1]
                    self.currently_playing_id = ids[ans_int - 1]
            except ValueError:
                # Handle the exception
                return

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")