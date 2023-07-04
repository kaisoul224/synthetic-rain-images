# synthetic-rain-images
This repo helps you to add synthetic rain to the image.

## Using
### Step 1:
Clone this repo
### Step 2:
Add 2 folders to repo
- imgs: folder to store source image
- result: folder to store images that have been added to rain
### Step 3:
Config the level of rain that you want
```bash
 # =============== config =================
        # Angle gave as integer between (-90 < angle < 90)
        # angle = 100 -> random
        angle = 100
        # The max length of raindrops in pixels(the actual length is random up to length)
        # should be matched somehow to the image resolution
        length = 20
        # Rain drop width
        thickness = 1
        # Number of raindrops to be added
        drop_nrs = 1000
        # Size of the blur filter
        blur = 4
        # Intensity(grayscale) of rain streaks
        intensity = 100
```
### Step 4:
Install some require libraries and Run the project
```bash
 python3 main.py
```
