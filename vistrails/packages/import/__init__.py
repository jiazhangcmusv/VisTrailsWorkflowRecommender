
identifier = 'edu.cmu.sv.import'
name = 'Import'
version = '1.0.0'


from RecommandationForm import ComponentSearchForm

form = ComponentSearchForm()

def menu_items():
    """menu_items() -> tuple of (str,function)
    It returns a list of pairs containing text for the menu and a
    callback function that will be executed when that menu item is selected.
    """
    def show():
        form.show();
        form.activateWindow()
        form.raise_()

    lst = []
    lst.append(("Import Programmableweb", show))
    
    return tuple(lst)