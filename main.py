from PIL import Image
import pytesseract

def process_image(iamge_name, lang_code):
	return pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)

def print_data(data):
	print(data)

def output_file(filename, data):
	file = open(filename, "w+")
	file.write(data)
	file.close()

def main():
	data_deu = process_image("test.png", "deu")
	print_data(data_deu)
	output_file("eng.txt", data_deu)

if  __name__ == '__main__':
	main()