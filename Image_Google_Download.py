# importing google_images_download module 
from google_images_download import google_images_download 

# creating object 
response = google_images_download.googleimagesdownload() 

search_queries = ["British people","Indian people","African people","Japanese people",
                  " Korean people","Chinese people","Turkish people","Egyptian people","Israeli people",
                  "Australian people","Brazilian people","Spanish people",
                  "Russian people","Mexican people","Canadian people","American people",
                  "Italian people","German people","French people","Scottish people",
                  "Arabian people"]


def downloadimages(query): 
	# keywords is the search query 
	# format is the image file format 
	# limit is the number of images to be downloaded 
	# print urs is to print the image file url 
	# size is the image size which can 
	# be specified manually ("large, medium, icon") 
	# aspect ratio denotes the height width ratio 
	# of images to download. ("tall, square, wide, panoramic") 
	arguments = {"keywords": query, 
				"format": "jpg", 
				"limit":500, 
				"print_urls":True, 
				"size": "medium",
                "chromedriver" : r"C:\Users\Ronith\Downloads\chromedriver_win32\chromedriver.exe"} 
	try: 
		response.download(arguments) 
	
	# Handling File NotFound Error	 
	except FileNotFoundError: 
		arguments = {"keywords": query, 
					"format": "jpg", 
					"limit":500, 
					"print_urls":True, 
					"size": "medium",
                    "chromedriver" : r"C:\Users\Ronith\Downloads\chromedriver_win32\chromedriver.exe"} 
					
		# Providing arguments for the searched query 
		try: 
			# Downloading the photos based 
			# on the given arguments 
			response.download(arguments) 
		except: 
			pass

# Driver Code 
for query in search_queries: 
	downloadimages(query) 
	print()
