'''
Created on Jan 10, 2013

@author: xiaoxiao
'''
from PyQt4.QtCore import Qt, QVariant
from PyQt4.QtGui import QTableView, QWidget, QPushButton, QStandardItemModel
import core.packagemanager
from db.programmableweb.mongo_source import DataSource
import datetime
import core.modules.module_registry
import core.modules.vistrails_module as vistrails_module
from core.modules.module_descriptor import ModuleDescriptor
from core.modules.vistrails_module import Module


class UpgradeWidget(QWidget):
    

    def init_datasource(self):
        self.data_source = DataSource()
    
    def init_view(self):
        self.table = QTableView(self)
        self.table.setMinimumSize(600, 600)

        manager = core.packagemanager.get_package_manager()
        package = manager.get_package("edu.cmu.sv.components", "1.0.0")
        modules = package.descriptors
        apis = []
        self.modules_to_upgrade = []
        for module in modules.values():
            api = self.data_source.api_by_id(module.name)
            if ("1.0" != module.version):
                apis.append(api)
                self.modules_to_upgrade.append(module)

        table_model = QStandardItemModel(len(apis), 4)
        row = 0
        for api in apis:
            table_model.setData(table_model.index(row, 0), QVariant(api['id']))
            table_model.setData(table_model.index(row, 1), QVariant(api['category']))
            table_model.setData(table_model.index(row, 2), QVariant(api['version']))
            table_model.setData(table_model.index(row, 3), QVariant(api['description']))
            row += 1

        table_model.setHeaderData(0, Qt.Horizontal, QVariant("Link"))
        table_model.setHeaderData(1, Qt.Horizontal, QVariant("Category"))
        table_model.setHeaderData(2, Qt.Horizontal, QVariant("Version"))
        table_model.setHeaderData(3, Qt.Horizontal, QVariant("Description"))
        self.table.setModel(table_model)


        btn = QPushButton(self)
        btn.clicked.connect(self.upgrade_api)
        btn.setText("Upgrade")
        btn.move(600, 500)

    def upgrade_api(self):
        model = self.table.selectionModel()
        indexes = model.selectedIndexes()
        for index in indexes:
            module = self.modules_to_upgrade[index.row()]
            now = datetime.datetime.now()
            name = "%s %d-%d-%d" % (module.name, now.year, now.month, now.day)
            manager = core.packagemanager.get_package_manager()
            package = manager.get_package("edu.cmu.sv.components", "1.0.0")
            new_module = vistrails_module.new_module(Module, name)
            core.modules.module_registry.set_current_package(package)
            new_descriptor = core.modules.module_registry.get_module_registry().add_module(new_module)
            core.modules.module_registry.get_module_registry().update_module(module, new_descriptor)
#            core.modules.module_registry.get_module_registry().delete_module(module.identifier, module.name)
            self.hide()
            return