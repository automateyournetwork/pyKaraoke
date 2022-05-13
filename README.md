# pyKaraoke - Use the musixmatch API to transform songs into Google Text-to-Speech

## Getting Started with karegoogle

### Get a Developer Account on MusixMatch
https://developer.musixmatch.com/
### Get an API Key

### Installing the bot
To install the bot there are a few simple steps:
#### Setup a virtual environment
##### Ubuntu Linux 
###### The following instructions are based on Windows WSL2 and Ubuntu however any flavour of Linux will work with possibly slightly different commands.

##### Confirm Python 3 is installed

#####
```console

$ python3 -V
Python 3.9.10

```

##### Create and activate a virtual environment

#####
```console

$ sudo apt install python3-venv
$ python3 -m venv karaoke
$ source karaoke/bin/activate
(karaoke)$

```
#### Install the bot
```console

(message_room)$pip install pykaraoke

```
### Windows

#### Confirm Python 3.9 is installed
##### [Download Python](https://python.org)
#### Create and activate a virtual environment
#####
```console

C:\>python3 -m venv karaoke
C:\>karaoke\Scripts\activate
(pykaraoke) C:\>

```
#### Install the requirements
```console

(message_room)$pip install pykaraoke

```

### Using the bot
#### Run the bot as an interactive session
```console

(karaoke)$ pykaraoke

```
#### The form questions:

##### Question 1 - API Token

##### Question 2 - Arist Name

##### Question 3 - Song Title


#### Environment variables

Every question can be stored as a variable in the environment. This is useful if you want to reuse the same question in multiple messages.

Linux:
export TOKEN=<your token>
export ARTIST=<artist name>
export SONG=<song title>

Windows:
set TOKEN=<your token>
set ARTIST=<artist name>
set SONG=<song title>