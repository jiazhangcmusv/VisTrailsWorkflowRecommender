
identifier = 'edu.cmu.sv.profile'
name = 'Profile'
version = '1.0.0'


def menu_items():
    """menu_items() -> tuple of (str,function)
    It returns a list of pairs containing text for the menu and a
    callback function that will be executed when that menu item is selected.
    """
    def name():
        pass
    
    def affiliate():
        pass
    
    def research_areas():
        pass
    
    def context():
        pass
    
    def project_description():
        pass
    
    def tags():
        pass
    
    def service_used():
        pass
    
    lst = []
    lst.append(("Name", name))
    lst.append(("Affiliate", affiliate))
    lst.append(("Research Areas", research_areas))
    lst.append(("Context", context))
    lst.append(("Project Description", project_description))
    lst.append(("Tags", tags))
    lst.append(("Service Used", service_used))
    return tuple(lst)