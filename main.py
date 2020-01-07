import time_image
from waitress import serve

serve(time_image.app, host='0.0.0.0', port='80')