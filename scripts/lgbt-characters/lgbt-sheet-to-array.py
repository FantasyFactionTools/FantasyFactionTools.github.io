import csv
import json

csvfile = open('LGBT Characters - Sheet1.tsv', 'r')

jsfile = open('../../lists/lgbt-characters.js', 'w')
jsfile.truncate()
jsfile.write("\nauthors = {};\n")

bbfile = open('lgbt-characters.txt', 'w')
bbfile.truncate()

fieldnames = ("genre","author","series","book title")
reader = csv.DictReader( csvfile, fieldnames, delimiter='\t')
next(reader, None)  # skip the headers

currentGenre = ""

for row in reader:
	if row['genre'] != "":
		currentGenre = row['genre']
		jsfile.write("\nauthors[\"" + currentGenre + "\"] = [];\n")
		bbfile.write("\n\n[color=brown][size=14pt][b]" + currentGenre + "[/b][/size][/color]\n")

	jsfile.write("authors[\"" + currentGenre + "\"].push({\"author\":\"" + row['author'] + "\", \"series\":\"" + row['series'] + "\", \"book-title\":\"" + row['book title'] + "\"});\n")

	bbfile.write("\n    [b]" + row['author'] + "[/b]")
	if row['book title'] != "":
		bbfile.write("\n    " + row['book title'])

	if row['series'] != "":
		bbfile.write("\n    [i]" + row['series'] + "[/i]")

	bbfile.write("\n")
