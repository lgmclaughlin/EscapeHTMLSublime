import sublime, sublime_plugin

class EscapeCommand(sublime_plugin.TextCommand):
    # characters to check for
    escapeChars = {
        '\'' : '&apos;',
        '\"' : '&quot;',
        '&'  : '&amp;',
        '<'  : '&lt;',
        '>'  : '&gt;',
        # Replace newlines with breaks for
        # HTML display
        '\n' : '<br />\n'
    }

    def run(self, edit):
        # Get all selected text
        sel = self.view.sel()
        # Loop through each region
        for region in sel:
            if len(region) > 0:
                arr = list(self.view.substr(region))
                # Loop through the string in array form and escape HTML
                for i, char in enumerate(arr):
                    if char in self.escapeChars:
                        arr[i] = self.escapeChars[char];
                # Replace the selection with transformed text
                self.view.replace(edit, region, ''.join(arr))
