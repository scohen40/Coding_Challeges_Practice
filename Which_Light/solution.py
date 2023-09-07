# You are reading a digital signal coming from a light sensor connected to a pin on a microcontroller. Your job is to figure out which light has been turned on based on it's behavior.

# You are given an unsorted list of integers from 0-255 representing the light level during a period of time, where each element is the reading for 1 millisecond of time.

# There is a fair amount of random light coming in, and a distinct period of time where a light is turned on. If a light is turned on, it will be on for a period of time longer than a few milliseconds - but you're not sure how long.

# Each light has a distinct pattern of lighting up:

# Halogen lights brighten slowly after an initial jump in luminosity, and dim almost instantly, and produce more variation in light emitted

# Florecent lights brighten faster than halogen lights, produce a steadier light than halogen, and dim more slowly.

# Incandecent lights brighten nearly immediately, and dim nearly immediately, and produce a consistent amount of light

# LED lights brighten immediately, dim immediately, and produce a brighter amount of consistent light than incandecent lights


# You are also not sure how bright it is in the room to begin with, so you cannot assume there is no light in the room to start. Only that an overhead light is on or off.
# Write a function that returns which kind of light bulb has turned on, as a string (one of "halogen", "florecent", "incandecent", "LED")

## Examples
example_one = [4,4,5,5,4,3,3,4,5,77,77,77,78,79,80,81,88,90,95,100,100,110,115,135,145,158,158,190,200,200,200,200,200,150,100,60,7,8,8,8] # halogen

example_two = [4,5,8, 9, 11, 2, 3,4,5,6,5,4,5,4,100,110,115,135,145,158,158,190,200,200,200,200,200,200,200,200,190,100,90,87,80,30,25,26,27,28,29,30,30,30,30,30,30,30] # florecent

example_three = [4,4,5,5,4,3,3,4,4,4,5,5,4,3,3,4,5,100,150,200,200,200,201,201,200,201,200,199,200,200,199,201,150,4,4,5,5,4,3,3,4,9,4,4,5,5,4,3,3,4,5,] # incandecent

example_four = [4,4,5,5,4,3,3,4,4,4,5,5,4,3,3,4,5,200,200,200,200,200,200,200,200,200,200,200,200,200,4,4,5,5,4,3,3,4,9,4,4,5,5,4,3,3,4,5,] # LED

#SOLUTION 1
def which_light(readings):
  ## detect a pattern in the data
  ## something about how fast it gets bright- the important info is last number and next number
  ## detect how quickly we get from 100 to 200
  ## if we go straight to 200, its LED
  start_brightness = None
  start_brightness_plateu = None
  start_brightness_peak = None
  finish_brightness = None
  BRIGHTNESS_THRESHOLD = 65
  BRIGHTNESS_PLATEU = 99
  BRIGHTNESS_PEAK = 200
  
  
  ## go through this array, detect patterns above
  for i in range(len(readings)):
    if readings[i] > BRIGHTNESS_THRESHOLD:
      if start_brightness is None:
        start_brightness = i
      if readings[i] > BRIGHTNESS_PLATEU: 
        if start_brightness_plateu is None:
          start_brightness_plateu = i
      if readings[i] == BRIGHTNESS_PEAK:
        if start_brightness_peak is None:
          start_brightness_peak = i
  print("start brightess:", start_brightness)
  print("start_brightness_plateu:", start_brightness_plateu)
  print("start_brightness_peak:", start_brightness_peak)

  if start_brightness != start_brightness_plateu:
    return "halogen"


  if start_brightness_peak - start_brightness_plateu > 5:
    return "florecent"

  if (start_brightness_peak - start_brightness_plateu) == 0:
    return "LED"
  else:
    return "incandecent"
    
  print(start_brightness_plateu - start_brightness_peak )
  

  ## return a string (one of "halogen", "florecent", "incandecent", "LED")

#SOLUTION 2
## attack-  the length of the start of when it starts to rise, to when it reaches maximum brightness
## amplitude - the height of the wave- the "max" 
## sustain - the consistency of the max 


def which_light(readings):
  attack_begin = 0
  attack_end = 0
  ## loop over the entire list
  for index in range(len(readings)):
    reading = readings[index]
  
  ## take note when the first jump in light value appears
    if reading - readings[index-1] > 60 and attack_begin == 0:
      attack_begin = index
  
  ## keep track of how long it takes to get to 200 (length of attack)
    if reading == 200 and attack_end == 0:
      attack_end = index

  attack_length = attack_end-attack_begin

  if attack_length > 10:
    return "halogen"
  if attack_length > 5 and attack_length < 10:
    return "florecent"
  if attack_length > 0 and attack_length < 5:
    return "incandecent"
  if attack_length == 0:
    return "LED"
  ## check to see if there is "wobble" in the plateau (sustain)
  ## check the length of the "decay" (how long does it take to go from 200 to at least 30 brightness)
  return attack_begin,attack_end, attack_length


print(which_light(example_one))
print(which_light(example_two))
print(which_light(example_three))
print(which_light(example_four))
