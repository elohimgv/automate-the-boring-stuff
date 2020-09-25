#! python3
# multiclipboard.pyw - Saves and loads pieces of text to the clipboard.
# Usage: python.exe multiclipboard.pyw save <keyword> - Saves clipboard to keyword.
#        python.exe multiclipboard.pyw <keyword> - Loads keyword to clipboard
#        python.exe multiclipboard.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()