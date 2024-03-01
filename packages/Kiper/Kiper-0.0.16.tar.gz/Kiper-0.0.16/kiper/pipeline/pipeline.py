import os
import importlib.util
from pathlib import Path
import toml
from .node import Node
import inspect

class Pipeline:
    def __init__(self):
        """
         Initialize the nodes dictionary. This is called by __init__ to initialize the node dictionary and its sub - classes
        """
        self.nodes = {}
      

    def run(self):
        """
         Run the nodes and return outputs. This is the entry point for the Node class. You can override this method to do something different
         
         
         Returns: 
         	 A dictionary of outputs keyed by
        """
        outputs = {}
        # Execute all nodes in the graph.
        for node_name, node in self.nodes.items():
            outputs[node_name] = node.execute()
        return outputs

    def add_node(self, name, func, inputs):
        """
         Add a node to the graph. This is a convenience method for creating a : class : ` Node ` and associating it with the graph.
         
         Args:
         	 name: The name of the node. It must be unique among all nodes in the graph.
         	 func: The function to run on the node. It must take a single argument : an instance of
         	 inputs: The inputs to the
        """
        self.nodes[name] = Node(name, func, inputs)

    def register(self, pipeline_instance):
        """
         Register a pipeline with the pipeline manager. This is a convenience method for the use of : meth : ` Pipeline. nodes `
         
         Args:
         	 pipeline_instance: An instance of : class : ` Pipeline
        """
        for pipline in pipeline_instance:
            if pipline not in self.nodes:
                raise ValueError(f"Pipeline '{pipline}' ist erforderlich, wurde aber nicht gefunden.")
        self.nodes.update(pipeline_instance.nodes)


class PipelineManager:
    def __init__(self):
        """
         Initialize the pipeline manager. This is called by __init__ and should not be called directly by user
        """
        self.pipelines = {}

    def load_pipelines(self, base_path=None):
        """
         Load Pipelines from project. toml and create module. This method is called by load_files ()
         
         Args:
         	 base_path: Base path to look
        """
        # Returns the base path of the file.
        if base_path is None: base_path = Path(os.path.dirname(os.path.abspath(inspect.stack()[1].filename)))

        project_toml_path = base_path / "project.toml"
        with open(project_toml_path, "r") as f:
            project_config = toml.load(f)
            pipeline_folder_name = project_config["project"]["place"]
            pipeline_folder = base_path / pipeline_folder_name
        
            for pipeline_name in pipeline_folder.iterdir():
                if pipeline_name.is_dir():
                    pipeline_name = pipeline_name.name
                    pipeline_module_path = pipeline_folder / pipeline_name / "pipeline.py"
                    if pipeline_module_path.exists():
                        spec = importlib.util.spec_from_file_location("pipeline_module", pipeline_module_path)
                        pipeline_module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(pipeline_module)
                        pipeline_register_function = getattr(pipeline_module, "register", None)
                        if callable(pipeline_register_function):
                            pipeline_definition = pipeline_register_function()
                            if isinstance(pipeline_definition, Pipeline):
                                self.pipelines[pipeline_name] = pipeline_definition
                            else:
                                raise ValueError(f"The register function in {pipeline_module_path} must return a Pipeline instance.")

    def run(self, pipeline_order):
        """
         Run a list of pipelines in the order they were added. This is useful for debugging and to get the results of each pipeline
         
         Args:
         	 pipeline_order: A list of pipeline names
         
         Returns: 
         	 A dictionary of results keyed by
        """
        results = {}
        for pipeline_name in pipeline_order:
            if pipeline_name in self.pipelines:
                pipeline = self.pipelines[pipeline_name]
                results[pipeline_name] = pipeline.run()
            else:
                raise ValueError(f"Pipeline '{pipeline_name}' not found.")

        return results