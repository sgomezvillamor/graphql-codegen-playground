# this requires to fetch json schema (instrospection graphql query) to generate the types
sgqlc-codegen schema --docstrings ../../schemas/tableau/schema.json tableau_schema.py
# this genrates the queries
sgqlc-codegen operation --schema ../../schemas/tableau/schema.json tableau_schema tableau_operations.py tableau_operations.gql
