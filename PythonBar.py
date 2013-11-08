import sublime, sublime_plugin, webbrowser

class RunInPythonbarCommand(sublime_plugin.WindowCommand):
    def run(self):
        path = self.window.active_view().file_name()
        if path == "None":
            print "not saved"
        else:
            passString = "PythonBar://do?run="+path
            webbrowser.open(passString)

class SaveInPythonbarCommand(sublime_plugin.WindowCommand):
    def run(self):
        path = self.window.active_view().file_name()
        if path == "None":
            print "not saved"
        else:
            passString = "PythonBar://do?save="+path
            webbrowser.open(passString)