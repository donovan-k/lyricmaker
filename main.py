##Donovan Kitten
##Lryic maker
##I thought of this code. INCLUDE THIS IN CODE IF USING USING.
import random

def opener(f): #opens file based on choice of genre
  f = genre + '.txt'
  f = open(f)
  return f

print('This is a lyric maker. You select which genre you want and a randomized set of words based on the genre is generated.\n')
d = 1 #while loop variable for picking genre

while d == 1:
  genre = input('Enter the genre you want (rap, rock, pop, or country: ')
  if (genre == 'rap') or (genre == 'rock') or (genre == 'pop') or (genre == 'country'):
    d = 0
  else:
    print('Please enter one of the specified genres')

f = opener(genre)
lines = f.read().split(' ')
num = len(lines)
f.close()
n = random.randint(0,num)
w = open('newSong.txt', 'w')
for i in range(0,169):  
  n = random.randint(0,num)
  w.write(lines[n-1])
  w.write(' ')

w.close()
