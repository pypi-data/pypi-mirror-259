import pandas as pd
import os
import importlib.util
from pathlib import Path
import inspect
import toml

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

import pandas as pd
import os
import importlib.util
from pathlib import Path
import inspect
import toml
import logging
logging.basicConfig(level=logging.DEBUG)
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
    def __init__(self):
        """
        Initialisiert den DataManager mit den Datenklassen aus der data.py-Datei.
        """
        self.data = {}
        data_classes = self.load_data_classes()
        self.auto_add(data_classes)

    def auto_add(self, data_classes):
        """
        Fügt automatisch die Datenklassen dem DataManager hinzu.
        """
        for data_class in data_classes:
            instance = data_class()
            self.add(instance.name, instance, instance.description)

    def add(self, name, value, description=None):
        """
        Fügt dem DataManager ein neues Datenobjekt hinzu.
        """
        self.data[name] = {'value': value, 'description': description}


    def load_data_classes(self, base_path=None):
        """
        Lädt die Datenklassen aus der data.py-Datei und gibt sie zurück.
        """
        data_classes = []
        if base_path is None:
            base_path = Path(os.path.dirname(os.path.abspath(inspect.stack()[1].filename)))

        project_toml_path = base_path / "project.toml"
        if os.path.exists(project_toml_path):
            with open(project_toml_path, "r") as f:
                config = toml.load(f)
                data_file = config.get("locations", {}).get("data_file")
                if data_file and os.path.exists(data_file):
                    try:
                        spec = importlib.util.spec_from_file_location("data_module", data_file)
                        data_module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(data_module)

                        for name, obj in inspect.getmembers(data_module):
                            if inspect.isclass(obj) and isinstance(obj, type) and obj != data_module.Data:
                                data_classes.append(obj)

                        # Log Info mit allen geladenen Klassen
                        for data_class in data_classes:
                            logging.info(f"Geladene Datenklasse: {data_class.__name__}, Beschreibung: {data_class.__doc__}, Datei: {data_file}")

                    except Exception as e:
                        # Log Fehler und beende den Prozess
                        logging.error(f"Fehler beim Laden der Datenklassen aus der Datei {data_file}: {e}")
                        exit(1)

        return data_classes

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

# Rest des Codes bleibt unverändert



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