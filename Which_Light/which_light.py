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
example_one = [
  4, 4, 5, 5, 4, 3, 3, 4, 5, 77, 77, 77, 78, 79, 80, 81, 88, 90, 95, 100, 100,
  110, 115, 135, 145, 158, 158, 190, 200, 200, 200, 200, 200, 150, 100, 60, 7,
  8, 8, 8
]  # halogen

example_two = [
  4, 5, 8, 9, 11, 2, 3, 4, 5, 6, 5, 4, 5, 4, 100, 110, 115, 135, 145, 158, 158,
  190, 200, 200, 200, 200, 200, 200, 200, 200, 190, 100, 90, 87, 80, 30, 25,
  26, 27, 28, 29, 30, 30, 30, 30, 30, 30, 30
]  # florecent

example_three = [
  4, 4, 5, 5, 4, 3, 3, 4, 4, 4, 5, 5, 4, 3, 3, 4, 5, 100, 150, 200, 200, 200,
  201, 201, 200, 201, 200, 199, 200, 200, 199, 201, 150, 4, 4, 5, 5, 4, 3, 3,
  4, 9, 4, 4, 5, 5, 4, 3, 3, 4, 5
]  # incandecent

example_four = [
  4, 4, 5, 5, 4, 3, 3, 4, 4, 4, 5, 5, 4, 3, 3, 4, 5, 200, 200, 200, 200, 200,
  200, 200, 200, 200, 200, 200, 200, 200, 4, 4, 5, 5, 4, 3, 3, 4, 9, 4, 4, 5,
  5, 4, 3, 3, 4, 5
]  # LED

#Questions 
#- how do you know when the light is actually on the brightest; if the reading can go to 255 according to the initial description, but the highest number in the readings examples is 200? 
#- how do you know the start of a turn on for the very gradual halogen turn ons that has a jump first to 77 and slowly builds to 200(the beightest on the list? Or with even the less gradual example florecent which jumps to 100 before gradually building to 200. Do we solely base the patterns (the initial turn on numbers, plateu numbers, highest numbers etc.) based on the examples? Are we supposed to hard code them in? What if there was a different example with diffent numbers fed in that met the criteria but didnt match the hardcoded patterns/rules? Like maybe the brightest would be 255 etc.

#MY SOLUTION
#ASSUMPTIONS:
#1. the examples' patterns for all four light types would hold for all input and we can therefore hardcode in what values to check for.
#2. there will be multiple values within each light tier (turning on, turned on, brightest, turning off)
#3. only the turning on/brightening patterns matter
#4. Use the following relevant values/criteria (hardcoded based on examples)
#start turning on > 76
#start turned on > 99
#start brightest > 199
def which_light(reading):
  BRIGHTNESS_THRESHOLD = 76 #arbitrarily picked based on the example
  BRIGHTNESS_PLATEU = 100 #picked based on the example
  BRIGHTNESS_PEAK = 200 #picked based on the example
  start_brightness = None
  start_brightness_plateu = None
  start_brightness_peak = None
  #check every millisecond in the reading for the above values indices
  millisecond_index = 0
  for millisecond in reading:
    if start_brightness is None:
      if millisecond > BRIGHTNESS_THRESHOLD:
        start_brightness = millisecond_index
        print("start turning on: ", start_brightness, ": ", millisecond)
    if start_brightness_plateu is None:
      if millisecond >= BRIGHTNESS_PLATEU:
        start_brightness_plateu = millisecond_index
        print("start turned on: ", start_brightness_plateu, ": ", millisecond)
    if start_brightness_peak is None:
      if millisecond >= BRIGHTNESS_PEAK:
        start_brightness_peak = millisecond_index
        print("start brightness: ", start_brightness_peak, ": ", millisecond)
    millisecond_index += 1

  #check if it's hallogen - if the first increase in brightness is between 77 and 99 inclusively
  if reading[start_brightness] < BRIGHTNESS_PLATEU: 
          return "halogen"
  #check it it's LED - IS THIS AN OK CHECK? THE SOLUTION USES THE INDICES TO CHECK IF NO SPACE BETWEEN PLATEU AND PEAK
  elif reading[start_brightness] >= BRIGHTNESS_PEAK: #if the first increase in brightness is greater than 199 we know it's LED 
    return "LED"
  #check if it's florecent - it takes over 2 milliseconds (arbitrarily picked based on the example) to get from 100 to over 199
  elif start_brightness_peak - start_brightness > 2:
    return "florecent"
  #check if it's incandecent - it takes less than 3 milliseconds (arbitrarily picked based on the example) to get from 100 to over 199
  elif start_brightness_peak - start_brightness < 3:
    return "incandecent"
  else:
    return None
  
print(which_light(example_one))
print(which_light(example_two))
print(which_light(example_three))
print(which_light(example_four))
