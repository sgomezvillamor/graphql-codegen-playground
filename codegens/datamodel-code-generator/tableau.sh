datamodel-codegen --input ../../schemas/tableau/schema.json --input-file-type json --output tableau_dataclasses.py --output-model-type dataclasses.dataclass
datamodel-codegen --input ../../schemas/tableau/schema.json --input-file-type json --output tableau_pydantic.py --output-model-type pydantic.BaseModel
