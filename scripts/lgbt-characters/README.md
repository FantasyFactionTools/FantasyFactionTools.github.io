## Managing the LGBT Characters List

#### Step One
Go to the Google Spreadsheet and make any adjustments to the list you'd like.  Author is required.  Series and Title are optional. 

_LGBT Characters in SFF:_
https://docs.google.com/spreadsheets/d/1_qeQ8ccoom9h5hi9TAuAvtGb8dT06KPc6HJjN_fi4t0/edit?usp=sharing

#### Step Two
Export the sheet as `LGBT Characters - Sheet1.tsv` into the `/scripts/lgbt-characters` directory.  Replace the old one.

#### Step Three
Run the python script to bake the data for the HTML page.

```
$:  python lgbt-sheet-to-array.py
```

It will do two things:

1. Generate Javascript data the HTML page uses to render the fancy list.
2. Generate a `lgbt-characters.txt` text file whose contents you can copy-paste into the Fantasy-Faction Forum.

#### Step Four
Commit your changes and it'll just show up on this page:  
[https://fantasyfactiontools.github.io/lists/lgbt-characters.html](https://fantasyfactiontools.github.io/lists/lgbt-characters.html)

_NOTE:  It could take a few minutes for the changes to propagate.  Give it a little bit before you see the updates._

Copy and paste the contents of `lgbt-characters.txt` into whereever you'd like in the forum.
