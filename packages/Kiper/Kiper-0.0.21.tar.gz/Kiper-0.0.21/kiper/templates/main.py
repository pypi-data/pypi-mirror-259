from kiper.pipeline.pipeline import PipelineManager


manager = PipelineManager()
manager.data_manager.list()
manager.load_pipelines()

# Define order for the piplines by foldername
pipeline_order = ["example_pipeline",]

results = manager.run(pipeline_order)
for pipeline_name, result in results.items():
    print(f"Results for pipeline '{pipeline_name}': {result}")
