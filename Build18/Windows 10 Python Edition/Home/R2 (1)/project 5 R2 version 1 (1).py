#i have to get this done, i will work on this project
#over the summer of 2018
#this program is modeled to look like windows 10, and act
#as the most possibly stripped down, but decent version
#of windows 10, other than *shudders* windows 10 S
#so far, it is looking GREAT!
#althought, it will take a while to add all the planned features...

#reset build 01
import simplegui
import simplemap


#future objects being added in, will appear later in the project

#desktop wallpaper
backdrop = object

#desktop cursor - this might be hard to make, and i don't 
#know if it still qualifies as an animation, as the user
#can move it around, and it can click and open programs
cursor = object

#recycle bin is openable, and contains: 
recycle_bin_shortcut_icon = object

#recycle bin contains: important_files.zip
recycle_bin_window = object

#opens the file explorer, but since this is a parody 
#and thousands of poor windows parodies exist
#it will actually open something, because this is a 
#windows 10 flash demo now, but it isn't flash, as it
#is made in python
file_explorer_shortcut_icon = object

#this is going to be a LEGIT® windows parody, not just
#a poorly made flash animation from 2005
file_explorer_window = object

#within the file explorer: in quick access tab, file is
#also openable, as this is a LEGIT® windows parody
#this button closes all windows, since there is no
#way to put files on this, because there is no virtual
#hard disk, and i can't add an entire window with stuff
#that is already on a perfectly good desktop screen
desktop_quick_access_button = object

#within the file explorer: in quick access tab, file is
#also openable, as this is a LEGIT® windows parody
#this will lead to your downloads folder, which will contan
#the next 3 objects i am going to define
downloads_quick_access_button = object

#within the file explorer: in downloads tab, file is
#also openable, as this is a LEGIT® windows parody
#this file just causes a bluescreen, since this is a 
#fake virtual virus that isn't in a virtual machine
#object 1 of 3 of the downloads directory
auto_execute_dot_bat_shortcut_icon = object

#within the file explorer: in downloads tab, file is
#also openable, as this is a LEGIT® windows parody
#this file deletes all web browsers, and you can get
#them back if you restart
#object 2 of 3 of the downloads directory
web_killer_dot_exe_shortcut_icon = object

#within the file explorer: in downloads tab, file is
#also openable, as this is a LEGIT® windows parody
#this file will give you a blue screen, as a lesson
#to people in the world who actually fall for this
#object 3 of 3 of the downloads directory
youtube_dot_com_dot_ink_dot_exe_shortcut_icon = object

#within the file explorer: in quick access tab, file is
#also openable, as this is a LEGIT® windows parody
#this button opens a document panel full of corrupt 
#documents, that when opened, will just cause an error
#message to come up, to teach people about file extensions
documents_quick_access_button = object

#this will bring up the window for the previously defined 
#program/object
documents_window = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 1 of 4 of the documents directory
the_first_meme_dot_rtff = object

#the error message for the previous object
error_corrupt_file_extension_error_window = object 

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 2 of 4 of the documents directory
nyan_cat_documentary_dot_pdfx = object

#the error message for the previous object
error_corrupt_file_extension_error_window = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 3 of 4 of the documents directory
the_perfect_windows_parody_dot_word = object

#the error message for the previous object
error_corrupt_file_extension_error_window = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 4 of 4 of the documents directory
a_brief_history_of_my_life_dot_html5 = object

#the error message for the previous object
error_corrupt_file_extension_error_window = object

#within the file explorer: in quick access tab, file is
#also openable, as this is a LEGIT® windows parody
#this button opens a picture panel full of corrupt 
#picture, that when opened, will just cause an error
#message to come up, to teach people about file extensions
pictures_quick_access_button = object

#this will bring up the window for the previously defined 
#program/object
pictures_window = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 1 of 6 of the pictures directory
bill_gates_dot_heif = object

#the error message for the previous object
error_heif_file_extension_is_not_supported_error_window = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 2 of 6 of the pictures directory
firefly_dot_picture = object

#the error message for the previous object
error_file_extension_is_not_supported_error_window = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 3 of 6 of the pictures directory
tropical_island_four_k_animated_dot_giphy = object

#the error message for the previous object
error_file_extension_is_not_supported_error_window = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 4 of 6 of the pictures directory
windows_logo_dot_bitmap = object

#the error message for the previous object
error_file_extension_is_not_supported_error_window = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 5 of 6 of the pictures directory
political_ad_dot_poster = object

#the error message for the previous object
error_file_extension_is_not_supported_error_window = object

#just brings up an error message, but isn't lazy, so it
#doesn't just close the current window, like most
#windows parodies from 2002-2009
#object 6 of 6 of the pictures directory
my_dog_dot_jpeg2000 = object

#the error message for the previous object
error_file_extension_is_not_supported_error_window = object

#the my computer icon, but it opens up quick access, as there are no
#files i can put onto this fake system
my_computer_shortcut_icon = object

#microsoft edge web browser, since the internet explorer joke is
#outdated. This cannot search, because that is the one thing i 
#don't know how to program. Maybe in the future, someone can
#reprogram it, and do some funny creative stuff
microsoft_edge_shortcut_icon = object

#the microsoft edge window that does nothing
microsoft_edge_new_tab = object

#the taskbar, cannot be interacted with, just a famous
#windows overlay that does stuff, but cannot do stuff 
#here since this is a windows "demo"
taskbar = object

#Microsoft was really lazy with the window 10 start button compared
#to windows Vista or windows 7, so i decided to do something creative
#when you hover over it (it changes to the modern microsoft logo)
start_button = object

#the network doesn't work correctly, but you can still run web browsers
#but can't search (fits perfectly) this idea has been tested in my windows
#xp virtual machine
network_shortcut_icon = object

#error for network
network_cannot_be_found_error = object

#opens up microsoft edge, then crashes, because "HA HA FUNNE MECROSAFT JOEK XD"
google_chrome_shortcut_icon = object

#crash like described
google_chrome_is_not_supported_get_edgy_and_try_edge_error = object

#since there is no files, it will be honest with you. it will open up a window
#to tell you about it
my_files_shortcut_icon = object

#what i just previously explained
no_files_cannot_be_placed_because_this_is_a_demo_error = object

#bonzi buddy joke, since its still 2016, right?
cortana_shortcut_icon = object

#what i just explained
bonzi_buddy_message_window = object

#the task view button doesn't work either, since this is just a demo
task_view_shortcut_icon = object

#what i told you, with a slight joke
we_cannot_view_your_tasks_because_we_are_not_you_and_it_is_not_supported_in_the_demo_message = object

#so many overprice jokes have been made, and it is too hard to reprogram office
#with the ability of no user typing, and limited assets, so it just
microsoft_word_2019_shortcut_icon = object

#so many overprice jokes have been made, and it is too hard to reprogram office
#with the ability of no user typing, and limited assets, so it just
microsoft_powerpoint_2019_shortcut_icon = object

#so many overprice jokes have been made, and it is too hard to reprogram office
#with the ability of no user typing, and limited assets, so it just
microsoft_excel_2019_shortcut_icon = object

#so many overprice jokes have been made, and it is too hard to reprogram office
#with the ability of no user typing, and limited assets, so it just
microsoft_access_2019_shortcut_icon = object

#crashes, because i don't know how to use hyper-v and i have to keep it funny
#for people who aren't tech savvy like me
hyper_v_shortcut_icon = object

#what i just told you, however i couldn't think of a decent joke
we_are_too_hyper_v_error = object

#restarts the program, since it was made in python 3
python_3_shortcut_icon = object

#only shows the english language, just as a joke
character_map_shortcut_icon = object

#the window for the character map
character_map_window = object

#oh no! i didn't update to paint 3d, gotta make another MS-PAINT joke...
MS_PAINT_shortcut_icon = object

#too many have been made and all are unoriginal (not really)
sorry_but_MS_Paint_is_too_professional_for_you_error = object

#Microsoft store, eh i don't know, i haven't had a good experience with it
#and most parodies from 2002-2009 make jokes about stuff they don't have
#a good experience with, so i guess i have to too
microsoft_store_shortcut_icon = object

#the terrible joke
credit_card_dot_exe_has_stopped_working = object


vlc_media_player_shortcut_icon = object
windows_defender_shortcut_icon = object
notepad_shortcut_icon = object
windows_movie_maker_2_6 = object
virtualbox_shortcut_icon = object
mozilla_firefox_shortcut_icon = object
minesweeper_shortcut_icon = object
three_d_pinball_shortcut_icon = object
bsod = object
snipping_tool_shortcut_icon = object

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
    
    

frame = simplegui.create_frame('Testing', 100, 100)
frame.set_draw_handler(draw_handler)
frame.start()    
frame = simplegui.create_frame('Project 5: Animation - Alpha 1 (python) ', 1670, 850)
frame.set_canvas_background("Grey")
frame.set_draw_handler(draw_handler)
frame.start()
print ("This program has been reset, since development was taking too long, ")
print ("and i wasn't getting much done. I am redoing the code, as i have finally")
print ("found a working module to work with that is easier for me to interpret")
print ("200+ lines of code have been removed, but remain available in the 10 older versions")
print ("===================================================================================")
print ("System: The program is now fully functional but can't do much yet")
print ("System:(solid grey background, with more shapes and colors)")
print ("System: now in 850p quality! (custom quality) ")
print ("Program: Quality: 1670x850")
print ("Program: Programmed with: Python 3.x")
print ("Program: Color mode: RGB")
print ("Program: Version: 9.1")
def draw (canvas):
    global x
    x = x + 10

    canvas.draw_circle("black"(x,x), 250, 250, yellow, red)
                         
                         
