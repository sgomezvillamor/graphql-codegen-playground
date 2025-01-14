datamodel-codegen --input ../../schemas/tableau/schema.json --input-file-type json --output tableau_dataclasses.py --output-model-type dataclasses.dataclass
datamodel-codegen --input ../../schemas/tableau/schema.json --input-file-type json --output tableau_pydantic.py --output-model-type pydantic.BaseModel
datamodel-codegen --input ../../schemas/tableau/schema.json --input-file-type json --output tableau_pydantic_v2.py --output-model-type pydantic_v2.BaseModel
datamodel-codegen --input ../../schemas/tableau/schema.graphql --input-file-type graphql --output tableau_pydantic_v2_graphql.py --output-model-type pydantic_v2.BaseModel
