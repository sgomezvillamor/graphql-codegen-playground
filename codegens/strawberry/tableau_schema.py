import strawberry
from datetime import datetime
from enum import Enum

@strawberry.type(description="""
A Directive provides a way to describe alternate runtime execution and type validation behavior in a GraphQL document.

In some cases, you need to provide options to alter GraphQL's execution behavior in ways field arguments will not suffice, such as conditionally including or skipping a field. Directives provide this by describing additional information to the executor.
""")
class __Directive:
    name: str
    description: str | None
    is_repeatable: bool
    locations: list[__DirectiveLocation]
    args: list[__InputValue]

@strawberry.enum
class __DirectiveLocation(Enum):
    QUERY = "QUERY"
    MUTATION = "MUTATION"
    SUBSCRIPTION = "SUBSCRIPTION"
    FIELD = "FIELD"
    FRAGMENT_DEFINITION = "FRAGMENT_DEFINITION"
    FRAGMENT_SPREAD = "FRAGMENT_SPREAD"
    INLINE_FRAGMENT = "INLINE_FRAGMENT"
    VARIABLE_DEFINITION = "VARIABLE_DEFINITION"
    SCHEMA = "SCHEMA"
    SCALAR = "SCALAR"
    OBJECT = "OBJECT"
    FIELD_DEFINITION = "FIELD_DEFINITION"
    ARGUMENT_DEFINITION = "ARGUMENT_DEFINITION"
    INTERFACE = "INTERFACE"
    UNION = "UNION"
    ENUM = "ENUM"
    ENUM_VALUE = "ENUM_VALUE"
    INPUT_OBJECT = "INPUT_OBJECT"
    INPUT_FIELD_DEFINITION = "INPUT_FIELD_DEFINITION"

@strawberry.type(description="One possible value for a given Enum. Enum values are unique values, not a placeholder for a string or numeric value. However an Enum value is returned in a JSON response as a string.")
class __EnumValue:
    name: str
    description: str | None
    is_deprecated: bool
    deprecation_reason: str | None

@strawberry.type(description="Object and Interface types are described by a list of Fields, each of which has a name, potentially a list of arguments, and a return type.")
class __Field:
    name: str
    description: str | None
    args: list[__InputValue]
    type: __Type
    is_deprecated: bool
    deprecation_reason: str | None

@strawberry.type(description="Arguments provided to Fields or Directives and the input fields of an InputObject are represented as Input Values which describe their type and optionally a default value.")
class __InputValue:
    name: str
    description: str | None
    type: __Type
    default_value: str | None = strawberry.field(description="A GraphQL-formatted string representing the default value for this input value.")
    is_deprecated: bool
    deprecation_reason: str | None

@strawberry.type(description="A GraphQL Schema defines the capabilities of a GraphQL server. It exposes all available types and directives on the server, as well as the entry points for query, mutation, and subscription operations.")
class __Schema:
    description: str | None
    types: list[__Type] = strawberry.field(description="A list of all types supported by this server.")
    query_type: __Type = strawberry.field(description="The type that query operations will be rooted at.")
    mutation_type: __Type | None = strawberry.field(description="If this server supports mutation, the type that mutation operations will be rooted at.")
    subscription_type: __Type | None = strawberry.field(description="If this server support subscription, the type that subscription operations will be rooted at.")
    directives: list[__Directive] = strawberry.field(description="A list of all directives supported by this server.")

@strawberry.type(description="""
The fundamental unit of any GraphQL Schema is the type. There are many kinds of types in GraphQL as represented by the `__TypeKind` enum.

Depending on the kind of a type, certain fields describe information about that type. Scalar types provide no information beyond a name, description and optional `specifiedByURL`, while Enum types provide their values. Object and Interface types provide the fields they describe. Abstract types, Union and Interface, provide the Object types possible at runtime. List and NonNull types compose other types.
""")
class __Type:
    kind: __TypeKind
    name: str | None
    description: str | None
    specified_by_url: str | None
    fields: list[__Field] | None
    interfaces: list[__Type] | None
    possible_types: list[__Type] | None
    enum_values: list[__EnumValue] | None
    input_fields: list[__InputValue] | None
    of_type: __Type | None

@strawberry.enum
class __TypeKind(Enum):
    SCALAR = "SCALAR"
    OBJECT = "OBJECT"
    INTERFACE = "INTERFACE"
    UNION = "UNION"
    ENUM = "ENUM"
    INPUT_OBJECT = "INPUT_OBJECT"
    LIST = "LIST"
    NON_NULL = "NON_NULL"

@strawberry.interface(description="Base GraphQL type for a field containing analytics metadata")
class AnalyticsField:
    aggregation: str | None = strawberry.field(description="Default aggregation of the field, i.e. 'Sum', 'Average'. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/calculations_aggregation.html#AggFuncs")
    aggregation_param: str | None = strawberry.field(description="For the percentile aggregation, the percentile number")
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    default_format: str | None = strawberry.field(description="Default format for number or date")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    semantic_role: str | None = strawberry.field(description="For geographic data, the geographic role of the field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_geographicroles.html")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")

@strawberry.enum
class AnalyticsFieldOrderField(Enum):
    ID = "ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class AnalyticsFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: AnalyticsFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class AnalyticsField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique Identifier of object to retrieve")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique Identifier of object to retrieve")

@strawberry.type(description="Connection Type for AnalyticsField")
class AnalyticsFieldsConnection:
    nodes: list[AnalyticsField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="AskDataExtensions to base Tableau functionality.")
class AskDataExtension:
    dashboard: Dashboard | None = strawberry.field(description="The dashboard that contains this askData extension")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API")
    lens: Lens | None = strawberry.field(description="Lens configured for the askData extension")

@strawberry.enum
class AskDataExtensionOrderField(Enum):
    ID = "ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class AskDataExtensionSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: AskDataExtensionOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class AskDataExtension_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API")

@strawberry.input(description="Filter by GraphQL field and given value")
class AskDataExtension_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API")

@strawberry.type(description="Connection Type for AskDataExtension")
class AskDataExtensionsConnection:
    nodes: list[AskDataExtension] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.interface(description="Base GraphQL type for a field containing data. Most types of Fields will implement this interface with exceptions like HierarchyField.")
class DataField:
    data_category: FieldRoleCategory | None = strawberry.field(description="Data category of the field")
    data_type: FieldDataType | None = strawberry.field(description="Type of the data in the field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.html")
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    role: FieldRole | None = strawberry.field(description="Role of the field: 'dimension', 'measure' or 'unknown'")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")

@strawberry.interface(description="Base GraphQL type for a field")
class Field:
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    description: str | None = strawberry.field(description="Description of field shown in server and desktop clients")
    description_inherited: list[InheritedStringResult | None] | None = strawberry.field(description="description that is shown in the Tableau UI")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    downstream_columns: list[Column] = strawberry.field(description="Columns downstream of this field")
    downstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns downstream of this field")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this field")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this field")
    downstream_datasources: list[PublishedDatasource] | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_fields: list[Field] = strawberry.field(description="Downstream fields that reference this field")
    downstream_fields_connection: FieldsConnection | None = strawberry.field(description="Downstream fields that reference this field")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this field")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this field")
    downstream_lenses: list[Lens] | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metrics: list[Metric] | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_owners: list[TableauUser] | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected downstream from the field")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected downstream from the field")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this field")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this field")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream of this field")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream of this field")
    downstream_workbooks: list[Workbook] | None = strawberry.field(description="Workbooks connected downstream from the field")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected downstream from the field")
    folder_name: str | None = strawberry.field(description="Name of folder if the field is in a folder. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_dwfeatures.html#Organize")
    fully_qualified_name: str | None = strawberry.field(description="Name internally used to uniquely identify fields")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    name: str | None = strawberry.field(description="Name shown in server")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")
    upstream_columns: list[Column | None] = strawberry.field(description="All upstream columns this field references")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="All upstream columns this field references")
    upstream_databases: list[Database] = strawberry.field(description="Databases connected upstream from the field")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases connected upstream from the field")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this field")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this field")
    upstream_fields: list[Field | None] = strawberry.field(description="fields that are upstream of this field")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this field")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the field")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the field")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables connected upstream from the field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables connected upstream from the field")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this field")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this field")

@strawberry.interface(description="Base GraphQL type for a field that references another field. For example, a CalculatedField can reference a ColumnField in its formula.")
class FieldReferencingField:
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    fields: list[Field] = strawberry.field(description="Fields referenced by this field")
    fields_connection: FieldsConnection | None = strawberry.field(description="Fields referenced by this field")
    fully_qualified_name: str | None = strawberry.field(description="Name internally used to uniquely identify fields")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")
    upstream_databases: list[Database] = strawberry.field(description="Databases connected upstream from the field")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases connected upstream from the field")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the field")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the field")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables connected upstream from the field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables connected upstream from the field")

@strawberry.interface(description="Inheritance target")
class Node:
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")

@strawberry.enum
class BinFieldOrderField(Enum):
    DATA_CATEGORY = "DATA_CATEGORY"
    DATA_TYPE = "DATA_TYPE"
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"
    IS_HIDDEN = "IS_HIDDEN"
    NAME = "NAME"
    ROLE = "ROLE"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class BinFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: BinFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class BinField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    is_hidden_within: list[bool | None] | None = strawberry.field(description="True if the field is hidden")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.input(description="Filter by GraphQL field and given value")
class BinField_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for BinField")
class BinFieldsConnection:
    nodes: list[BinField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class CalculatedFieldOrderField(Enum):
    DATA_CATEGORY = "DATA_CATEGORY"
    DATA_TYPE = "DATA_TYPE"
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"
    IS_HIDDEN = "IS_HIDDEN"
    NAME = "NAME"
    ROLE = "ROLE"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class CalculatedFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: CalculatedFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class CalculatedField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    is_hidden_within: list[bool | None] | None = strawberry.field(description="True if the field is hidden")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.input(description="Filter by GraphQL field and given value")
class CalculatedField_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for CalculatedField")
class CalculatedFieldsConnection:
    nodes: list[CalculatedField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.interface(description="""
A content item that can have labels.  
*Available in Tableau Cloud March 2023 / Server 2023.1 and later.*
""")
class CanHaveLabels:
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    labels: list[Label] = strawberry.field(description="The labels on a content item. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a content item. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="The name of the asset")

@strawberry.enum
class CanHaveLabelsOrderField(Enum):
    ID = "ID"
    LUID = "LUID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class CanHaveLabelsSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: CanHaveLabelsOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class CanHaveLabels_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")

@strawberry.type(description="Connection Type for CanHaveLabels")
class CanHaveLabelsesConnection:
    nodes: list[CanHaveLabels] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.interface(description="A content item that can be certified")
class Certifiable:
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="The data quality certifications on a content item")
    data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications on a content item")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    is_certified: bool = strawberry.field(description="True if this content item contains an active data quality certification")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="The name of the asset")

@strawberry.enum
class CertifiableOrderField(Enum):
    ID = "ID"
    IS_CERTIFIED = "IS_CERTIFIED"
    LUID = "LUID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class CertifiableSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: CertifiableOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Certifiable_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    is_certified: bool | None = strawberry.field(description="True if this content item contains an active data quality certification")
    is_certified_within: list[bool | None] | None = strawberry.field(description="True if this content item contains an active data quality certification")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")

@strawberry.type(description="Connection Type for Certifiable")
class CertifiablesConnection:
    nodes: list[Certifiable] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.interface(description="A database containing tables")
class Database:
    certification_note: str | None = strawberry.field(description="Notes related to this database being marked as certified")
    certifier: TableauUser | None = strawberry.field(description="User who marked this database as certified")
    connection_type: str | None = strawberry.field(description="Connection type shortname")
    contact: TableauUser | None = strawberry.field(description="Contact for this database")
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="The data quality certifications on a database")
    data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications on a database")
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="The optional data quality warning on a database")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a database")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a database")
    description: str | None = strawberry.field(description="User modifiable description of this database")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected to the database")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected to the database")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this database")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this database")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published datasources connected to the database")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published datasources connected to the database")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this database")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this database")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses connected to the database")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected to the database")
    downstream_metric_definitions: list[MetricDefinition | None] = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics connected to the database")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected to the database")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners connected to the database")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners connected to the database")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected to the database")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected to the database")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this database")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this database")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks connected to the database")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected to the database")
    has_active_warning: bool = strawberry.field(description="True if the database has an active data quality warning")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool = strawberry.field(description="True if this database contains an active data quality certification")
    is_controlled_permissions_enabled: bool | None = strawberry.field(description="True if this database has its permission locked")
    is_embedded: bool | None = strawberry.field(description="True if this database is embedded in Tableau content, e.g., a packaged workbook")
    is_grouped: bool | None = strawberry.field(description="True if this database has been grouped with other databases")
    labels: list[Label] = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_vizportal_url_id: str | None = strawberry.field(description="The ID of the project in which the database is visible. Will be empty if the database is not in a project.")
    referenced_by_queries: list[CustomSQLTable | None] | None = strawberry.field(description="The custom SQL queries that reference this database")
    referenced_by_queries_connection: CustomSQLTablesConnection | None = strawberry.field(description="The custom SQL queries that reference this database")
    tables: list[DatabaseTable | None] | None = strawberry.field(description="Tables belonging to this database")
    tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables belonging to this database")
    tags: list[Tag] = strawberry.field(description="Tags associated with the database")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the database")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream of this database")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream of this database")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this database")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this database")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream of this database")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream of this database")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream of this database")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream of this database")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this database, for use in client-to-server communications")

@strawberry.interface(description="A content item that has a list of tags")
class Taggable:
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="The name of the asset")
    tags: list[Tag] = strawberry.field(description="Tags associated with the content item")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the content item")

@strawberry.interface(description="A content item that can have data quality warnings")
class Warnable:
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="The optional data quality warning on a content item")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a content item")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a content item")
    has_active_warning: bool = strawberry.field(description="True if the content has an active data quality warning")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="The name of the asset")

@strawberry.enum
class CloudFileOrderField(Enum):
    CONNECTION_TYPE = "CONNECTION_TYPE"
    DOWNSTREAM_DATASOURCES_COUNT = "DOWNSTREAM_DATASOURCES_COUNT"
    DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT = "DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    IS_CERTIFIED = "IS_CERTIFIED"
    IS_EMBEDDED = "IS_EMBEDDED"
    LUID = "LUID"
    NAME = "NAME"
    PROJECT_NAME = "PROJECT_NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class CloudFileSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: CloudFileOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class CloudFile_Filter:
    connection_type: str | None = strawberry.field(description="Connection type shortname")
    connection_type_within: list[str | None] | None = strawberry.field(description="Connection type shortname")
    has_active_warning: bool | None = strawberry.field(description="True if the database has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the database has an active data quality warning")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_certified_within: list[bool | None] | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_embedded: bool | None = strawberry.field(description="True if this file is embedded in Tableau content, e.g., a packaged workbook")
    is_embedded_within: list[bool | None] | None = strawberry.field(description="True if this file is embedded in Tableau content, e.g., a packaged workbook")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.type(description="Connection Type for CloudFile")
class CloudFilesConnection:
    nodes: list[CloudFile] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class ColumnFieldOrderField(Enum):
    DATA_CATEGORY = "DATA_CATEGORY"
    DATA_TYPE = "DATA_TYPE"
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    ID = "ID"
    IS_HIDDEN = "IS_HIDDEN"
    NAME = "NAME"
    ROLE = "ROLE"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class ColumnFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: ColumnFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class ColumnField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    is_hidden_within: list[bool | None] | None = strawberry.field(description="True if the field is hidden")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.input(description="Filter by GraphQL field and given value")
class ColumnField_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for ColumnField")
class ColumnFieldsConnection:
    nodes: list[ColumnField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class ColumnOrderField(Enum):
    DISPLAY_NAME = "DISPLAY_NAME"
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    LUID = "LUID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class ColumnSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: ColumnOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Column_Filter:
    display_name: str | None = strawberry.field(description="Optional display name for column")
    display_name_within: list[str | None] | None = strawberry.field(description="Optional display name for column")
    has_active_warning: bool | None = strawberry.field(description="True if this column has an active data quality warning. Available in Tableau Cloud October 2022 / Server 2022.3 and later.")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if this column has an active data quality warning. Available in Tableau Cloud October 2022 / Server 2022.3 and later.")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name of column")
    name_within: list[str | None] | None = strawberry.field(description="Name of column")

@strawberry.input(description="Filter by GraphQL field and given value")
class Column_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name of column")
    name_within: list[str | None] | None = strawberry.field(description="Name of column")

@strawberry.type(description="Connection Type for Column")
class ColumnsConnection:
    nodes: list[Column] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class CombinedFieldOrderField(Enum):
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"
    IS_HIDDEN = "IS_HIDDEN"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class CombinedFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: CombinedFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class CombinedField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    is_hidden_within: list[bool | None] | None = strawberry.field(description="True if the field is hidden")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.input(description="Filter by GraphQL field and given value")
class CombinedField_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for CombinedField")
class CombinedFieldsConnection:
    nodes: list[CombinedField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class CombinedSetFieldOrderField(Enum):
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"
    IS_HIDDEN = "IS_HIDDEN"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class CombinedSetFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: CombinedSetFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class CombinedSetField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    is_hidden_within: list[bool | None] | None = strawberry.field(description="True if the field is hidden")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.input(description="Filter by GraphQL field and given value")
class CombinedSetField_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for CombinedSetField")
class CombinedSetFieldsConnection:
    nodes: list[CombinedSetField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.interface(description="A table containing columns")
class Table:
    columns: list[Column] = strawberry.field(description="Columns contained in this table")
    columns_connection: ColumnsConnection | None = strawberry.field(description="Columns contained in this table")
    description: str | None = strawberry.field(description="User modifiable description of this table")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected to the table")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected to the table")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this table")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this table")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published datasources connected to the table")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published datasources connected to the table")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this table")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this table")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses connected downstream from the table")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from the table")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics connected to the table")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected to the table")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners of workbooks and published datasources connected to the table")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners of workbooks and published datasources connected to the table")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected to the table")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected to the table")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this table")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this table")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this table")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this table")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection downstream of this table")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection downstream of this table")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks connected to the table")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected to the table")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_embedded: bool | None = strawberry.field(description="True if this table is embedded in Tableau content, e.g., a packaged workbook")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream of this table")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream of this table")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this table")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this table")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream of this table")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream of this table")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream of this table")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream of this table")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this table")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this table")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this table")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this table")

@strawberry.enum
class CustomSQLTableOrderField(Enum):
    COLUMNS_COUNT = "COLUMNS_COUNT"
    DOWNSTREAM_DASHBOARDS_COUNT = "DOWNSTREAM_DASHBOARDS_COUNT"
    DOWNSTREAM_DATASOURCES_COUNT = "DOWNSTREAM_DATASOURCES_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    ID = "ID"
    IS_UNSUPPORTED_CUSTOM_SQL = "IS_UNSUPPORTED_CUSTOM_SQL"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class CustomSQLTableSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: CustomSQLTableOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class CustomSQLTable_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_unsupported_custom_sql: bool | None = strawberry.field(description="True if the query is unsupported by Tableau Catalog, in which case lineage may be incomplete")
    is_unsupported_custom_sql_within: list[bool | None] | None = strawberry.field(description="True if the query is unsupported by Tableau Catalog, in which case lineage may be incomplete")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.type(description="Connection Type for CustomSQLTable")
class CustomSQLTablesConnection:
    nodes: list[CustomSQLTable] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.interface(description="A view contained in a published workbook. Views can be sheets or dashboards.")
class View:
    created_at: datetime = strawberry.field(description="Time the view was created")
    document_view_id: str | None = strawberry.field(description="Unique ID for the view generated for and stored within the workbook, survives renames, and is used for internal processes")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    index: int | None = strawberry.field(description="Index of view; the order it appears in the workbook")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server (Blank if sheet is hidden in Workbook)")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    path: str | None = strawberry.field(description="Server path to view")
    referenced_by_metrics: list[Metric | None] | None = strawberry.field(description="The Metrics that reference this View")
    referenced_by_metrics_connection: MetricsConnection | None = strawberry.field(description="The Metrics that reference this View")
    tags: list[Tag] = strawberry.field(description="Tags associated with the view")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the view")
    updated_at: datetime = strawberry.field(description="Time the view was updated")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this view")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this view")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this view. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this view. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    workbook: Workbook | None = strawberry.field(description="The workbook that contains this view")

@strawberry.enum
class DashboardOrderField(Enum):
    DOCUMENT_VIEW_ID = "DOCUMENT_VIEW_ID"
    ID = "ID"
    LUID = "LUID"
    NAME = "NAME"
    PATH = "PATH"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class DashboardSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: DashboardOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Dashboard_Filter:
    document_view_id: str | None = strawberry.field(description="Unique ID for the dashboard generated for and stored within the workbook, survives renames, and is used for internal processes")
    document_view_id_within: list[str | None] | None = strawberry.field(description="Unique ID for the dashboard generated for and stored within the workbook, survives renames, and is used for internal processes")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server (Blank if worksheet is hidden in Workbook)")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server (Blank if worksheet is hidden in Workbook)")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    path: str | None = strawberry.field(description="Server path to dashboard")
    path_within: list[str | None] | None = strawberry.field(description="Server path to dashboard")

@strawberry.type(description="Connection Type for Dashboard")
class DashboardsConnection:
    nodes: list[Dashboard] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class DataCloudOrderField(Enum):
    CONNECTION_TYPE = "CONNECTION_TYPE"
    DOWNSTREAM_DATASOURCES_COUNT = "DOWNSTREAM_DATASOURCES_COUNT"
    DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT = "DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    IS_CERTIFIED = "IS_CERTIFIED"
    IS_EMBEDDED = "IS_EMBEDDED"
    LUID = "LUID"
    NAME = "NAME"
    PROJECT_NAME = "PROJECT_NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class DataCloudSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: DataCloudOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class DataCloud_Filter:
    connection_type: str | None = strawberry.field(description="Connection type shortname")
    connection_type_within: list[str | None] | None = strawberry.field(description="Connection type shortname")
    has_active_warning: bool | None = strawberry.field(description="True if the database has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the database has an active data quality warning")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used with the Metadata API.  Not the same as the locally unique identifier used with the REST API.")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used with the Metadata API.  Not the same as the locally unique identifier used with the REST API.")
    is_certified: bool | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_certified_within: list[bool | None] | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_embedded: bool | None = strawberry.field(description="True if this database is embedded in Tableau content, e.g., a packaged workbook")
    is_embedded_within: list[bool | None] | None = strawberry.field(description="True if this database is embedded in Tableau content, e.g., a packaged workbook")
    luid: str | None = strawberry.field(description="Locally unique identifier used with the REST API.")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used with the REST API.")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.type(description="Connection Type for DataCloud")
class DataCloudsConnection:
    nodes: list[DataCloud] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class DataFieldOrderField(Enum):
    DATA_CATEGORY = "DATA_CATEGORY"
    DATA_TYPE = "DATA_TYPE"
    ID = "ID"
    ROLE = "ROLE"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class DataFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: DataFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class DataField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique Identifier of object to retrieve")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique Identifier of object to retrieve")

@strawberry.type(description="Connection Type for DataField")
class DataFieldsConnection:
    nodes: list[DataField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.interface(description="""
A label that can be attached to assets.  
*Available in Tableau Cloud March 2023 / Server 2023.1 and later.*
""")
class Label:
    asset: CanHaveLabels | None = strawberry.field(description="The asset that contains the label")
    author: TableauUser | None = strawberry.field(description="User who last updated this label")
    author_display_name: str | None = strawberry.field(description="Name of the user who last updated this label")
    category: str = strawberry.field(description="Category of the label")
    created_at: datetime = strawberry.field(description="Time the label was created")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    is_active: bool = strawberry.field(description="True if the label is active")
    is_elevated: bool = strawberry.field(description="True if the label is elevated")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    message: str | None = strawberry.field(description="Message of the label")
    updated_at: datetime = strawberry.field(description="Time the label was last updated")
    value: str = strawberry.field(description="Value of the label")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this label, for use in client-to-server communications")

@strawberry.enum
class DataQualityCertificationOrderField(Enum):
    CATEGORY = "CATEGORY"
    ID = "ID"
    IS_ACTIVE = "IS_ACTIVE"
    IS_ELEVATED = "IS_ELEVATED"
    LUID = "LUID"
    VALUE = "VALUE"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class DataQualityCertificationSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: DataQualityCertificationOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class DataQualityCertification_Filter:
    category: str | None = strawberry.field(description="Category of the label")
    category_within: list[str | None] | None = strawberry.field(description="Category of the label")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    is_active: bool | None = strawberry.field(description="True if the data quality certification is active")
    is_active_within: list[bool | None] | None = strawberry.field(description="True if the data quality certification is active")
    is_elevated: bool | None = strawberry.field(description="True if the data quality certification is elevated")
    is_elevated_within: list[bool | None] | None = strawberry.field(description="True if the data quality certification is elevated")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    value: str | None = strawberry.field(description="Value of the label")
    value_within: list[str | None] | None = strawberry.field(description="Value of the label")

@strawberry.type(description="Connection Type for DataQualityCertification")
class DataQualityCertificationsConnection:
    nodes: list[DataQualityCertification] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class DataQualityWarningOrderField(Enum):
    CATEGORY = "CATEGORY"
    ID = "ID"
    IS_ACTIVE = "IS_ACTIVE"
    IS_ELEVATED = "IS_ELEVATED"
    IS_SEVERE = "IS_SEVERE"
    LUID = "LUID"
    VALUE = "VALUE"
    WARNING_TYPE = "WARNING_TYPE"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class DataQualityWarningSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: DataQualityWarningOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class DataQualityWarning_Filter:
    category: str | None = strawberry.field(description="Category of the label")
    category_within: list[str | None] | None = strawberry.field(description="Category of the label")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    is_active: bool | None = strawberry.field(description="True if the data quality warning is active")
    is_active_within: list[bool | None] | None = strawberry.field(description="True if the data quality warning is active")
    is_elevated: bool | None = strawberry.field(description="True if the data quality warning is elevated")
    is_elevated_within: list[bool | None] | None = strawberry.field(description="True if the data quality warning is elevated")
    is_severe: bool | None = strawberry.field(description="Synonymous with isElevated")
    is_severe_within: list[bool | None] | None = strawberry.field(description="Synonymous with isElevated")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    value: str | None = strawberry.field(description="Value of the label")
    value_within: list[str | None] | None = strawberry.field(description="Value of the label")
    warning_type: str | None = strawberry.field(description="Synonymous with value")
    warning_type_within: list[str | None] | None = strawberry.field(description="Synonymous with value")

@strawberry.type(description="Connection Type for DataQualityWarning")
class DataQualityWarningsConnection:
    nodes: list[DataQualityWarning] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class DatabaseOrderField(Enum):
    CONNECTION_TYPE = "CONNECTION_TYPE"
    DOWNSTREAM_DATASOURCES_COUNT = "DOWNSTREAM_DATASOURCES_COUNT"
    DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT = "DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    IS_CERTIFIED = "IS_CERTIFIED"
    IS_EMBEDDED = "IS_EMBEDDED"
    LUID = "LUID"
    NAME = "NAME"
    PROJECT_NAME = "PROJECT_NAME"

@strawberry.enum
class DatabaseServerOrderField(Enum):
    CONNECTION_TYPE = "CONNECTION_TYPE"
    DOWNSTREAM_DATASOURCES_COUNT = "DOWNSTREAM_DATASOURCES_COUNT"
    DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT = "DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    HOST_NAME = "HOST_NAME"
    ID = "ID"
    IS_CERTIFIED = "IS_CERTIFIED"
    IS_EMBEDDED = "IS_EMBEDDED"
    LUID = "LUID"
    NAME = "NAME"
    PROJECT_NAME = "PROJECT_NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class DatabaseServerSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: DatabaseServerOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class DatabaseServer_Filter:
    connection_type: str | None = strawberry.field(description="Connection type shortname")
    connection_type_within: list[str | None] | None = strawberry.field(description="Connection type shortname")
    has_active_warning: bool | None = strawberry.field(description="True if the database has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the database has an active data quality warning")
    host_name: str | None = strawberry.field(description="Hostname of the database")
    host_name_within: list[str | None] | None = strawberry.field(description="Hostname of the database")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_certified_within: list[bool | None] | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_embedded: bool | None = strawberry.field(description="A database server is never embedded in Tableau content")
    is_embedded_within: list[bool | None] | None = strawberry.field(description="A database server is never embedded in Tableau content")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.type(description="Connection Type for DatabaseServer")
class DatabaseServersConnection:
    nodes: list[DatabaseServer] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class DatabaseSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: DatabaseOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.enum
class DatabaseTableOrderField(Enum):
    COLUMNS_COUNT = "COLUMNS_COUNT"
    CONNECTION_TYPE = "CONNECTION_TYPE"
    DOWNSTREAM_DASHBOARDS_COUNT = "DOWNSTREAM_DASHBOARDS_COUNT"
    DOWNSTREAM_DATASOURCES_COUNT = "DOWNSTREAM_DATASOURCES_COUNT"
    DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT = "DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    FULL_NAME = "FULL_NAME"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    IS_CERTIFIED = "IS_CERTIFIED"
    IS_EMBEDDED = "IS_EMBEDDED"
    LUID = "LUID"
    NAME = "NAME"
    PROJECT_NAME = "PROJECT_NAME"
    SCHEMA = "SCHEMA"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class DatabaseTableSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: DatabaseTableOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class DatabaseTable_Filter:
    connection_type: str | None = strawberry.field(description="Connection type of parent database")
    connection_type_within: list[str | None] | None = strawberry.field(description="Connection type of parent database")
    full_name: str | None = strawberry.field(description="Fully qualified table name")
    full_name_within: list[str | None] | None = strawberry.field(description="Fully qualified table name")
    has_active_warning: bool | None = strawberry.field(description="True if the table has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the table has an active data quality warning")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool | None = strawberry.field(description="True if this table contains an active data quality certification")
    is_certified_within: list[bool | None] | None = strawberry.field(description="True if this table contains an active data quality certification")
    is_embedded: bool | None = strawberry.field(description="True if this table is embedded in Tableau content")
    is_embedded_within: list[bool | None] | None = strawberry.field(description="True if this table is embedded in Tableau content")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the table is visible. Will be empty if the table is not in a project.")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project in which the table is visible. Will be empty if the table is not in a project.")
    schema: str | None = strawberry.field(description="""
Name of table schema.
    
Note: For some databases, such as Amazon Athena and Exasol, the schema attribute may not return the correct schema name for the table. For more information, see https://help.tableau.com/current/api/metadata_api/en-us/docs/meta_api_model.html#schema_attribute.
""")
    schema_within: list[str | None] | None = strawberry.field(description="""
Name of table schema.
    
Note: For some databases, such as Amazon Athena and Exasol, the schema attribute may not return the correct schema name for the table. For more information, see https://help.tableau.com/current/api/metadata_api/en-us/docs/meta_api_model.html#schema_attribute.
""")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.type(description="Connection Type for DatabaseTable")
class DatabaseTablesConnection:
    nodes: list[DatabaseTable] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.input(description="Filter by GraphQL field and given value")
class Database_Filter:
    connection_type: str | None = strawberry.field(description="Connection type shortname")
    connection_type_within: list[str | None] | None = strawberry.field(description="Connection type shortname")
    has_active_warning: bool | None = strawberry.field(description="True if the database has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the database has an active data quality warning")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_certified_within: list[bool | None] | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_embedded: bool | None = strawberry.field(description="True if this database is embedded in Tableau content, e.g., a packaged workbook")
    is_embedded_within: list[bool | None] | None = strawberry.field(description="True if this database is embedded in Tableau content, e.g., a packaged workbook")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.type(description="Connection Type for Database")
class DatabasesConnection:
    nodes: list[Database] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.interface(description="""
Root GraphQL type for embedded and published data sources

Data sources are a way to represent how Tableau Desktop and Tableau Server model and connect to data. Data sources can be published separately, as a published data source, or may be contained in a workbook as an embedded data source.

See https://onlinehelp.tableau.com/current/server/en-us/datasource.htm
""")
class Datasource:
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    created_at: datetime | None = strawberry.field(description="Time the datasource was created. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    datasource_filters: list[DatasourceFilter] = strawberry.field(description="Data source filters contained in this data source")
    datasource_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="Data source filters contained in this data source")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards downstream from this data source")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards downstream from this data source")
    downstream_owners: list[TableauUser] = strawberry.field(description="Workbook owners downstream from this data source")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners downstream from this data source")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets downstream from this data source")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets downstream from this data source")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks downstream from this data source")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks downstream from this data source")
    extract_last_incremental_update_time: datetime | None = strawberry.field(description="Time an extract was last incrementally updated")
    extract_last_refresh_time: datetime | None = strawberry.field(description="Time an extract was last fully refreshed")
    extract_last_update_time: datetime | None = strawberry.field(description="Time an extract was last updated by either a full refresh, incremental update, or creation")
    fields: list[Field] = strawberry.field(description="Fields usable in workbooks connected to this data source")
    fields_connection: FieldsConnection | None = strawberry.field(description="Fields usable in workbooks connected to this data source")
    has_extracts: bool | None = strawberry.field(description="True if datasource contains extracted data")
    has_user_reference: bool | None = strawberry.field(description="True if data source contains a formula that involves a user function (for example, USERNAME or ISMEMBEROF)")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    lenses: list[Lens | None] | None = strawberry.field(description="The lenses derived from this datasource")
    lenses_connection: LensesConnection | None = strawberry.field(description="The lenses derived from this datasource")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    updated_at: datetime | None = strawberry.field(description="Time the datasource was last updated. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream from this data source")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream from this data source")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream from this data source")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream from this data source")

@strawberry.enum
class DatasourceFieldOrderField(Enum):
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    ID = "ID"
    IS_HIDDEN = "IS_HIDDEN"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class DatasourceFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: DatasourceFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class DatasourceField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    is_hidden_within: list[bool | None] | None = strawberry.field(description="True if the field is hidden")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.input(description="Filter by GraphQL field and given value")
class DatasourceField_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for DatasourceField")
class DatasourceFieldsConnection:
    nodes: list[DatasourceField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="""
Data source filters include/exclude certain values from a single field to filter out rows of data from this data source. For data security reasons, we don't track the values used in the filter in this schema, but you can see the field used in the filter.

See https://onlinehelp.tableau.com/current/pro/desktop/en-us/filtering_datasource.html
""")
class DatasourceFilter:
    datasource: Datasource | None = strawberry.field(description="Data source that contains this datasource filter")
    field: Field = strawberry.field(description="Field used by this filter.")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")

@strawberry.enum
class DatasourceFilterOrderField(Enum):
    ID = "ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class DatasourceFilterSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: DatasourceFilterOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class DatasourceFilter_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")

@strawberry.type(description="Connection Type for DatasourceFilter")
class DatasourceFiltersConnection:
    nodes: list[DatasourceFilter] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class DatasourceOrderField(Enum):
    CONTAINS_UNSUPPORTED_CUSTOM_SQL = "CONTAINS_UNSUPPORTED_CUSTOM_SQL"
    DOWNSTREAM_OWNERS_COUNT = "DOWNSTREAM_OWNERS_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class DatasourceSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: DatasourceOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Datasource_Filter:
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    contains_unsupported_custom_sql_within: list[bool | None] | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for Datasource")
class DatasourcesConnection:
    nodes: list[Datasource] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class EmbeddedDatasourceOrderField(Enum):
    CONTAINS_UNSUPPORTED_CUSTOM_SQL = "CONTAINS_UNSUPPORTED_CUSTOM_SQL"
    DOWNSTREAM_OWNERS_COUNT = "DOWNSTREAM_OWNERS_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class EmbeddedDatasourceSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: EmbeddedDatasourceOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class EmbeddedDatasource_Filter:
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    contains_unsupported_custom_sql_within: list[bool | None] | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for EmbeddedDatasource")
class EmbeddedDatasourcesConnection:
    nodes: list[EmbeddedDatasource] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class ExtractType(Enum):
    FULL = "FULL"
    INCREMENTAL = "INCREMENTAL"

@strawberry.input(description="Filter by GraphQL field and given value")
class ExtractType_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique Identifier of object to retrieve")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique Identifier of object to retrieve")

@strawberry.enum
class FieldDataType(Enum):
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    DATETIME = "DATETIME"
    INTEGER = "INTEGER"
    REAL = "REAL"
    SPATIAL = "SPATIAL"
    STRING = "STRING"
    TABLE = "TABLE"
    TUPLE = "TUPLE"
    UNKNOWN = "UNKNOWN"

@strawberry.input(description="Filter by GraphQL field and given value")
class FieldDataType_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique Identifier of object to retrieve")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique Identifier of object to retrieve")

@strawberry.enum
class FieldOrderField(Enum):
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    ID = "ID"
    IS_HIDDEN = "IS_HIDDEN"
    NAME = "NAME"

@strawberry.enum
class FieldReferencingFieldOrderField(Enum):
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class FieldReferencingFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: FieldReferencingFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class FieldReferencingField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique Identifier of object to retrieve")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique Identifier of object to retrieve")

@strawberry.type(description="Connection Type for FieldReferencingField")
class FieldReferencingFieldsConnection:
    nodes: list[FieldReferencingField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class FieldRole(Enum):
    DIMENSION = "DIMENSION"
    MEASURE = "MEASURE"
    UNKNOWN = "UNKNOWN"

@strawberry.enum
class FieldRoleCategory(Enum):
    NOMINAL = "NOMINAL"
    ORDINAL = "ORDINAL"
    QUANTITATIVE = "QUANTITATIVE"
    UNKNOWN = "UNKNOWN"

@strawberry.input(description="Filter by GraphQL field and given value")
class FieldRoleCategory_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique Identifier of object to retrieve")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique Identifier of object to retrieve")

@strawberry.input(description="Filter by GraphQL field and given value")
class FieldRole_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique Identifier of object to retrieve")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique Identifier of object to retrieve")

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class FieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: FieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Field_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    is_hidden_within: list[bool | None] | None = strawberry.field(description="True if the field is hidden")
    name: str | None = strawberry.field(description="Name shown in server")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.input(description="Filter by GraphQL field and given value")
class Field_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server")

@strawberry.type(description="Connection Type for Field")
class FieldsConnection:
    nodes: list[Field] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class FileOrderField(Enum):
    CONNECTION_TYPE = "CONNECTION_TYPE"
    DOWNSTREAM_DATASOURCES_COUNT = "DOWNSTREAM_DATASOURCES_COUNT"
    DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT = "DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    IS_CERTIFIED = "IS_CERTIFIED"
    IS_EMBEDDED = "IS_EMBEDDED"
    LUID = "LUID"
    NAME = "NAME"
    PROJECT_NAME = "PROJECT_NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class FileSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: FileOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class File_Filter:
    connection_type: str | None = strawberry.field(description="Connection type shortname")
    connection_type_within: list[str | None] | None = strawberry.field(description="Connection type shortname")
    has_active_warning: bool | None = strawberry.field(description="True if the database has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the database has an active data quality warning")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_certified_within: list[bool | None] | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_embedded: bool | None = strawberry.field(description="True if this file is embedded in Tableau content, e.g., a packaged workbook")
    is_embedded_within: list[bool | None] | None = strawberry.field(description="True if this file is embedded in Tableau content, e.g., a packaged workbook")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.type(description="Connection Type for File")
class FilesConnection:
    nodes: list[File] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.interface(description="A wrapper for an input field contained in a published flow.")
class FlowInputField:
    child_fields: list[FlowOutputField] = strawberry.field(description="Fields that are children of this field")
    child_fields_connection: FlowOutputFieldsConnection | None = strawberry.field(description="Fields that are children of this field")
    flow: Flow | None = strawberry.field(description="A flow to which these fields input")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    upstream_databases: list[Database] = strawberry.field(description="Databases that are upstream from this inputField.")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are upstream from this inputField.")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Flows that are upstream from this inputField.")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Flows that are upstream from this inputField.")
    upstream_flows: list[Flow] = strawberry.field(description="Flows that are upstream from this inputField.")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are upstream from this inputField.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables that are upstream of this field.")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables that are upstream of this field.")

@strawberry.enum
class FlowColumnInputFieldOrderField(Enum):
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class FlowColumnInputFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: FlowColumnInputFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class FlowColumnInputField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for FlowColumnInputField")
class FlowColumnInputFieldsConnection:
    nodes: list[FlowColumnInputField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.interface(description="A wrapper for an output field contained in a published flow.")
class FlowOutputField:
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards that are downstream from this outputField")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards that are downstream from this outputField")
    downstream_databases: list[Database] = strawberry.field(description="Databases that are downstream from this outputField")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are downstream from this outputField")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources that are downstream from this outputField")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources that are downstream from this outputField")
    downstream_flows: list[Flow] = strawberry.field(description="Flows that are downstream from this outputField")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are downstream from this outputField")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses that are downstream from this outputField")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses that are downstream from this outputField")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this flow output field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this flow output field.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics that are downstream from this outputField")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics that are downstream from this outputField")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners that are downstream from this outputField")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners that are downstream from this outputField")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets that are downstream from this outputField")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that are downstream from this outputField")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables that are downstream from this outputField")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables that are downstream from this outputField")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="VirtualConnectionTables that are downstream of this outputField")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="VirtualConnectionTables that are downstream of this outputField")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="VirtualConnections that are downstream of this outputField")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="VirtualConnections that are downstream of this outputField")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks that are downstream from this outputField")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks that are downstream from this outputField")
    flow: list[Flow | None] | None = strawberry.field(description="The flow that outputs these fields")
    flow_connection: FlowsConnection | None = strawberry.field(description="The flow that outputs these fields")
    flow_output_step: FlowOutputStep | None = strawberry.field(description="The flow output step that contains this field")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    parent_fields: list[FlowInputField] = strawberry.field(description="Fields that are parents of this field")
    parent_fields_connection: FlowInputFieldsConnection | None = strawberry.field(description="Fields that are parents of this field")
    upstream_databases: list[Database] = strawberry.field(description="Databases that are upstream from this outputField")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are upstream from this outputField")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources that are upstream from this outputField")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources that are upstream from this outputField")
    upstream_flows: list[Flow] = strawberry.field(description="Flows that are upstream from this outputField.")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are upstream from this outputField.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables that are upstream from this outputField")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables that are upstream from this outputField")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="VirtualConnectionTables that are upstream of this outputField")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="VirtualConnectionTables that are upstream of this outputField")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="VirtualConnections that are upstream of this outputField")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="VirtualConnections that are upstream of this outputField")

@strawberry.enum
class FlowColumnOutputFieldOrderField(Enum):
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class FlowColumnOutputFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: FlowColumnOutputFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class FlowColumnOutputField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for FlowColumnOutputField")
class FlowColumnOutputFieldsConnection:
    nodes: list[FlowColumnOutputField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class FlowFieldInputFieldOrderField(Enum):
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class FlowFieldInputFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: FlowFieldInputFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class FlowFieldInputField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for FlowFieldInputField")
class FlowFieldInputFieldsConnection:
    nodes: list[FlowFieldInputField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class FlowFieldOutputFieldOrderField(Enum):
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class FlowFieldOutputFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: FlowFieldOutputFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class FlowFieldOutputField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for FlowFieldOutputField")
class FlowFieldOutputFieldsConnection:
    nodes: list[FlowFieldOutputField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class FlowInputFieldOrderField(Enum):
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class FlowInputFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: FlowInputFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class FlowInputField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for FlowInputField")
class FlowInputFieldsConnection:
    nodes: list[FlowInputField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class FlowOrderField(Enum):
    CONTAINER_NAME = "CONTAINER_NAME"
    CONTAINS_UNSUPPORTED_CUSTOM_SQL = "CONTAINS_UNSUPPORTED_CUSTOM_SQL"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    LUID = "LUID"
    NAME = "NAME"
    PROJECT_NAME = "PROJECT_NAME"
    VIZPORTAL_URL_ID = "VIZPORTAL_URL_ID"

@strawberry.enum
class FlowOutputFieldOrderField(Enum):
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class FlowOutputFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: FlowOutputFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class FlowOutputField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for FlowOutputField")
class FlowOutputFieldsConnection:
    nodes: list[FlowOutputField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="A flow output step")
class FlowOutputStep:
    flow: Flow | None = strawberry.field(description="The flow that contains this output step")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    output_fields: list[FlowOutputField] = strawberry.field(description="Fields output by this step")
    output_fields_connection: FlowOutputFieldsConnection | None = strawberry.field(description="Fields output by this step")
    step_id: str | None = strawberry.field(description="Identifier internal to flow")

@strawberry.enum
class FlowOutputStepOrderField(Enum):
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class FlowOutputStepSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: FlowOutputStepOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class FlowOutputStep_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for FlowOutputStep")
class FlowOutputStepsConnection:
    nodes: list[FlowOutputStep] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class FlowSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: FlowOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Flow_Filter:
    container_name: str | None = strawberry.field(description="The name of the container in which the flow is visible and usable. Either a personal space or project.")
    container_name_within: list[str | None] | None = strawberry.field(description="The name of the container in which the flow is visible and usable. Either a personal space or project.")
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the flow contains unsupported custom SQL, in which case lineage may be incomplete")
    contains_unsupported_custom_sql_within: list[bool | None] | None = strawberry.field(description="True if the flow contains unsupported custom SQL, in which case lineage may be incomplete")
    has_active_warning: bool | None = strawberry.field(description="True if the flow has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the flow has an active data quality warning")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the flow is visible and usable")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project in which the flow is visible and usable")
    vizportal_url_id: str | None = strawberry.field(description="VizPortal URL ID; used for URL generation")
    vizportal_url_id_within: list[str | None] | None = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description="Connection Type for Flow")
class FlowsConnection:
    nodes: list[Flow] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class GenericLabelOrderField(Enum):
    CATEGORY = "CATEGORY"
    ID = "ID"
    IS_ACTIVE = "IS_ACTIVE"
    IS_ELEVATED = "IS_ELEVATED"
    LUID = "LUID"
    VALUE = "VALUE"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class GenericLabelSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: GenericLabelOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class GenericLabel_Filter:
    category: str | None = strawberry.field(description="Category of the label")
    category_within: list[str | None] | None = strawberry.field(description="Category of the label")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    is_active: bool | None = strawberry.field(description="True if the label is active")
    is_active_within: list[bool | None] | None = strawberry.field(description="True if the label is active")
    is_elevated: bool | None = strawberry.field(description="True if the label is elevated")
    is_elevated_within: list[bool | None] | None = strawberry.field(description="True if the label is elevated")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    value: str | None = strawberry.field(description="Value of the label")
    value_within: list[str | None] | None = strawberry.field(description="Value of the label")

@strawberry.type(description="Connection Type for GenericLabel")
class GenericLabelsConnection:
    nodes: list[GenericLabel] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class GroupFieldOrderField(Enum):
    DATA_CATEGORY = "DATA_CATEGORY"
    DATA_TYPE = "DATA_TYPE"
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"
    IS_HIDDEN = "IS_HIDDEN"
    NAME = "NAME"
    ROLE = "ROLE"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class GroupFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: GroupFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class GroupField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    is_hidden_within: list[bool | None] | None = strawberry.field(description="True if the field is hidden")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.input(description="Filter by GraphQL field and given value")
class GroupField_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for GroupField")
class GroupFieldsConnection:
    nodes: list[GroupField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class HierarchyFieldOrderField(Enum):
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"
    IS_HIDDEN = "IS_HIDDEN"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class HierarchyFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: HierarchyFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class HierarchyField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    is_hidden_within: list[bool | None] | None = strawberry.field(description="True if the field is hidden")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.input(description="Filter by GraphQL field and given value")
class HierarchyField_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for HierarchyField")
class HierarchyFieldsConnection:
    nodes: list[HierarchyField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class InheritanceType(Enum):
    FIRST = "FIRST"

@strawberry.type(description="Wrapper type containing the inherited result")
class InheritedStringResult:
    asset: Node | None = strawberry.field(description="The object (i.e., inheritance source) where the attribute was inherited from")
    asset_id: str = strawberry.field(description="Unique identifier of the object (i.e., inheritance source) that is providing the inherited attribute")
    attribute: str = strawberry.field(description="Name of the property that is being inherited")
    distance: int | None = strawberry.field(description="Number of edges in between the inheritance source and inheritance target")
    edges: list[str] | None = strawberry.field(description="The edges between inheritance source and inheritance target")
    value: str | None = strawberry.field(description="Inherited value")

@strawberry.enum
class LabelOrderField(Enum):
    CATEGORY = "CATEGORY"
    ID = "ID"
    IS_ACTIVE = "IS_ACTIVE"
    IS_ELEVATED = "IS_ELEVATED"
    LUID = "LUID"
    VALUE = "VALUE"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class LabelSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: LabelOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Label_Filter:
    category: str | None = strawberry.field(description="Category of the label")
    category_within: list[str | None] | None = strawberry.field(description="Category of the label")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    is_active: bool | None = strawberry.field(description="True if the label is active")
    is_active_within: list[bool | None] | None = strawberry.field(description="True if the label is active")
    is_elevated: bool | None = strawberry.field(description="True if the label is elevated")
    is_elevated_within: list[bool | None] | None = strawberry.field(description="True if the label is elevated")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    value: str | None = strawberry.field(description="Value of the label")
    value_within: list[str | None] | None = strawberry.field(description="Value of the label")

@strawberry.type(description="Connection Type for Label")
class LabelsConnection:
    nodes: list[Label] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="""
Lenses are curated, embeddable Ask Data experiences.  
*Introduced in Tableau Cloud June 2022 / Server 2022.3.*  
*Retired in Tableau Cloud February 2024 / Server 2024.2.*
""")
class Lens:
    ask_data_extensions: list[AskDataExtension | None] | None = strawberry.field(description="The lens configured in askData extension")
    ask_data_extensions_connection: AskDataExtensionsConnection | None = strawberry.field(description="The lens configured in askData extension")
    created_at: datetime = strawberry.field(description="Time the Lens was created")
    datasource: Datasource = strawberry.field(description="Datasource this lens is derived from")
    description: str | None = strawberry.field(description="Description of the Lens")
    downstream_dashboards: list[Dashboard] = strawberry.field(description='"Dashboards connected to the Lens"')
    downstream_dashboards_connection: DashboardsConnection | None
    downstream_metrics: list[Metric] = strawberry.field(description='"Metrics connected to the Lens"')
    downstream_metrics_connection: MetricsConnection | None
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners of contents connected to the Lens")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners of contents connected to the Lens")
    downstream_workbooks: list[Workbook] = strawberry.field(description='"Workbooks connected to the Lens"')
    downstream_workbooks_connection: WorkbooksConnection | None
    fields: list[LensField] = strawberry.field(description="The list of fields")
    fields_connection: LensFieldsConnection | None = strawberry.field(description="The list of fields")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server")
    owner: TableauUser = strawberry.field(description="User who owns this Lens")
    project_vizportal_url_id: str = strawberry.field(description="The ID of the project in which the Lens is visible and usable.")
    site: TableauSite = strawberry.field(description="The site in which the Lens is visible and usable")
    updated_at: datetime = strawberry.field(description="Time the Lens was last updated")
    upstream_databases: list[Database | None] | None = strawberry.field(description="The Databases that are upstream to this Lens")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="The Databases that are upstream to this Lens")
    upstream_datasources: list[PublishedDatasource | None] | None = strawberry.field(description="The datasource that are upstream of this lens")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="The datasource that are upstream of this lens")
    upstream_fields: list[Field | None] | None = strawberry.field(description="The fields that are upstream of this lens")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="The fields that are upstream of this lens")
    upstream_flows: list[Flow | None] | None = strawberry.field(description="The flows that are upstream of this Lens")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="The flows that are upstream of this Lens")
    upstream_tables: list[Table] = strawberry.field(description="Tables that are upstream of this Lens")
    upstream_tables_connection: TablesConnection | None = strawberry.field(description="Tables that are upstream of this Lens")
    upstream_virtual_connection_tables: list[VirtualConnectionTable | None] | None = strawberry.field(description="The virtual connection table upstream to this Lens")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="The virtual connection table upstream to this Lens")
    upstream_virtual_connections: list[VirtualConnection | None] | None = strawberry.field(description="The virtual connection upstream to this Lens")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="The virtual connection upstream to this Lens")
    vizportal_url_id: str = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description="Lens Fields contain extra information based on an underlying datasource field")
class LensField:
    containing_lens: Lens | None = strawberry.field(description="The Lens which contains this lens field")
    datasource_field: Field = strawberry.field(description="Underlying datasource field this lens field is based on")
    description: str | None = strawberry.field(description="Description of field shown in Ask Data. If null or empty, use description inherited from datasource field.")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name of field shown locally in Ask Data. If null or empty, use name inherited from datasource field.")

@strawberry.enum
class LensFieldOrderField(Enum):
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class LensFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: LensFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class LensField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name of field shown locally in Ask Data. If null or empty, use name inherited from datasource field.")
    name_within: list[str | None] | None = strawberry.field(description="Name of field shown locally in Ask Data. If null or empty, use name inherited from datasource field.")

@strawberry.input(description="Filter by GraphQL field and given value")
class LensField_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")

@strawberry.type(description="Connection Type for LensField")
class LensFieldsConnection:
    nodes: list[LensField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class LensOrderField(Enum):
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"
    LUID = "LUID"
    NAME = "NAME"
    OWNER_COUNT = "OWNER_COUNT"
    VIZPORTAL_URL_ID = "VIZPORTAL_URL_ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class LensSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: LensOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Lens_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server")
    vizportal_url_id: str | None = strawberry.field(description="VizPortal URL ID; used for URL generation")
    vizportal_url_id_within: list[str | None] | None = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description="Connection Type for Lens")
class LensesConnection:
    nodes: list[Lens] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="Wrapper type including edge information")
class LinkedFlow:
    asset: Flow = strawberry.field(description="Object in this linked flow")
    asset_id: str = strawberry.field(description="Unique identifier of the object in this linked flow")
    from_edges: list[str] | None = strawberry.field(description="The nodes preceding this node")
    to_edges: list[str] | None = strawberry.field(description="The nodes following this node")

@strawberry.enum
class LinkedFlowOrderField(Enum):
    ID = "ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class LinkedFlowSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: LinkedFlowOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class LinkedFlow_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique Identifier of object to retrieve")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique Identifier of object to retrieve")

@strawberry.type(description="Connection Type for LinkedFlow")
class LinkedFlowsConnection:
    nodes: list[LinkedFlow] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="""
A Tableau Pulse metric definition.  
*Available in Tableau Cloud June 2024 and later. Tableau Pulse is not available in Tableau Server.*
""")
class MetricDefinition:
    fields: list[Field] = strawberry.field(description="Fields contained in the metric definition")
    fields_connection: FieldsConnection | None = strawberry.field(description="Fields contained in the metric definition")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the Metadata API. Not the same as the locally unique identifier used with the REST API.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server.")
    name: str = strawberry.field(description="Name of the metric definition.")
    site: TableauSite = strawberry.field(description="The site which contains the metric definition.")
    upstream_columns: list[Column] = strawberry.field(description="Columns upstream from the metric definition.")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns upstream from the metric definition.")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream from the metric definition")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream from the metric definition")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Data sources upstream from the metric definition.")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Data sources upstream from the metric definition.")
    upstream_fields: list[Field] = strawberry.field(description="Fields upstream from the metric definition.")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="Fields upstream from the metric definition.")
    upstream_flow_output_fields: list[FlowOutputField] = strawberry.field(description="Flow output fields upstream from the metric definition.")
    upstream_flow_output_fields_connection: FlowOutputFieldsConnection | None = strawberry.field(description="Flow output fields upstream from the metric definition.")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream from the metric definition.")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream from the metric definition.")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from the metric definition.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from the metric definition.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream from the metric definition.")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream from the metric definition.")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream from the metric definition.")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream from the metric definition.")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream from the metric definition.")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream from the metric definition.")

@strawberry.enum
class MetricDefinitionOrderField(Enum):
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"
    LUID = "LUID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class MetricDefinitionSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: MetricDefinitionOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class MetricDefinition_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the Metadata API. Not the same as the locally unique identifier used with the REST API.")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the Metadata API. Not the same as the locally unique identifier used with the REST API.")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server.")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server.")
    name: str | None = strawberry.field(description="Name of the metric definition.")
    name_within: list[str | None] | None = strawberry.field(description="Name of the metric definition.")

@strawberry.type(description="Connection Type for MetricDefinition")
class MetricDefinitionsConnection:
    nodes: list[MetricDefinition] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class MetricOrderField(Enum):
    CONTAINER_NAME = "CONTAINER_NAME"
    ID = "ID"
    LUID = "LUID"
    NAME = "NAME"
    OWNER_COUNT = "OWNER_COUNT"
    PROJECT_NAME = "PROJECT_NAME"
    VIZPORTAL_URL_ID = "VIZPORTAL_URL_ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class MetricSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: MetricOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Metric_Filter:
    container_name: str | None = strawberry.field(description="The name of the container in which the metric is visible and usable. This is always a project.")
    container_name_within: list[str | None] | None = strawberry.field(description="The name of the container in which the metric is visible and usable. This is always a project.")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the Metric is visible and usable.")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project in which the Metric is visible and usable.")
    vizportal_url_id: str | None = strawberry.field(description="VizPortal URL ID; used for URL generation")
    vizportal_url_id_within: list[str | None] | None = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description="Connection Type for Metric")
class MetricsConnection:
    nodes: list[Metric] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class NodeOrderField(Enum):
    ID = "ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class NodeSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: NodeOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Node_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")

@strawberry.type(description="Connection Type for Node")
class NodesConnection:
    nodes: list[Node] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class OrderDirection(Enum):
    ASC = "ASC"
    DESC = "DESC"

@strawberry.type(description="Information about pagination in a connection")
class PageInfo:
    end_cursor: str | None = strawberry.field(description="Cursor to use in subsequent query to fetch next page of objects")
    has_next_page: bool = strawberry.field(description="Indicates if there are more objects to fetch")

@strawberry.type(description="Tableau Parameter. For more info see https://onlinehelp.tableau.com/current/pro/desktop/en-us/parameters_create.html")
class Parameter:
    datasource: PublishedDatasource | None = strawberry.field(description="Published data source that contains this parameter")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name of parameter")
    parent_name: str | None = strawberry.field(description="Name of the parameter's parent")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this parameter")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this parameter")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this parameter")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this parameter")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this parameter references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this parameter references")
    workbook: Workbook | None = strawberry.field(description="Workbook that contains this parameter")

@strawberry.enum
class ParameterOrderField(Enum):
    ID = "ID"
    NAME = "NAME"
    PARENT_NAME = "PARENT_NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class ParameterSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: ParameterOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Parameter_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name of parameter")
    name_within: list[str | None] | None = strawberry.field(description="Name of parameter")
    parent_name: str | None = strawberry.field(description="Name of the parameter's parent")
    parent_name_within: list[str | None] | None = strawberry.field(description="Name of the parameter's parent")

@strawberry.type(description="Connection Type for Parameter")
class ParametersConnection:
    nodes: list[Parameter] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class PermissionMode(Enum):
    FILTER_RESULTS = "FILTER_RESULTS"
    OBFUSCATE_RESULTS = "OBFUSCATE_RESULTS"

@strawberry.enum
class PublishedDatasourceOrderField(Enum):
    CONTAINER_NAME = "CONTAINER_NAME"
    CONTAINS_UNSUPPORTED_CUSTOM_SQL = "CONTAINS_UNSUPPORTED_CUSTOM_SQL"
    DOWNSTREAM_OWNERS_COUNT = "DOWNSTREAM_OWNERS_COUNT"
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    FIELDS_COUNT = "FIELDS_COUNT"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    IS_CERTIFIED = "IS_CERTIFIED"
    LUID = "LUID"
    NAME = "NAME"
    OWNER_COUNT = "OWNER_COUNT"
    PROJECT_NAME = "PROJECT_NAME"
    VIZPORTAL_URL_ID = "VIZPORTAL_URL_ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class PublishedDatasourceSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: PublishedDatasourceOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class PublishedDatasource_Filter:
    container_name: str | None = strawberry.field(description="The name of the container in which the published data source is visible and usable. Either a personal space or project.")
    container_name_within: list[str | None] | None = strawberry.field(description="The name of the container in which the published data source is visible and usable. Either a personal space or project.")
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    contains_unsupported_custom_sql_within: list[bool | None] | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    has_active_warning: bool | None = strawberry.field(description="True if the data source has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the data source has an active data quality warning")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool | None = strawberry.field(description="True if this data source contains an active data quality certification")
    is_certified_within: list[bool | None] | None = strawberry.field(description="True if this data source contains an active data quality certification")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project that contains this published data source.")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project that contains this published data source.")
    vizportal_url_id: str | None = strawberry.field(description="VizPortal URL ID; used for URL generation")
    vizportal_url_id_within: list[str | None] | None = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description="Connection Type for PublishedDatasource")
class PublishedDatasourcesConnection:
    nodes: list[PublishedDatasource] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="Query root for Metadata GraphQL interface")
class Query:
    ask_data_extensions: list[AskDataExtension] = strawberry.field(description="Fetches AskDataExtensions by filtering on id or name")
    ask_data_extensions_connection: AskDataExtensionsConnection = strawberry.field(description="Fetch AskDataExtensions with support for pagination")
    bin_fields: list[BinField] = strawberry.field(description="Fetches BinFields by filtering on id or name")
    bin_fields_connection: BinFieldsConnection = strawberry.field(description="Fetch BinFields with support for pagination")
    calculated_fields: list[CalculatedField] = strawberry.field(description="Fetches CalculatedFields by filtering on id or name")
    calculated_fields_connection: CalculatedFieldsConnection = strawberry.field(description="Fetch CalculatedFields with support for pagination")
    cloud_files: list[CloudFile] = strawberry.field(description="Fetches CloudFiles by filtering on id or name")
    cloud_files_connection: CloudFilesConnection = strawberry.field(description="Fetch CloudFiles with support for pagination")
    column_fields: list[ColumnField] = strawberry.field(description="Fetches ColumnFields by filtering on id or name")
    column_fields_connection: ColumnFieldsConnection = strawberry.field(description="Fetch ColumnFields with support for pagination")
    columns: list[Column] = strawberry.field(description="Fetches Columns by filtering on id or name")
    columns_connection: ColumnsConnection = strawberry.field(description="Fetch Columns with support for pagination")
    combined_fields: list[CombinedField] = strawberry.field(description="Fetches CombinedFields by filtering on id or name")
    combined_fields_connection: CombinedFieldsConnection = strawberry.field(description="Fetch CombinedFields with support for pagination")
    combined_set_fields: list[CombinedSetField] = strawberry.field(description="Fetches CombinedSetFields by filtering on id or name")
    combined_set_fields_connection: CombinedSetFieldsConnection = strawberry.field(description="Fetch CombinedSetFields with support for pagination")
    custom_sql_tables: list[CustomSQLTable] = strawberry.field(description="Fetches CustomSQLTables by filtering on id or name")
    custom_sql_tables_connection: CustomSQLTablesConnection = strawberry.field(description="Fetch CustomSQLTables with support for pagination")
    dashboards: list[Dashboard] = strawberry.field(description="Fetches Dashboards by filtering on id or name")
    dashboards_connection: DashboardsConnection = strawberry.field(description="Fetch Dashboards with support for pagination")
    data_clouds: list[DataCloud] = strawberry.field(description="Fetches DataClouds by filtering on id or name")
    data_clouds_connection: DataCloudsConnection = strawberry.field(description="Fetch DataClouds with support for pagination")
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="Fetches DataQualityCertifications by filtering on id or name")
    data_quality_certifications_connection: DataQualityCertificationsConnection = strawberry.field(description="Fetch DataQualityCertifications with support for pagination")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Fetches DataQualityWarnings by filtering on id or name")
    data_quality_warnings_connection: DataQualityWarningsConnection = strawberry.field(description="Fetch DataQualityWarnings with support for pagination")
    database_servers: list[DatabaseServer] = strawberry.field(description="Fetches DatabaseServers by filtering on id or name")
    database_servers_connection: DatabaseServersConnection = strawberry.field(description="Fetch DatabaseServers with support for pagination")
    database_tables: list[DatabaseTable] = strawberry.field(description="Fetches DatabaseTables by filtering on id or name")
    database_tables_connection: DatabaseTablesConnection = strawberry.field(description="Fetch DatabaseTables with support for pagination")
    databases: list[Database] = strawberry.field(description="Fetches Databases by filtering on id or name")
    databases_connection: DatabasesConnection = strawberry.field(description="Fetch Databases with support for pagination")
    datasource_fields: list[DatasourceField] = strawberry.field(description="Fetches DatasourceFields by filtering on id or name")
    datasource_fields_connection: DatasourceFieldsConnection = strawberry.field(description="Fetch DatasourceFields with support for pagination")
    datasource_filters: list[DatasourceFilter] = strawberry.field(description="Fetches DatasourceFilters by filtering on id or name")
    datasource_filters_connection: DatasourceFiltersConnection = strawberry.field(description="Fetch DatasourceFilters with support for pagination")
    datasources: list[Datasource] = strawberry.field(description="Fetches Datasources by filtering on id or name")
    datasources_connection: DatasourcesConnection = strawberry.field(description="Fetch Datasources with support for pagination")
    embedded_datasources: list[EmbeddedDatasource] = strawberry.field(description="Fetches EmbeddedDatasources by filtering on id or name")
    embedded_datasources_connection: EmbeddedDatasourcesConnection = strawberry.field(description="Fetch EmbeddedDatasources with support for pagination")
    fields: list[Field] = strawberry.field(description="Fetches Fields by filtering on id or name")
    fields_connection: FieldsConnection = strawberry.field(description="Fetch Fields with support for pagination")
    files: list[File] = strawberry.field(description="Fetches Files by filtering on id or name")
    files_connection: FilesConnection = strawberry.field(description="Fetch Files with support for pagination")
    flow_column_input_fields: list[FlowColumnInputField] = strawberry.field(description="Fetches FlowColumnInputFields by filtering on id or name")
    flow_column_input_fields_connection: FlowColumnInputFieldsConnection = strawberry.field(description="Fetch FlowColumnInputFields with support for pagination")
    flow_column_output_fields: list[FlowColumnOutputField] = strawberry.field(description="Fetches FlowColumnOutputFields by filtering on id or name")
    flow_column_output_fields_connection: FlowColumnOutputFieldsConnection = strawberry.field(description="Fetch FlowColumnOutputFields with support for pagination")
    flow_field_input_fields: list[FlowFieldInputField] = strawberry.field(description="Fetches FlowFieldInputFields by filtering on id or name")
    flow_field_input_fields_connection: FlowFieldInputFieldsConnection = strawberry.field(description="Fetch FlowFieldInputFields with support for pagination")
    flow_field_output_fields: list[FlowFieldOutputField] = strawberry.field(description="Fetches FlowFieldOutputFields by filtering on id or name")
    flow_field_output_fields_connection: FlowFieldOutputFieldsConnection = strawberry.field(description="Fetch FlowFieldOutputFields with support for pagination")
    flow_output_steps: list[FlowOutputStep] = strawberry.field(description="Fetches FlowOutputSteps by filtering on id or name")
    flow_output_steps_connection: FlowOutputStepsConnection = strawberry.field(description="Fetch FlowOutputSteps with support for pagination")
    flows: list[Flow] = strawberry.field(description="Fetches Flows by filtering on id or name")
    flows_connection: FlowsConnection = strawberry.field(description="Fetch Flows with support for pagination")
    generic_labels: list[GenericLabel] = strawberry.field(description="Fetches GenericLabels by filtering on id or name")
    generic_labels_connection: GenericLabelsConnection = strawberry.field(description="Fetch GenericLabels with support for pagination")
    group_fields: list[GroupField] = strawberry.field(description="Fetches GroupFields by filtering on id or name")
    group_fields_connection: GroupFieldsConnection = strawberry.field(description="Fetch GroupFields with support for pagination")
    hierarchy_fields: list[HierarchyField] = strawberry.field(description="Fetches HierarchyFields by filtering on id or name")
    hierarchy_fields_connection: HierarchyFieldsConnection = strawberry.field(description="Fetch HierarchyFields with support for pagination")
    lens_fields: list[LensField] = strawberry.field(description="Fetches LensFields by filtering on id or name")
    lens_fields_connection: LensFieldsConnection = strawberry.field(description="Fetch LensFields with support for pagination")
    lenses: list[Lens] = strawberry.field(description="Fetches Lenses by filtering on id or name")
    lenses_connection: LensesConnection = strawberry.field(description="Fetch Lenss with support for pagination")
    metric_definitions: list[MetricDefinition] = strawberry.field(description="Fetches MetricDefinitions by filtering on id or name")
    metric_definitions_connection: MetricDefinitionsConnection = strawberry.field(description="Fetch MetricDefinitions with support for pagination")
    metrics: list[Metric] = strawberry.field(description="Fetches Metrics by filtering on id or name")
    metrics_connection: MetricsConnection = strawberry.field(description="Fetch Metrics with support for pagination")
    parameters: list[Parameter] = strawberry.field(description="Fetches Parameters by filtering on id or name")
    parameters_connection: ParametersConnection = strawberry.field(description="Fetch Parameters with support for pagination")
    published_datasources: list[PublishedDatasource] = strawberry.field(description="Fetches PublishedDatasources by filtering on id or name")
    published_datasources_connection: PublishedDatasourcesConnection = strawberry.field(description="Fetch PublishedDatasources with support for pagination")
    set_fields: list[SetField] = strawberry.field(description="Fetches SetFields by filtering on id or name")
    set_fields_connection: SetFieldsConnection = strawberry.field(description="Fetch SetFields with support for pagination")
    sheets: list[Sheet] = strawberry.field(description="Fetches Sheets by filtering on id or name")
    sheets_connection: SheetsConnection = strawberry.field(description="Fetch Sheets with support for pagination")
    table_additional_detailses: list[TableAdditionalDetails] = strawberry.field(description="Fetches TableAdditionalDetailses by filtering on id or name")
    table_additional_detailses_connection: TableAdditionalDetailsesConnection = strawberry.field(description="Fetch TableAdditionalDetailss with support for pagination")
    tableau_sites: list[TableauSite] = strawberry.field(description="Fetches TableauSites by filtering on id or name")
    tableau_sites_connection: TableauSitesConnection = strawberry.field(description="Fetch TableauSites with support for pagination")
    tableau_users: list[TableauUser] = strawberry.field(description="Fetches TableauUsers by filtering on id or name")
    tableau_users_connection: TableauUsersConnection = strawberry.field(description="Fetch TableauUsers with support for pagination")
    tables: list[Table] = strawberry.field(description="Fetches Tables by filtering on id or name")
    tables_connection: TablesConnection = strawberry.field(description="Fetch Tables with support for pagination")
    tags: list[Tag] = strawberry.field(description="Fetches Tags by filtering on id or name")
    tags_connection: TagsConnection = strawberry.field(description="Fetch Tags with support for pagination")
    views: list[View] = strawberry.field(description="Fetches Views by filtering on id or name")
    views_connection: ViewsConnection = strawberry.field(description="Fetch Views with support for pagination")
    virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Fetches VirtualConnectionTables by filtering on id or name")
    virtual_connection_tables_connection: VirtualConnectionTablesConnection = strawberry.field(description="Fetch VirtualConnectionTables with support for pagination")
    virtual_connections: list[VirtualConnection] = strawberry.field(description="Fetches VirtualConnections by filtering on id or name")
    virtual_connections_connection: VirtualConnectionsConnection = strawberry.field(description="Fetch VirtualConnections with support for pagination")
    web_data_connectors: list[WebDataConnector] = strawberry.field(description="Fetches WebDataConnectors by filtering on id or name")
    web_data_connectors_connection: WebDataConnectorsConnection = strawberry.field(description="Fetch WebDataConnectors with support for pagination")
    workbooks: list[Workbook] = strawberry.field(description="Fetches Workbooks by filtering on id or name")
    workbooks_connection: WorkbooksConnection = strawberry.field(description="Fetch Workbooks with support for pagination")
    __schema: __Schema
    __type: __Type | None

@strawberry.enum
class RemoteType(Enum):
    ARRAY = "ARRAY"
    BOOL = "BOOL"
    BSTR = "BSTR"
    BYREF = "BYREF"
    BYTES = "BYTES"
    CY = "CY"
    DATE = "DATE"
    DBDATE = "DBDATE"
    DBTIME = "DBTIME"
    DBTIMESTAMP = "DBTIMESTAMP"
    DECIMAL = "DECIMAL"
    EMPTY = "EMPTY"
    ERROR = "ERROR"
    FILETIME = "FILETIME"
    GUID = "GUID"
    HCHAPTER = "HCHAPTER"
    I1 = "I1"
    I2 = "I2"
    I4 = "I4"
    I8 = "I8"
    IDISPATCH = "IDISPATCH"
    IUNKNOWN = "IUNKNOWN"
    NULL = "NULL"
    NUMERIC = "NUMERIC"
    PROPVARIANT = "PROPVARIANT"
    R4 = "R4"
    R8 = "R8"
    RESERVED = "RESERVED"
    STR = "STR"
    UDT = "UDT"
    UI1 = "UI1"
    UI2 = "UI2"
    UI4 = "UI4"
    UI8 = "UI8"
    VARIANT = "VARIANT"
    VARNUMERIC = "VARNUMERIC"
    VECTOR = "VECTOR"
    WDC_BOOL = "WDC_BOOL"
    WDC_DATE = "WDC_DATE"
    WDC_DATETIME = "WDC_DATETIME"
    WDC_FLOAT = "WDC_FLOAT"
    WDC_GEOMETRY = "WDC_GEOMETRY"
    WDC_INT = "WDC_INT"
    WDC_STRING = "WDC_STRING"
    WSTR = "WSTR"

@strawberry.input(description="Filter by GraphQL field and given value")
class RemoteType_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique Identifier of object to retrieve")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique Identifier of object to retrieve")

@strawberry.enum
class SetFieldOrderField(Enum):
    DOWNSTREAM_SHEETS_COUNT = "DOWNSTREAM_SHEETS_COUNT"
    FIELDS_COUNT = "FIELDS_COUNT"
    ID = "ID"
    IS_HIDDEN = "IS_HIDDEN"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class SetFieldSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: SetFieldOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class SetField_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    is_hidden_within: list[bool | None] | None = strawberry.field(description="True if the field is hidden")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.input(description="Filter by GraphQL field and given value")
class SetField_Required_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")

@strawberry.type(description="Connection Type for SetField")
class SetFieldsConnection:
    nodes: list[SetField] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class SheetOrderField(Enum):
    DATASOURCE_FIELDS_COUNT = "DATASOURCE_FIELDS_COUNT"
    DOCUMENT_VIEW_ID = "DOCUMENT_VIEW_ID"
    ID = "ID"
    LUID = "LUID"
    NAME = "NAME"
    PATH = "PATH"
    SHEET_FIELD_INSTANCES_COUNT = "SHEET_FIELD_INSTANCES_COUNT"
    WORKSHEET_FIELDS_COUNT = "WORKSHEET_FIELDS_COUNT"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class SheetSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: SheetOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Sheet_Filter:
    document_view_id: str | None = strawberry.field(description="Unique ID for the sheet generated for and stored within the workbook, survives renames, and is used for internal processes")
    document_view_id_within: list[str | None] | None = strawberry.field(description="Unique ID for the sheet generated for and stored within the workbook, survives renames, and is used for internal processes")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server (Blank if worksheet is hidden in Workbook)")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server (Blank if worksheet is hidden in Workbook)")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    path: str | None = strawberry.field(description="Server path to sheet")
    path_within: list[str | None] | None = strawberry.field(description="Server path to sheet")

@strawberry.type(description="Connection Type for Sheet")
class SheetsConnection:
    nodes: list[Sheet] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="""
Additional details for the DatabaseTable type  

*Available in Tableau Cloud February 2024 / Server 2024.2 and later.*
""")
class TableAdditionalDetails:
    category: str | None = strawberry.field(description="Category of the Data Cloud object")
    cdp_internal_id: str | None = strawberry.field(description="Internal ID of the Data Cloud object")
    created_by: str | None = strawberry.field(description="The Data Cloud user who created this object")
    data_cloud_api_name: str | None = strawberry.field(description="API name of the Data Cloud object")
    id: strawberry.ID = strawberry.field(description="Unique identifier used with the Metadata API.  Not the same as the locally unique identifier used with the REST API.")
    table: list[DatabaseTable | None] | None = strawberry.field(description="The tables that this additional detail is for")
    table_connection: DatabaseTablesConnection | None = strawberry.field(description="The tables that this additional detail is for")

@strawberry.enum
class TableAdditionalDetailsOrderField(Enum):
    ID = "ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class TableAdditionalDetailsSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: TableAdditionalDetailsOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class TableAdditionalDetails_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used with the Metadata API.  Not the same as the locally unique identifier used with the REST API.")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used with the Metadata API.  Not the same as the locally unique identifier used with the REST API.")

@strawberry.type(description="Connection Type for TableAdditionalDetails")
class TableAdditionalDetailsesConnection:
    nodes: list[TableAdditionalDetails] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class TableOrderField(Enum):
    COLUMNS_COUNT = "COLUMNS_COUNT"
    DOWNSTREAM_DASHBOARDS_COUNT = "DOWNSTREAM_DASHBOARDS_COUNT"
    DOWNSTREAM_DATASOURCES_COUNT = "DOWNSTREAM_DATASOURCES_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class TableSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: TableOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.enum
class TableType(Enum):
    CALCULATEDINSIGHT = "CALCULATEDINSIGHT"
    DATABASETABLE = "DATABASETABLE"
    DATALAKE = "DATALAKE"
    DATAMODEL = "DATAMODEL"

@strawberry.input(description="Filter by GraphQL field and given value")
class TableType_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique Identifier of object to retrieve")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique Identifier of object to retrieve")

@strawberry.input(description="Filter by GraphQL field and given value")
class Table_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.type(description="Site on Tableau server")
class TableauSite:
    created_at: datetime | None = strawberry.field(description="Time the site was created. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    flows: list[Flow | None] | None = strawberry.field(description="The flows that are part of this site")
    flows_connection: FlowsConnection | None = strawberry.field(description="The flows that are part of this site")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    lenses: list[Lens | None] | None = strawberry.field(description="The Lenses that are part of this site")
    lenses_connection: LensesConnection | None = strawberry.field(description="The Lenses that are part of this site")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that are part of this site.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that are part of this site.")
    metrics: list[Metric | None] | None = strawberry.field(description="The Metrics that are part of this site")
    metrics_connection: MetricsConnection | None = strawberry.field(description="The Metrics that are part of this site")
    name: str = strawberry.field(description="Name shown in server")
    published_datasources: list[PublishedDatasource | None] | None = strawberry.field(description="The published data sources that are part of this site")
    published_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="The published data sources that are part of this site")
    uri: str = strawberry.field(description="URI of this site, e.g., 'sites/4'")
    virtual_connections: list[VirtualConnection | None] | None = strawberry.field(description="The virtual connections that are part of this site")
    virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="The virtual connections that are part of this site")
    workbooks: list[Workbook | None] | None = strawberry.field(description="The workbooks that are part of this site")
    workbooks_connection: WorkbooksConnection | None = strawberry.field(description="The workbooks that are part of this site")

@strawberry.enum
class TableauSiteOrderField(Enum):
    ID = "ID"
    LUID = "LUID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class TableauSiteSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: TableauSiteOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class TableauSite_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server")

@strawberry.type(description="Connection Type for TableauSite")
class TableauSitesConnection:
    nodes: list[TableauSite] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="User on a site on Tableau server")
class TableauUser:
    authored_data_quality_certifications: list[DataQualityCertification | None] | None = strawberry.field(description="The data quality certifications this user has authored")
    authored_data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications this user has authored")
    authored_data_quality_warnings: list[DataQualityWarning | None] | None = strawberry.field(description="The data quality warnings this user has authored")
    authored_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings this user has authored")
    authored_labels: list[Label | None] | None = strawberry.field(description="The labels this user has authored")
    authored_labels_connection: LabelsConnection | None = strawberry.field(description="The labels this user has authored")
    certified_databases: list[Database | None] | None = strawberry.field(description="The databases that this user has certified")
    certified_databases_connection: DatabasesConnection | None = strawberry.field(description="The databases that this user has certified")
    certified_datasources: list[PublishedDatasource | None] | None = strawberry.field(description="The published data sources that this user has certified")
    certified_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="The published data sources that this user has certified")
    certified_tables: list[DatabaseTable | None] | None = strawberry.field(description="The tables that this user has certified")
    certified_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="The tables that this user has certified")
    contact_for_databases: list[Database | None] | None = strawberry.field(description="The databases that this user is the contact for")
    contact_for_databases_connection: DatabasesConnection | None = strawberry.field(description="The databases that this user is the contact for")
    contact_for_tables: list[DatabaseTable | None] | None = strawberry.field(description="The tables that this user is the contact for")
    contact_for_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="The tables that this user is the contact for")
    domain: str | None = strawberry.field(description="Domain this user belongs to")
    email: str | None = strawberry.field(description="Email address of this user")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Display name of this user")
    owned_datasources: list[PublishedDatasource | None] | None = strawberry.field(description="The published data sources that belong to this user")
    owned_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="The published data sources that belong to this user")
    owned_flows: list[Flow | None] | None = strawberry.field(description="The flows that belong to this user")
    owned_flows_connection: FlowsConnection | None = strawberry.field(description="The flows that belong to this user")
    owned_lenses: list[Lens | None] | None = strawberry.field(description="The Lenses that belong to this user")
    owned_lenses_connection: LensesConnection | None = strawberry.field(description="The Lenses that belong to this user")
    owned_metrics: list[Metric | None] | None = strawberry.field(description="The Metrics that belong to this user")
    owned_metrics_connection: MetricsConnection | None = strawberry.field(description="The Metrics that belong to this user")
    owned_virtual_connection_tables: list[VirtualConnectionTable | None] | None = strawberry.field(description="The virtual connection tables that belong to this user")
    owned_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="The virtual connection tables that belong to this user")
    owned_virtual_connections: list[VirtualConnection | None] | None = strawberry.field(description="The virtual connections that belong to this user")
    owned_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="The virtual connections that belong to this user")
    owned_workbooks: list[Workbook | None] | None = strawberry.field(description="The workbooks that belong to this user")
    owned_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="The workbooks that belong to this user")
    uri: str = strawberry.field(description="URI of this user, e.g., 'sites/1/users/1396'")
    username: str | None = strawberry.field(description="Username of this user")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this user, for use in client-to-server communications")

@strawberry.enum
class TableauUserOrderField(Enum):
    DOMAIN = "DOMAIN"
    EMAIL = "EMAIL"
    ID = "ID"
    LUID = "LUID"
    NAME = "NAME"
    USERNAME = "USERNAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class TableauUserSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: TableauUserOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class TableauUser_Filter:
    domain: str | None = strawberry.field(description="Domain this user belongs to")
    domain_within: list[str | None] | None = strawberry.field(description="Domain this user belongs to")
    email: str | None = strawberry.field(description="Email address of this user")
    email_within: list[str | None] | None = strawberry.field(description="Email address of this user")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Display name of this user")
    name_within: list[str | None] | None = strawberry.field(description="Display name of this user")
    username: str | None = strawberry.field(description="Username of this user")
    username_within: list[str | None] | None = strawberry.field(description="Username of this user")

@strawberry.type(description="Connection Type for TableauUser")
class TableauUsersConnection:
    nodes: list[TableauUser] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="Connection Type for Table")
class TablesConnection:
    nodes: list[Table] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="A tag associated with content items")
class Tag:
    assets: list[Taggable | None] | None = strawberry.field(description="The assets that are associated with this tag")
    assets_connection: TaggablesConnection | None = strawberry.field(description="The assets that are associated with this tag")
    columns: list[Column | None] | None = strawberry.field(description="The columns that are associated with this tag")
    columns_connection: ColumnsConnection | None = strawberry.field(description="The columns that are associated with this tag")
    database_tables: list[DatabaseTable | None] | None = strawberry.field(description="The tables that are associated with this tag")
    database_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="The tables that are associated with this tag")
    databases: list[Database | None] | None = strawberry.field(description="The databases that are associated with this tag")
    databases_connection: DatabasesConnection | None = strawberry.field(description="The databases that are associated with this tag")
    flows: list[Flow | None] | None = strawberry.field(description="The flows that are associated with this tag")
    flows_connection: FlowsConnection | None = strawberry.field(description="The flows that are associated with this tag")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.")
    metrics: list[Metric | None] | None = strawberry.field(description="The Metrics that are associated with this tag")
    metrics_connection: MetricsConnection | None = strawberry.field(description="The Metrics that are associated with this tag")
    name: str | None = strawberry.field(description="The name of the tag")
    published_datasources: list[PublishedDatasource | None] | None = strawberry.field(description="The published datasources that are associated with this tag")
    published_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="The published datasources that are associated with this tag")
    views: list[View | None] | None = strawberry.field(description="The views that are associated with this tag")
    views_connection: ViewsConnection | None = strawberry.field(description="The views that are associated with this tag")
    virtual_connection_tables: list[VirtualConnectionTable | None] | None = strawberry.field(description="The virtual connection tables that are associated with this tag")
    virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="The virtual connection tables that are associated with this tag")
    virtual_connections: list[VirtualConnection | None] | None = strawberry.field(description="The virtual connections that are associated with this tag")
    virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="The virtual connections that are associated with this tag")
    workbooks: list[Workbook | None] | None = strawberry.field(description="The workbooks that are associated with this tag")
    workbooks_connection: WorkbooksConnection | None = strawberry.field(description="The workbooks that are associated with this tag")

@strawberry.enum
class TagOrderField(Enum):
    ID = "ID"
    NAME = "NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class TagSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: TagOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Tag_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.")
    name: str | None = strawberry.field(description="The name of the tag")
    name_within: list[str | None] | None = strawberry.field(description="The name of the tag")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.enum
class TaggableOrderField(Enum):
    ID = "ID"
    LUID = "LUID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class TaggableSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: TaggableOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Taggable_Filter:
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")

@strawberry.type(description="Connection Type for Taggable")
class TaggablesConnection:
    nodes: list[Taggable] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.type(description="Connection Type for Tag")
class TagsConnection:
    nodes: list[Tag] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class ViewOrderField(Enum):
    DOCUMENT_VIEW_ID = "DOCUMENT_VIEW_ID"
    ID = "ID"
    LUID = "LUID"
    NAME = "NAME"
    PATH = "PATH"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class ViewSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: ViewOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class View_Filter:
    document_view_id: str | None = strawberry.field(description="Unique ID for the view generated for and stored within the workbook, survives renames, and is used for internal processes")
    document_view_id_within: list[str | None] | None = strawberry.field(description="Unique ID for the view generated for and stored within the workbook, survives renames, and is used for internal processes")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server (Blank if sheet is hidden in Workbook)")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server (Blank if sheet is hidden in Workbook)")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    path: str | None = strawberry.field(description="Server path to view")
    path_within: list[str | None] | None = strawberry.field(description="Server path to view")

@strawberry.type(description="Connection Type for View")
class ViewsConnection:
    nodes: list[View] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class VirtualConnectionOrderField(Enum):
    CONNECTION_TYPE = "CONNECTION_TYPE"
    CONTAINER_NAME = "CONTAINER_NAME"
    DOWNSTREAM_DATASOURCES_COUNT = "DOWNSTREAM_DATASOURCES_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    IS_CERTIFIED = "IS_CERTIFIED"
    LUID = "LUID"
    NAME = "NAME"
    OWNER_COUNT = "OWNER_COUNT"
    PROJECT_NAME = "PROJECT_NAME"
    VIZPORTAL_URL_ID = "VIZPORTAL_URL_ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class VirtualConnectionSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: VirtualConnectionOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.enum
class VirtualConnectionTableOrderField(Enum):
    COLUMNS_COUNT = "COLUMNS_COUNT"
    CONTAINS_UNSUPPORTED_CUSTOM_SQL = "CONTAINS_UNSUPPORTED_CUSTOM_SQL"
    DOWNSTREAM_DASHBOARDS_COUNT = "DOWNSTREAM_DASHBOARDS_COUNT"
    DOWNSTREAM_DATASOURCES_COUNT = "DOWNSTREAM_DATASOURCES_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    EXTRACT_LAST_REFRESHED_AT = "EXTRACT_LAST_REFRESHED_AT"
    EXTRACT_LAST_REFRESH_TYPE = "EXTRACT_LAST_REFRESH_TYPE"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    IS_CERTIFIED = "IS_CERTIFIED"
    IS_EXTRACTED = "IS_EXTRACTED"
    LUID = "LUID"
    NAME = "NAME"
    OWNER_COUNT = "OWNER_COUNT"
    VIZPORTAL_URL_ID = "VIZPORTAL_URL_ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class VirtualConnectionTableSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: VirtualConnectionTableOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class VirtualConnectionTable_Filter:
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    contains_unsupported_custom_sql_within: list[bool | None] | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    extract_last_refreshed_at: datetime | None = strawberry.field(description="The time the data for this table's extract was refreshed.")
    extract_last_refreshed_at_within: list[datetime | None] | None = strawberry.field(description="The time the data for this table's extract was refreshed.")
    has_active_warning: bool | None = strawberry.field(description="True if the table has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the table has an active data quality warning")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool | None = strawberry.field(description="True if this virtual connection table contains an active data quality certification")
    is_certified_within: list[bool | None] | None = strawberry.field(description="True if this virtual connection table contains an active data quality certification")
    is_extracted: bool | None = strawberry.field(description="Whether or not queries to this table are using an extract.")
    is_extracted_within: list[bool | None] | None = strawberry.field(description="Whether or not queries to this table are using an extract.")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    vizportal_url_id: str | None = strawberry.field(description="VizPortal URL ID; used for URL generation")
    vizportal_url_id_within: list[str | None] | None = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description="Connection Type for VirtualConnectionTable")
class VirtualConnectionTablesConnection:
    nodes: list[VirtualConnectionTable] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.input(description="Filter by GraphQL field and given value")
class VirtualConnection_Filter:
    connection_type: str | None = strawberry.field(description="Connection type of this virtual connection")
    connection_type_within: list[str | None] | None = strawberry.field(description="Connection type of this virtual connection")
    container_name: str | None = strawberry.field(description="The name of the container in which the virtual connection is visible and usable. Either a personal space or project.")
    container_name_within: list[str | None] | None = strawberry.field(description="The name of the container in which the virtual connection is visible and usable. Either a personal space or project.")
    has_active_warning: bool | None = strawberry.field(description="True if the virtual connection has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the virtual connection has an active data quality warning")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool | None = strawberry.field(description="True if this virtual connection contains an active data quality certification")
    is_certified_within: list[bool | None] | None = strawberry.field(description="True if this virtual connection contains an active data quality certification")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project that contains this virtual connection.")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project that contains this virtual connection.")
    vizportal_url_id: str | None = strawberry.field(description="Vizportal URL ID; used for URL generation")
    vizportal_url_id_within: list[str | None] | None = strawberry.field(description="Vizportal URL ID; used for URL generation")

@strawberry.type(description="Connection Type for VirtualConnection")
class VirtualConnectionsConnection:
    nodes: list[VirtualConnection] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class WarnableOrderField(Enum):
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    LUID = "LUID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class WarnableSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: WarnableOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Warnable_Filter:
    has_active_warning: bool | None = strawberry.field(description="True if the content has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the content has an active data quality warning")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")

@strawberry.type(description="Connection Type for Warnable")
class WarnablesConnection:
    nodes: list[Warnable] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class WebDataConnectorOrderField(Enum):
    CONNECTION_TYPE = "CONNECTION_TYPE"
    DOWNSTREAM_DATASOURCES_COUNT = "DOWNSTREAM_DATASOURCES_COUNT"
    DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT = "DOWNSTREAM_VIRTUAL_CONNECTIONS_COUNT"
    DOWNSTREAM_WORKBOOKS_COUNT = "DOWNSTREAM_WORKBOOKS_COUNT"
    HAS_ACTIVE_WARNING = "HAS_ACTIVE_WARNING"
    ID = "ID"
    IS_CERTIFIED = "IS_CERTIFIED"
    IS_EMBEDDED = "IS_EMBEDDED"
    LUID = "LUID"
    NAME = "NAME"
    PROJECT_NAME = "PROJECT_NAME"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class WebDataConnectorSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: WebDataConnectorOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class WebDataConnector_Filter:
    connection_type: str | None = strawberry.field(description="The type of web data connector")
    connection_type_within: list[str | None] | None = strawberry.field(description="The type of web data connector")
    has_active_warning: bool | None = strawberry.field(description="True if the database has an active data quality warning")
    has_active_warning_within: list[bool | None] | None = strawberry.field(description="True if the database has an active data quality warning")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the Metadata API. Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the Metadata API. Not the same as the numeric ID used on server")
    is_certified: bool | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_certified_within: list[bool | None] | None = strawberry.field(description="True if this database contains an active data quality certification")
    is_embedded: bool | None = strawberry.field(description="A web data connector is always embedded in Tableau content")
    is_embedded_within: list[bool | None] | None = strawberry.field(description="A web data connector is always embedded in Tableau content")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    text: str | None = strawberry.field(description="Filter the output based on text query.")

@strawberry.type(description="Connection Type for WebDataConnector")
class WebDataConnectorsConnection:
    nodes: list[WebDataConnector] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

@strawberry.enum
class WorkbookOrderField(Enum):
    CONTAINER_NAME = "CONTAINER_NAME"
    CONTAINS_UNSUPPORTED_CUSTOM_SQL = "CONTAINS_UNSUPPORTED_CUSTOM_SQL"
    DASHBOARDS_COUNT = "DASHBOARDS_COUNT"
    EMBEDDED_DATASOURCES_COUNT = "EMBEDDED_DATASOURCES_COUNT"
    ID = "ID"
    LUID = "LUID"
    NAME = "NAME"
    OWNER_COUNT = "OWNER_COUNT"
    PROJECT_LUID = "PROJECT_LUID"
    PROJECT_NAME = "PROJECT_NAME"
    SHEETS_COUNT = "SHEETS_COUNT"
    VIEWS_COUNT = "VIEWS_COUNT"
    VIZPORTAL_URL_ID = "VIZPORTAL_URL_ID"

@strawberry.input(description="Sort by given fields. The sort orders defined first in the list will take priority. If there are no given sort orders or a tie on the final sorted field then the resulting set will be sorted by ID in ascending order.")
class WorkbookSortOrder:
    direction: OrderDirection = strawberry.field(description="Order direction to sort output")
    field: WorkbookOrderField = strawberry.field(description="GraphQL field to sort on")

@strawberry.input(description="Filter by GraphQL field and given value")
class Workbook_Filter:
    container_name: str | None = strawberry.field(description="The name of the container in which the workbook is visible and usable. Either a personal space or project.")
    container_name_within: list[str | None] | None = strawberry.field(description="The name of the container in which the workbook is visible and usable. Either a personal space or project.")
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the workbook contains unsupported custom SQL, in which case lineage may be incomplete")
    contains_unsupported_custom_sql_within: list[bool | None] | None = strawberry.field(description="True if the workbook contains unsupported custom SQL, in which case lineage may be incomplete")
    id: strawberry.ID | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    id_within: list[strawberry.ID | None] | None = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    luid: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    luid_within: list[str | None] | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    name_within: list[str | None] | None = strawberry.field(description="Name shown in server and desktop clients")
    project_luid: str | None = strawberry.field(description="The luid of the project in which the workbook is visible and usable. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    project_luid_within: list[str | None] | None = strawberry.field(description="The luid of the project in which the workbook is visible and usable. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    project_name: str | None = strawberry.field(description="The name of the project in which the workbook is visible and usable.")
    project_name_within: list[str | None] | None = strawberry.field(description="The name of the project in which the workbook is visible and usable.")
    vizportal_url_id: str | None = strawberry.field(description="VizPortal URL ID; used for URL generation")
    vizportal_url_id_within: list[str | None] | None = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description="Connection Type for Workbook")
class WorkbooksConnection:
    nodes: list[Workbook] = strawberry.field(description="List of nodes")
    page_info: PageInfo = strawberry.field(description="Information for pagination")
    total_count: int = strawberry.field(description="Total number of objects in connection")

schema = strawberry.Schema(query=Query)

@strawberry.type(description="GraphQL type for a binned continuous measure field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/calculations_bins.html")
class BinField(DataField, Field, FieldReferencingField, Node):
    bin_size: str | None = strawberry.field(description="Size of the bin")
    data_category: FieldRoleCategory | None = strawberry.field(description="Data category of the field")
    data_type: FieldDataType | None = strawberry.field(description="Type of the data in the field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.html")
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    description: str | None = strawberry.field(description="Description of field shown in server and desktop clients")
    description_inherited: list[InheritedStringResult | None] | None = strawberry.field(description="description that is shown in the Tableau UI")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    downstream_columns: list[Column] = strawberry.field(description="Columns downstream of this field")
    downstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns downstream of this field")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this field")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this field")
    downstream_datasources: list[PublishedDatasource] | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_fields: list[Field] = strawberry.field(description="downstream fields that reference this field")
    downstream_fields_connection: FieldsConnection | None = strawberry.field(description="downstream fields that reference this field")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this field")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this field")
    downstream_lenses: list[Lens] | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metrics: list[Metric] | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_owners: list[TableauUser] | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected downstream from the field")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected downstream from the field")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this field")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this field")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream of this field")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream of this field")
    downstream_workbooks: list[Workbook] | None = strawberry.field(description="Workbooks connected downstream from the field")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected downstream from the field")
    fields: list[Field] = strawberry.field(description="List of fields, if any, that this field references")
    fields_connection: FieldsConnection | None = strawberry.field(description="List of fields, if any, that this field references")
    folder_name: str | None = strawberry.field(description="Name of folder if the field is in a folder. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_dwfeatures.html#Organize")
    formula: str | None = strawberry.field(description="Formula of the calculated field")
    fully_qualified_name: str | None = strawberry.field(description="Name internally used to uniquely identify fields")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    parameters: list[Parameter] = strawberry.field(description="List of parameters, if any, used in this field")
    parameters_connection: ParametersConnection | None = strawberry.field(description="List of parameters, if any, used in this field")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    role: FieldRole | None = strawberry.field(description="Role of the field: 'dimension', 'measure' or 'unknown'")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")
    upstream_columns: list[Column | None] = strawberry.field(description="All upstream columns this field references")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="All upstream columns this field references")
    upstream_databases: list[Database] = strawberry.field(description="Databases connected upstream from the field")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases connected upstream from the field")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources connected upstream from the field")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected upstream from the field")
    upstream_fields: list[Field | None] = strawberry.field(description="fields that are upstream of this field")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this field")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the field")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the field")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables connected upstream from the field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables connected upstream from the field")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this field")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this field")

@strawberry.type(description="GraphQL type for a calculated field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields.html")
class CalculatedField(AnalyticsField, DataField, Field, FieldReferencingField, Node):
    aggregation: str | None = strawberry.field(description="Default aggregation of the field, i.e. 'Sum', 'Average'. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/calculations_aggregation.html#AggFuncs")
    aggregation_param: str | None = strawberry.field(description="For the percentile aggregation, the percentile number")
    data_category: FieldRoleCategory | None = strawberry.field(description="Data category of the field")
    data_type: FieldDataType | None = strawberry.field(description="Type of the data in the field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.html")
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    default_format: str | None = strawberry.field(description="Default format for number or date")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    description: str | None = strawberry.field(description="Description of field shown in server and desktop clients")
    description_inherited: list[InheritedStringResult | None] | None = strawberry.field(description="description that is shown in the Tableau UI")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    downstream_columns: list[Column] = strawberry.field(description="Columns downstream of this field")
    downstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns downstream of this field")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this field")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this field")
    downstream_datasources: list[PublishedDatasource] | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_fields: list[Field] = strawberry.field(description="downstream fields that reference this field")
    downstream_fields_connection: FieldsConnection | None = strawberry.field(description="downstream fields that reference this field")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this field")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this field")
    downstream_lenses: list[Lens] | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metrics: list[Metric] | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_owners: list[TableauUser] | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected downstream from the field")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected downstream from the field")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this field")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this field")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream of this field")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream of this field")
    downstream_workbooks: list[Workbook] | None = strawberry.field(description="Workbooks connected downstream from the field")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected downstream from the field")
    fields: list[Field] = strawberry.field(description="List of fields, if any, that this field references")
    fields_connection: FieldsConnection | None = strawberry.field(description="List of fields, if any, that this field references")
    folder_name: str | None = strawberry.field(description="Name of folder if the field is in a folder. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_dwfeatures.html#Organize")
    formula: str | None = strawberry.field(description="Formula of the calculated field")
    fully_qualified_name: str | None = strawberry.field(description="Name internally used to uniquely identify fields")
    has_user_reference: bool | None = strawberry.field(description="True if field formula that involves a user function (for example, USERNAME or ISMEMBEROF)")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_auto_generated: bool | None = strawberry.field(description="True if Tableau automatically created this field. A list of autogenerated fields are here: https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_understanddatawindow.html#AutoFields")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    parameters: list[Parameter] = strawberry.field(description="List of parameters, if any, used in this field")
    parameters_connection: ParametersConnection | None = strawberry.field(description="List of parameters, if any, used in this field")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    role: FieldRole | None = strawberry.field(description="Role of the field: 'dimension', 'measure' or 'unknown'")
    semantic_role: str | None = strawberry.field(description="For geographic data, the geographic role of the field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_geographicroles.html")
    sheet: Sheet | None = strawberry.field(description="Sheet that contains this calculated field")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")
    upstream_columns: list[Column | None] = strawberry.field(description="All upstream columns this field references")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="All upstream columns this field references")
    upstream_databases: list[Database] = strawberry.field(description="Databases connected upstream from the field")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases connected upstream from the field")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources connected upstream from the field")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected upstream from the field")
    upstream_fields: list[Field | None] = strawberry.field(description="fields that are upstream of this field")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this field")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the field")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the field")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables connected upstream from the field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables connected upstream from the field")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this field")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this field")

@strawberry.type(description="ColumnFields are a type of field which directly connects to a column in some type of table.")
class ColumnField(AnalyticsField, DataField, Field, Node):
    aggregation: str | None = strawberry.field(description="Default aggregation of the field, i.e. 'Sum', 'Average'. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/calculations_aggregation.html#AggFuncs")
    aggregation_param: str | None = strawberry.field(description="For the percentile aggregation, the percentile number")
    columns: list[Column] = strawberry.field(description="List of columns, if any, that this field references")
    columns_connection: ColumnsConnection | None = strawberry.field(description="List of columns, if any, that this field references")
    data_category: FieldRoleCategory | None = strawberry.field(description="Data category of the field")
    data_type: FieldDataType | None = strawberry.field(description="Type of the data in the field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.html")
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    default_format: str | None = strawberry.field(description="Default format for number or date")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    description: str | None = strawberry.field(description="Description of field shown in server and desktop clients")
    description_inherited: list[InheritedStringResult | None] | None = strawberry.field(description="description that is shown in the Tableau UI")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    downstream_columns: list[Column] = strawberry.field(description="Columns downstream of this field")
    downstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns downstream of this field")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this field")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this field")
    downstream_datasources: list[PublishedDatasource] | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_fields: list[Field] = strawberry.field(description="downstream fields that reference this field")
    downstream_fields_connection: FieldsConnection | None = strawberry.field(description="downstream fields that reference this field")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this field")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this field")
    downstream_lenses: list[Lens] | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metrics: list[Metric] | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_owners: list[TableauUser] | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected downstream from the field")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected downstream from the field")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this field")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this field")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream of this field")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream of this field")
    downstream_workbooks: list[Workbook] | None = strawberry.field(description="Workbooks connected downstream from the field")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected downstream from the field")
    folder_name: str | None = strawberry.field(description="Name of folder if the field is in a folder. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_dwfeatures.html#Organize")
    fully_qualified_name: str | None = strawberry.field(description="Name internally used to uniquely identify fields")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    role: FieldRole | None = strawberry.field(description="Role of the field: 'dimension', 'measure' or 'unknown'")
    semantic_role: str | None = strawberry.field(description="For geographic data, the geographic role of the field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_geographicroles.html")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")
    upstream_columns: list[Column | None] = strawberry.field(description="All upstream columns this field references")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="All upstream columns this field references")
    upstream_databases: list[Database] = strawberry.field(description="Databases connected upstream from the field")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases connected upstream from the field")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources connected upstream from the field")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected upstream from the field")
    upstream_fields: list[Field | None] = strawberry.field(description="fields that are upstream of this field")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this field")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the field")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the field")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables connected upstream from the field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables connected upstream from the field")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this field")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this field")

@strawberry.type(description="GraphQL type for a combined field. Combined fields concatanate fields together into one string.")
class CombinedField(Field, FieldReferencingField, Node):
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    description: str | None = strawberry.field(description="Description of field shown in server and desktop clients")
    description_inherited: list[InheritedStringResult | None] | None = strawberry.field(description="description that is shown in the Tableau UI")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    downstream_columns: list[Column] = strawberry.field(description="Columns downstream of this field")
    downstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns downstream of this field")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this field")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this field")
    downstream_datasources: list[PublishedDatasource] | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_fields: list[Field] = strawberry.field(description="downstream fields that reference this field")
    downstream_fields_connection: FieldsConnection | None = strawberry.field(description="downstream fields that reference this field")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this field")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this field")
    downstream_lenses: list[Lens] | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metrics: list[Metric] | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_owners: list[TableauUser] | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected downstream from the field")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected downstream from the field")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this field")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this field")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream of this field")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream of this field")
    downstream_workbooks: list[Workbook] | None = strawberry.field(description="Workbooks connected downstream from the field")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected downstream from the field")
    fields: list[Field] = strawberry.field(description="List of fields, if any, that this field references")
    fields_connection: FieldsConnection | None = strawberry.field(description="List of fields, if any, that this field references")
    folder_name: str | None = strawberry.field(description="Name of folder if the field is in a folder. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_dwfeatures.html#Organize")
    fully_qualified_name: str | None = strawberry.field(description="Name internally used to uniquely identify fields")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")
    upstream_columns: list[Column | None] = strawberry.field(description="All upstream columns this field references")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="All upstream columns this field references")
    upstream_databases: list[Database] = strawberry.field(description="Databases connected upstream from the field")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases connected upstream from the field")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources connected upstream from the field")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected upstream from the field")
    upstream_fields: list[Field | None] = strawberry.field(description="fields that are upstream of this field")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this field")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the field")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the field")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables connected upstream from the field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables connected upstream from the field")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this field")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this field")

@strawberry.type(description="GraphQL type for a combined set field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/sortgroup_sets_create.html#Combine")
class CombinedSetField(Field, FieldReferencingField, Node):
    combination_type: str | None = strawberry.field(description="How the sets are combined. 'All Members in Both Sets', 'Shared Members in Both Sets', or 'Except Shared Members'")
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    delimiter: str | None = strawberry.field(description="Delimiter used to separate members of the two sets. Usually ',' or ';'")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    description: str | None = strawberry.field(description="Description of field shown in server and desktop clients")
    description_inherited: list[InheritedStringResult | None] | None = strawberry.field(description="description that is shown in the Tableau UI")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    downstream_columns: list[Column] = strawberry.field(description="Columns downstream of this field")
    downstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns downstream of this field")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this field")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this field")
    downstream_datasources: list[PublishedDatasource] | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_fields: list[Field] = strawberry.field(description="downstream fields that reference this field")
    downstream_fields_connection: FieldsConnection | None = strawberry.field(description="downstream fields that reference this field")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this field")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this field")
    downstream_lenses: list[Lens] | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metrics: list[Metric] | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_owners: list[TableauUser] | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected downstream from the field")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected downstream from the field")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this field")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this field")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream of this field")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream of this field")
    downstream_workbooks: list[Workbook] | None = strawberry.field(description="Workbooks connected downstream from the field")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected downstream from the field")
    fields: list[Field] = strawberry.field(description="List of fields, if any, that this field references")
    fields_connection: FieldsConnection | None = strawberry.field(description="List of fields, if any, that this field references")
    folder_name: str | None = strawberry.field(description="Name of folder if the field is in a folder. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_dwfeatures.html#Organize")
    fully_qualified_name: str | None = strawberry.field(description="Name internally used to uniquely identify fields")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")
    upstream_columns: list[Column | None] = strawberry.field(description="All upstream columns this field references")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="All upstream columns this field references")
    upstream_databases: list[Database] = strawberry.field(description="Databases connected upstream from the field")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases connected upstream from the field")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources connected upstream from the field")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected upstream from the field")
    upstream_fields: list[Field | None] = strawberry.field(description="fields that are upstream of this field")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this field")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the field")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the field")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables connected upstream from the field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables connected upstream from the field")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this field")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this field")

@strawberry.type(description="GraphQL type for a data source field. Data source fields can only exist in embedded data sources which connect to a published data source. A data source field is an embedded data source's 'layered' representation of a field that already exists in the published data source and is mostly a copy of the field in the published data source. Data source fields can get their own descriptions and renames local to the embedded data source, but cannot otherwise be modified in the embedded data source.")
class DatasourceField(Field, Node):
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    description: str | None = strawberry.field(description="Description of field shown in server and desktop clients")
    description_inherited: list[InheritedStringResult | None] | None = strawberry.field(description="description that is shown in the Tableau UI")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    downstream_columns: list[Column] = strawberry.field(description="Columns downstream of this field")
    downstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns downstream of this field")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this field")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this field")
    downstream_datasources: list[PublishedDatasource] | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_fields: list[Field] = strawberry.field(description="downstream fields that reference this field")
    downstream_fields_connection: FieldsConnection | None = strawberry.field(description="downstream fields that reference this field")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this field")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this field")
    downstream_lenses: list[Lens] | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metrics: list[Metric] | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_owners: list[TableauUser] | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected downstream from the field")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected downstream from the field")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this field")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this field")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream of this field")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream of this field")
    downstream_workbooks: list[Workbook] | None = strawberry.field(description="Workbooks connected downstream from the field")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected downstream from the field")
    folder_name: str | None = strawberry.field(description="Name of folder if the field is in a folder. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_dwfeatures.html#Organize")
    fully_qualified_name: str | None = strawberry.field(description="Name internally used to uniquely identify fields")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    remote_field: Field | None = strawberry.field(description="Reference to a field from a published data source. This property only exists on Fields that are in an embedded data source with a connection to a published data source.")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")
    upstream_columns: list[Column | None] = strawberry.field(description="All upstream columns this field references")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="All upstream columns this field references")
    upstream_databases: list[Database] = strawberry.field(description="Databases connected upstream from the field")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases connected upstream from the field")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources connected upstream from the field")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected upstream from the field")
    upstream_fields: list[Field | None] = strawberry.field(description="fields that are upstream of this field")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this field")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the field")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the field")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables connected upstream from the field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables connected upstream from the field")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this field")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this field")

@strawberry.type(description="GraphQL type for a group field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/sortgroup_groups_creating.html")
class GroupField(DataField, Field, FieldReferencingField, Node):
    data_category: FieldRoleCategory | None = strawberry.field(description="Data category of the field")
    data_type: FieldDataType | None = strawberry.field(description="Type of the data in the field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.html")
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    description: str | None = strawberry.field(description="Description of field shown in server and desktop clients")
    description_inherited: list[InheritedStringResult | None] | None = strawberry.field(description="description that is shown in the Tableau UI")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    downstream_columns: list[Column] = strawberry.field(description="Columns downstream of this field")
    downstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns downstream of this field")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this field")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this field")
    downstream_datasources: list[PublishedDatasource] | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_fields: list[Field] = strawberry.field(description="downstream fields that reference this field")
    downstream_fields_connection: FieldsConnection | None = strawberry.field(description="downstream fields that reference this field")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this field")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this field")
    downstream_lenses: list[Lens] | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metrics: list[Metric] | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_owners: list[TableauUser] | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected downstream from the field")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected downstream from the field")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this field")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this field")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream of this field")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream of this field")
    downstream_workbooks: list[Workbook] | None = strawberry.field(description="Workbooks connected downstream from the field")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected downstream from the field")
    fields: list[Field] = strawberry.field(description="List of fields, if any, that this field references")
    fields_connection: FieldsConnection | None = strawberry.field(description="List of fields, if any, that this field references")
    folder_name: str | None = strawberry.field(description="Name of folder if the field is in a folder. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_dwfeatures.html#Organize")
    fully_qualified_name: str | None = strawberry.field(description="Name internally used to uniquely identify fields")
    has_other: bool | None = strawberry.field(description="Field has an 'Other' group. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/sortgroup_groups_creating.html#Include")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    role: FieldRole | None = strawberry.field(description="Role of the field: 'dimension', 'measure' or 'unknown'")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")
    upstream_columns: list[Column | None] = strawberry.field(description="All upstream columns this field references")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="All upstream columns this field references")
    upstream_databases: list[Database] = strawberry.field(description="Databases connected upstream from the field")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases connected upstream from the field")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources connected upstream from the field")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected upstream from the field")
    upstream_fields: list[Field | None] = strawberry.field(description="fields that are upstream of this field")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this field")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the field")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the field")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables connected upstream from the field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables connected upstream from the field")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this field")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this field")

@strawberry.type(description="GraphQL type for a hierarchy. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/qs_hierarchies.html")
class HierarchyField(Field, FieldReferencingField, Node):
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    description: str | None = strawberry.field(description="Description of field shown in server and desktop clients")
    description_inherited: list[InheritedStringResult | None] | None = strawberry.field(description="description that is shown in the Tableau UI")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    downstream_columns: list[Column] = strawberry.field(description="Columns downstream of this field")
    downstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns downstream of this field")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this field")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this field")
    downstream_datasources: list[PublishedDatasource] | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_fields: list[Field] = strawberry.field(description="downstream fields that reference this field")
    downstream_fields_connection: FieldsConnection | None = strawberry.field(description="downstream fields that reference this field")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this field")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this field")
    downstream_lenses: list[Lens] | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metrics: list[Metric] | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_owners: list[TableauUser] | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected downstream from the field")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected downstream from the field")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this field")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this field")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream of this field")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream of this field")
    downstream_workbooks: list[Workbook] | None = strawberry.field(description="Workbooks connected downstream from the field")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected downstream from the field")
    fields: list[Field] = strawberry.field(description="List of fields, if any, that this field references")
    fields_connection: FieldsConnection | None = strawberry.field(description="List of fields, if any, that this field references")
    folder_name: str | None = strawberry.field(description="Name of folder if the field is in a folder. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_dwfeatures.html#Organize")
    fully_qualified_name: str | None = strawberry.field(description="Name internally used to uniquely identify fields")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")
    upstream_columns: list[Column | None] = strawberry.field(description="All upstream columns this field references")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="All upstream columns this field references")
    upstream_databases: list[Database] = strawberry.field(description="Databases connected upstream from the field")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases connected upstream from the field")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources connected upstream from the field")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected upstream from the field")
    upstream_fields: list[Field | None] = strawberry.field(description="fields that are upstream of this field")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this field")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the field")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the field")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables connected upstream from the field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables connected upstream from the field")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this field")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this field")

@strawberry.type(description="GraphQL type for a set field. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/sortgroup_sets_create.html")
class SetField(Field, FieldReferencingField, Node):
    datasource: Datasource | None = strawberry.field(description="Data source that contains this field")
    derived_lens_fields: list[LensField | None] | None = strawberry.field(description="List of lens fields which are derived from this field")
    derived_lens_fields_connection: LensFieldsConnection | None = strawberry.field(description="List of lens fields which are derived from this field")
    description: str | None = strawberry.field(description="Description of field shown in server and desktop clients")
    description_inherited: list[InheritedStringResult | None] | None = strawberry.field(description="description that is shown in the Tableau UI")
    direct_sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this field")
    direct_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this field")
    downstream_columns: list[Column] = strawberry.field(description="Columns downstream of this field")
    downstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns downstream of this field")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this field")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this field")
    downstream_datasources: list[PublishedDatasource] | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected downstream from this field")
    downstream_fields: list[Field] = strawberry.field(description="downstream fields that reference this field")
    downstream_fields_connection: FieldsConnection | None = strawberry.field(description="downstream fields that reference this field")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this field")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this field")
    downstream_lenses: list[Lens] | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this field.")
    downstream_metrics: list[Metric] | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the field")
    downstream_owners: list[TableauUser] | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners (authors) connected downstream from the field")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected downstream from the field")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected downstream from the field")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this field")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this field")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this field")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream of this field")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream of this field")
    downstream_workbooks: list[Workbook] | None = strawberry.field(description="Workbooks connected downstream from the field")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected downstream from the field")
    fields: list[Field] = strawberry.field(description="List of fields, if any, that this field references")
    fields_connection: FieldsConnection | None = strawberry.field(description="List of fields, if any, that this field references")
    folder_name: str | None = strawberry.field(description="Name of folder if the field is in a folder. See https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_dwfeatures.html#Organize")
    fully_qualified_name: str | None = strawberry.field(description="Name internally used to uniquely identify fields")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_hidden: bool | None = strawberry.field(description="True if the field is hidden")
    metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions that reference this data source field.")
    metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions that reference this data source field.")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    parameters: list[Parameter] = strawberry.field(description="List of parameters, if any, used in this field")
    parameters_connection: ParametersConnection | None = strawberry.field(description="List of parameters, if any, used in this field")
    referenced_by_bins: list[BinField | None] | None = strawberry.field(description="The bin field that references this field")
    referenced_by_bins_connection: BinFieldsConnection | None = strawberry.field(description="The bin field that references this field")
    referenced_by_calculations: list[CalculatedField | None] | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_calculations_connection: CalculatedFieldsConnection | None = strawberry.field(description="The calculated field that references this field")
    referenced_by_combined_fields: list[CombinedField | None] | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_fields_connection: CombinedFieldsConnection | None = strawberry.field(description="The combined field that references this field")
    referenced_by_combined_sets: list[CombinedSetField | None] | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_combined_sets_connection: CombinedSetFieldsConnection | None = strawberry.field(description="Thie combined set field that references this field")
    referenced_by_fields: list[FieldReferencingField | None] | None = strawberry.field(description="The field that references this field")
    referenced_by_fields_connection: FieldReferencingFieldsConnection | None = strawberry.field(description="The field that references this field")
    referenced_by_filters: list[DatasourceFilter | None] | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="The data source filters that include this field")
    referenced_by_flow_field_input_field: list[FlowFieldInputField | None] | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_input_field_connection: FlowFieldInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this field")
    referenced_by_flow_field_output_field: list[FlowFieldOutputField | None] | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_flow_field_output_field_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this field")
    referenced_by_groups: list[GroupField | None] | None = strawberry.field(description="The group field that references this field")
    referenced_by_groups_connection: GroupFieldsConnection | None = strawberry.field(description="The group field that references this field")
    referenced_by_hierarchies: list[HierarchyField | None] | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_hierarchies_connection: HierarchyFieldsConnection | None = strawberry.field(description="The hierarchy field that references this field")
    referenced_by_remote_fields: list[DatasourceField | None] | None = strawberry.field(description="The field that references this remote field")
    referenced_by_remote_fields_connection: DatasourceFieldsConnection | None = strawberry.field(description="The field that references this remote field")
    referenced_by_sets: list[SetField | None] | None = strawberry.field(description="The set field that this field references")
    referenced_by_sets_connection: SetFieldsConnection | None = strawberry.field(description="The set field that this field references")
    sheets: list[Sheet | None] | None = strawberry.field(description="Sheets that reference this data source field")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that reference this data source field")
    upstream_columns: list[Column | None] = strawberry.field(description="All upstream columns this field references")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="All upstream columns this field references")
    upstream_databases: list[Database] = strawberry.field(description="Databases connected upstream from the field")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases connected upstream from the field")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources connected upstream from the field")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources connected upstream from the field")
    upstream_fields: list[Field | None] = strawberry.field(description="fields that are upstream of this field")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this field")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the field")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the field")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables connected upstream from the field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables connected upstream from the field")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this field")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this field")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this field")

@strawberry.type(description="""
Metrics are time series data constructed from fields contained in views.  
*Retired in Tableau Cloud February 2024 / Server 2024.2.*
""")
class Metric(Taggable):
    container_name: str | None = strawberry.field(description="The name of the container in which the metric is visible and usable. This is always a project.")
    container_type: str = strawberry.field(description="The type of the container in which the metric is visible and usable. This is always a project.")
    created_at: datetime = strawberry.field(description="Time the Metric was created")
    description: str | None = strawberry.field(description="Description of the Metric")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    owner: TableauUser = strawberry.field(description="User who owns this Metric")
    project_name: str | None = strawberry.field(description="The name of the project in which the Metric is visible and usable.")
    project_vizportal_url_id: str = strawberry.field(description="The ID of the project in which the Metric is visible and usable.")
    site: TableauSite = strawberry.field(description="The site in which the Metric is visible and usable")
    tags: list[Tag] = strawberry.field(description="Tags associated with the Metric")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the Metric")
    underlying_view: View | None = strawberry.field(description="The original View off of which the Metric is based")
    updated_at: datetime = strawberry.field(description="Time the Metric was last updated")
    upstream_columns: list[Column | None] | None = strawberry.field(description="Columns that are upstream of this metric")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns that are upstream of this metric")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this Metric")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this Metric")
    upstream_databases: list[Database | None] | None = strawberry.field(description="Databases that are upstream of this metric")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are upstream of this metric")
    upstream_datasources: list[PublishedDatasource | None] | None = strawberry.field(description="The Published Datasources that are upstream to this Metric")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="The Published Datasources that are upstream to this Metric")
    upstream_fields: list[Field | None] | None = strawberry.field(description="fields that are upstream of this metric")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this metric")
    upstream_flow_column_output_fields: list[FlowColumnOutputField | None] | None = strawberry.field(description="OutputFields that are upstream of this Metric")
    upstream_flow_column_output_fields_connection: FlowColumnOutputFieldsConnection | None = strawberry.field(description="OutputFields that are upstream of this Metric")
    upstream_flow_field_output_fields: list[FlowFieldOutputField | None] | None = strawberry.field(description="OutputFields that are upstream of this Metric")
    upstream_flow_field_output_fields_connection: FlowFieldOutputFieldsConnection | None = strawberry.field(description="OutputFields that are upstream of this Metric")
    upstream_flow_output_fields: list[FlowOutputField | None] | None = strawberry.field(description="OutputFields that are upstream of this Metric")
    upstream_flow_output_fields_connection: FlowOutputFieldsConnection | None = strawberry.field(description="OutputFields that are upstream of this Metric")
    upstream_flows: list[Flow | None] | None = strawberry.field(description="The flows that are upstream of this metric")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="The flows that are upstream of this metric")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this Metric. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this Metric. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_lenses: list[Lens | None] | None = strawberry.field(description="The Lenses that are upstream of this workbook")
    upstream_lenses_connection: LensesConnection | None = strawberry.field(description="The Lenses that are upstream of this workbook")
    upstream_tables: list[DatabaseTable | None] = strawberry.field(description="tables that are upstream of this metric")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="tables that are upstream of this metric")
    upstream_workbooks: list[Workbook | None] | None = strawberry.field(description="Workbooks that are upstream of this metric")
    upstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks that are upstream of this metric")
    vizportal_url_id: str = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description='Workbooks are used to package up Tableau visualizations (which are called "sheets" in the Metadata API) and data models (which are called "embedded data sources" when they are owned by a workbook).')
class Workbook(Taggable):
    container_name: str | None = strawberry.field(description="The name of the container in which the workbook is visible and usable. Either a personal space or project.")
    container_type: str = strawberry.field(description="The type of the container in which the workbook is visible and usable. Either personal space or project.")
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the workbook contains unsupported custom SQL, in which case lineage may be incomplete")
    created_at: datetime = strawberry.field(description="Time the workbook was created")
    dashboards: list[Dashboard] = strawberry.field(description="Dashboards that are contained in this workbook")
    dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards that are contained in this workbook")
    description: str | None = strawberry.field(description="Description of the workbook")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics downstream from this workbook")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics downstream from this workbook")
    downstream_owners: list[TableauUser] = strawberry.field(description="Metric owners downstream from this workbook")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Metric owners downstream from this workbook")
    embedded_datasources: list[EmbeddedDatasource] = strawberry.field(description="Data sources that are embedded in this workbook")
    embedded_datasources_connection: EmbeddedDatasourcesConnection | None = strawberry.field(description="Data sources that are embedded in this workbook")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    owner: TableauUser = strawberry.field(description="User who owns this workbook")
    parameters: list[Parameter] = strawberry.field(description="Parameters that are contained in this workbook")
    parameters_connection: ParametersConnection | None = strawberry.field(description="Parameters that are contained in this workbook")
    project_luid: str | None = strawberry.field(description="The luid of the project in which the workbook is visible and usable. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    project_name: str | None = strawberry.field(description="The name of the project in which the workbook is visible and usable.")
    project_vizportal_url_id: str | None = strawberry.field(description="The ID of the project in which the workbook is visible and usable. Will be null if the workbook is not in a project.")
    sheets: list[Sheet] = strawberry.field(description="Worksheets that are contained in this workbook")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Worksheets that are contained in this workbook")
    site: TableauSite = strawberry.field(description="The site in which the workbook is visible and usable")
    tags: list[Tag] = strawberry.field(description="Tags associated with the workbook")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the workbook")
    updated_at: datetime = strawberry.field(description="Time the workbook was updated")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this workbook")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this workbook")
    upstream_databases: list[Database | None] = strawberry.field(description="The Databases that are upstream to this Workbook")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="The Databases that are upstream to this Workbook")
    upstream_datasources: list[PublishedDatasource | None] = strawberry.field(description="The Published Datasources that are upstream to this Workbook")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="The Published Datasources that are upstream to this Workbook")
    upstream_flows: list[Flow | None] | None = strawberry.field(description="The flows that are upstream of this workbook")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="The flows that are upstream of this workbook")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this workbook. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this workbook. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_lenses: list[Lens | None] | None = strawberry.field(description="The Lenses that are upstream of this workbook")
    upstream_lenses_connection: LensesConnection | None = strawberry.field(description="The Lenses that are upstream of this workbook")
    upstream_tables: list[DatabaseTable | None] = strawberry.field(description="The tables upstream to this Workbook")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="The tables upstream to this Workbook")
    upstream_virtual_connection_tables: list[VirtualConnectionTable | None] = strawberry.field(description="The virtual connection table upstream to this Workbook")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="The virtual connection table upstream to this Workbook")
    upstream_virtual_connections: list[VirtualConnection | None] = strawberry.field(description="The virtual connection upstream to this Workbook")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="The virtual connection upstream to this Workbook")
    uri: str | None = strawberry.field(description="Uri of the workbook")
    views: list[View] = strawberry.field(description="Views that are contained in this workbook")
    views_connection: ViewsConnection | None = strawberry.field(description="Views that are contained in this workbook")
    vizportal_url_id: str = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description="A cloud file connection")
class CloudFile(CanHaveLabels, Certifiable, Database, Taggable, Warnable):
    certification_note: str | None = strawberry.field(description="Notes related to this database being marked as certified")
    certifier: TableauUser | None = strawberry.field(description="User who marked this database as certified")
    connection_type: str | None = strawberry.field(description="Connection type shortname")
    contact: TableauUser | None = strawberry.field(description="Contact for this database")
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="The data quality certifications on a database")
    data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications on a database")
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="The optional data quality warning on a database")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a database")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a database")
    description: str | None = strawberry.field(description="User modifiable description of this database")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected to the database")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected to the database")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this database")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this database")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published datasources connected to the database")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published datasources connected to the database")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this database")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this database")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses connected to the database")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected to the database")
    downstream_metric_definitions: list[MetricDefinition | None] = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics connected to the database")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected to the database")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners connected to the database")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners connected to the database")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected to the database")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected to the database")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this database")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this database")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks connected to the database")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected to the database")
    file_extension: str | None = strawberry.field(description="The file extension")
    file_id: str | None = strawberry.field(description="The ID used by the provider for the cloud file. Each provider uses IDs in a different format.")
    has_active_warning: bool = strawberry.field(description="True if the database has an active data quality warning")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool = strawberry.field(description="True if this database contains an active data quality certification")
    is_controlled_permissions_enabled: bool | None = strawberry.field(description="True if this database has its permission locked")
    is_embedded: bool | None = strawberry.field(description="True if this file is embedded in Tableau content, e.g., a packaged workbook")
    is_grouped: bool | None = strawberry.field(description="True if this database has been grouped with other databases")
    labels: list[Label] = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    mime_type: str | None = strawberry.field(description="The MIME type")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_vizportal_url_id: str | None = strawberry.field(description="The ID of the project in which the database is visible. Will be empty if the database is not in a project.")
    provider: str | None = strawberry.field(description="The provider of the cloud file, e.g., onedrive, google-sheets, dropbox, and box")
    referenced_by_queries: list[CustomSQLTable | None] | None = strawberry.field(description="The custom SQL queries that reference this database")
    referenced_by_queries_connection: CustomSQLTablesConnection | None = strawberry.field(description="The custom SQL queries that reference this database")
    request_url: str | None = strawberry.field(description="URL for requesting the cloud file")
    tables: list[DatabaseTable | None] | None = strawberry.field(description="Tables belonging to this database")
    tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables belonging to this database")
    tags: list[Tag] = strawberry.field(description="Tags associated with the database")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the database")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream of this database")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream of this database")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this database")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this database")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream of this database")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream of this database")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream of this database")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream of this database")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this database, for use in client-to-server communications")

@strawberry.type(description="GraphQL type for a table column")
class Column(CanHaveLabels, Node, Taggable, Warnable):
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="The optional data quality warning on this column.")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on this column. Available in Tableau Cloud October 2022 / Server 2022.3 and later.")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on this column. Available in Tableau Cloud October 2022 / Server 2022.3 and later.")
    description: str | None = strawberry.field(description="User modifiable description of this column")
    description_inherited: list[InheritedStringResult | None] | None = strawberry.field(description="description that is shown in the Tableau UI")
    display_name: str | None = strawberry.field(description="Optional display name for column")
    downstream_columns: list[Column] = strawberry.field(description="Columns downstream from the column")
    downstream_columns_connection: ColumnsConnection | None = strawberry.field(description="Columns downstream from the column")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards downstream from the column")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards downstream from the column")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream from the column")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream from the column")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published datasources downstream from the column")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published datasources downstream from the column")
    downstream_fields: list[Field] = strawberry.field(description="Fields downstream from the column")
    downstream_fields_connection: FieldsConnection | None = strawberry.field(description="Fields downstream from the column")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream from the column")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream from the column")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses downstream from the column")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses downstream from the column")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from the column.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from the column.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics downstream from the column")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics downstream from the column")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners of workbooks and published datasources downstream from the column")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners of workbooks and published datasources downstream from the column")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets downstream from the column")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets downstream from the column")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream from the column")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream from the column")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream from the column")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream from the column")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream from the column")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream from the column")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks downstream from the column")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks downstream from the column")
    has_active_warning: bool = strawberry.field(description="True if this column has an active data quality warning. Available in Tableau Cloud October 2022 / Server 2022.3 and later.")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_nullable: bool | None = strawberry.field(description="True if this column may contain null values")
    labels: list[Label] = strawberry.field(description="The labels on this column.  Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on this column.  Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name of column")
    referenced_by_fields: list[ColumnField | None] | None = strawberry.field(description="The column field that references this column")
    referenced_by_fields_connection: ColumnFieldsConnection | None = strawberry.field(description="The column field that references this column")
    referenced_by_flow_column_input_field: list[FlowColumnInputField | None] | None = strawberry.field(description="A flow input field that wraps this column")
    referenced_by_flow_column_input_field_connection: FlowColumnInputFieldsConnection | None = strawberry.field(description="A flow input field that wraps this column")
    referenced_by_flow_column_output_field: list[FlowColumnOutputField | None] | None = strawberry.field(description="A flow output field that wraps this column")
    referenced_by_flow_column_output_field_connection: FlowColumnOutputFieldsConnection | None = strawberry.field(description="A flow output field that wraps this column")
    referenced_by_remote_column: list[Column | None] | None = strawberry.field(description="A column that logically represents this column.")
    referenced_by_remote_column_connection: ColumnsConnection | None = strawberry.field(description="A column that logically represents this column.")
    remote_column: Column | None = strawberry.field(description="A column that this column logically represents.")
    remote_type: RemoteType = strawberry.field(description="Remote type on the database. Types correspond to OLEDB types here: https://referencesource.microsoft.com/#system.data/System/Data/OleDb/OLEDB_Enum.cs,364")
    table: Table | None = strawberry.field(description="The table that this column belongs to")
    tags: list[Tag] = strawberry.field(description="Tags associated with the column")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the column")
    upstream_columns: list[Column | None] = strawberry.field(description="All upstream columns this column references")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="All upstream columns this column references")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream from the Table")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream from the Table")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream from this column")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream from this column")
    upstream_fields: list[Field | None] = strawberry.field(description="fields that are upstream of this column")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="fields that are upstream of this column")
    upstream_flows: list[Flow] = strawberry.field(description="Flows connected upstream from the column")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows connected upstream from the column")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream from the column")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream from the column")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream from the column")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream from the column")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream from the column")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream from the column")
    vizportal_id: str | None = strawberry.field(description="Vizportal ID of this column, for use in client-to-server communications")

@strawberry.type(description="""
A Data Cloud connection  
*Available in Tableau Cloud February 2024 / Server 2024.2 and later.*
""")
class DataCloud(CanHaveLabels, Certifiable, Database, Taggable, Warnable):
    certification_note: str | None = strawberry.field(description="Notes related to this database being marked as certified")
    certifier: TableauUser | None = strawberry.field(description="User who marked this database as certified")
    connection_type: str | None = strawberry.field(description="Connection type shortname")
    contact: TableauUser | None = strawberry.field(description="Contact for this database")
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="The data quality certifications on a database")
    data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications on a database")
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="The optional data quality warning on a database")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a database")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a database")
    description: str | None = strawberry.field(description="User modifiable description of this database")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected to the database")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected to the database")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this database")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this database")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published datasources connected to the database")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published datasources connected to the database")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this database")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this database")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses connected to the database")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected to the database")
    downstream_metric_definitions: list[MetricDefinition | None] = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics connected to the database")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected to the database")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners connected to the database")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners connected to the database")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected to the database")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected to the database")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this database")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this database")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks connected to the database")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected to the database")
    has_active_warning: bool = strawberry.field(description="True if the database has an active data quality warning")
    id: strawberry.ID = strawberry.field(description="Unique identifier used with the Metadata API.  Not the same as the locally unique identifier used with the REST API.")
    is_certified: bool = strawberry.field(description="True if this database contains an active data quality certification")
    is_controlled_permissions_enabled: bool | None = strawberry.field(description="True if this database has its permission locked")
    is_embedded: bool | None = strawberry.field(description="True if this database is embedded in Tableau content, e.g., a packaged workbook")
    is_grouped: bool | None = strawberry.field(description="True if this database has been grouped with other databases")
    labels: list[Label] = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used with the REST API.")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_vizportal_url_id: str | None = strawberry.field(description="The ID of the project in which the database is visible. Will be empty if the database is not in a project.")
    referenced_by_queries: list[CustomSQLTable | None] | None = strawberry.field(description="The custom SQL queries that reference this database")
    referenced_by_queries_connection: CustomSQLTablesConnection | None = strawberry.field(description="The custom SQL queries that reference this database")
    tables: list[DatabaseTable | None] | None = strawberry.field(description="Tables belonging to this database")
    tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables belonging to this database")
    tags: list[Tag] = strawberry.field(description="Tags associated with the database")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the database")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream of this database")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream of this database")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this database")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this database")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream of this database")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream of this database")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream of this database")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream of this database")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this database, for use in client-to-server communications")

@strawberry.type(description="A database server connection")
class DatabaseServer(CanHaveLabels, Certifiable, Database, Taggable, Warnable):
    certification_note: str | None = strawberry.field(description="Notes related to this database being marked as certified")
    certifier: TableauUser | None = strawberry.field(description="User who marked this database as certified")
    connection_type: str | None = strawberry.field(description="Connection type shortname")
    contact: TableauUser | None = strawberry.field(description="Contact for this database")
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="The data quality certifications on a database")
    data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications on a database")
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="The optional data quality warning on a database")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a database")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a database")
    description: str | None = strawberry.field(description="User modifiable description of this database")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected to the database")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected to the database")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this database")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this database")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published datasources connected to the database")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published datasources connected to the database")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this database")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this database")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses connected to the database")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected to the database")
    downstream_metric_definitions: list[MetricDefinition | None] = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics connected to the database")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected to the database")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners connected to the database")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners connected to the database")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected to the database")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected to the database")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this database")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this database")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks connected to the database")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected to the database")
    extended_connection_type: str | None = strawberry.field(description="optional Extended Connection info for specific connection types, eg hive for Cloudera Hadoop")
    has_active_warning: bool = strawberry.field(description="True if the database has an active data quality warning")
    host_name: str | None = strawberry.field(description="Hostname of the database")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool = strawberry.field(description="True if this database contains an active data quality certification")
    is_controlled_permissions_enabled: bool | None = strawberry.field(description="True if this database has its permission locked")
    is_embedded: bool | None = strawberry.field(description="A database server is never embedded in Tableau content")
    is_grouped: bool | None = strawberry.field(description="True if this database has been grouped with other databases")
    labels: list[Label] = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    port: int | None = strawberry.field(description="Port number of the database connection")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_vizportal_url_id: str | None = strawberry.field(description="The ID of the project in which the database is visible. Will be empty if the database is not in a project.")
    referenced_by_queries: list[CustomSQLTable | None] | None = strawberry.field(description="The custom SQL queries that reference this database")
    referenced_by_queries_connection: CustomSQLTablesConnection | None = strawberry.field(description="The custom SQL queries that reference this database")
    service: str | None = strawberry.field(description="service string for certain datasources eg Oracle")
    tables: list[DatabaseTable | None] | None = strawberry.field(description="Tables belonging to this database")
    tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables belonging to this database")
    tags: list[Tag] = strawberry.field(description="Tags associated with the database")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the database")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream of this database")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream of this database")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this database")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this database")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream of this database")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream of this database")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream of this database")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream of this database")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this database, for use in client-to-server communications")

@strawberry.type(description="A file connection")
class File(CanHaveLabels, Certifiable, Database, Taggable, Warnable):
    certification_note: str | None = strawberry.field(description="Notes related to this database being marked as certified")
    certifier: TableauUser | None = strawberry.field(description="User who marked this database as certified")
    connection_type: str | None = strawberry.field(description="Connection type shortname")
    contact: TableauUser | None = strawberry.field(description="Contact for this database")
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="The data quality certifications on a database")
    data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications on a database")
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="The optional data quality warning on a database")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a database")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a database")
    description: str | None = strawberry.field(description="User modifiable description of this database")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected to the database")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected to the database")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this database")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this database")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published datasources connected to the database")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published datasources connected to the database")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this database")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this database")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses connected to the database")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected to the database")
    downstream_metric_definitions: list[MetricDefinition | None] = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics connected to the database")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected to the database")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners connected to the database")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners connected to the database")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected to the database")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected to the database")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this database")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this database")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks connected to the database")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected to the database")
    file_path: str | None = strawberry.field(description="Path to file")
    has_active_warning: bool = strawberry.field(description="True if the database has an active data quality warning")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the Metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool = strawberry.field(description="True if this database contains an active data quality certification")
    is_controlled_permissions_enabled: bool | None = strawberry.field(description="True if this database has its permission locked")
    is_embedded: bool | None = strawberry.field(description="True if this file is embedded in Tableau content, e.g., a packaged workbook")
    is_grouped: bool | None = strawberry.field(description="True if this database has been grouped with other databases")
    labels: list[Label] = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_vizportal_url_id: str | None = strawberry.field(description="The ID of the project in which the database is visible. Will be empty if the database is not in a project.")
    referenced_by_queries: list[CustomSQLTable | None] | None = strawberry.field(description="The custom SQL queries that reference this database")
    referenced_by_queries_connection: CustomSQLTablesConnection | None = strawberry.field(description="The custom SQL queries that reference this database")
    tables: list[DatabaseTable | None] | None = strawberry.field(description="Tables belonging to this database")
    tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables belonging to this database")
    tags: list[Tag] = strawberry.field(description="Tags associated with the database")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the database")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream of this database")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream of this database")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this database")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this database")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream of this database")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream of this database")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream of this database")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream of this database")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this database, for use in client-to-server communications")

@strawberry.type(description="Flows are used to prepare data, which can include aggregation, cleaning, preprocessing, etc.")
class Flow(CanHaveLabels, Taggable, Warnable):
    container_name: str | None = strawberry.field(description="The name of the container in which the flow is visible and usable. Either a personal space or project.")
    container_type: str = strawberry.field(description="The type of the container in which the flow is visible and usable. Either personal space or project.")
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the flow contains unsupported custom SQL, in which case lineage may be incomplete")
    created_at: datetime | None = strawberry.field(description="Time the flow was created. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="The optional data quality warning on a flow")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a flow")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a flow")
    description: str | None = strawberry.field(description="Description of the flow")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards that are downstream from this flow")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards that are downstream from this flow")
    downstream_databases: list[Database] = strawberry.field(description="Databases that are downstream from this flow.")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are downstream from this flow.")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published Data Sources that are downstream from this flow.")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published Data Sources that are downstream from this flow.")
    downstream_flows: list[Flow] = strawberry.field(description="Flows that are downstream from this flow.")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are downstream from this flow.")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses that are downstream from this flow")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses that are downstream from this flow")
    downstream_linked_flows: list[LinkedFlow] = strawberry.field(description="Linked flows that are downstream from this flow.")
    downstream_linked_flows_connection: LinkedFlowsConnection | None = strawberry.field(description="Linked flows that are downstream from this flow.")
    downstream_metric_definitions: list[MetricDefinition | None] = strawberry.field(description="Metric definitions downstream from this flow.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this flow.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics that are downstream from this flow")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics that are downstream from this flow")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners that are downstream from this flow")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners that are downstream from this flow")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets that are downstream from this flow")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that are downstream from this flow")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables that are downstream from this flow.")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables that are downstream from this flow.")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="VirtualConnectionTables that are downstream of this flow")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="VirtualConnectionTables that are downstream of this flow")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="VirtualConnections that are downstream of this flow")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="VirtualConnections that are downstream of this flow")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks that are downstream from this flow")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks that are downstream from this flow")
    has_active_warning: bool = strawberry.field(description="True if the flow has an active data quality warning")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    input_fields: list[FlowInputField] = strawberry.field(description="Fields that are inputs to this flow")
    input_fields_connection: FlowInputFieldsConnection | None = strawberry.field(description="Fields that are inputs to this flow")
    labels: list[Label] = strawberry.field(description="The labels on a flow. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a flow. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    next_downstream_flows: list[Flow] = strawberry.field(description="Flows that are next immediate downstream from this flow.")
    next_downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are next immediate downstream from this flow.")
    next_upstream_flows: list[Flow | None] = strawberry.field(description="Flows that are next immediate upstream from this flow.")
    next_upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are next immediate upstream from this flow.")
    output_fields: list[FlowOutputField] = strawberry.field(description="Fields that are outputs of this flow")
    output_fields_connection: FlowOutputFieldsConnection | None = strawberry.field(description="Fields that are outputs of this flow")
    output_steps: list[FlowOutputStep] = strawberry.field(description="Output steps for this flow")
    output_steps_connection: FlowOutputStepsConnection | None = strawberry.field(description="Output steps for this flow")
    owner: TableauUser | None = strawberry.field(description="User who owns this flow")
    personal_space_url_link: str | None = strawberry.field(description="The link to the personal space in which the flow is visible and usable. Will be null if the flow is not in a personal space.")
    project_name: str | None = strawberry.field(description="The name of the project in which the flow is visible and usable")
    project_vizportal_url_id: str | None = strawberry.field(description="The ID of the project in which the flow is visible and usable. Will be null if the flow is not in a project.")
    site: TableauSite | None = strawberry.field(description="The site in which the flow is visible and usable")
    tags: list[Tag] = strawberry.field(description="Tags associated with a flow")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with a flow")
    updated_at: datetime | None = strawberry.field(description="Time the flow was updated. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this flow")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this flow")
    upstream_databases: list[Database] = strawberry.field(description="Databases that are upstream from this flow.")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are upstream from this flow.")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources that are upstream from this flow.")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources that are upstream from this flow.")
    upstream_flows: list[Flow] = strawberry.field(description="Flows that are upstream from this flow.")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are upstream from this flow.")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this flow. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this flow. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_linked_flows: list[LinkedFlow] = strawberry.field(description="Linked flows that are upstream from this flow.")
    upstream_linked_flows_connection: LinkedFlowsConnection | None = strawberry.field(description="Linked flows that are upstream from this flow.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables that are upstream from this flow.")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables that are upstream from this flow.")
    upstream_virtual_connection_tables: list[VirtualConnectionTable | None] = strawberry.field(description="The virtual connection table upstream to this Flow")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="The virtual connection table upstream to this Flow")
    upstream_virtual_connections: list[VirtualConnection | None] | None = strawberry.field(description="The virtual connection upstream to this Flow")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="The virtual connection upstream to this Flow")
    uri: str | None = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    vizportal_url_id: str = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description="""
A virtual connection.  
*Available in Tableau Cloud March 2022 / Server 2022.1 and later.*
""")
class VirtualConnection(CanHaveLabels, Certifiable, Taggable, Warnable):
    connection_type: str | None = strawberry.field(description="Connection type of this virtual connection")
    container_name: str | None = strawberry.field(description="The name of the container in which the virtual connection is visible and usable. Either a personal space or project.")
    container_type: str = strawberry.field(description="The type of the container in which the virtual connection is visible and usable. Either personal space or project.")
    created_at: datetime | None = strawberry.field(description="Time the Virtual Connection was created. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="The data quality certifications on a virtual connection")
    data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications on a virtual connection")
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="Singular data quality warning, deprecated but required to implement @warnable")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a virtual connection")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a virtual connection")
    description: str | None = strawberry.field(description="User modifiable description of this virtual connection")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards downstream of this virtual connection")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards downstream of this virtual connection")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published Data Sources downstream of this virtual connection")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published Data Sources downstream of this virtual connection")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this virtual connection")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this virtual connection")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses downstream of this published connection")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses downstream of this published connection")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this VirtualConnection.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this VirtualConnection.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics downstream of this virtual connection")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics downstream of this virtual connection")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners connected to the database")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners connected to the database")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets downstream of this virtual connection")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets downstream of this virtual connection")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="VirtualConnectionTables downstream of this virtual connection")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="VirtualConnectionTables downstream of this virtual connection")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks downstream of this virtual connection")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks downstream of this virtual connection")
    has_active_warning: bool = strawberry.field(description="True if the virtual connection has an active data quality warning")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool = strawberry.field(description="True if this virtual connection contains an active data quality certification")
    labels: list[Label] = strawberry.field(description="The labels on a virtual connection. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a virtual connection. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    owner: TableauUser = strawberry.field(description="User who owns this virtual connection")
    project_name: str | None = strawberry.field(description="The name of the project that contains this virtual connection.")
    project_vizportal_url_id: str | None = strawberry.field(description="The ID of the project in which the virtual connection is visible and usable. Will return null if the published virtual connection is not in a project.")
    site: TableauSite = strawberry.field(description="The site which contains this virtual connection")
    tables: list[VirtualConnectionTable] = strawberry.field(description="The tables exposed by this virtual connection")
    tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="The tables exposed by this virtual connection")
    tags: list[Tag] = strawberry.field(description="Tags associated with the virtual connection")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the virtual connection")
    updated_at: datetime | None = strawberry.field(description="Time the Virtual Connection was last updated. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this virtual connection")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this virtual connection")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream of this virtual connection")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream of this virtual connection")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this virtual connection")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this virtual connection")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream of this virtual connection")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream of this virtual connection")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this virtual connection. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this virtual connection. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream of this virtual connection")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream of this virtual connection")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="The virtual connection tables that are upstream to this virtual connection")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="The virtual connection tables that are upstream to this virtual connection")
    uri: str | None = strawberry.field(description="Uri of the virtual connection")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this table, for use in client-to-server communications")
    vizportal_url_id: str = strawberry.field(description="Vizportal URL ID; used for URL generation")

@strawberry.type(description="A web data connector")
class WebDataConnector(CanHaveLabels, Certifiable, Database, Taggable, Warnable):
    certification_note: str | None = strawberry.field(description="Notes related to the web data connector table being marked as certified")
    certifier: TableauUser | None = strawberry.field(description="User who marked this database as certified")
    connection_type: str | None = strawberry.field(description="The type of web data connector")
    connector_url: str | None = strawberry.field(description="The url for the sign-in page of the web data connector")
    contact: TableauUser | None = strawberry.field(description="Contact for this database")
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="The data quality certifications on a database")
    data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications on a database")
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="The optional data quality warning on a database")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a database")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a database")
    description: str | None = strawberry.field(description="User modifiable description of this database")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected to the database")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected to the database")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this database")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this database")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published datasources connected to the database")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published datasources connected to the database")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this database")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this database")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses connected to the database")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected to the database")
    downstream_metric_definitions: list[MetricDefinition | None] = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this database.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics connected to the database")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected to the database")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners connected to the database")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners connected to the database")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected to the database")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected to the database")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this database")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this database")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables downstream of this database")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks connected to the database")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected to the database")
    has_active_warning: bool = strawberry.field(description="True if the database has an active data quality warning")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the Metadata API. Not the same as the numeric ID used on server")
    is_certified: bool = strawberry.field(description="True if this database contains an active data quality certification")
    is_controlled_permissions_enabled: bool | None = strawberry.field(description="True if this database has its permission locked")
    is_embedded: bool | None = strawberry.field(description="A web data connector is always embedded in Tableau content")
    is_grouped: bool | None = strawberry.field(description="True if this database has been grouped with other databases")
    labels: list[Label] = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the database is visible. Will be empty if the database is not in a project.")
    project_vizportal_url_id: str | None = strawberry.field(description="The ID of the project in which the database is visible. Will be empty if the database is not in a project.")
    referenced_by_queries: list[CustomSQLTable | None] | None = strawberry.field(description="The custom SQL queries that reference this database")
    referenced_by_queries_connection: CustomSQLTablesConnection | None = strawberry.field(description="The custom SQL queries that reference this database")
    tables: list[DatabaseTable | None] | None = strawberry.field(description="Tables belonging to this database")
    tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables belonging to this database")
    tags: list[Tag] = strawberry.field(description="Tags associated with the database")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the database")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this database")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream of this database")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream of this database")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this database")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this database")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream of this database")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream of this database")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this database. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream of this database")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream of this database")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables upstream of this database")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables upstream of this database")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this database, for use in client-to-server communications")

@strawberry.type(description='A table that represents the result of evaluating a custom SQL query. These "tables" are owned by the Tableau data source (embedded or published) which contains the SQL query, so they only exist within that data source.')
class CustomSQLTable(Table):
    columns: list[Column] = strawberry.field(description="Columns contained in this table")
    columns_connection: ColumnsConnection | None = strawberry.field(description="Columns contained in this table")
    connection_type: str | None = strawberry.field(description="Connection type shortname")
    database: Database | None = strawberry.field(description="Database this query is executed on")
    description: str | None = strawberry.field(description="User modifiable description of this table")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected to the table")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected to the table")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this table")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this table")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published datasources connected to the table")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published datasources connected to the table")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this table")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this table")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses connected downstream from the table")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from the table")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics connected downstream from the table")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the table")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners of workbooks and published datasources connected to the table")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners of workbooks and published datasources connected to the table")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected to the table")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected to the table")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this table")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this table")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this table")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this table")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection downstream of this table")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection downstream of this table")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks connected to the table")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected to the table")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_embedded: bool | None = strawberry.field(description="A custom SQL tables is always embedded in Tableau content")
    is_unsupported_custom_sql: bool | None = strawberry.field(description="True if the query is unsupported by Tableau Catalog, in which case lineage may be incomplete")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    query: str | None = strawberry.field(description="Text of the query")
    tables: list[DatabaseTable] = strawberry.field(description="Actual tables that this query references.")
    tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Actual tables that this query references.")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream of this table")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream of this table")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this table")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this table")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream of this table")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream of this table")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream of this table")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream of this table")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this table")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this table")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connection tables upstream of this table")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connection tables upstream of this table")

@strawberry.type(description="A table that is contained in a database")
class DatabaseTable(CanHaveLabels, Certifiable, Table, Taggable, Warnable):
    additional_details: TableAdditionalDetails | None = strawberry.field(description="Additional details regarding this table")
    certification_note: str | None = strawberry.field(description="Notes related to the database table being marked as certified")
    certifier: TableauUser | None = strawberry.field(description="User who marked this table as certified")
    columns: list[Column] = strawberry.field(description="Columns contained in this table")
    columns_connection: ColumnsConnection | None = strawberry.field(description="Columns contained in this table")
    connection_type: str | None = strawberry.field(description="Connection type of parent database")
    contact: TableauUser | None = strawberry.field(description="Contact for this table")
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="The data quality certifications on a table")
    data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications on a table")
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="The optional data quality warning on a table")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a table")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a table")
    database: Database | None = strawberry.field(description="The database to which this table belongs")
    description: str | None = strawberry.field(description="User modifiable description of this table")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the table")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the table")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this table")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this table")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published datasources connected to the table")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published datasources connected to the table")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this table")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this table")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses connected downstream from the table")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from the table")
    downstream_metric_definitions: list[MetricDefinition | None] = strawberry.field(description="Metric definitions downstream from this databaseTable.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this databaseTable.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics connected downstream from the table")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics connected downstream from the table")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners of workbooks and published datasources connected to the table")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners of workbooks and published datasources connected to the table")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected to the table")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected to the table")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this table")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this table")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream from this table")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream from this table")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream from this table")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream from this table")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks connected to the table")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected to the table")
    full_name: str | None = strawberry.field(description="Fully qualified table name")
    has_active_warning: bool = strawberry.field(description="True if the table has an active data quality warning")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool = strawberry.field(description="True if this table contains an active data quality certification")
    is_embedded: bool | None = strawberry.field(description="True if this table is embedded in Tableau content")
    labels: list[Label] = strawberry.field(description="The labels on a table. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a table. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    project_name: str | None = strawberry.field(description="The name of the project in which the table is visible. Will be empty if the table is not in a project.")
    project_vizportal_url_id: str | None = strawberry.field(description="The ID of the project in which the table is visible. Will be empty if the table is not in a project.")
    referenced_by_queries: list[CustomSQLTable | None] | None = strawberry.field(description="The custom SQL queries that reference this table")
    referenced_by_queries_connection: CustomSQLTablesConnection | None = strawberry.field(description="The custom SQL queries that reference this table")
    schema: str | None = strawberry.field(description="""
Name of table schema.
    
Note: For some databases, such as Amazon Athena and Exasol, the schema attribute may not return the correct schema name for the table. For more information, see https://help.tableau.com/current/api/metadata_api/en-us/docs/meta_api_model.html#schema_attribute.
""")
    table_type: TableType = strawberry.field(description="Type of the table")
    tags: list[Tag] = strawberry.field(description="Tags associated with the table")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the table")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this table")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this table")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream of this table")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream of this table")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this table")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this table")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream of this table")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream of this table")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this table. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this table. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream of this table")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream of this table")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream from this table")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream from this table")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream from this table")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream from this table")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this table, for use in client-to-server communications")

@strawberry.type(description="""
A table in a virtual connection.  
*Available in Tableau Cloud March 2022 / Server 2022.1 and later.*
""")
class VirtualConnectionTable(CanHaveLabels, Certifiable, Table, Taggable, Warnable):
    columns: list[Column] = strawberry.field(description="Columns contained by this table")
    columns_connection: ColumnsConnection | None = strawberry.field(description="Columns contained by this table")
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="The data quality certifications on a virtual connection table")
    data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications on a virtual connection table")
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="Singular data quality warning, deprecated but required to implement @warnable")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a virtual connection table")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a virtual connection table")
    description: str | None = strawberry.field(description="User modifiable description of this table")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected to the table")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected to the table")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream of this table")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream of this table")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Published datasources connected to the table")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Published datasources connected to the table")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream of this table")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream of this table")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses connected to the table")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected to the table")
    downstream_metric_definitions: list[MetricDefinition | None] = strawberry.field(description="Metric definitions downstream from this virtualConnectionTable.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this virtualConnectionTable.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics downstream of this table")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics downstream of this table")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners of workbooks and published datasources connected to the table")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners of workbooks and published datasources connected to the table")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets connected to the table")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets connected to the table")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream of this table")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream of this table")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this table")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this table")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream of this table")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream of this table")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks connected to the table")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks connected to the table")
    extract_last_refresh_type: ExtractType | None = strawberry.field(description="The type of this table's last extract refresh (incremental or full).")
    extract_last_refreshed_at: datetime | None = strawberry.field(description="The time the data for this table's extract was refreshed.")
    has_active_warning: bool = strawberry.field(description="True if the table has an active data quality warning")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool = strawberry.field(description="True if this virtual connection table contains an active data quality certification")
    is_embedded: bool | None = strawberry.field(description="True if this table is embedded in Tableau content, e.g., a packaged workbook")
    is_extracted: bool | None = strawberry.field(description="Whether or not queries to this table are using an extract.")
    labels: list[Label] = strawberry.field(description="The labels on a virtual connection table. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a virtual connection table. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    owner: TableauUser = strawberry.field(description="User who owns this virtual connection table")
    tags: list[Tag] = strawberry.field(description="Tags associated with this table")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with this table")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this virtual connection")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this virtual connection")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream of this table")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream of this table")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream of this table")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream of this table")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream of this table")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream of this table")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this virtual connection. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this virtual connection. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream of this table")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream of this table")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables upstream of this table")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables upstream of this table")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections upstream of this table")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections upstream of this table")
    uri: str | None = strawberry.field(description="Uri of the virtual connection table")
    virtual_connection: VirtualConnection | None = strawberry.field(description="The parent virtual connection for this table")
    vizportal_id: str | None = strawberry.field(description="Vizportal ID of this column, for use in client-to-server communications")
    vizportal_url_id: str = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description="A dashboard contained in a published workbook.")
class Dashboard(Taggable, View):
    ask_data_extensions: list[AskDataExtension] = strawberry.field(description="AskDataExtensions that are added into this dashboard")
    ask_data_extensions_connection: AskDataExtensionsConnection | None = strawberry.field(description="AskDataExtensions that are added into this dashboard")
    created_at: datetime = strawberry.field(description="Time the dashboard was created")
    document_view_id: str | None = strawberry.field(description="Unique ID for the dashboard generated for and stored within the workbook, survives renames, and is used for internal processes")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    index: int | None = strawberry.field(description="Index of view; the order it appears in the workbook")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server (Blank if worksheet is hidden in Workbook)")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    path: str | None = strawberry.field(description="Server path to dashboard")
    referenced_by_metrics: list[Metric | None] | None = strawberry.field(description="The Metrics that reference this View")
    referenced_by_metrics_connection: MetricsConnection | None = strawberry.field(description="The Metrics that reference this View")
    sheets: list[Sheet] = strawberry.field(description="Sheets referenced by this dashboard")
    sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets referenced by this dashboard")
    tags: list[Tag] = strawberry.field(description="Tags associated with the view")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the view")
    updated_at: datetime = strawberry.field(description="Time the dashboard was updated")
    upstream_columns: list[Column | None] | None = strawberry.field(description="The columns that are upstream of this dashboard")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="The columns that are upstream of this dashboard")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this dashboard")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this dashboard")
    upstream_databases: list[Database | None] | None = strawberry.field(description="The databases that are upstream of this dashboard")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="The databases that are upstream of this dashboard")
    upstream_datasources: list[Datasource | None] | None = strawberry.field(description="The data sources that are upstream of this dashboard")
    upstream_datasources_connection: DatasourcesConnection | None = strawberry.field(description="The data sources that are upstream of this dashboard")
    upstream_fields: list[Field | None] | None = strawberry.field(description="The fields that are upstream of this dashboard")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="The fields that are upstream of this dashboard")
    upstream_flows: list[Flow | None] | None = strawberry.field(description="The flows that are upstream of this dashboard")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="The flows that are upstream of this dashboard")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this dashboard Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this dashboard Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_lenses: list[Lens | None] | None = strawberry.field(description="The Lenses that are upstream of this dashboard")
    upstream_lenses_connection: LensesConnection | None = strawberry.field(description="The Lenses that are upstream of this dashboard")
    upstream_sheet_field_instances: list[Field | None] | None = strawberry.field(description="Sheet field instances used by the sheets referenced by this dashboard")
    upstream_sheet_field_instances_connection: FieldsConnection | None = strawberry.field(description="Sheet field instances used by the sheets referenced by this dashboard")
    upstream_tables: list[Table | None] | None = strawberry.field(description="The tables that are upstream of this dashboard")
    upstream_tables_connection: TablesConnection | None = strawberry.field(description="The tables that are upstream of this dashboard")
    workbook: Workbook | None = strawberry.field(description="The workbook that contains this view")

@strawberry.type(description="A sheet contained in a published workbook.")
class Sheet(Taggable, View):
    contained_in_dashboards: list[Dashboard | None] | None = strawberry.field(description="Dashboards that contain this sheet")
    contained_in_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards that contain this sheet")
    created_at: datetime = strawberry.field(description="Time the sheet was created")
    datasource_fields: list[Field | None] | None = strawberry.field(description="Fields that are contained in an embedded data source and are also referenced by the worksheet. If a worksheet uses calculated fields (or any other FieldReferencingField), this list will also include all of the referenced fields.")
    datasource_fields_connection: FieldsConnection | None = strawberry.field(description="Fields that are contained in an embedded data source and are also referenced by the worksheet. If a worksheet uses calculated fields (or any other FieldReferencingField), this list will also include all of the referenced fields.")
    document_view_id: str | None = strawberry.field(description="Unique ID for the sheet generated for and stored within the workbook, survives renames, and is used for internal processes")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    index: int | None = strawberry.field(description="Index of view; the order it appears in the workbook")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server (Blank if worksheet is hidden in Workbook)")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    parent_embedded_datasources: list[EmbeddedDatasource] = strawberry.field(description="Parent embedded data source of this sheet")
    parent_embedded_datasources_connection: EmbeddedDatasourcesConnection | None = strawberry.field(description="Parent embedded data source of this sheet")
    path: str | None = strawberry.field(description="Server path to sheet")
    referenced_by_metrics: list[Metric | None] | None = strawberry.field(description="The Metrics that reference this View")
    referenced_by_metrics_connection: MetricsConnection | None = strawberry.field(description="The Metrics that reference this View")
    sheet_field_instances: list[Field | None] | None = strawberry.field(description="All fields in the collection worksheetFields as well as the fields in datasourceFields used directly by this sheet. If the worksheet uses calculated fields this list will not include referenced fields that are not directly used by the sheet.")
    sheet_field_instances_connection: FieldsConnection | None = strawberry.field(description="All fields in the collection worksheetFields as well as the fields in datasourceFields used directly by this sheet. If the worksheet uses calculated fields this list will not include referenced fields that are not directly used by the sheet.")
    tags: list[Tag] = strawberry.field(description="Tags associated with the view")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the view")
    updated_at: datetime = strawberry.field(description="Time the sheet was updated")
    upstream_columns: list[Column | None] = strawberry.field(description="The columns that are upstream of this sheet")
    upstream_columns_connection: ColumnsConnection | None = strawberry.field(description="The columns that are upstream of this sheet")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this sheet")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this sheet")
    upstream_databases: list[Database | None] | None = strawberry.field(description="The databases that are upstream of this sheet")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="The databases that are upstream of this sheet")
    upstream_datasources: list[Datasource | None] | None = strawberry.field(description="The data sources that are upstream of this sheet")
    upstream_datasources_connection: DatasourcesConnection | None = strawberry.field(description="The data sources that are upstream of this sheet")
    upstream_fields: list[Field | None] = strawberry.field(description="The fields that are upstream of this sheet")
    upstream_fields_connection: FieldsConnection | None = strawberry.field(description="The fields that are upstream of this sheet")
    upstream_flows: list[Flow | None] | None = strawberry.field(description="The flows that are upstream of this sheet")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="The flows that are upstream of this sheet")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this sheet. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this sheet. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[Table | None] | None = strawberry.field(description="The tables that are upstream of this sheet")
    upstream_tables_connection: TablesConnection | None = strawberry.field(description="The tables that are upstream of this sheet")
    workbook: Workbook | None = strawberry.field(description="The workbook that contains this view")
    worksheet_fields: list[CalculatedField | None] | None = strawberry.field(description="Calculated fields which were created on this sheet, e.g. in the rows or columns shelves and which may not be used on other sheets that use this embedded data source")
    worksheet_fields_connection: CalculatedFieldsConnection | None = strawberry.field(description="Calculated fields which were created on this sheet, e.g. in the rows or columns shelves and which may not be used on other sheets that use this embedded data source")

@strawberry.type(description="A data quality certification associated with a content item")
class DataQualityCertification(Label):
    asset: CanHaveLabels | None = strawberry.field(description="The asset that contains the data quality certification")
    author: TableauUser | None = strawberry.field(description="User who last updated this data quality certification")
    author_display_name: str | None = strawberry.field(description="Name of the user who last updated this data quality certification")
    category: str = strawberry.field(description="Category of the label")
    created_at: datetime = strawberry.field(description="Time the data quality certification was created")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    is_active: bool = strawberry.field(description="True if the data quality certification is active")
    is_elevated: bool = strawberry.field(description="True if the data quality certification is elevated")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    message: str | None = strawberry.field(description="Message of the data quality certification")
    updated_at: datetime = strawberry.field(description="Time the data quality certification was last updated")
    value: str = strawberry.field(description="Value of the label")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this data quality certifcation, for use in client-to-server communications")

@strawberry.type(description="A data quality warning associated with a content item")
class DataQualityWarning(Label):
    asset: CanHaveLabels | None = strawberry.field(description="The asset that contains the data quality warning")
    author: TableauUser | None = strawberry.field(description="User who last updated this data quality warning")
    author_display_name: str | None = strawberry.field(description="Name of the user who last updated this data quality warning")
    category: str = strawberry.field(description="Category of the label")
    created_at: datetime = strawberry.field(description="Time the data quality warning was created")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    is_active: bool = strawberry.field(description="True if the data quality warning is active")
    is_elevated: bool = strawberry.field(description="True if the data quality warning is elevated")
    is_severe: bool = strawberry.field(description="Synonymous with isElevated")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    message: str | None = strawberry.field(description="Message of the data quality warning")
    updated_at: datetime = strawberry.field(description="Time the data quality warning was last updated")
    value: str = strawberry.field(description="Value of the label")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this data quality warning, for use in client-to-server communications")
    warning_type: str = strawberry.field(description="Synonymous with value")

@strawberry.type(description="""
A label that can be attached to assets.  
*Available in Tableau Cloud March 2023 / Server 2023.1 and later.*
""")
class GenericLabel(Label):
    asset: CanHaveLabels | None = strawberry.field(description="The asset that contains the label")
    author: TableauUser | None = strawberry.field(description="User who last updated this label")
    author_display_name: str | None = strawberry.field(description="Name of the user who last updated this label")
    category: str = strawberry.field(description="Category of the label")
    created_at: datetime = strawberry.field(description="Time the label was created")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API. Not the same as the numeric ID used on server")
    is_active: bool = strawberry.field(description="True if the label is active")
    is_elevated: bool = strawberry.field(description="True if the label is elevated")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    message: str | None = strawberry.field(description="Message of the label")
    updated_at: datetime = strawberry.field(description="Time the label was last updated")
    value: str = strawberry.field(description="Value of the label")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this label, for use in client-to-server communications")

@strawberry.type(description="A data source embedded in a workbook")
class EmbeddedDatasource(Datasource):
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    created_at: datetime | None = strawberry.field(description="Time the datasource was created. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    datasource_filters: list[DatasourceFilter] = strawberry.field(description="Data source filters contained in this data source")
    datasource_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="Data source filters contained in this data source")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards downstream from this data source")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards downstream from this data source")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream from this data source")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream from this data source")
    downstream_owners: list[TableauUser] = strawberry.field(description="Workbook owners downstream from this data source")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners downstream from this data source")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets downstream from this data source")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets downstream from this data source")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks downstream from this data source")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks downstream from this data source")
    extract_last_incremental_update_time: datetime | None = strawberry.field(description="Time an extract was last incrementally updated")
    extract_last_refresh_time: datetime | None = strawberry.field(description="Time an extract was last fully refreshed")
    extract_last_update_time: datetime | None = strawberry.field(description="Time an extract was last updated by either a full refresh, incremental update, or creation")
    fields: list[Field] = strawberry.field(description="Fields, usually measures or dimensions, contained in the data source")
    fields_connection: FieldsConnection | None = strawberry.field(description="Fields, usually measures or dimensions, contained in the data source")
    has_extracts: bool | None = strawberry.field(description="True if datasource contains extracted data")
    has_user_reference: bool | None = strawberry.field(description="True if data source contains a formula that involves a user function (for example, USERNAME or ISMEMBEROF)")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    lenses: list[Lens | None] | None = strawberry.field(description="The lenses derived from this datasource")
    lenses_connection: LensesConnection | None = strawberry.field(description="The lenses derived from this datasource")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    parent_published_datasources: list[PublishedDatasource] = strawberry.field(description="Parent published data sources of this embedded data source")
    parent_published_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Parent published data sources of this embedded data source")
    updated_at: datetime | None = strawberry.field(description="Time the datasource was last updated. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this data source")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this data source")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream from this data source")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream from this data source")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream from this data source")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream from this data source")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream from this data source")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream from this data source")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this data source. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this data source. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream from this data source")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream from this data source")
    workbook: Workbook | None = strawberry.field(description="Workbook that contains these embedded datasources")

@strawberry.type(description="A Tableau data source that has been published separately to Tableau Server. It can be used by multiple workbooks.")
class PublishedDatasource(CanHaveLabels, Certifiable, Datasource, Taggable, Warnable):
    certification_note: str | None = strawberry.field(description="Notes related to the data source being marked as certified")
    certifier: TableauUser | None = strawberry.field(description="User who marked this data source as certified")
    certifier_display_name: str | None = strawberry.field(description="Name of the user who marked this data source as certified")
    container_name: str | None = strawberry.field(description="The name of the container in which the published data source is visible and usable. Either a personal space or project.")
    container_type: str = strawberry.field(description="The type of the container in which the published data source is visible and usable. Either personal space or project.")
    contains_unsupported_custom_sql: bool | None = strawberry.field(description="True if the datasource contains unsupported custom SQL, in which case lineage may be incomplete")
    created_at: datetime | None = strawberry.field(description="Time the datasource was created. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    data_quality_certifications: list[DataQualityCertification] = strawberry.field(description="The data quality certifications on a published datasource")
    data_quality_certifications_connection: DataQualityCertificationsConnection | None = strawberry.field(description="The data quality certifications on a published datasource")
    data_quality_warning: DataQualityWarning | None = strawberry.field(description="The optional data quality warning on a published datasource")
    data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="The data quality warnings on a published datasource")
    data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="The data quality warnings on a published datasource")
    datasource_filters: list[DatasourceFilter] = strawberry.field(description="Data source filters contained in this data source")
    datasource_filters_connection: DatasourceFiltersConnection | None = strawberry.field(description="Data source filters contained in this data source")
    description: str | None = strawberry.field(description="Description of the datasource")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards connected downstream from the field")
    downstream_databases: list[Database] = strawberry.field(description="Databases downstream from this data source")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases downstream from this data source")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources downstream from this data source")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources downstream from this data source")
    downstream_flows: list[Flow] = strawberry.field(description="Flows downstream from this data source")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows downstream from this data source")
    downstream_lenses: list[Lens] | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses connected downstream from this field")
    downstream_metric_definitions: list[MetricDefinition | None] = strawberry.field(description="Metric definitions downstream from the data source.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from the data source.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics downstream from this data source")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics downstream from this data source")
    downstream_owners: list[TableauUser] = strawberry.field(description="Workbook owners downstream from this data source")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Workbook owners downstream from this data source")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets downstream from this data source")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets downstream from this data source")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables downstream from this data source")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables downstream from this data source")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="Virtual connection tables downstream of this data source")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="Virtual connection tables downstream of this data source")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="Virtual connections downstream from this data source")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="Virtual connections downstream from this data source")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks downstream from this data source")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks downstream from this data source")
    extract_last_incremental_update_time: datetime | None = strawberry.field(description="Time an extract was last incrementally updated")
    extract_last_refresh_time: datetime | None = strawberry.field(description="Time an extract was last fully refreshed")
    extract_last_update_time: datetime | None = strawberry.field(description="Time an extract was last updated by either a full refresh, incremental update, or creation")
    fields: list[Field] = strawberry.field(description="Fields usable in workbooks connected to this data source")
    fields_connection: FieldsConnection | None = strawberry.field(description="Fields usable in workbooks connected to this data source")
    has_active_warning: bool = strawberry.field(description="True if the data source has an active data quality warning")
    has_extracts: bool | None = strawberry.field(description="True if datasource contains extracted data")
    has_user_reference: bool | None = strawberry.field(description="True if data source contains a formula that involves a user function (for example, USERNAME or ISMEMBEROF)")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API.  Not the same as the numeric ID used on server")
    is_certified: bool = strawberry.field(description="True if this data source contains an active data quality certification")
    labels: list[Label] = strawberry.field(description="The labels on a published datasource. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    labels_connection: LabelsConnection | None = strawberry.field(description="The labels on a published datasource. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    lenses: list[Lens | None] | None = strawberry.field(description="The lenses derived from this datasource")
    lenses_connection: LensesConnection | None = strawberry.field(description="The lenses derived from this datasource")
    luid: str = strawberry.field(description="Locally unique identifier used for the REST API on the Tableau Server")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    owner: TableauUser = strawberry.field(description="User who owns this data source")
    parameters: list[Parameter] = strawberry.field(description="List of parameters, if any, used in this data source")
    parameters_connection: ParametersConnection | None = strawberry.field(description="List of parameters, if any, used in this data source")
    project_name: str | None = strawberry.field(description="The name of the project that contains this published data source.")
    project_vizportal_url_id: str | None = strawberry.field(description="The ID of the project in which the published data source is visible and usable. Will return null if the published data source is not in a project.")
    site: TableauSite = strawberry.field(description="The site which contains this published data source")
    tags: list[Tag] = strawberry.field(description="Tags associated with the published datasource")
    tags_connection: TagsConnection | None = strawberry.field(description="Tags associated with the published datasource")
    updated_at: datetime | None = strawberry.field(description="Time the datasource was last updated. Available in Tableau Cloud June 2022 / Server 2022.3 and later.")
    upstream_data_quality_warnings: list[DataQualityWarning] = strawberry.field(description="Data quality warnings upstream from this data source")
    upstream_data_quality_warnings_connection: DataQualityWarningsConnection | None = strawberry.field(description="Data quality warnings upstream from this data source")
    upstream_databases: list[Database] = strawberry.field(description="Databases upstream from this data source")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases upstream from this data source")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources upstream from this data source")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources upstream from this data source")
    upstream_flows: list[Flow] = strawberry.field(description="Flows upstream from this data source")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows upstream from this data source")
    upstream_labels: list[Label] = strawberry.field(description="Labels upstream from this data source. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_labels_connection: LabelsConnection | None = strawberry.field(description="Labels upstream from this data source. Available in Tableau Cloud March 2023 / Server 2023.1 and later.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables upstream from this data source")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables upstream from this data source")
    upstream_virtual_connection_tables: list[VirtualConnectionTable | None] = strawberry.field(description="The virtual connection table upstream to this Datasource")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="The virtual connection table upstream to this Datasource")
    upstream_virtual_connections: list[VirtualConnection | None] = strawberry.field(description="The virtual connection upstream to this Datasource")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="The virtual connection upstream to this Datasource")
    uri: str | None = strawberry.field(description="Uri of the datasource")
    vizportal_id: str = strawberry.field(description="Vizportal ID of this published datasource, for use in client-to-server communications")
    vizportal_url_id: str = strawberry.field(description="VizPortal URL ID; used for URL generation")

@strawberry.type(description="Column input field implementation")
class FlowColumnInputField(FlowInputField):
    child_fields: list[FlowOutputField] = strawberry.field(description="Fields that are children of this field")
    child_fields_connection: FlowOutputFieldsConnection | None = strawberry.field(description="Fields that are children of this field")
    column: Column | None = strawberry.field(description="The underlying wrapped column")
    field_id: str | None = strawberry.field(description="Identifier internal to flow")
    flow: Flow | None = strawberry.field(description="A flow to which these fields input")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    upstream_databases: list[Database] = strawberry.field(description="Databases that are upstream from this outputField.")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are upstream from this outputField.")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="PublishedDatasources that are upstream from this outputField.")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="PublishedDatasources that are upstream from this outputField.")
    upstream_flows: list[Flow] = strawberry.field(description="Flows that are upstream from this outputField.")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are upstream from this outputField.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables that are upstream of this field")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables that are upstream of this field")

@strawberry.type(description="Field input field implementation")
class FlowFieldInputField(FlowInputField):
    child_fields: list[FlowOutputField] = strawberry.field(description="Fields that are children of this field")
    child_fields_connection: FlowOutputFieldsConnection | None = strawberry.field(description="Fields that are children of this field")
    field: Field | None = strawberry.field(description="The underlying wrapped field")
    field_id: str | None = strawberry.field(description="Identifier internal to flow")
    flow: Flow | None = strawberry.field(description="A flow to which these fields input")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    upstream_databases: list[Database] = strawberry.field(description="Databases that are upstream from this outputField.")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are upstream from this outputField.")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources that are upstream from this outputField.")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources that are upstream from this outputField.")
    upstream_flows: list[Flow] = strawberry.field(description="Flows that are upstream from this outputField.")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are upstream from this outputField.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables that are upstream of this field.")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables that are upstream of this field.")

@strawberry.type(description="Column output field implementation")
class FlowColumnOutputField(FlowOutputField):
    column: Column | None = strawberry.field(description="The underlying wrapped column")
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards that are downstream from this outputField")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards that are downstream from this outputField")
    downstream_databases: list[Database] = strawberry.field(description="Databases that are downstream from this outputField")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are downstream from this outputField")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources that are downstream from this outputField")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources that are downstream from this outputField")
    downstream_flows: list[Flow] = strawberry.field(description="Flows that are downstream from this outputField")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are downstream from this outputField")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses that are downstream from this outputField")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses that are downstream from this outputField")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this flow output field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this flow output field.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics that are downstream from this outputField")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics that are downstream from this outputField")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners that are downstream from this outputField")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners that are downstream from this outputField")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets that are downstream from this outputField")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that are downstream from this outputField")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables that are downstream from this outputField")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables that are downstream from this outputField")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="VirtualConnectionTables that are downstream of this outputField")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="VirtualConnectionTables that are downstream of this outputField")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="VirtualConnections that are downstream of this outputField")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="VirtualConnections that are downstream of this outputField")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks that are downstream from this outputField")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks that are downstream from this outputField")
    field_id: str | None = strawberry.field(description="Identifier internal to flow")
    flow: list[Flow | None] | None = strawberry.field(description="The flow that outputs these fields")
    flow_connection: FlowsConnection | None = strawberry.field(description="The flow that outputs these fields")
    flow_output_step: FlowOutputStep | None = strawberry.field(description="The flow output step that contains this field")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    parent_fields: list[FlowInputField] = strawberry.field(description="Fields that are parents of this field")
    parent_fields_connection: FlowInputFieldsConnection | None = strawberry.field(description="Fields that are parents of this field")
    upstream_databases: list[Database] = strawberry.field(description="Databases that are upstream from this outputField")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are upstream from this outputField")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources that are upstream from this flow.")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources that are upstream from this flow.")
    upstream_flows: list[Flow] = strawberry.field(description="Flows that are upstream from this flow")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are upstream from this flow")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables that are upstream from this outputField")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables that are upstream from this outputField")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="VirtualConnectionTables that are upstream of this outputField")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="VirtualConnectionTables that are upstream of this outputField")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="VirtualConnections that are upstream of this outputField")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="VirtualConnections that are upstream of this outputField")

@strawberry.type(description="Field output field implementation")
class FlowFieldOutputField(FlowOutputField):
    downstream_dashboards: list[Dashboard] = strawberry.field(description="Dashboards that are downstream from this outputField")
    downstream_dashboards_connection: DashboardsConnection | None = strawberry.field(description="Dashboards that are downstream from this outputField")
    downstream_databases: list[Database] = strawberry.field(description="Databases that are downstream from this outputField")
    downstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are downstream from this outputField")
    downstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources that are downstream from this outputField")
    downstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources that are downstream from this outputField")
    downstream_flows: list[Flow] = strawberry.field(description="Flows that are downstream from this outputField")
    downstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are downstream from this outputField")
    downstream_lenses: list[Lens] = strawberry.field(description="Lenses that are downstream from this outputField")
    downstream_lenses_connection: LensesConnection | None = strawberry.field(description="Lenses that are downstream from this outputField")
    downstream_metric_definitions: list[MetricDefinition | None] | None = strawberry.field(description="Metric definitions downstream from this flow output field.")
    downstream_metric_definitions_connection: MetricDefinitionsConnection | None = strawberry.field(description="Metric definitions downstream from this flow output field.")
    downstream_metrics: list[Metric] = strawberry.field(description="Metrics that are downstream from this outputField")
    downstream_metrics_connection: MetricsConnection | None = strawberry.field(description="Metrics that are downstream from this outputField")
    downstream_owners: list[TableauUser] = strawberry.field(description="Owners that are downstream from this outputField")
    downstream_owners_connection: TableauUsersConnection | None = strawberry.field(description="Owners that are downstream from this outputField")
    downstream_sheets: list[Sheet] = strawberry.field(description="Sheets that are downstream from this outputField")
    downstream_sheets_connection: SheetsConnection | None = strawberry.field(description="Sheets that are downstream from this outputField")
    downstream_tables: list[DatabaseTable] = strawberry.field(description="Tables that are downstream from this outputField")
    downstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables that are downstream from this outputField")
    downstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="VirtualConnectionTables that are downstream of this outputField")
    downstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="VirtualConnectionTables that are downstream of this outputField")
    downstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="VirtualConnections that are downstream of this outputField")
    downstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="VirtualConnections that are downstream of this outputField")
    downstream_workbooks: list[Workbook] = strawberry.field(description="Workbooks that are downstream from this outputField")
    downstream_workbooks_connection: WorkbooksConnection | None = strawberry.field(description="Workbooks that are downstream from this outputField")
    field: Field | None = strawberry.field(description="The underlying wrapped field")
    field_id: str | None = strawberry.field(description="Identifier internal to flow")
    flow: list[Flow | None] | None = strawberry.field(description="The flow that outputs these fields")
    flow_connection: FlowsConnection | None = strawberry.field(description="The flow that outputs these fields")
    flow_output_step: FlowOutputStep | None = strawberry.field(description="The flow output step that contains this field")
    id: strawberry.ID = strawberry.field(description="Unique identifier used by the metadata API")
    name: str | None = strawberry.field(description="Name shown in server and desktop clients")
    parent_fields: list[FlowInputField] = strawberry.field(description="Fields that are parents of this field")
    parent_fields_connection: FlowInputFieldsConnection | None = strawberry.field(description="Fields that are parents of this field")
    upstream_databases: list[Database] = strawberry.field(description="Databases that are upstream from this outputField")
    upstream_databases_connection: DatabasesConnection | None = strawberry.field(description="Databases that are upstream from this outputField")
    upstream_datasources: list[PublishedDatasource] = strawberry.field(description="Datasources that are upstream from this output field.")
    upstream_datasources_connection: PublishedDatasourcesConnection | None = strawberry.field(description="Datasources that are upstream from this output field.")
    upstream_flows: list[Flow] = strawberry.field(description="Flows that are upstream from this flow.")
    upstream_flows_connection: FlowsConnection | None = strawberry.field(description="Flows that are upstream from this flow.")
    upstream_tables: list[DatabaseTable] = strawberry.field(description="Tables that are upstream from this outputField")
    upstream_tables_connection: DatabaseTablesConnection | None = strawberry.field(description="Tables that are upstream from this outputField")
    upstream_virtual_connection_tables: list[VirtualConnectionTable] = strawberry.field(description="VirtualConnectionTables that are upstream of this outputField")
    upstream_virtual_connection_tables_connection: VirtualConnectionTablesConnection | None = strawberry.field(description="VirtualConnectionTables that are upstream of this outputField")
    upstream_virtual_connections: list[VirtualConnection] = strawberry.field(description="VirtualConnections that are upstream of this outputField")
    upstream_virtual_connections_connection: VirtualConnectionsConnection | None = strawberry.field(description="VirtualConnections that are upstream of this outputField")
