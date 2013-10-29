#Copied imports from HTTP package init.py file
from PyQt4 import QtGui
from core.modules.vistrails_module import ModuleError
from core.configuration import get_vistrails_persistent_configuration
from gui.utils import show_warning
import core.modules.vistrails_module
import core.modules
import core.modules.basic_modules
import core.modules.module_registry
import core.system
from core import debug

from component_search_form import *

class ComponentSearch(core.modules.vistrails_module.Module):
    pass

def initialize(*args, **keywords):
    reg = core.modules.module_registry.get_module_registry()
    basic = core.modules.basic_modules
    
    reg.add_module(ComponentSearch, abstract=True)
