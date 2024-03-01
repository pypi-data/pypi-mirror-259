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
    def __init__(self, caller_path):
        """
        Initialisiert den DataManager mit den Datenklassen aus der data.py-Datei,
        basierend auf dem Pfad des aufrufenden Skripts.
        """
        self.data = {}
        self.caller_base_path =caller_path
        data_classes = self.load_data_classes()
        self.auto_add(data_classes)

    

    def load_data_classes(self):
        """
        Lädt die Datenklassen aus der data.py-Datei und gibt sie zurück.
        Nutzt den übergebenen Basispfad.
        """
        data_classes = []
        project_toml_path = self.caller_base_path / "project.toml"
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

    def auto_add(self, data_classes):
        """
        Fügt automatisch die Datenklassen dem DataManager hinzu.
        """
        for data_class in data_classes:
            instance = data_class()
            # Hier verwenden wir den gewünschten Namen für das Datenobjekt
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
        Get data by name. This method returns the data associated with the given name.

        Args:
            name: Name of the data to get.

        Returns:
            Data associated with the given name, or None if not found.
        """
        data_info = self.data.get(name)
        if data_info:
            return data_info['value'].data
        else:
            print(f"Datenobjekt '{name}' nicht gefunden.")
            print("Inhalt des self.data-Dictionaries:")
            for data_name, data_info in self.data.items():
                print(f"Name: {data_name}, Wert: {data_info['value']}")
            return None




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