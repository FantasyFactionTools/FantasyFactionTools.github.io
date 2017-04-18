import csv
import json

csvfile = open('LGBT Characters - Sheet1.tsv', 'r')
jsfile = open('lgbt-characters.js', 'w')
jsfile.truncate()

fieldnames = ("genre","author","series","book title")
reader = csv.DictReader( csvfile, fieldnames, delimiter='\t')
next(reader, None)  # skip the headers

currentGenre = ""

for row in reader:
	if row['genre'] != "":
		currentGenre = row['genre']
		jsfile.write("\nauthors[\"" + currentGenre + "\"] = [];\n")

    #json.dump(row, jsonfile)
	jsfile.write("authors[\"" + currentGenre + "\"].push({\"author\":\"" + row['author'] + "\", \"series\":\"" + row['series'] + "\", \"book-title\":\"" + row['book title'] + "\"});\n")
