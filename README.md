# ZS_Fixer
Simple script for fixing a bug that occurs when editing a Z-S Overview in the game Eve Online.
Fixes the faulty html tags that don't get handled properly after saving an overview setting in-game.

## Installs
You need Python 3.x

The .bat and .py files need to be in the same folder, otherwise location doesn't matter.

If you have both Python 2 and 3 installed, you might have to change the
```python``` command to ```python3``` and/or change the PATH variable.

To get rid of the any key confirmation at the end of the .bat file, you can comment out the ```pause```.

## Manual fix

When saving a Sharashawa or Z-S Overview, the html tags get escaped and they no longer work correctly. This is a pain in the butt.
To fix it, you need to export the overview from Eve, open the file in a text editor (eg. Notepad++) and replace these as follows:
```&lt;``` into ```<``` and ```&gt;``` into ```>```
Then import the files again (remember to reset your overview before doing it).
