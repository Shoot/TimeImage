# TimeImage
Displays the current time on an image using PIL for image generation and Flask to provide a way to get the image.
## Requirements
Python 3
## Install
Download the latest version from [here](https://github.com/Shoot/TimeImage/archive/master.zip) and extract it to a new folder. You will need to install all the requirements from the `requirements.txt` file using pip.
## Configuration
Any configuration can be done in the `config.json` file, with the following values:
- `"image"` is the file you will be using as the background.
- `"timezone"` is the timezone you will be getting the time from, using names from the [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) time zone format.
- `"font"` has two values, `"file"` which is the font file to use, and `"size"` which is the size of the font.
- `"offset"` also has two values, `"x"` and `"y"`, each corresponding to added offset on the placement of the time.
## Running
Start the `main.py` file, you should then be able to access it on `http://localhost`.
A live example is available [here](http://dawn.sh:81) with the `America/New_York` timezone.
