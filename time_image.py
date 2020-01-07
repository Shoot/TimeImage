import io
import os
import json
import pytz
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw
from flask import Flask, send_file, make_response

class TimeImage:
	def __init__(self):
		# Store the latest image so we don't have to re-generate a new image constantly
		self.latest = {'time': None, 'image': None}

		# Raise an exception if the config file doesn't exist
		if not os.path.isfile('config.json'):
			raise Exception('Config file does not exist')
		
		# Load the config file
		with open('config.json', 'r', encoding='utf-8') as file:
			self.config = json.loads(file.read())

		# Validate the config file
		if not os.path.isfile(self.config['image']) and self.config['image']:
			raise Exception('Invalid background image file')

		if not self.config['timezone'] in pytz.all_timezones:
			raise Exception('Invalid timezone')

		if not os.path.isfile(self.config['font']['file']) and self.config['font']['file']:
			raise Exception('Invalid font file')

	def current_time(self, timezone):
		""" Generates the time string """
		return datetime.now(tz=pytz.timezone(timezone)).strftime("%I:%M%p")

	def generate_image(self):
		""" Generates the time image """
		string = self.current_time(self.config['timezone'])

		# Check if image has already been generated
		if self.latest['time'] == string:
			return self.latest['image']

		image = Image.open(self.config['image']).convert("RGBA")

		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype(self.config['font']['file'], self.config['font']['size'])

		W, H = image.size
		w, h = draw.textsize(string, font=font)

		# Add the text to the image
		draw.text((((W - w) / 2) + self.config['offset']['x'], ((H - h) / 2) + self.config['offset']['y']), string, font=font)

		self.latest = {'time': string, 'image': image}

		return image

	def generate_response(self, image):
		""" Generates the response which is returned to the user """

		# Save the image to a buffer
		output = io.BytesIO()
		image.save(output, format="PNG")
		output.seek(0, 0)

		# Form the response and add the file which is held in the buffer
		response = make_response(send_file(output, mimetype="image/png", as_attachment=False))
		response.headers = {
			"Cache-Control": "no-cache, no-store, must-revalidate",
			"Pragma": "no-cache",
			"Expires": "0"
		}

		# Return the response to the user
		return response

ti = TimeImage()
app = Flask(__name__)

@app.route('/')
def index():
	return ti.generate_response(ti.generate_image())