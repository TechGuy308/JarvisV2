#Access tools like calculator or calender

import tools.launch_app as launch_app
import tools.open_file as open_file

#import summarize


def tool_search_files(filename):
    open_file.search_for_file(filename)
    
def tool_open_file(self, filepath):
    try:
        open_file.open(filepath)
    except Exception as e:
        return "System failed to open files"
    
def tool_launch_app(app):
    launch_app.open_app(app)

    
        