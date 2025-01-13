# this requires to fetch json schema (instrospection graphql query) to generate the types
sgqlc-codegen schema --docstrings ../../schemas/github/schema.json github_schema.py
# this genrates the queries
sgqlc-codegen operation --schema ../../schemas/github/schema.json github_schema github_operations.py github_operations.gql
