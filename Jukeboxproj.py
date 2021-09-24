# Author: Ryan Mera
# Date: 4/20/2021
# Description: Project 3




def printMenu():

  input("Press m for Menu: ")

  done = False
  while done == False:
    print("-----------------")
    print("(L)oad Catalog")
    print("(S)earch catalog")
    print("(A)nalyse catalog")
    print("(P)rint catalog")
    print("(Q)uit catalog")
    print("-----------------")
    question = input("")


    #Loads the selected file into getListFromFile
    if question == "L":
      loadCatalog = input('Select a File from the catalog: (1) Dream Theater, ')

      if loadCatalog == '1':
        album = getListFromFile("SongDT.csv")
        print(' ')
        print('Loaded: Dream Theater')

        done = False

    #Searches using user input Query word and returns total result number
    elif question == "S":
      print(' ')
      queryFile = input('Please enter your search Query: ')
      print(' ')
      findSong(album,queryFile)
      done = False

    #Prints catalog stats for the selected CSV
    elif question == "A":
      printCatalogStats(album)

      done = False

    #Prints list of songs
    elif question == "P":
      printAlbum(album)
      done = False

    #Quits the program
    elif question == "Q":
      print("Exiting the program")
      done = True
    
    #Keeps the loop going if an invalid option is selected
    else:
      print("Please select a valid input")
      done = False

#--------------------------------------------------

def getListFromFile (inputFile):

    outputList = []

    try:

        source = open(inputFile,"r", encoding="utf-8")

        outputList =  source.readlines()

        source.close()

    except FileNotFoundError:

        print("Unable to open input file: " + inputFile)

    return outputList


#------------------------

#Formats the Apostrophes off of listofSongs using res then splits that by commas. Then uses an index for band/album/song/duration and skips 4 for every print
def songFormat(track):

    y = track.split(",")
    artist = y[0]
    album = y[1]
    title = y[2]
    runtime = y[3]
    
    integer_runtime = int(runtime)
    minutes = int((integer_runtime) / 60)
    seconds = int(((integer_runtime) / 60 - int(minutes))*60)
    
    print()
    print("------------------------------")
    print("Artist: "+artist)
    print("Album: "+album)
    print("Title: "+title)
    print("Runtime(s): "+"{:02d}:{:02d}".format(minutes,seconds))

def printAlbum(songList):

    for item in songList:

        songFormat(item)

#Prints songs using the above format function 

#------------

#Finds a queried word in songQuery and adds 1 to results for each matching word
def findSong(queryList, songQuery):

    #Variables for findSongs

    results = 0


    #Adds 1 to results for each matching word
    for item in queryList:

      if songQuery in item:
        
        results+=1
      
      else:

        continue

    
    print(' ')
    print('Matching: '+str(results))

#Function to generate csv statistics for a band/album/song/runtime
def printCatalogStats(songList):
    
    artist_num = []
    album_num = []
    title_num = []
    playtime_num = 0
    
    for song in songList:
        y = song.split(",")
        artist = y[0]
        album = y[1]
        title = y[2]
        runtime = y[3]

        if artist not in artist_num:
            artist_num.append(artist)

        if album not in album_num:
            album_num.append(album)

        if title not in title_num:
            title_num.append(title)

        playtime_num = playtime_num + int(runtime)
        
    total_artist = len(artist_num)
    total_album = len(album_num)
    total_title = len (title_num)
    total_runtime = playtime_num

    print("Catalog Statistics:")
    print("Number of Artists: " + str(total_artist))
    print("Number of Albums: " + str(total_album))
    print("Number of Songs: " + str(total_title))
    print("Catalog Playtime: " + str(total_runtime) + " seconds")
    print("------------------------------")
    
    


songList = 'songdt.csv'
songFix = getListFromFile(songList)

begin = "x"

printMenu()
