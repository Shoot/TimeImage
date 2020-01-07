import time_image
from waitress import serve

def main():
	serve(time_image.app, host='0.0.0.0', port='80')

if __name__ == "__main__":
	main()