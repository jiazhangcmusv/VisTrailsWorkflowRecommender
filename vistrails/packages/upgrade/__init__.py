
from upgrade_widget import UpgradeWidget

identifier = 'edu.cmu.sv.upgrade'
name = 'Component Upgrade'
version = '1.0.0'

widget = UpgradeWidget()

def menu_items():
    """menu_items() -> tuple of (str,function)
    It returns a list of pairs containing text for the menu and a
    callback function that will be executed when that menu item is selected.
    """
    def show_upgrade_form():
        widget.init_datasource()
        widget.init_view()
        widget.show()
        widget.activateWindow()

    lst = []
    lst.append(("Upgrade Programmable Web", show_upgrade_form))
    return tuple(lst)