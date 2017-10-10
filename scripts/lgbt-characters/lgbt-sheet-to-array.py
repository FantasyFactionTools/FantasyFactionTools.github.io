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
lgbt_book_list = {}

for row in reader:
	if row['genre'] != "":
		currentGenre = row['genre']
		jsfile.write("\nauthors[\"" + currentGenre + "\"] = [];\n")

		if currentGenre not in lgbt_book_list:
			lgbt_book_list[currentGenre] = []

	jsfile.write("authors[\"" + currentGenre + "\"].push({\"author\":\"" + row['author'] + "\", \"series\":\"" + row['series'] + "\", \"book-title\":\"" + row['book title'] + "\"});\n")
	lgbt_book_list[currentGenre].append({"genre":currentGenre, "author":row['author'], "book-title":row['book title'], "series":row['series']})



currentGenre = ""
currentAuthor = ""

for genre in lgbt_book_list:

	sorted_genre_list = sorted(lgbt_book_list[genre], key=lambda k: k['book-title'])

	for book in sorted_genre_list:

		if currentGenre != book['genre']:
			currentGenre = book['genre']
			bbfile.write("\n\n[color=brown][size=14pt][b]" + currentGenre + "[/b][/size][/color]\n")

		if currentAuthor != book['author']:
			bbfile.write("\n    [b]" + book['author'] + "[/b]")
			currentAuthor = book['author']
		
		if book['book-title'] != "":
			bbfile.write("\n    " + book['book-title'])

		if book['series'] != "":
			bbfile.write("\n    [i]" + book['series'] + "[/i]")

		bbfile.write("\n")

