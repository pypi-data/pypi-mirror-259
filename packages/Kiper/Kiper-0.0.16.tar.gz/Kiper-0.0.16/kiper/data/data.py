import pandas as pd

class Data:
    def __init__(self, name, data, description=None):
        """
         Initializes the object with data. This is the constructor for the class. You can override this if you want to do something other than initialize the object with a different name and / or data
         
         Args:
         	 name: The name of the object
         	 data: The data to be stored in the object's data
         	 description: A description of the
        """
        
        self.name = name
        self.data = data
        self.description = description

class DataManager:
    def __init__(self, data_classes):
        """
         Initialize the data dictionary. This is called by __init__ to initialize the data dictionary
         
         Args:
         	 data_classes: a list of data
        """
        self.data = {}
        self.auto_add(data_classes)

    def auto_add(self, data_classes):
        """
         Add data classes to the data store. This is a convenience method for use when you don't know what you're doing.
         
         Args:
         	 data_classes: A list of data classes to add
        """
        # Add data classes to the list of data classes.
        for data_class in data_classes:
            instance = data_class()
            self.add(instance.name, instance, instance.description)


    def add(self, name, value, description=None):
        """
            Add a value to the data. This is a convenience method for adding values to the data.
            
            Args:
                name: The name of the value to add. It must be unique.
                value: The value to add. It must be a string.
                description: A description of the value. It must be a string
        """
       
        self.data[name] = {'value': value, 'description': description}

    def get(self, name):
        """
            Get value by name. This is a shortcut for : meth : ` get `
            
            Args:
                name: Name of the value to get.
            
            Returns: 
                Value of the given name or None if not found
        """
       
        return self.data.get(name)

    def update(self, name, new_value):
        """
         Updates a value in the data. If the key does not exist nothing happens
         
         Args:
         	 name: Name of the key to update
         	 new_value: New value to set for the key
        """
        
        if name in self.data:
            self.data[name]['value'] = new_value
            print(f"Datenobjekt '{name}' erfolgreich aktualisiert.")
        else:
            print(f"Datenobjekt '{name}' nicht gefunden. Kann nicht aktualisiert werden.")

    def list(self):
        """List all the keys in the data (Just for Development)"""
        
        print("Gespeicherte Datenobjekte:")
        for name, data_info in self.data.items():
            value_type = type(data_info['value'])
            description = data_info['description']
            print(f"{name}: {value_type} - {description}")


# Beispielklassen für Daten
"""
class SapData(Data):
    def __init__(self):
        super().__init__(
            name="SAP-Daten",
            data="asd",
            description="Daten aus dem SAP-System"
        )

class DrcData(Data):
    def __init__(self):
        super().__init__(
            name="DRC-Daten",
            data=None,
            description="Daten aus dem DRC-System"
        )

# Beispielverwendung des DataManager

def main():
    data_manager = DataManager([SapData, DrcData])
    data_manager.list()

if __name__ == "__main__":
    main()
"""