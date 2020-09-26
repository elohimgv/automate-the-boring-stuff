#! python3
# extMcp.pyw - Saves and loads pieces of text to the clipboard.
# Usage: python.exe extMcp.pyw save <keyword> - Saves clipboard to keyword.
#        python.exe extMcp.pyw <keyword> - Loads keyword to clipboard
#        python.exe extMcp.pyw list - Loads all keywords to clipboard.
#        python.exe extMcp.pyw delete <keyword> - Delete keyword to clipboard.
#        python.exe extMcp.pyw delete all - Delete all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
data = str(list(mcbShelf.keys()))

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(data)
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete' and sys.argv[2] in data:
    del mcbShelf[sys.argv[2]] 
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete' and sys.argv[2].lower() == 'all':
    mcbShelf.clear()

mcbShelf.close()
