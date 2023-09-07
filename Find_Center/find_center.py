## You are a software engineer at a computer vision startup
## your job is to find the center of a source of light represented by a 2D array that contains integers that show the brightness at that corresponding pixel. Find the center of the source of light in the image, and return it's coordinates as an array representing the X,Y of the center of the light.

image3 = [
  [0, 0, 0, 0, 1, 2, 3, 4, 5, 4, 3],
  [0, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4],
  [0, 0, 1, 2, 3, 4, 5, 6, 7, 6, 5],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 7, 6],
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7],
  [2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8],
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7],
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 7, 7],
  [0, 0, 1, 2, 3, 4, 5, 6, 7, 6, 4],
  [0, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4],
]

# INCOMPLETE FIRST ATTEMPT
def find_center1(image):
  
  # check every pixel in the image for the highest brightness

  #check the first row for the brightest pixel
  
  #check every row
  for row in range(len(image)-1):
    for col in range(len(image[row])-1):
    #check the pixel in every column in that row for the brightest one
    #if the current pixel is not the last 
      if col < len(image[row]-1):
      #if the currect pixel is is greater than the next 
        if image[row][col] > image[row][col+1]:
        #check the pixel in the next rows at the same column for the brightest/greatest 
         for pixel in range(row, len(image)-1):
           #if it's the last one 
    #if it is the last one 
      #check every pixel underneath it to find the brightest one
