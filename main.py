# To find any note on the guitar REALLY FAST (if you're a programmer who can do simple modular arithmetic in their head), then simply learn this algorithm in your head.
# The maths comes from https://sunilchebolu.wordpress.com/2014/11/14/a-formula-for-finding-notes-on-a-guitar-fretboard/

# First you need to commit to memorising some VERY VERY basic stuff about the guitar.

#1: Memorise this dictionary of number to note (this quizlet might help): 

note_num_mappings = {
    0: 'E',
    1: 'F',
    2: 'F#',
    3: 'G',
    4: 'G#',
    5: 'A',
    6: 'A#',
    7: 'B',
    8: 'C',
    9: 'C#',
    10: 'D',
    11: 'D#'
}

#2: Memorise this dictionary of string number to number of semitones offset from 6th string:

string_num_offset = {
    6: 0,
    5: 5,
    4: 10,
    3: 15,
    2: 19,
    1: 0
} #key is string number and value is offset (in number of semitones) from the 6th string


# Now that you have these dictionaries memorised, define these two variables to whatever fret/string number combination you want the note name for...

fret_num = 5 
string_num = 2

#...and just plug into the simple equation (which you need to be good at doing in your head, it's very simple though with a bit of practice...):

result_note_num = (fret_num + string_num_offset[string_num]) % 12

#...and translate back to notes to get your result
result_note = note_num_mappings[result_note_num]
print('The result note is ' + result_note)

