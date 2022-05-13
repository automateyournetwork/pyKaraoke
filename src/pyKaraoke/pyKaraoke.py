import sys
import rich_click as click
import json
import webbrowser
from jinja2 import Environment, FileSystemLoader
from musixmatch import Musixmatch
from pathlib import Path
from gtts import gTTS
from rich import print
# -------------------------
# Jinja2
# -------------------------

from jinja2 import Environment, FileSystemLoader
template_dir = Path(__file__).resolve().parent
env = Environment(loader=FileSystemLoader(template_dir))
class GetJson():
    def __init__(self,
        token,
        artist,
        title,
        ):

        self.token = token
        self.artist = artist
        self.title = title

    def create_song(self):
        musixmatch  = Musixmatch(self.token)
        artist =  self.artist
        title = self.title
        language = 'en-US'
        get_lyrics = musixmatch.matcher_lyrics_get(title, artist)
        if get_lyrics['message']['body']['lyrics']['lyrics_copyright'] != "Unfortunately we're not authorized to show these lyrics.":
            lyrics = get_lyrics['message']['body']['lyrics']['lyrics_body']
        else: 
            lyrics = "Unfortunately we're not authorized to sing these lyrics due to copyrights."
        print (lyrics)
        template_dir = Path(__file__).resolve().parent
        env = Environment(loader=FileSystemLoader(str(template_dir)))
        mp3_template = env.get_template('song.j2')
        mp3_output = mp3_template.render(artist = artist,
            title = title,
            lyrics = lyrics)
        print(mp3_output)
        mp3 = gTTS(text = mp3_output, lang=language)
        #Save MP3
        mp3.save(f'{self.artist}_{self.title}.mp3')
        click.secho(
          f"MP3 file created at { sys.path[0] }/{self.artist}_{self.title}.mp3",
            fg='green')
        webbrowser.open(f"{self.artist}_{self.title}.mp3")                  

@click.command()
@click.option('--token',
    prompt='API Token',
    help='Type in your musixmatch token',
    required=True, envvar="TOKEN")
@click.option('--artist',
    prompt='Song Artist',
    help='Song Artist',
    required=True, envvar="ARTIST")
@click.option('--title',
    prompt='Song Title',
    help='Song Title',
    required=True, envvar="TITLE")
    
def cli(token,artist,title):
    invoke_class = GetJson(token,artist,title)
    invoke_class.create_song()

if __name__ == "__main__":
    cli()
