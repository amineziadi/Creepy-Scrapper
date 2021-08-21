#Welcome to CreepyScraper
#This tool created to scrap twitter's tweets using Nitter Web Site by grapping the searched data

"""
Import section
"""

#Import argparse for tool creation
import argparse

#Import ernno to catch the errors
import errno

#Import requests to catch source codes from a website
import requests

#Import BeatifulSoup from bs4
from bs4 import BeautifulSoup

"""
Tools arguments and building section
"""

#Give the discription for Creepy-Scrapper
parser = argparse.ArgumentParser(description="Creepy-Scrapper is one of the best tools to scraping tweets from Twitter using the Nitter plateform")

"""
Arguments section
"""

#item argument
parser.add_argument(
	'-i',
	'--item',
	type=str,
	help="Enter the item you looking for."
)
#wordlist of items argument
parser.add_argument(
	'-w',
	'--word_list',
	type = str,
	help="Enter the word list of items."
)
#output file argument
parser.add_argument(
	'-o',
	'--file_output',
	type = str,
	help = "Enter the output file name to saving data in."
)

args = parser.parse_args()

#Pass input arguments to variables
item = args.item if args.item else ''
word_list = args.word_list if args.word_list else ''
output_file = args.file_output if args.file_output else ''

"""
Define the functions we need in this tool 
"""

#Define a function called wordlist wich is returning the lines of file in array
def wordlist(word_list):
	with open(word_list, 'r') as wl:
		lines = []
		for line in wl:
			line = line.replace(' ','')
			if line != '\n':					
				lines.append(line.strip())
	return lines

#Define function called get_website wich is returning the html code using BeautifulSoup of a searching from Nitter 
def get_website(item):
	html_text = requests.get("https://nitter.eu/search?f=tweets&q="+item).text
	#Put the source code in a soup variable using b4s
	soup = BeautifulSoup(html_text, "lxml")	
	return soup

#Define a function called get_tweets wich is returning the twitts in array of arrays
def get_tweets(content):
	posts = content.find_all("div", class_ = "timeline-item")
	data = []
	for post in posts:
		tweet_data = []
		#Collecting the fullName and the userName and the tweet from every post
		full_name = post.find("a", class_="fullname").text
		user_name = post.find("a", class_="username").text
		tweet = post.find("div", class_="tweet-content media-body").text
		tweet_date = post.find("span", class_="tweet-date").text
		tweet_data.append(full_name)
		tweet_data.append(user_name)
		tweet_data.append(tweet_date)
		tweet_data.append(tweet)
		data.append(tweet_data)
	return data

#Define a function called save_file wich is saving the result data in an output file
def save_file(tweets,output_file):
	f = open(output_file,"w")
	for tweet in tweets:
		for t in tweet:
			f.write(t+"\n")
		f.write("*************************************************************\n")
	f.close()

#Define a function called save_multi_data wich is save
def save_multi_data(data,output_file):
	f = open(output_file,"w")
	for tweets in data:
		for tweet in tweets:
			for t in tweet:
				f.write(t+"\n")
			f.write("*************************************************************\n")
		f.write("**************************Other Searching***********************************\n")
	f.close()

"""
Testing and ouptut section
"""

#The main function
if __name__ == "__main__":
	print("Welcome to this pretty Ceepy-Scrapper type -h for the help options")
	if word_list:
		try:
			with open(word_list) as words:
				# File exists
				wl = wordlist(word_list)
				print("The search Items is {0}".format(wl))
				#Not useful offline
				data = []
				for w in wl:
					content = get_website(w)
					tweets = get_tweets(content)
					#Store the tweets in other array
					data.append(tweets) 
				#Store the data in output file
				save_multi_data(data,output_file)	
				print("****************************************")
				print("Your output file is {0} ".format(output_file))			
		except IOError as e:
			# Raise the exception if it is not ENOENT (No such file or directory)
			if e.errno != errno.ENOENT:
				raise
				# No such file or directory
			print("The search Item is {0}".format(item))
			"""
			#Not useful offline
			content = getWebsite(item)
			tweets = getTweets(content)
			#Store the data in output file
			save_file(tweets,output_file)
			"""
	else:
		print("The search Item is {0}".format(item))
		#Not useful offline
		content = get_website(item)
		tweets = get_tweets(content)
		"""
		#print(tweets) for testing
		for tweet in tweets:
			print(tweet)
		"""
		#Store the data in output file
		save_file(tweets,output_file)
		print("****************************************")
		print("Your output file is {0} ".format(output_file))

#**********************************************************************************
"""
	Thanks to everyone that help me by good words for this project and wait the updates ;)
	Special thank to 'Azrotronik' github account : https://github.com/Azrotronik 
	Any idea? Just send me now on my email adresse : amine.ziadi1002@gmail.com
	New versions coming soon for saving the media data ;)
"""
