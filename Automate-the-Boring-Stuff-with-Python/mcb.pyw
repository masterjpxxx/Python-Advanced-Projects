#! python3
# mcb.pyw - This program saves and loads pieces of information in the clipboard for later use
# Usage: mcb.pyw save <keyword> - Saves the text to the keyword
#        mcb.pyw delete <keyword> - deletes the text in the keyboard
#        mcb.pyw clearAll   - clears of the keywords saved
#        mcb.pyw <keyword> - Loads the Keyword to Clip Board
#        mcb.pyw list - loads all keywords to the clip board

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save Clipboard content

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
# List keywords and Load Content
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] == 'clearAll':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    

mcbShelf.close()