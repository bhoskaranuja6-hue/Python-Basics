# 1) print twinkle twinkle little star poem
import pip


print("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
Then the traveller in the dark,
Thanks you for your tiny spark;
He could not see which way to go,
If you did not twinkle so.
In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye,
Till the sun is in the sky.
As your bright and tiny spark
Lights the traveller in the dark,
Though I know not what you are,
Twinkle, twinkle, little star""")

# 2) use REPL and print the table of 5
# done in terminal

# 3) install external module and use it perform an operation of your interest
import pyttsx3
engine = pyttsx3.init()
# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female


