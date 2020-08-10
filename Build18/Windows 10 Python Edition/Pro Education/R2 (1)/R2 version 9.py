#i have to get this done, i will work on this project
#over the summer of 2018
#this program is modeled to look like windows 10, and act
#as the most possibly stripped down, but decent version
#of windows 10, other than *shudders* windows 10 S
#so far, it is looking GREAT!
#althought, it will take a while to add all the planned features...
#this is the second alpha build, where i added new object descriptions, and finished up the list while being extremely unoriginal

#DEVELOPER QUESTIONS ANSWERED HERE
#*********************************************
#Question: Why did you claim to make this "a better windows parody"?
#*********************************************
#Answer: I have seen A LOT of windows Parodies made by kids from 2002-2009 on YouTube 
#Some of them reuploaded from newgrounds and other flash sites
#and there are a lot of misconceptions. They were funny at the time (to some people) but these
#days, they are so common, that they became stale. I plan on revolutionizing the idea
#*********************************************
#Question: Is this program at all helpful?
#*********************************************
#Answer: Somewhat. People are allowed to reprogram the project, which teaches programming
#and there are also some fake files located in the file explorer (9 files) that teach 
#people about fake and non-existant file formats (as of this date: 6.14.2018)
#Other than that, it is all fun and games!
#*********************************************
#Question: How long did this take to make?
#*********************************************
#Answer: This was a school project for my 10th grade programming class that i decided to
#take further development on. It was originally made on py3.codeskulptor.org as an
#assignment for animation. I think it counts as animation, since it is also interactive
#pther than movements. This took about 1-2 hours a day from May 23rd to June 8th, but
#it got remade, as there was originally no motive
#*********************************************
#Question: Is this project appropriate for kids?
#*********************************************
#Answer: Somewhat, i recommend parental guidance. Some of the jokes are [PG] (if you overthink them)
#But most likely, your kids won't get the jokes, unless they got it from somewhere else. rating: [PG]
#[E10+]
#*********************************************
#Question: Did you enjoy making this?
#*********************************************
#Answer: Yes, it was really fun, and it had a good outcome. I liked writing the jokes, and the scripts
#for this program
#*********************************************

#severe development error
#this will be really hard for me to make since:
#1: i need to find several images for this project, and put them in
#2: i have to make it functional
#3: it might require some workers to develop
#4: this may take the whole summer, as it is really advanced
#5: i cannot easily find workers for this project

#reset build 08

#import library
import simplegui
import simplemap

#Image bootloader (base64)
#Currently can't activate the code, due to issues

#>>> import base64
#>>> encoded = base64.b64encode('data to be encoded')
#>>> encoded
#'ZGF0YSB0byBiZSBlbmNvZGVk' 
#>>> data = base64.b64decode(encoded)
#>>> data
#'data to be encoded'

#future objects being added in, will appear later in the project

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the startup_sound.m4a sound, when you 
#start up the simulation past the login screen. This is not the 
#Actual Windows 10 startup sound, it is custom, but we wanted to use
#Something besides the windows 7 startup sound (the default hidden
#startup sound for windows 10)
startup_sound = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#User screen/signin screen
sign_in_screen = object

#password box (doesn't work)
password_box = object

#User icon
user_icon = object

#desktop wallpaper
backdrop = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly
#img.show()

#desktop cursor - this might be hard to make, and i don't 
#know if it still qualifies as an animation, as the user
#can move it around, and it can click and open programs
cursor = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the hardclick.m4a sound, when you hold
#Your mouse down for 0.5 seconds 
hard_click = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the double.m4a sound, when you double click
#on any object, or pixel on the screen
double_click = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#recycle bin is openable, and contains: 
recycle_bin_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#recycle bin contains: important_files.zip
recycle_bin_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#opens the file explorer, but since this is a parody 
#and thousands of poor windows parodies exist
#it will actually open something, because this is a 
#windows 10 flash demo now, but it isn't flash, as it
#is made in python
file_explorer_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly


#this is going to be a LEGIT� windows parody, not just
#a poorly made flash animation from 2005
file_explorer_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly


#within the file explorer: in quick access tab, file is
#also openable, as this is a LEGIT� windows parody
#this button closes all windows, since there is no
#way to put files on this, because there is no virtual
#hard disk, and i can't add an entire window with stuff
#that is already on a perfectly good desktop screen
desktop_quick_access_button = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly


#within the file explorer: in quick access tab, file is
#also openable, as this is a LEGIT� windows parody
#this will lead to your downloads folder, which will contan
#the next 3 objects i am going to define
downloads_quick_access_button = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly


#within the file explorer: in downloads tab, file is
#also openable, as this is a LEGIT� windows parody
#this file just causes a bluescreen, since this is a 
#fake virtual virus that isn't in a virtual machine
#object 1 of 3 of the downloads directory
auto_execute_dot_bat_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly


#within the file explorer: in downloads tab, file is
#also openable, as this is a LEGIT� windows parody
#this file deletes all web browsers, and you can get
#them back if you restart
#object 2 of 3 of the downloads directory
web_killer_dot_exe_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly


#within the file explorer: in downloads tab, file is
#also openable, as this is a LEGIT� windows parody
#this file will give you a blue screen, as a lesson
#to people in the world who actually fall for this
#object 3 of 3 of the downloads directory
youtube_dot_com_dot_ink_dot_exe_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly


#within the file explorer: in quick access tab, file is
#also openable, as this is a LEGIT� windows parody
#this button opens a document panel full of corrupt 
#documents, that when opened, will just cause an error
#message to come up, to teach people about file extensions
documents_quick_access_button = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly


#this will bring up the window for the previously defined 
#program/object
documents_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly


#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 1 of 4 of the documents directory
the_first_meme_dot_rtff = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the error message for the previous object
error_corrupt_file_extension_error_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object


#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 2 of 4 of the documents directory
nyan_cat_documentary_dot_pdfx = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly


#the error message for the previous object
error_corrupt_file_extension_error_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object


#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 3 of 4 of the documents directory
the_perfect_windows_parody_dot_word = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly


#the error message for the previous object
error_corrupt_file_extension_error_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 4 of 4 of the documents directory
a_brief_history_of_my_life_dot_html5 = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the error message for the previous object
error_corrupt_file_extension_error_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#within the file explorer: in quick access tab, file is
#also openable, as this is a LEGIT� windows parody
#this button opens a picture panel full of corrupt 
#picture, that when opened, will just cause an error
#message to come up, to teach people about file extensions
pictures_quick_access_button = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this will bring up the window for the previously defined 
#program/object
pictures_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 1 of 6 of the pictures directory
bill_gates_dot_heif = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the error message for the previous object
error_heif_file_extension_is_not_supported_error_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 2 of 6 of the pictures directory
firefly_dot_picture = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the error message for the previous object
error_file_extension_is_not_supported_error_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 3 of 6 of the pictures directory
tropical_island_four_k_animated_dot_giphy = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the error message for the previous object
error_file_extension_is_not_supported_error_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 4 of 6 of the pictures directory
windows_logo_dot_bitmap = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the error message for the previous object
error_file_extension_is_not_supported_error_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 5 of 6 of the pictures directory
political_ad_dot_poster = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the error message for the previous object
error_file_extension_is_not_supported_error_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 6 of 6 of the pictures directory
my_dog_dot_jpeg2000 = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the error message for the previous object
error_file_extension_is_not_supported_error_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#the my computer icon, but it opens up quick access, as there are no
#files i can put onto this fake system
my_computer_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#microsoft edge web browser, since the internet explorer joke is
#outdated. This cannot search, because that is the one thing i 
#don't know how to program. Maybe in the future, someone can
#reprogram it, and do some funny creative stuff
microsoft_edge_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the microsoft edge window that does nothing
microsoft_edge_new_tab = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the taskbar, cannot be interacted with, just a famous
#windows overlay that does stuff, but cannot do stuff 
#here since this is a windows "demo"
taskbar = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#Microsoft was really lazy with the window 10 start button compared
#to windows Vista or windows 7, so i decided to do something creative
#when you hover over it (it changes to the modern microsoft logo)
start_button = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#Windows 10 refined the classic start menu from Windows 7, and improved it by adding
#Tiles to the site (Windows 8, 8.1) and kept the app list, like Windows XP, Windows Vista,
#And Windows 7. This was a smart move, but the owner things that this doesn't feel like the
#Same thing. However, we are adding the start menu here, this is the script for the start menu
#Background
start_menu_bitmap = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#Power options button, this brings up the power options for Windows 10, however, in the real
#Windows 10, you can also ALT + F4 the desktop, or press CTRL + ALT + DEL to get the power
#Options as well, but this can be easy access at times
power_options_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#Restart button, the bottom option of the power options menu in Windows 10
#This function doesn't work yet, but it will restart the simulation, and bring you
#Back to the power screen
restart_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#Shutdown button, the middle option of the power options menu in Windows 10
#This function doesn't work yet, but it will shutdown the simulation, and close
#Out of the simulation, bringing you back to the launcher screen
shutdown_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#Sleep button, the top option of the power options menu in Windows 10
#This function doesn't work yet, but it will put the simulation into sleep mode
#Until you move the mouse, then it will resume (just like Windows 10 does)
sleep_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#User options button, the button that will let you switch users, or sign out, back to
#The sign-in screen
user_options_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#sign out button, the button that will let you sign out back to the
#The sign-in screen
sign_out_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#switch users button, the button that will let you sign back to the
#The sign-in screen, and switch users
switch_users_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#recently used pane, this pane shows you the apps you recently used
#This is just the pane, and it doesn't work yet, but all the apps you use
#Will show up here, with a max query of 6 apps
recent_pane = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the network doesn't work correctly, but you can still run web browsers
#but can't search (fits perfectly) this idea has been tested in my windows
#xp virtual machine
network_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#error for network
network_cannot_be_found_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#opens up microsoft edge, then crashes, because "HA HA FUNNE MECROSAFT JOEK XD"
google_chrome_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#crash like described
google_chrome_is_not_supported_get_edgy_and_try_edge_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#since there is no files, it will be honest with you. it will open up a window
#to tell you about it
my_files_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#what i just previously explained
no_files_cannot_be_placed_because_this_is_a_demo_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#bonzi buddy joke, since its still 2016, right?
cortana_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#what i just explained
bonzi_buddy_message_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#the task view button doesn't work either, since this is just a demo
task_view_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#what i told you, with a slight joke
we_cannot_view_your_tasks_because_we_are_not_you_and_it_is_not_supported_in_the_demo_message = object

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#so many overprice jokes have been made, and it is too hard to reprogram office
#with the ability of no user typing, and limited assets, so it just
microsoft_word_2019_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#so many overprice jokes have been made, and it is too hard to reprogram office
#with the ability of no user typing, and limited assets, so it just
microsoft_powerpoint_2019_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#so many overprice jokes have been made, and it is too hard to reprogram office
#with the ability of no user typing, and limited assets, so it just
microsoft_excel_2019_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#so many overprice jokes have been made, and it is too hard to reprogram office
#with the ability of no user typing, and limited assets, so it just
microsoft_access_2019_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#crashes, because i don't know how to use hyper-v and i have to keep it funny
#for people who aren't tech savvy like me
hyper_v_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#what i just told you, however i couldn't think of a decent joke
we_are_too_hyper_v_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#restarts the program, since it was made in python 3
python_3_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#only shows the english language, just as a joke
character_map_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the window for the character map
character_map_window = object

#oh no! i didn't update to paint 3d, gotta make another MS-PAINT joke...
MS_PAINT_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#too many have been made and all are unoriginal (not really)
sorry_but_MS_Paint_is_too_professional_for_you_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#Microsoft store, eh i don't know, i haven't had a good experience with it
#and most parodies from 2002-2009 make jokes about stuff they don't have
#a good experience with, so i guess i have to too
microsoft_store_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the terrible joke
credit_card_dot_exe_has_stopped_working = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#VLC is a very good video program, and i couldn't disclude it, however i don't want to make
#an animation to make it play videos, since this system is supposed to have no files (other
#than system and program files) so it will just make a default traffic joke
vlc_media_player_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the start to the joke i just told you about
vlc_media_player_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the actual joke (probably not that good)
this_traffic_cone_does_not_belong_here_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#its an important windows element, i have to use it
windows_defender_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the followup to the windows defender shortcut icon
windows_defender_main_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the "legit" scan
scanning_for_viruses_dialog_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the notify.m4a sound, the sound that is played
#when this notification message is activated
notify_sound_one = object

#the joke (since this is a parody)
memz_is_not_a_virus_you_novice_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#notepad, the classic windows program, that people use to break into school programs
notepad_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the joke
this_window_cannot_break_do_not_fork_it_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#YTP maker, the classic age of YouTube started with this program... time to trash it >:)
windows_movie_maker_2_6 = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#Because i had to do it to'em
your_video_family_photos_compilation_dot_mp4_failed_to_render_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object
    
#its a classic, but hyper-v has to be superior here
virtualbox_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#hyper-v redirect
oracle_is_not_a_windows_product_how_did_it_get_on_here_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the notify.m4a sound, the sound that is played
#when this notification message is activated
notify_sound_one = object

#mozilla firefox is nice
mozilla_firefox_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#you gotta respect the edge
redirecting_to_microsoft_edge_message = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the notify.m4a sound, the sound that is played
#when this notification message is activated
notify_sound_one = object

#classic windows game that almost no-one knew how to play
minesweeper_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#the window for it
minesweeper_really_good_game_gif_window = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#running out of ideas, sorry
failed_to_sweep_up_mines_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#another classic windows game
three_d_pinball_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#really low on ideas
the_ball_got_pinned_quitting_error = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#not that well used by pros, due to the screenshot command, but is still very helfpul at times
snipping_tool_shortcut_icon = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#we haven't referenced the historical clippy yet, he had to come in here somewhere
snippy_is_the_new_clippy_message = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the error.m4a sound, the sound that is played
#when this error message is activated
error_sound_one = object

#the blue screen of death, had to be added
bsod = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#this is a function that doesn't work yet, as it is still classified 
#as an object. This actives the shutdown_sound.m4a sound, when you 
#shut down up the simulation past. This is the actual windows 10
#shutdown sound, even though it is the windows 7 one (Microsoft 
#Reused it) (the default hidden shutdown sound for windows 10)
shutdown_sound = object
#image script (beta)
#from PIL import Image
#
#img = Image.new( 'RGB', (255,255), "black") # Create a new black image
#pixels = img.load() # Create the pixel map
#for i in range(img.size[0]):    # For every pixel:
#    for j in range(img.size[1]):
#        pixels[i,j] = (i, j, 100) # Set the colour accordingly

#This is just filler until i can get the assets loaded into the project, and emulating them properly
#It is just a bunch of shapes, this will not be in the final product
lop = int
lop == 0
#lop =#= int #random code
###
def draw_handler(canvas):
    canvas.draw_circle((100, 101), 200, 120, "Green")
    canvas.draw_circle([202, 305], 300, 120, "Red")
    canvas.draw_circle((850, 740), 200, 504, "Blue", "White")
    canvas.draw_circle([176, 802], 300, 101, "Yellow", "Orange")
    canvas.draw_circle((320, 421), 256, 128, "Black")
    canvas.draw_circle([220, 312], 496, 128, "Pink")
    canvas.draw_circle((870, 940), 418, 550, "Purple", "Black")
    canvas.draw_circle([226, 848], 350, 141, "Yellow", "Red")
    x = 5
while (lop == 0):
    import simplegui
    import simplemap
    global x
    x = x + 5
    #canvas.draw_circle((100, 101), 200, 120, "Green")
    #canvas.draw_circle([202, 305], 300, 120, "Red")
    #canvas.draw_circle((850, 740), 200, 504, "Blue", "White")
    #canvas.draw_circle([176, 802], 300, 101, "Yellow", "Orange")
    canvas.draw_circle((randint), randint, randint, "Green")
    canvas.draw_circle([randint], randint, randint, "Red")
    canvas.draw_circle((randint), randint, randint, "Blue", "White")
    canvas.draw_circle([randint], randint, randint, "Yellow", "Orange")

#another part building up to the filler bootloader
frame = simplegui.create_frame('Testing', 100, 100)
frame.set_draw_handler(draw_handler)
frame.start()    
frame = simplegui.create_frame('Windows 10 Python Edition - Alpha 8 (python) ', 1670, 850)
frame.set_canvas_background("Grey")
frame.set_draw_handler(draw_handler)
frame.start()
print ("0 [- User Output and Help Log Version 18 (june 14th 2018 build) -]")
print ("1 This program has been reset, since development was taking too long, ")
print ("2 and i wasn't getting much done. I am redoing the code, as i have finally")
print ("3 found a working module to work with that is easier for me to interpret")
print ("4 200+ lines of code have been removed, but remain available in the 10 older versions")
print ("5 ===================================================================================")
print ("6 System: The program is now fully functional but can't do much yet")
print ("7 System:(solid grey background, with more shapes and colors)")
print ("8 Still just defining all the code")
print ("9 System: now in 850p quality! (custom quality) ")
print ("10 Program: Quality: 1670x850")
print ("11 Program: Programmed with: Python 3.x")
print ("12 Program: Color mode: RGB")
print ("13 Program: Version: 9.8")
print ("14 Note: the GUI window that just loaded is just filler, that will not be in the final product")
print ("15 DEVELOPER QUESTIONS ANSWERED HERE")
print ("16 *********************************************")
print ("17 Question: Why did you claim to make this 'a better windows parody'?")
print ("18 *********************************************")
print ("19 Answer: I have seen A LOT of windows Parodies made by kids from 2002-2009 on YouTube")
print ("20 Some of them reuploaded from newgrounds and other flash sites")
print ("21 and there are a lot of misconceptions. They were funny at the time (to some people) but these")
print ("22 days, they are so common, that they became stale. I plan on revolutionizing the idea")
print ("23 *********************************************")
print ("24 Question: Is this program at all helpful?")
print ("25 *********************************************")
print ("26 Answer: Somewhat. People are allowed to reprogram the project, which teaches programming")
print ("27 and there are also some fake files located in the file explorer (9 files) that teach")
print ("28 people about fake and non-existant file formats (as of this date: 6.8.2018)")
print ("29 Other than that, it is all fun and games!")
print ("30 *********************************************")
print ("31 Question: How long did this take to make?")
print ("32 *********************************************")
print ("33 Answer: This was a school project for my 10th grade programming class that i decided to")
print ("34 take further development on. It was originally made on py3.codeskulptor.org as an")
print ("35 assignment for animation. I think it counts as animation, since it is also interactive")
print ("36 other than movements. This took about 1-2 hours a day from May 23rd to June 8th, but")
print ("37 it got remade, as there was originally no motive")
print ("38 *********************************************")
print ("39 Question: Is this project appropriate for kids?")
print ("40 *********************************************")
print ("41 Answer: Somewhat, i recommend parental guidance. Some of the jokes are [PG] (if you overthink them)")
print ("42 But most likely, your kids won't get the jokes, unless they got it from somewhere else. rating: [PG]")
print ("43 [E10+]")
print ("44 *********************************************")
print ("45 Question: Did you enjoy making this?")
print ("46 *********************************************")
print ("47 Answer: Yes, it was really fun, and it had a good outcome. I liked writing the jokes, and the scripts")
print ("48 for this program")
print ("49 *********************************************")
print ("50 This program is completely open source and i have made it easy to understand")
print ("51 If you want to develop, download the project to your computer (the .py file)")
print ("52 Then edit it with Notepad, Notepad++, Visual studio, or other scripting software")
print ("53 That is compatible with python 3")
print ("54 Please do not blantly reupload this with no changes, slight changes, removed credits")
print ("55 As plagiarism is not looked down upon nicely")
print ("56 *********************************************")
print ("57 More developer notes")
print ("58 Total lines of code 1596 (internal) outputted for user 127 (still from within the same 1596 lines of code)")
print ("59 There are some unicode characters, but they are currently undefined")
print ("60 due to an error, but if you want to fix them, the unicode character")
print ("61 is the registered trademark symbol")
print ("62 follow the comments, as they are clear and easy to understand")
print ("63 be careful editing the images, make sure you are replacing them with")
print ("64 24 bit bitmap (.bmp) files, or they won't work, unless you edit the")
print ("65 bootloader")
print ("66 also, please make sure you are experienced with python, and to have")
print ("67 an extra copy of the file available, unless you want to redownload")
print ("68 or completely change it")
print ("69 some recommended development programs")
print ("70 Notepad (comes with every version of Windows)")
print ("71 Notepad ++ (free advanced notepad software, designed for developing with")
print ("72 over a hundred different programming languages")
print ("73 Visual Studio (premium programming software from Microsoft, with a 30 day")
print ("74 free trial, after that it costs real money)")
print ("75 Python 3.6.5 (the version of python this was made with)")
print ("76 you don't HAVE TO edit this project, but if you want to, get to it!")
print ("77 update log")
print ("78 version 15")
print ("79 added update log")
print ("80 updated dates within code")
print ("81 updated user output and help log")
print ("82 Version 15.1")
print ("83 updated update log")
print ("84 updated dates within code")
print ("85 added code for new image processor, once we find the starting module")
print ("86 program is now being designed around the PIL module for the imaging (research needed)")
print ("86 it will be fully implemented")
print ("87 program is now over 1000 lines of code")
print ("88 updated user output and help log")
print ("89 now fully updated to website standards")
print ("90 downgraded version to half, the next version will go back to normal")
print ("91 program now has an official name, not just project 5 animation")
print ("92 Version 16")
print ("93 i didn't want to have such a big update so close to another big update, but i did")
print ("94 Updated update log")
print ("95 Added License pack (assets folder)")
print ("96 Added Sound System")
print ("97 Added startup sound")
print ("98 Added shutdown sound")
print ("99 Added clicking sounds")
print ("100 Added Start Menu")
print ("101 Added users")
print ("102 Added Alarm Sounds")
print ("103 Added error sounds")
print ("104 Version 17")
print ("105 Updated update log")
print ("106 added new lock screens, and wallpaper graphics")
print ("107 Version 18")
print ("108 MASSIVE UPDATE")
print ("109 name changes:")
print ("110 Since this is no longer a school project, it now says 'Windows 10 Python Edition' instead")
print ("111 of 'python project 5'")
print ("112 now contains directories for all 12 versions of windows 10")
print ("113 version list:")
print ("114 Windows 10 home")
print ("115 Windows 10 Pro")
print ("116 Windows 10 Enterprise")
print ("117 Windows 10 Education")
print ("118 Windows 10 Pro Education")
print ("119 Windows 10 Enterprise LTSB")
print ("120 Windows 10 Mobile Enterprise")
print ("121 Windows 10 Mobile")
print ("122 Windows 10 LoT")
print ("123 Windows 10 S")
print ("124 Windows 10 Team")
print ("125 Windows 10 Pro for Workstations")
print ("126 Code improvements")
def draw (canvas):
    global x
    x = x + 10

    canvas.draw_circle("black"(x,x), 250, 250, yellow, red)                  
