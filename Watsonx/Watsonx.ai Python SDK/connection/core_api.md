ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/core_api.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Core [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#core "Link to this heading")

## Connections [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#connections "Link to this heading")

_class_ client.Connections( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections "Link to this definition")

Store and manage connections.

ConfigurationMetaNames _=<ibm\_watsonx\_ai.metanames.ConnectionMetaNamesobject>_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.ConfigurationMetaNames "Link to this definition")

MetaNames for connection creation.

create( _meta\_props_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.create) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.create "Link to this definition")

Create a connection. Examples of PROPERTIES field input:

1. MySQL


> ```
> client.connections.ConfigurationMetaNames.PROPERTIES: {
>     "database": "database",
>     "password": "password",
>     "port": "3306",
>     "host": "host url",
>     "ssl": "false",
>     "username": "username"
> }
>
> ```

2. Google BigQuery


> 1. Method 1: Using service account json. The generated service account json can be provided as input as-is. Provide actual values in json. The example below is only indicative to show the fields. For information on how to generate the service account json, refer to Google BigQuery documentation.
>
>
> > ```
> > client.connections.ConfigurationMetaNames.PROPERTIES: {
> >     "type": "service_account",
> >     "project_id": "project_id",
> >     "private_key_id": "private_key_id",
> >     "private_key": "private key contents",
> >     "client_email": "client_email",
> >     "client_id": "client_id",
> >     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
> >     "token_uri": "https://oauth2.googleapis.com/token",
> >     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
> >     "client_x509_cert_url": "client_x509_cert_url"
> > }
> >
> > ```
>
> 2. Method 2: Using OAuth Method. For information on how to generate a OAuth token, refer to Google BigQuery documentation.
>
>
> > ```
> > client.connections.ConfigurationMetaNames.PROPERTIES: {
> >     "access_token": "access token generated for big query",
> >     "refresh_token": "refresh token",
> >     "project_id": "project_id",
> >     "client_secret": "This is your gmail account password",
> >     "client_id": "client_id"
> > }
> >
> > ```

3. MS SQL


> ```
> client.connections.ConfigurationMetaNames.PROPERTIES: {
>     "database": "database",
>     "password": "password",
>     "port": "1433",
>     "host": "host",
>     "username": "username"
> }
>
> ```

4. Teradata


> ```
> client.connections.ConfigurationMetaNames.PROPERTIES: {
>     "database": "database",
>     "password": "password",
>     "port": "1433",
>     "host": "host",
>     "username": "username"
> }
>
> ```


Parameters:

**meta\_props** ( _dict_) –

metadata of the connection configuration. To see available meta names, use:

```
client.connections.ConfigurationMetaNames.get()

```

Returns:

metadata of the stored connection

Return type:

dict

**Example:**

```
sqlserver_data_source_type_id = client.connections.get_datasource_type_id_by_name('sqlserver')
connections_details = client.connections.create({
    client.connections.ConfigurationMetaNames.NAME: "sqlserver connection",
    client.connections.ConfigurationMetaNames.DESCRIPTION: "connection description",
    client.connections.ConfigurationMetaNames.DATASOURCE_TYPE: sqlserver_data_source_type_id,
    client.connections.ConfigurationMetaNames.PROPERTIES: { "database": "database",
                                                            "password": "password",
                                                            "port": "1433",
                                                            "host": "host",
                                                            "username": "username"}
})

```

delete( _connection\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.delete "Link to this definition")

Delete a stored connection.

Parameters:

**connection\_id** ( _str_) – unique ID of the connection to be deleted

Returns:

status (“SUCCESS” or “FAILED”)

Return type:

str

**Example:**

```
client.connections.delete(connection_id)

```

get\_datasource\_type\_details\_by\_id( _datasource\_type\_id_, _connection\_properties=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.get_datasource_type_details_by_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.get_datasource_type_details_by_id "Link to this definition")

Get datasource type details for the given datasource type ID.

Parameters:

- **datasource\_type\_id** ( _str_) – ID of the datasource type

- **connection\_properties** ( _bool_) – if True, the connection properties are included in the returned details. defaults to False


Returns:

Datasource type details

Return type:

dict

**Example:**

```
client.connections.get_datasource_type_details_by_id(datasource_type_id)

```

get\_datasource\_type\_id\_by\_name( _name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.get_datasource_type_id_by_name) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.get_datasource_type_id_by_name "Link to this definition")

Get a stored datasource type ID for the given datasource type name.

Parameters:

**name** ( _str_) – name of datasource type

Returns:

ID of datasource type

Return type:

str

**Example:**

```
client.connections.get_datasource_type_id_by_name('cloudobjectstorage')

```

get\_datasource\_type\_uid\_by\_name( _name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.get_datasource_type_uid_by_name) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.get_datasource_type_uid_by_name "Link to this definition")

Get a stored datasource type ID for the given datasource type name.

_Deprecated:_ Use `Connections.get_datasource_type_id_by_name(name)` instead.

Parameters:

**name** ( _str_) – name of datasource type

Returns:

ID of datasource type

Return type:

str

**Example:**

```
client.connections.get_datasource_type_uid_by_name('cloudobjectstorage')

```

get\_details( _connection\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.get_details "Link to this definition")

Get connection details for the given unique connection ID.
If no connection\_id is passed, details for all connections are returned.

Parameters:

**connection\_id** ( _str_) – unique ID of the connection

Returns:

metadata of the stored connection

Return type:

dict

**Example:**

```
connection_details = client.connections.get_details(connection_id)
connection_details = client.connections.get_details()

```

_static_ get\_id( _connection\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.get_id "Link to this definition")

Get ID of a stored connection.

Parameters:

**connection\_details** ( _dict_) – metadata of the stored connection

Returns:

unique ID of the stored connection

Return type:

str

**Example:**

```
connection_id = client.connection.get_id(connection_details)

```

_static_ get\_uid( _connection\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.get_uid) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.get_uid "Link to this definition")

Get the unique ID of a stored connection.

_Deprecated:_ Use `Connections.get_id(details)` instead.

Parameters:

**connection\_details** ( _dict_) – metadata of the stored connection

Returns:

unique ID of the stored connection

Return type:

str

**Example:**

```
connection_uid = client.connection.get_uid(connection_details)

```

get\_uploaded\_db\_drivers() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.get_uploaded_db_drivers) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.get_uploaded_db_drivers "Link to this definition")

Get uploaded db driver jar names and paths.
Supported for IBM Cloud Pak® for Data, version 4.6.1 and up.

**Output**

Important

Returns dictionary containing name and path for connection files.

**return type**: Dict\[Str, Str\]

**Example:**

```
>>> result = client.connections.get_uploaded_db_drivers()

```

list() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.list "Link to this definition")

Return pd.DataFrame table with all stored connections in a table format.

Returns:

pandas.DataFrame with listed connections

Return type:

pandas.DataFrame

**Example:**

```
client.connections.list()

```

list\_datasource\_types() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.list_datasource_types) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.list_datasource_types "Link to this definition")

Print stored datasource types assets in a table format.

Returns:

pandas.DataFrame with listed datasource types

Return type:

pandas.DataFrame

**Example:** [https://test.cloud.ibm.com/apidocs/watsonx-ai#trainings-list](https://test.cloud.ibm.com/apidocs/watsonx-ai#trainings-list)

```
client.connections.list_datasource_types()

```

list\_uploaded\_db\_drivers() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.list_uploaded_db_drivers) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.list_uploaded_db_drivers "Link to this definition")

Return pd.DataFrame table with uploaded db driver jars in table a format. Supported for IBM Cloud Pak® for Data only.

Returns:

pandas.DataFrame with listed uploaded db drivers

Return type:

pandas.DataFrame

**Example:**

```
client.connections.list_uploaded_db_drivers()

```

sign\_db\_driver\_url( _jar\_name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.sign_db_driver_url) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.sign_db_driver_url "Link to this definition")

Get a signed db driver jar URL to be used during JDBC generic connection creation.
The jar name passed as argument needs to be uploaded into the system first.
Supported for IBM Cloud Pak® for Data only, version 4.0.4 and later.

Parameters:

**jar\_name** ( _str_) – name of db driver jar

Returns:

URL of signed db driver

Return type:

str

**Example:**

```
jar_uri = client.connections.sign_db_driver_url('db2jcc4.jar')

```

upload\_db\_driver( _path_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/connections.html#Connections.upload_db_driver) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Connections.upload_db_driver "Link to this definition")

Upload db driver jar. Supported for IBM Cloud Pak® for Data only, version 4.0.4 and up.

Parameters:

**path** ( _str_) – path to the db driver jar file

**Example:**

```
client.connections.upload_db_driver('example/path/db2jcc4.jar')

```

_class_ metanames.ConnectionMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#ConnectionMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.ConnectionMetaNames "Link to this definition")

Set of MetaNames for Connection.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| NAME | str | Y | `my_space` |
| DESCRIPTION | str | N | `my_description` |
| DATASOURCE\_TYPE | str | Y | `1e3363a5-7ccf-4fff-8022-4850a8024b68` |
| PROPERTIES | dict | Y | `{'database': 'db_name', 'host': 'host_url', 'password': 'password', 'username': 'user'}` |
| FLAGS | list | N | `['personal_credentials']` |

## Data assets [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#data-assets "Link to this heading")

_class_ client.Assets( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/assets.html#Assets) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Assets "Link to this definition")

Store and manage data assets.

ConfigurationMetaNames _=<ibm\_watsonx\_ai.metanames.AssetsMetaNamesobject>_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Assets.ConfigurationMetaNames "Link to this definition")

MetaNames for Data Assets creation.

create( _name_, _file\_path_, _duplicate\_action=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/assets.html#Assets.create) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Assets.create "Link to this definition")

Create a data asset and upload content to it.

Parameters:

- **name** ( _str_) – name to be given to the data asset

- **file\_path** ( _str_) – path to the content file to be uploaded

- **duplicate\_action** ( _AssetDuplicateAction_ _,_ _optional_) – determines behaviour when asset with the same name already exists,
if not specified, the value from catalogs/projects/spaces will be used


Returns:

metadata of the stored data asset

Return type:

dict

**Example:**

```
asset_details = client.data_assets.create(name="sample_asset", file_path="/path/to/file")

```

delete( _asset\_id=None_, _purge\_on\_delete=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/assets.html#Assets.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Assets.delete "Link to this definition")

Soft delete the stored data asset. The asset will be moved to trashed assets
and will not be visible in asset list. To permanently delete assets set purge\_on\_delete parameter to True.

Parameters:

- **asset\_id** ( _str_) – unique ID of the data asset

- **purge\_on\_delete** ( _bool_ _,_ _optional_) – if set to True will purge the asset


Returns:

status (“SUCCESS” or “FAILED”) or dictionary, if deleted asynchronously

Return type:

str or dict

**Example:**

```
client.data_assets.delete(asset_id)

```

download( _asset\_id=None_, _filename=''_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/assets.html#Assets.download) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Assets.download "Link to this definition")

Download and store the content of a data asset.

Parameters:

- **asset\_id** ( _str_) – unique ID of the data asset to be downloaded

- **filename** ( _str_) – filename to be used for the downloaded file


Returns:

normalized path to the downloaded asset content

Return type:

str

**Example:**

```
client.data_assets.download(asset_id,"sample_asset.csv")

```

get\_content( _asset\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/assets.html#Assets.get_content) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Assets.get_content "Link to this definition")

Download the content of a data asset.

Parameters:

**asset\_id** ( _str_) – unique ID of the data asset to be downloaded

Returns:

the asset content

Return type:

bytes

**Example:**

```
content = client.data_assets.get_content(asset_id).decode('ascii')

```

get\_details( _asset\_id=None_, _get\_all=None_, _limit=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/assets.html#Assets.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Assets.get_details "Link to this definition")

Get data asset details. If no asset\_id is passed, details for all assets are returned.

Parameters:

- **asset\_id** ( _str_) – unique ID of the asset

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

metadata of the stored data asset

Return type:

dict

**Example:**

```
asset_details = client.data_assets.get_details(asset_id)

```

_static_ get\_href( _asset\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/assets.html#Assets.get_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Assets.get_href "Link to this definition")

Get the URL of a stored data asset.

Parameters:

**asset\_details** ( _dict_) – details of the stored data asset

Returns:

href of the stored data asset

Return type:

str

**Example:**

```
asset_details = client.data_assets.get_details(asset_id)
asset_href = client.data_assets.get_href(asset_details)

```

_static_ get\_id( _asset\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/assets.html#Assets.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Assets.get_id "Link to this definition")

Get the unique ID of a stored data asset.

Parameters:

**asset\_details** ( _dict_) – details of the stored data asset

Returns:

unique ID of the stored data asset

Return type:

str

**Example:**

```
asset_id = client.data_assets.get_id(asset_details)

```

list( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/assets.html#Assets.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Assets.list "Link to this definition")

Lists stored data assets in a table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number for fetched records

Return type:

DataFrame

Returns:

listed elements

**Example:**

```
client.data_assets.list()

```

store( _meta\_props_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/assets.html#Assets.store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Assets.store "Link to this definition")

Create a data asset and upload content to it.

Parameters:

**meta\_props** ( _dict_) –

metadata of the space configuration. To see available meta names, use:

```
client.data_assets.ConfigurationMetaNames.get()

```

**Example:**

Example of data asset creation for files:

```
metadata = {
    client.data_assets.ConfigurationMetaNames.NAME: 'my data assets',
    client.data_assets.ConfigurationMetaNames.DESCRIPTION: 'sample description',
    client.data_assets.ConfigurationMetaNames.DATA_CONTENT_NAME: 'sample.csv'
}
asset_details = client.data_assets.store(meta_props=metadata)

```

Example of data asset creation using a connection:

```
metadata = {
    client.data_assets.ConfigurationMetaNames.NAME: 'my data assets',
    client.data_assets.ConfigurationMetaNames.DESCRIPTION: 'sample description',
    client.data_assets.ConfigurationMetaNames.CONNECTION_ID: '39eaa1ee-9aa4-4651-b8fe-95d3ddae',
    client.data_assets.ConfigurationMetaNames.DATA_CONTENT_NAME: 't1/sample.csv'
}
asset_details = client.data_assets.store(meta_props=metadata)

```

Example of data asset creation with a database sources type connection:

```
metadata = {
    client.data_assets.ConfigurationMetaNames.NAME: 'my data assets',
    client.data_assets.ConfigurationMetaNames.DESCRIPTION: 'sample description',
    client.data_assets.ConfigurationMetaNames.CONNECTION_ID: '23eaf1ee-96a4-4651-b8fe-95d3dadfe',
    client.data_assets.ConfigurationMetaNames.DATA_CONTENT_NAME: 't1'
}
asset_details = client.data_assets.store(meta_props=metadata)

```

_class_ metanames.AssetsMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#AssetsMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.AssetsMetaNames "Link to this definition")

Set of MetaNames for Data Asset Specs.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| NAME | str | Y | `my_data_asset` |
| DATA\_CONTENT\_NAME | str | Y | `/test/sample.csv` |
| CONNECTION\_ID | str | N | `39eaa1ee-9aa4-4651-b8fe-95d3ddae` |
| DESCRIPTION | str | N | `my_description` |
| DUPLICATE\_ACTION | str | N | `REJECT` |

## Trashed assets [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#trashed-assets "Link to this heading")

_class_ client.TrashedAssets( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/trashed_assets.html#TrashedAssets) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TrashedAssets "Link to this definition")

Manage trashed assets.

delete( _asset\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/trashed_assets.html#TrashedAssets.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TrashedAssets.delete "Link to this definition")

Delete a trashed asset.

Parameters:

**asset\_id** ( _str_) – trashed asset ID

Returns:

status “SUCCESS” if deletion is successful

Return type:

Literal\[“SUCCESS”\]

**Example:**

```
client.trashed_assets.delete(asset_id)

```

get\_details( _asset\_id=None_, _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/trashed_assets.html#TrashedAssets.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TrashedAssets.get_details "Link to this definition")

Get metadata of a given trashed asset. If no asset\_id is specified, all trashed assets metadata is returned.

Parameters:

- **asset\_id** ( _str_ _,_ _optional_) – trashed asset ID

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

export metadata

Return type:

dict (if asset\_id is not None) or {“resources”: \[dict\]} (if asset\_id is None)

**Example:**

```
details = client.trashed_assets.get_details(asset_id)
details = client.trashed_assets.get_details()
details = client.trashed_assets.get_details(limit=100)

```

_static_ get\_id( _trashed\_asset\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/trashed_assets.html#TrashedAssets.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TrashedAssets.get_id "Link to this definition")

Get the ID of a trashed asset.

Parameters:

**trashed\_asset\_details** ( _dict_) – metadata of the trashed asset

Returns:

unique ID of the trashed asset

Return type:

str

**Example:**

```
asset_id = client.trashed_assets.get_id(trashed_asset_details)

```

list( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/trashed_assets.html#TrashedAssets.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TrashedAssets.list "Link to this definition")

List trashed assets.

Parameters:

**limit** ( _int_ _,_ _optional_) – set the limit for number of listed trashed assets,
default is None (all trashed assets should be fetched)

Returns:

Pandas DataFrame with information about trashed assets

Return type:

pandas.DataFrame

**Example:**

```
trashed_assets_list = client.trashed_assets.list()
print(trashed_assets_list)

# Result:
#        NAME  ASSET_TYPE                              ASSET_ID
# 0  data.csv  data_asset  8e421c27-767d-4824-9aab-dc5c7c19ba87

```

purge\_all() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/trashed_assets.html#TrashedAssets.purge_all) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TrashedAssets.purge_all "Link to this definition")

Purge all trashed asset.

Note

If there is more than 20 trashed assets, they will be removed asynchronously.
It may take a few seconds until all trashed assets will disappear from trashed assets list.

Returns:

status “SUCCESS” if purge is successful

Return type:

Literal\[“SUCCESS”\]

**Example:**

```
client.trashed_assets.purge_all()

```

restore( _asset\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/trashed_assets.html#TrashedAssets.restore) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TrashedAssets.restore "Link to this definition")

Restore a trashed asset.

Parameters:

**asset\_id** ( _str_) – trashed asset ID

Returns:

details of restored asset

Return type:

dict

**Example:**

```
asset_details = client.trashed_assets.restore(asset_id)

```

## Deployments [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#deployments "Link to this heading")

_class_ client.Deployments( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments "Link to this definition")

Deploy and score published artifacts (models and functions).

_class_ HardwareRequestSizes( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.HardwareRequestSizes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes "Link to this definition")

An enum class that represents the different hardware request sizes
available.

capitalize() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.capitalize "Link to this definition")

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower
case.

casefold() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.casefold "Link to this definition")

Return a version of the string suitable for caseless comparisons.

center( _width_, _fillchar=''_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.center "Link to this definition")

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count( _sub_\[, _start_\[, _end_\]\])→int [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.count "Link to this definition")

Return the number of non-overlapping occurrences of substring sub in
string S\[start:end\]. Optional arguments start and end are
interpreted as in slice notation.

encode( _encoding='utf-8'_, _errors='strict'_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.encode "Link to this definition")

Encode the string using the codec registered for encoding.

encoding

The encoding in which to encode the string.

errors

The error handling scheme to use for encoding errors.
The default is ‘strict’ meaning that encoding errors raise a
UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and
‘xmlcharrefreplace’ as well as any other name registered with
codecs.register\_error that can handle UnicodeEncodeErrors.

endswith( _suffix_\[, _start_\[, _end_\]\])→bool [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.endswith "Link to this definition")

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.

expandtabs( _tabsize=8_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.expandtabs "Link to this definition")

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find( _sub_\[, _start_\[, _end_\]\])→int [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.find "Link to this definition")

Return the lowest index in S where substring sub is found,
such that sub is contained within S\[start:end\]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

format( _\*args_, _\*\*kwargs_)→str [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.format "Link to this definition")

Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces (‘{’ and ‘}’).

format\_map( _mapping_)→str [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.format_map "Link to this definition")

Return a formatted version of S, using substitutions from mapping.
The substitutions are identified by braces (‘{’ and ‘}’).

index( _sub_\[, _start_\[, _end_\]\])→int [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.index "Link to this definition")

Return the lowest index in S where substring sub is found,
such that sub is contained within S\[start:end\]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

isalnum() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.isalnum "Link to this definition")

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and
there is at least one character in the string.

isalpha() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.isalpha "Link to this definition")

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there
is at least one character in the string.

isascii() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.isascii "Link to this definition")

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.

isdecimal() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.isdecimal "Link to this definition")

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and
there is at least one character in the string.

isdigit() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.isdigit "Link to this definition")

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there
is at least one character in the string.

isidentifier() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.isidentifier "Link to this definition")

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
such as “def” or “class”.

islower() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.islower "Link to this definition")

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and
there is at least one cased character in the string.

isnumeric() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.isnumeric "Link to this definition")

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at
least one character in the string.

isprintable() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.isprintable "Link to this definition")

Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in
repr() or if it is empty.

isspace() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.isspace "Link to this definition")

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there
is at least one character in the string.

istitle() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.istitle "Link to this definition")

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.

isupper() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.isupper "Link to this definition")

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and
there is at least one cased character in the string.

join( _iterable_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.join "Link to this definition")

Concatenate any number of strings.

The string whose method is called is inserted in between each given string.
The result is returned as a new string.

Example: ‘.’.join(\[‘ab’, ‘pq’, ‘rs’\]) -> ‘ab.pq.rs’

ljust( _width_, _fillchar=''_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.ljust "Link to this definition")

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.lower "Link to this definition")

Return a copy of the string converted to lowercase.

lstrip( _chars=None_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.lstrip "Link to this definition")

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

_static_ maketrans() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.maketrans "Link to this definition")

Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode
ordinals (integers) or characters to Unicode ordinals, strings or None.
Character keys will be then converted to ordinals.
If there are two arguments, they must be strings of equal length, and
in the resulting dictionary, each character in x will be mapped to the
character at the same position in y. If there is a third argument, it
must be a string, whose characters will be mapped to None in the result.

partition( _sep_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.partition "Link to this definition")

Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found,
returns a 3-tuple containing the part before the separator, the separator
itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string
and two empty strings.

removeprefix( _prefix_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.removeprefix "Link to this definition")

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string\[len(prefix):\].
Otherwise, return a copy of the original string.

removesuffix( _suffix_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.removesuffix "Link to this definition")

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty,
return string\[:-len(suffix)\]. Otherwise, return a copy of the original
string.

replace( _old_, _new_, _count=-1_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.replace "Link to this definition")

Return a copy with all occurrences of substring old replaced by new.

> count
>
> Maximum number of occurrences to replace.
> -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

rfind( _sub_\[, _start_\[, _end_\]\])→int [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.rfind "Link to this definition")

Return the highest index in S where substring sub is found,
such that sub is contained within S\[start:end\]. Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex( _sub_\[, _start_\[, _end_\]\])→int [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.rindex "Link to this definition")

Return the highest index in S where substring sub is found,
such that sub is contained within S\[start:end\]. Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust( _width_, _fillchar=''_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.rjust "Link to this definition")

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rpartition( _sep_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.rpartition "Link to this definition")

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If
the separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings
and the original string.

rsplit( _sep=None_, _maxsplit=-1_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.rsplit "Link to this definition")

Return a list of the substrings in the string, using sep as the separator string.

> sep
>
> The separator used to split the string.
>
> When set to None (the default value), will split on any whitespace
> character (including \\n \\r \\t \\f and spaces) and will discard
> empty strings from the result.
>
> maxsplit
>
> Maximum number of splits (starting from the left).
> -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

rstrip( _chars=None_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.rstrip "Link to this definition")

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

split( _sep=None_, _maxsplit=-1_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.split "Link to this definition")

Return a list of the substrings in the string, using sep as the separator string.

> sep
>
> The separator used to split the string.
>
> When set to None (the default value), will split on any whitespace
> character (including \\n \\r \\t \\f and spaces) and will discard
> empty strings from the result.
>
> maxsplit
>
> Maximum number of splits (starting from the left).
> -1 (the default value) means no limit.

Note, str.split() is mainly useful for data that has been intentionally
delimited. With natural text that includes punctuation, consider using
the regular expression module.

splitlines( _keepends=False_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.splitlines "Link to this definition")

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and
true.

startswith( _prefix_\[, _start_\[, _end_\]\])→bool [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.startswith "Link to this definition")

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try.

strip( _chars=None_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.strip "Link to this definition")

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.swapcase "Link to this definition")

Convert uppercase characters to lowercase and lowercase characters to uppercase.

title() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.title "Link to this definition")

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining
cased characters have lower case.

translate( _table_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.translate "Link to this definition")

Replace each character in the string using the given translation table.

> table
>
> Translation table, which must be a mapping of Unicode ordinals to
> Unicode ordinals, strings, or None.

The table must implement lookup/indexing via \_\_getitem\_\_, for instance a
dictionary or list. If this operation raises LookupError, the character is
left untouched. Characters mapped to None are deleted.

upper() [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.upper "Link to this definition")

Return a copy of the string converted to uppercase.

zfill( _width_, _/_) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.HardwareRequestSizes.zfill "Link to this definition")

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

create( _artifact\_id=None_, _meta\_props=None_, _rev\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.create) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.create "Link to this definition")

Create a deployment from an artifact. An artifact is a model or function that can be deployed.

Parameters:

- **artifact\_id** ( _str_) – ID of the published artifact (the model or function ID)

- **meta\_props** ( _dict_ _,_ _optional_) –

meta props. To see the available list of meta names, use:





```
client.deployments.ConfigurationMetaNames.get()

```

- **rev\_id** ( _str_ _,_ _optional_) – revision ID of the deployment


Returns:

metadata of the created deployment

Return type:

dict

**Example:**

```
meta_props = {
    client.deployments.ConfigurationMetaNames.NAME: "SAMPLE DEPLOYMENT NAME",
    client.deployments.ConfigurationMetaNames.ONLINE: {},
    client.deployments.ConfigurationMetaNames.HARDWARE_SPEC : { "id":  "e7ed1d6c-2e89-42d7-aed5-8sb972c1d2b"},
    client.deployments.ConfigurationMetaNames.SERVING_NAME : 'sample_deployment'
}
deployment_details = client.deployments.create(artifact_id, meta_props)

```

create\_job( _deployment\_id_, _meta\_props_, _retention=None_, _transaction\_id=None_, _\_asset\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.create_job) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.create_job "Link to this definition")

Create an asynchronous deployment job.

Parameters:

- **deployment\_id** ( _str_) – unique ID of the deployment

- **meta\_props** ( _dict_) – metaprops. To see the available list of metanames,
use `client.deployments.ScoringMetaNames.get()`
or `client.deployments.DecisionOptimizationmetaNames.get()`

- **retention** ( _int_ _,_ _optional_) – how many job days job meta should be retained,
takes integer values >= -1, supported only on Cloud

- **transaction\_id** ( _str_ _,_ _optional_) – transaction ID to be passed with the payload


Returns:

metadata of the created async deployment job

Return type:

dict or str

Note

- The valid payloads for scoring input are either list of values, pandas or numpy dataframes.


**Example:**

```
scoring_payload = {client.deployments.ScoringMetaNames.INPUT_DATA: [{'fields': ['GENDER','AGE','MARITAL_STATUS','PROFESSION'],\
                                                                         'values': [['M',23,'Single','Student'],\
                                                                                    ['M',55,'Single','Executive']]}]}
async_job = client.deployments.create_job(deployment_id, scoring_payload)

```

delete( _deployment\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.delete "Link to this definition")

Delete a deployment.

Parameters:

**deployment\_id** ( _str_) – unique ID of the deployment

Returns:

status (“SUCCESS” or “FAILED”)

Return type:

str

**Example:**

```
client.deployments.delete(deployment_id)

```

delete\_job( _job\_id=None_, _hard\_delete=False_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.delete_job) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.delete_job "Link to this definition")

Delete a deployment job that is running. This method can also delete metadata
details of completed or canceled jobs when hard\_delete parameter is set to True.

Parameters:

- **job\_id** ( _str_) – unique ID of the deployment job to be deleted

- **hard\_delete** ( _bool_ _,_ _optional_) –

specify True or False:

True \- To delete the completed or canceled job.

False \- To cancel the currently running deployment job.


Returns:

status (“SUCCESS” or “FAILED”)

Return type:

str

**Example:**

```
client.deployments.delete_job(job_id)

```

generate( _deployment\_id_, _prompt=None_, _params=None_, _guardrails=False_, _guardrails\_hap\_params=None_, _guardrails\_pii\_params=None_, _concurrency\_limit=8_, _async\_mode=False_, _validate\_prompt\_variables=True_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.generate) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.generate "Link to this definition")

Generate a raw response with prompt for given deployment\_id.

Parameters:

- **deployment\_id** ( _str_) – unique ID of the deployment

- **prompt** ( _str_ _,_ _optional_) – prompt needed for text generation. If deployment\_id points to the Prompt Template asset, then the prompt argument must be None, defaults to None

- **params** ( _dict_ _,_ _optional_) – meta props for text generation, use `ibm_watsonx_ai.metanames.GenTextParamsMetaNames().show()` to view the list of MetaNames

- **guardrails** ( _bool_ _,_ _optional_) – If True, then potentially hateful, abusive, and/or profane language (HAP) was detected
filter is toggle on for both prompt and generated text, defaults to False

- **guardrails\_hap\_params** ( _dict_ _,_ _optional_) – meta props for HAP moderations, use `ibm_watsonx_ai.metanames.GenTextModerationsMetaNames().show()`
to view the list of MetaNames

- **concurrency\_limit** ( _int_ _,_ _optional_) – number of requests to be sent in parallel, maximum is 10

- **async\_mode** ( _bool_ _,_ _optional_) – If True, then yield results asynchronously (using generator). In this case both the prompt and
the generated text will be concatenated in the final response - under generated\_text, defaults
to False

- **validate\_prompt\_variables** ( _bool_) – If True, prompt variables provided in params are validated with the ones in Prompt Template Asset.
This parameter is only applicable in a Prompt Template Asset deployment scenario and should not be changed for different cases, defaults to True


Returns:

scoring result containing generated content

Return type:

dict

generate\_text( _deployment\_id_, _prompt=None_, _params=None_, _raw\_response=False_, _guardrails=False_, _guardrails\_hap\_params=None_, _guardrails\_pii\_params=None_, _concurrency\_limit=8_, _validate\_prompt\_variables=True_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.generate_text) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.generate_text "Link to this definition")

Given the selected deployment (deployment\_id), a text prompt as input, and the parameters and concurrency\_limit,
the selected inference will generate a completion text as generated\_text response.

Parameters:

- **deployment\_id** ( _str_) – unique ID of the deployment

- **prompt** ( _str_ _,_ _optional_) – the prompt string or list of strings. If the list of strings is passed, requests will be managed in parallel with the rate of concurency\_limit, defaults to None

- **params** ( _dict_ _,_ _optional_) – meta props for text generation, use `ibm_watsonx_ai.metanames.GenTextParamsMetaNames().show()` to view the list of MetaNames

- **raw\_response** ( _bool_ _,_ _optional_) – returns the whole response object

- **guardrails** ( _bool_ _,_ _optional_) – If True, then potentially hateful, abusive, and/or profane language (HAP) was detected
filter is toggle on for both prompt and generated text, defaults to False

- **guardrails\_hap\_params** ( _dict_ _,_ _optional_) – meta props for HAP moderations, use `ibm_watsonx_ai.metanames.GenTextModerationsMetaNames().show()`
to view the list of MetaNames

- **concurrency\_limit** ( _int_ _,_ _optional_) – number of requests to be sent in parallel, maximum is 10

- **validate\_prompt\_variables** ( _bool_) – If True, prompt variables provided in params are validated with the ones in Prompt Template Asset.
This parameter is only applicable in a Prompt Template Asset deployment scenario and should not be changed for different cases, defaults to True


Returns:

generated content

Return type:

str

Note

By default only the first occurance of HAPDetectionWarning is displayed. To enable printing all warnings of this category, use:

```
import warnings
from ibm_watsonx_ai.foundation_models.utils import HAPDetectionWarning

warnings.filterwarnings("always", category=HAPDetectionWarning)

```

generate\_text\_stream( _deployment\_id_, _prompt=None_, _params=None_, _raw\_response=False_, _guardrails=False_, _guardrails\_hap\_params=None_, _guardrails\_pii\_params=None_, _validate\_prompt\_variables=True_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.generate_text_stream) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.generate_text_stream "Link to this definition")

Given the selected deployment (deployment\_id), a text prompt as input and parameters,
the selected inference will generate a streamed text as generate\_text\_stream.

Parameters:

- **deployment\_id** ( _str_) – unique ID of the deployment

- **prompt** ( _str_ _,_ _optional_) – the prompt string, defaults to None

- **params** ( _dict_ _,_ _optional_) – meta props for text generation, use `ibm_watsonx_ai.metanames.GenTextParamsMetaNames().show()` to view the list of MetaNames

- **raw\_response** ( _bool_ _,_ _optional_) – yields the whole response object

- **guardrails** ( _bool_ _,_ _optional_) – If True, then potentially hateful, abusive, and/or profane language (HAP) was detected
filter is toggle on for both prompt and generated text, defaults to False

- **guardrails\_hap\_params** ( _dict_ _,_ _optional_) – meta props for HAP moderations, use `ibm_watsonx_ai.metanames.GenTextModerationsMetaNames().show()`
to view the list of MetaNames

- **validate\_prompt\_variables** ( _bool_) – If True, prompt variables provided in params are validated with the ones in Prompt Template Asset.
This parameter is only applicable in a Prompt Template Asset deployment scenario and should not be changed for different cases, defaults to True


Returns:

generated content

Return type:

str

Note

By default only the first occurance of HAPDetectionWarning is displayed. To enable printing all warnings of this category, use:

```
import warnings
from ibm_watsonx_ai.foundation_models.utils import HAPDetectionWarning

warnings.filterwarnings("always", category=HAPDetectionWarning)

```

get\_details( _deployment\_id=None_, _serving\_name=None_, _limit=None_, _asynchronous=False_, _get\_all=False_, _spec\_state=None_, _\_silent=False_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_details "Link to this definition")

Get information about deployment(s).
If deployment\_id is not passed, all deployment details are returned.

Parameters:

- **deployment\_id** ( _str_ _,_ _optional_) – unique ID of the deployment

- **serving\_name** ( _str_ _,_ _optional_) – serving name that filters deployments

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks

- **spec\_state** ( _SpecStates_ _,_ _optional_) – software specification state, can be used only when deployment\_id is None


Returns:

metadata of the deployment(s)

Return type:

dict (if deployment\_id is not None) or {“resources”: \[dict\]} (if deployment\_id is None)

**Example:**

```
deployment_details = client.deployments.get_details(deployment_id)
deployment_details = client.deployments.get_details(deployment_id=deployment_id)
deployments_details = client.deployments.get_details()
deployments_details = client.deployments.get_details(limit=100)
deployments_details = client.deployments.get_details(limit=100, get_all=True)
deployments_details = []
for entry in client.deployments.get_details(limit=100, asynchronous=True, get_all=True):
    deployments_details.extend(entry)

```

get\_download\_url( _deployment\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_download_url) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_download_url "Link to this definition")

Get deployment\_download\_url from the deployment details.

Parameters:

**deployment\_details** ( _dict_) – created deployment details

Returns:

deployment download URL that is used to get file deployment (for example: Core ML)

Return type:

str

**Example:**

```
deployment_url = client.deployments.get_download_url(deployment)

```

_static_ get\_href( _deployment\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_href "Link to this definition")

Get deployment\_href from the deployment details.

Parameters:

**deployment\_details** ( _dict_) – metadata of the deployment

Returns:

deployment href that is used to manage the deployment

Return type:

str

**Example:**

```
deployment_href = client.deployments.get_href(deployment)

```

_static_ get\_id( _deployment\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_id "Link to this definition")

Get the deployment ID from the deployment details.

Parameters:

**deployment\_details** ( _dict_) – metadata of the deployment

Returns:

deployment ID that is used to manage the deployment

Return type:

str

**Example:**

```
deployment_id = client.deployments.get_id(deployment)

```

get\_job\_details( _job\_id=None_, _include=None_, _limit=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_job_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_job_details "Link to this definition")

Get information about deployment job(s).
If deployment job\_id is not passed, all deployment jobs details are returned.

Parameters:

- **job\_id** ( _str_ _,_ _optional_) – unique ID of the job

- **include** ( _str_ _,_ _optional_) – fields to be retrieved from ‘decision\_optimization’
and ‘scoring’ section mentioned as value(s) (comma separated) as output response fields

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

metadata of deployment job(s)

Return type:

dict (if job\_id is not None) or {“resources”: \[dict\]} (if job\_id is None)

**Example:**

```
deployment_details = client.deployments.get_job_details()
deployments_details = client.deployments.get_job_details(job_id=job_id)

```

get\_job\_href( _job\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_job_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_job_href "Link to this definition")

Get the href of a deployment job.

Parameters:

**job\_details** ( _dict_) – metadata of the deployment job

Returns:

href of the deployment job

Return type:

str

**Example:**

```
job_details = client.deployments.get_job_details(job_id=job_id)
job_status = client.deployments.get_job_href(job_details)

```

get\_job\_id( _job\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_job_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_job_id "Link to this definition")

Get the unique ID of a deployment job.

Parameters:

**job\_details** ( _dict_) – metadata of the deployment job

Returns:

unique ID of the deployment job

Return type:

str

**Example:**

```
job_details = client.deployments.get_job_details(job_id=job_id)
job_status = client.deployments.get_job_id(job_details)

```

get\_job\_status( _job\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_job_status) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_job_status "Link to this definition")

Get the status of a deployment job.

Parameters:

**job\_id** ( _str_) – unique ID of the deployment job

Returns:

status of the deployment job

Return type:

dict

**Example:**

```
job_status = client.deployments.get_job_status(job_id)

```

get\_job\_uid( _job\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_job_uid) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_job_uid "Link to this definition")

Get the unique ID of a deployment job.

_Deprecated:_ Use `get_job_id(job_details)` instead.

Parameters:

**job\_details** ( _dict_) – metadata of the deployment job

Returns:

unique ID of the deployment job

Return type:

str

**Example:**

```
job_details = client.deployments.get_job_details(job_uid=job_uid)
job_status = client.deployments.get_job_uid(job_details)

```

_static_ get\_scoring\_href( _deployment\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_scoring_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_scoring_href "Link to this definition")

Get scoring URL from deployment details.

Parameters:

**deployment\_details** ( _dict_) – metadata of the deployment

Returns:

scoring endpoint URL that is used to make scoring requests

Return type:

str

**Example:**

```
scoring_href = client.deployments.get_scoring_href(deployment)

```

_static_ get\_serving\_href( _deployment\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_serving_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_serving_href "Link to this definition")

Get serving URL from the deployment details.

Parameters:

**deployment\_details** ( _dict_) – metadata of the deployment

Returns:

serving endpoint URL that is used to make scoring requests

Return type:

str

**Example:**

```
scoring_href = client.deployments.get_serving_href(deployment)

```

_static_ get\_uid( _deployment\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.get_uid) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.get_uid "Link to this definition")

Get deployment\_uid from the deployment details.

_Deprecated:_ Use `get_id(deployment_details)` instead.

Parameters:

**deployment\_details** ( _dict_) – metadata of the deployment

Returns:

deployment UID that is used to manage the deployment

Return type:

str

**Example:**

```
deployment_uid = client.deployments.get_uid(deployment)

```

is\_serving\_name\_available( _serving\_name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.is_serving_name_available) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.is_serving_name_available "Link to this definition")

Check if the serving name is available for use.

Parameters:

**serving\_name** ( _str_) – serving name that filters deployments

Returns:

information about whether the serving name is available

Return type:

bool

**Example:**

```
is_available = client.deployments.is_serving_name_available('test')

```

list( _limit=None_, _artifact\_type=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.list "Link to this definition")

Returns deployments in a table format.

Parameters:

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **artifact\_type** ( _str_ _,_ _optional_) – return only deployments with the specified artifact\_type


Returns:

pandas.DataFrame with the listed deployments

Return type:

pandas.DataFrame

**Example:**

```
client.deployments.list()

```

list\_jobs( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.list_jobs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.list_jobs "Link to this definition")

Return the async deployment jobs in a table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records

Returns:

pandas.DataFrame with listed deployment jobs

Return type:

pandas.DataFrame

Note

This method list only async deployment jobs created for WML deployment.

**Example:**

```
client.deployments.list_jobs()

```

run\_ai\_service( _deployment\_id_, _ai\_service\_payload_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.run_ai_service) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.run_ai_service "Link to this definition")

Execute an AI service by providing a scoring payload.

Parameters:

- **deployment\_id** ( _str_) – unique ID of the deployment

- **ai\_service\_payload** ( _dict_) – AI service payload to be passed to generate the method


Returns:

response of the AI service

Return type:

Any

Note

- By executing this class method, a POST request is performed.

- In case of method not allowed error, try sending requests directly to your deployed ai service.


run\_ai\_service\_stream( _deployment\_id_, _ai\_service\_payload_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.run_ai_service_stream) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.run_ai_service_stream "Link to this definition")

Execute an AI service by providing a scoring payload.

Parameters:

- **deployment\_id** ( _str_) – unique ID of the deployment

- **ai\_service\_payload** ( _dict_) – AI service payload to be passed to generate the method


Returns:

stream of the response of the AI service

Return type:

Generator

score( _deployment\_id_, _meta\_props_, _transaction\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.score) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.score "Link to this definition")

Make scoring requests against the deployed artifact.

Parameters:

- **deployment\_id** ( _str_) – unique ID of the deployment to be scored

- **meta\_props** ( _dict_) – meta props for scoring, use `client.deployments.ScoringMetaNames.show()` to view the list of ScoringMetaNames

- **transaction\_id** ( _str_ _,_ _optional_) – transaction ID to be passed with the records during payload logging


Returns:

scoring result that contains prediction and probability

Return type:

dict

Note

- _client.deployments.ScoringMetaNames.INPUT\_DATA_ is the only metaname valid for sync scoring.

- The valid payloads for scoring input are either list of values, pandas or numpy dataframes.


**Example:**

```
scoring_payload = {client.deployments.ScoringMetaNames.INPUT_DATA:
    [{'fields':\
        ['GENDER','AGE','MARITAL_STATUS','PROFESSION'],\
        'values': [\
            ['M',23,'Single','Student'],\
            ['M',55,'Single','Executive']\
        ]\
    }]
}
predictions = client.deployments.score(deployment_id, scoring_payload)

```

update( _deployment\_id=None_, _changes=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#Deployments.update) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Deployments.update "Link to this definition")

Updates existing deployment metadata. If ASSET is patched, then ‘id’ field is mandatory
and it starts a deployment with the provided asset id/rev. Deployment ID remains the same.

Parameters:

- **deployment\_id** ( _str_) – unique ID of deployment to be updated

- **changes** ( _dict_) – elements to be changed, where keys are ConfigurationMetaNames


Returns:

metadata of the updated deployment

Return type:

dict or None

**Examples**

```
metadata = {client.deployments.ConfigurationMetaNames.NAME:"updated_Deployment"}
updated_deployment_details = client.deployments.update(deployment_id, changes=metadata)

metadata = {client.deployments.ConfigurationMetaNames.ASSET: {  "id": "ca0cd864-4582-4732-b365-3165598dc945",
                                                                "rev":"2" }}
deployment_details = client.deployments.update(deployment_id, changes=metadata)

```

_class_ metanames.DeploymentMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#DeploymentMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.DeploymentMetaNames "Link to this definition")

Set of MetaNames for Deployments Specs.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| TAGS | list | N | `['string']` | `['string1', 'string2']` |
| NAME | str | N |  | `my_deployment` |
| DESCRIPTION | str | N |  | `my_deployment` |
| CUSTOM | dict | N |  | `{}` |
| ASSET | dict | N |  | `{'id': '4cedab6d-e8e4-4214-b81a-2ddb122db2ab', 'rev': '1'}` |
| PROMPT\_TEMPLATE | dict | N |  | `{'id': '4cedab6d-e8e4-4214-b81a-2ddb122db2ab'}` |
| HARDWARE\_SPEC | dict | N |  | `{'id': '3342-1ce536-20dc-4444-aac7-7284cf3befc'}` |
| HARDWARE\_REQUEST | dict | N |  | `{'size': 'gpu_s', 'num_nodes': 1}` |
| HYBRID\_PIPELINE\_HARDWARE\_SPECS | list | N |  | `[{'node_runtime_id': 'auto_ai.kb', 'hardware_spec': {'id': '3342-1ce536-20dc-4444-aac7-7284cf3befc', 'num_nodes': '2'}}]` |
| ONLINE | dict | N |  | `{}` |
| BATCH | dict | N |  | `{}` |
| DETACHED | dict | N |  | `{}` |
| R\_SHINY | dict | N |  | `{'authentication': 'anyone_with_url'}` |
| VIRTUAL | dict | N |  | `{}` |
| OWNER | str | N |  | `<owner_id>` |
| BASE\_MODEL\_ID | str | N |  | `google/flan-ul2` |
| BASE\_DEPLOYMENT\_ID | str | N |  | `76a60161-facb-4968-a475-a6f1447c44bf` |
| PROMPT\_VARIABLES | dict | N |  | `{'key': 'value'}` |

_class_ ibm\_watsonx\_ai.utils.enums.RShinyAuthenticationValues( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/enums.html#RShinyAuthenticationValues) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.enums.RShinyAuthenticationValues "Link to this definition")

Allowable values of R\_Shiny authentication.

ANYONE\_WITH\_URL _='anyone\_with\_url'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.enums.RShinyAuthenticationValues.ANYONE_WITH_URL "Link to this definition")ANY\_VALID\_USER _='any\_valid\_user'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.enums.RShinyAuthenticationValues.ANY_VALID_USER "Link to this definition")MEMBERS\_OF\_DEPLOYMENT\_SPACE _='members\_of\_deployment\_space'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.enums.RShinyAuthenticationValues.MEMBERS_OF_DEPLOYMENT_SPACE "Link to this definition")_class_ metanames.ScoringMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#ScoringMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.ScoringMetaNames "Link to this definition")

Set of MetaNames for Scoring.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| NAME | str | N |  | `jobs test` |
| INPUT\_DATA | list | N | `[{'name(optional)': 'string', 'id(optional)': 'string', 'fields(optional)': 'array[string]', 'values': 'array[array[string]]'}]` | `[{'fields': ['name', 'age', 'occupation'], 'values': [['john', 23, 'student']]}]` |
| INPUT\_DATA\_REFERENCES | list | N | `[{'id(optional)': 'string', 'type(required)': 'string', 'connection(required)': {'href(required)': 'string'}, 'location(required)': {'bucket': 'string', 'path': 'string'}, 'schema(optional)': {'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}}]` |  |
| OUTPUT\_DATA\_REFERENCE | dict | N | `{'type(required)': 'string', 'connection(required)': {'href(required)': 'string'}, 'location(required)': {'bucket': 'string', 'path': 'string'}, 'schema(optional)': {'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}}` |  |
| EVALUATIONS\_SPEC | list | N | `[{'id(optional)': 'string', 'input_target(optional)': 'string', 'metrics_names(optional)': 'array[string]'}]` | `[{'id': 'string', 'input_target': 'string', 'metrics_names': ['auroc', 'accuracy']}]` |
| ENVIRONMENT\_VARIABLES | dict | N |  | `{'my_env_var1': 'env_var_value1', 'my_env_var2': 'env_var_value2'}` |
| SCORING\_PARAMETERS | dict | N |  | `{'forecast_window': 50}` |

_class_ metanames.DecisionOptimizationMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#DecisionOptimizationMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.DecisionOptimizationMetaNames "Link to this definition")

Set of MetaNames for Decision Optimization.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| INPUT\_DATA | list | N | `[{'name(optional)': 'string', 'id(optional)': 'string', 'fields(optional)': 'array[string]', 'values': 'array[array[string]]'}]` | `[{'fields': ['name', 'age', 'occupation'], 'values': [['john', 23, 'student']]}]` |
| INPUT\_DATA\_REFERENCES | list | N | `[{'name(optional)': 'string', 'id(optional)': 'string', 'fields(optional)': 'array[string]', 'values': 'array[array[string]]'}]` | `[{'fields': ['name', 'age', 'occupation'], 'values': [['john', 23, 'student']]}]` |
| OUTPUT\_DATA | list | N | `[{'name(optional)': 'string'}]` |  |
| OUTPUT\_DATA\_REFERENCES | list | N | `{'name(optional)': 'string', 'type(required)': 'string', 'connection(required)': {'endpoint_url(required)': 'string', 'access_key_id(required)': 'string', 'secret_access_key(required)': 'string'}, 'location(required)': {'bucket': 'string', 'path': 'string'}, 'schema(optional)': {'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}}` |  |
| SOLVE\_PARAMETERS | dict | N |  |  |

_class_ ibm\_watsonx\_ai.deployments.RuntimeContext( _api\_client_, _request\_payload\_json=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#RuntimeContext) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.deployments.RuntimeContext "Link to this definition")

Class included to keep the interface compatible with the Deployment’s RuntimeContext
used in AIServices implementation.

Parameters:

- **api\_client** ( [_APIClient_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#client.APIClient "client.APIClient")) – initialized APIClient object with a set project ID or space ID. If passed, `credentials` and `project_id`/ `space_id` are not required.

- **request\_payload\_json** ( _dict_ _,_ _optional_) – Request payload for testing of generate/ generate\_stream call of AI Service.


\`\`
RuntimeContext\`\` initialized for testing purposes before deployment:

```
context = RuntimeContext(api_client=client, request_payload_json={"field": "value"})

```

Examples of `RuntimeContext` usage within AI Service source code:

```
def deployable_ai_service(context, **custom):
    task_token = context.generate_token()

    def generate(context) -> dict:
        user_token = context.get_token()
        headers = context.get_headers()
        json_body = context.get_json()
        ...
        return {"body": json_body}

    return generate

generate = deployable_ai_service(context)
generate_output = generate(context)  # returns {"body": {"field": "value"}}

```

Change the JSON body in `RuntimeContext`:

```
context.request_payload_json = {"field2": "value2"}

generate = deployable_ai_service(context)
generate_output = generate(context)  # returns {"body": {"field2": "value2"}}

```

generate\_token() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#RuntimeContext.generate_token) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.deployments.RuntimeContext.generate_token "Link to this definition")

Return refreshed token.

get\_headers() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#RuntimeContext.get_headers) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.deployments.RuntimeContext.get_headers "Link to this definition")

Return headers with refreshed token

get\_json() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#RuntimeContext.get_json) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.deployments.RuntimeContext.get_json "Link to this definition")

Get payload JSON send in body of API request to the generate or generate\_stream method in deployed AIService.
For testing purposes the payload JSON need to be set in RuntimeContext initialization
or later as request\_payload\_json property.

get\_token() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/deployments.html#RuntimeContext.get_token) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.deployments.RuntimeContext.get_token "Link to this definition")

Return user token.

## Export/Import [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#export-import "Link to this heading")

_class_ client.Export( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/export_assets.html#Export) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Export "Link to this definition")cancel( _export\_id_, _space\_id=None_, _project\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/export_assets.html#Export.cancel) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Export.cancel "Link to this definition")

Cancel an export job. space\_id or project\_id has to be provided.

Note

To delete an export\_id job, use `delete()` API.

Parameters:

- **export\_id** ( _str_) – export job identifier

- **space\_id** ( _str_ _,_ _optional_) – space identifier

- **project\_id** ( _str_ _,_ _optional_) – project identifier


Returns:

status (“SUCCESS” or “FAILED”)

Return type:

str

**Example:**

```
client.export_assets.cancel(export_id='6213cf1-252f-424b-b52d-5cdd9814956c',
                            space_id='3421cf1-252f-424b-b52d-5cdd981495fe')

```

delete( _export\_id_, _space\_id=None_, _project\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/export_assets.html#Export.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Export.delete "Link to this definition")

Delete the given export\_id job. space\_id or project\_id has to be provided.

Parameters:

- **export\_id** ( _str_) – export job identifier

- **space\_id** ( _str_ _,_ _optional_) – space identifier

- **project\_id** ( _str_ _,_ _optional_) – project identifier


Returns:

status (“SUCCESS” or “FAILED”)

Return type:

str

**Example:**

```
client.export_assets.delete(export_id='6213cf1-252f-424b-b52d-5cdd9814956c',
                            space_id= '98a53931-a8c0-4c2f-8319-c793155e4598')

```

get\_details( _export\_id=None_, _space\_id=None_, _project\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/export_assets.html#Export.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Export.get_details "Link to this definition")

Get metadata of a given export job. If no export\_id is specified, all export metadata is returned.

Parameters:

- **export\_id** ( _str_ _,_ _optional_) – export job identifier

- **space\_id** ( _str_ _,_ _optional_) – space identifier

- **project\_id** ( _str_ _,_ _optional_) – project identifier

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

export metadata

Return type:

dict (if export\_id is not None) or {“resources”: \[dict\]} (if export\_id is None)

**Example:**

```
details = client.export_assets.get_details(export_id, space_id= '98a53931-a8c0-4c2f-8319-c793155e4598')
details = client.export_assets.get_details()
details = client.export_assets.get_details(limit=100)
details = client.export_assets.get_details(limit=100, get_all=True)
details = []
for entry in client.export_assets.get_details(limit=100, asynchronous=True, get_all=True):
    details.extend(entry)

```

get\_exported\_content( _export\_id_, _space\_id=None_, _project\_id=None_, _file\_path=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/export_assets.html#Export.get_exported_content) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Export.get_exported_content "Link to this definition")

Get the exported content as a zip file.

Parameters:

- **export\_id** ( _str_) – export job identifier

- **space\_id** ( _str_ _,_ _optional_) – space identifier

- **project\_id** ( _str_ _,_ _optional_) – project identifier

- **file\_path** ( _str_ _,_ _optional_) – name of local file to create, this should be absolute path of the file
and the file shouldn’t exist


Returns:

path to the downloaded function content

Return type:

str

**Example:**

```
client.export_assets.get_exported_content(export_id,
                                    space_id='98a53931-a8c0-4c2f-8319-c793155e4598',
                                    file_path='/home/user/my_exported_content.zip')

```

_static_ get\_id( _export\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/export_assets.html#Export.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Export.get_id "Link to this definition")

Get the ID of the export job from export details.

Parameters:

**export\_details** ( _dict_) – metadata of the export job

Returns:

ID of the export job

Return type:

str

**Example:**

```
id = client.export_assets.get_id(export_details)

```

list( _space\_id=None_, _project\_id=None_, _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/export_assets.html#Export.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Export.list "Link to this definition")

Return export jobs in a table format.

Parameters:

- **space\_id** ( _str_ _,_ _optional_) – space identifier

- **project\_id** ( _str_ _,_ _optional_) – project identifier

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

pandas.DataFrame with listed connections

Return type:

pandas.DataFrame

**Example:**

```
client.export_assets.list()

```

start( _meta\_props_, _space\_id=None_, _project\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/export_assets.html#Export.start) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Export.start "Link to this definition")

Start the export. You must provide the space\_id or the project\_id.
ALL\_ASSETS is by default False. You don’t need to provide it unless it is set to True.
You must provide one of the following in the meta\_props: ALL\_ASSETS, ASSET\_TYPES, or ASSET\_IDS. Only one of these can be
provided.

In the meta\_props:

ALL\_ASSETS is a boolean. When set to True, it exports all assets in the given space.
ASSET\_IDS is an array that contains the list of assets IDs to be exported.
ASSET\_TYPES is used to provide the asset types to be exported. All assets of that asset type will be exported.

> Eg: wml\_model, wml\_model\_definition, wml\_pipeline, wml\_function, wml\_experiment,
> software\_specification, hardware\_specification, package\_extension, script

Parameters:

- **meta\_props** ( _dict_) – metadata,
to see available meta names use `client.export_assets.ConfigurationMetaNames.get()`

- **space\_id** ( _str_ _,_ _optional_) – space identifier

- **project\_id** – project identifier


Returns:

Response json

Return type:

dict

**Example:**

```
metadata = {
    client.export_assets.ConfigurationMetaNames.NAME: "export_model",
    client.export_assets.ConfigurationMetaNames.ASSET_IDS: ["13a53931-a8c0-4c2f-8319-c793155e7517",\
                                                            "13a53931-a8c0-4c2f-8319-c793155e7518"]}

details = client.export_assets.start(meta_props=metadata, space_id="98a53931-a8c0-4c2f-8319-c793155e4598")

```

```
metadata = {
    client.export_assets.ConfigurationMetaNames.NAME: "export_model",
    client.export_assets.ConfigurationMetaNames.ASSET_TYPES: ["wml_model"]}

details = client.export_assets.start(meta_props=metadata, space_id="98a53931-a8c0-4c2f-8319-c793155e4598")

```

```
metadata = {
    client.export_assets.ConfigurationMetaNames.NAME: "export_model",
    client.export_assets.ConfigurationMetaNames.ALL_ASSETS: True}

details = client.export_assets.start(meta_props=metadata, space_id="98a53931-a8c0-4c2f-8319-c793155e4598")

```

_class_ client.Import( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/import_assets.html#Import) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Import "Link to this definition")cancel( _import\_id_, _space\_id=None_, _project\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/import_assets.html#Import.cancel) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Import.cancel "Link to this definition")

Cancel an import job. You must provide the space\_id or the project\_id.

Note

To delete an import\_id job, use delete() api

Parameters:

- **import\_id** ( _str_) – import the job identifier

- **space\_id** ( _str_ _,_ _optional_) – space identifier

- **project\_id** ( _str_ _,_ _optional_) – project identifier


**Example:**

```
client.import_assets.cancel(import_id='6213cf1-252f-424b-b52d-5cdd9814956c',
                            space_id='3421cf1-252f-424b-b52d-5cdd981495fe')

```

delete( _import\_id_, _space\_id=None_, _project\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/import_assets.html#Import.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Import.delete "Link to this definition")

Deletes the given import\_id job. You must provide the space\_id or the project\_id.

Parameters:

- **import\_id** ( _str_) – import the job identifier

- **space\_id** ( _str_ _,_ _optional_) – space identifier

- **project\_id** ( _str_ _,_ _optional_) – project identifier


**Example:**

```
client.import_assets.delete(import_id='6213cf1-252f-424b-b52d-5cdd9814956c',
                            space_id= '98a53931-a8c0-4c2f-8319-c793155e4598')

```

get\_details( _import\_id=None_, _space\_id=None_, _project\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/import_assets.html#Import.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Import.get_details "Link to this definition")

Get metadata of the given import job. If no import\_id is specified, all import metadata is returned.

Parameters:

- **import\_id** ( _str_ _,_ _optional_) – import the job identifier

- **space\_id** ( _str_ _,_ _optional_) – space identifier

- **project\_id** ( _str_ _,_ _optional_) – project identifier

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

import(s) metadata

Return type:

dict (if import\_id is not None) or {“resources”: \[dict\]} (if import\_id is None)

**Example:**

```
details = client.import_assets.get_details(import_id)
details = client.import_assets.get_details()
details = client.import_assets.get_details(limit=100)
details = client.import_assets.get_details(limit=100, get_all=True)
details = []
for entry in client.import_assets.get_details(limit=100, asynchronous=True, get_all=True):
    details.extend(entry)

```

_static_ get\_id( _import\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/import_assets.html#Import.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Import.get_id "Link to this definition")

Get ID of the import job from import details.

Parameters:

**import\_details** ( _dict_) – metadata of the import job

Returns:

ID of the import job

Return type:

str

**Example:**

```
id = client.import_assets.get_id(import_details)

```

list( _space\_id=None_, _project\_id=None_, _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/import_assets.html#Import.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Import.list "Link to this definition")

Return import jobs in a table format.

Parameters:

- **space\_id** ( _str_ _,_ _optional_) – space identifier

- **project\_id** ( _str_ _,_ _optional_) – project identifier

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

pandas.DataFrame with listed assets

Return type:

pandas.DataFrame

**Example:**

```
client.import_assets.list()

```

start( _file\_path_, _space\_id=None_, _project\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/import_assets.html#Import.start) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Import.start "Link to this definition")

Start the import. You must provide the space\_id or the project\_id.

Parameters:

- **file\_path** ( _str_) – file path to the zip file with exported assets

- **space\_id** ( _str_ _,_ _optional_) – space identifier

- **project\_id** ( _str_ _,_ _optional_) – project identifier


Returns:

response json

Return type:

dict

**Example:**

```
details = client.import_assets.start(space_id="98a53931-a8c0-4c2f-8319-c793155e4598",
                                     file_path="/home/user/data_to_be_imported.zip")

```

## Factsheets (IBM Cloud only) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#factsheets-ibm-cloud-only "Link to this heading")

**Warning!** Not supported for IBM Cloud Pak® for Data.

_class_ client.Factsheets( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/factsheets.html#Factsheets) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Factsheets "Link to this definition")

Link WML Model to Model Entry.

list\_model\_entries( _catalog\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/factsheets.html#Factsheets.list_model_entries) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Factsheets.list_model_entries "Link to this definition")

Return all WKC Model Entry assets for a catalog.

Parameters:

**catalog\_id** ( _str_ _,_ _optional_) – catalog ID where you want to register model. If no catalog\_id is provided, WKC Model Entry assets from all catalogs are listed.

Returns:

all WKC Model Entry assets for a catalog

Return type:

dict

**Example:**

```
model_entries = client.factsheets.list_model_entries(catalog_id)

```

register\_model\_entry( _model\_id_, _meta\_props_, _catalog\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/factsheets.html#Factsheets.register_model_entry) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Factsheets.register_model_entry "Link to this definition")

Link WML Model to Model Entry

Parameters:

- **model\_id** ( _str_) – ID of the published model/asset

- **meta\_props** ( _dict_ _\[_ _str_ _,_ _str_ _\]_) –

metaprops, to see the available list of meta names use:





```
client.factsheets.ConfigurationMetaNames.get()

```

- **catalog\_id** ( _str_ _,_ _optional_) – catalog ID where you want to register model


Returns:

metadata of the registration

Return type:

dict

**Example:**

```
meta_props = {
    client.factsheets.ConfigurationMetaNames.ASSET_ID: '83a53931-a8c0-4c2f-8319-c793155e7517'}

registration_details = client.factsheets.register_model_entry(model_id, catalog_id, meta_props)

```

or

```
meta_props = {
    client.factsheets.ConfigurationMetaNames.NAME: "New model entry",
    client.factsheets.ConfigurationMetaNames.DESCRIPTION: "New model entry"}

registration_details = client.factsheets.register_model_entry(model_id, meta_props)

```

unregister\_model\_entry( _asset\_id_, _catalog\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/factsheets.html#Factsheets.unregister_model_entry) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Factsheets.unregister_model_entry "Link to this definition")

Unregister WKC Model Entry

Parameters:

- **asset\_id** ( _str_) – ID of the WKC model entry

- **catalog\_id** ( _str_ _,_ _optional_) – catalog ID where the asset is stored, when not provided,
default client space or project will be taken


**Example:**

```
model_entries = client.factsheets.unregister_model_entry(asset_id='83a53931-a8c0-4c2f-8319-c793155e7517',
                                                         catalog_id='34553931-a8c0-4c2f-8319-c793155e7517')

```

or

```
client.set.default_space('98f53931-a8c0-4c2f-8319-c793155e7517')
model_entries = client.factsheets.unregister_model_entry(asset_id='83a53931-a8c0-4c2f-8319-c793155e7517')

```

_class_ metanames.FactsheetsMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#FactsheetsMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.FactsheetsMetaNames "Link to this definition")

Set of MetaNames for Factsheets metanames.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| ASSET\_ID | str | N | `13a53931-a8c0-4c2f-8319-c793155e7517` |
| NAME | str | N | `New model entry` |
| DESCRIPTION | str | N | `New model entry` |
| MODEL\_ENTRY\_CATALOG\_ID | str | Y | `13a53931-a8c0-4c2f-8319-c793155e7517` |

## Hardware specifications [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#hardware-specifications "Link to this heading")

_class_ client.HwSpec( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/hw_spec.html#HwSpec) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.HwSpec "Link to this definition")

Store and manage hardware specs.

ConfigurationMetaNames _=<ibm\_watsonx\_ai.metanames.HwSpecMetaNamesobject>_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.HwSpec.ConfigurationMetaNames "Link to this definition")

MetaNames for Hardware Specification.

delete( _hw\_spec\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/hw_spec.html#HwSpec.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.HwSpec.delete "Link to this definition")

Delete a hardware specification.

Parameters:

**hw\_spec\_id** ( _str_) – unique ID of the hardware specification to be deleted

Returns:

status (“SUCCESS” or “FAILED”)

Return type:

str

get\_details( _hw\_spec\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/hw_spec.html#HwSpec.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.HwSpec.get_details "Link to this definition")

Get hardware specification details.

Parameters:

**hw\_spec\_id** ( _str_) – unique ID of the hardware spec

Returns:

metadata of the hardware specifications

Return type:

dict

**Example:**

```
hw_spec_details = client.hardware_specifications.get_details(hw_spec_uid)

```

_static_ get\_href( _hw\_spec\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/hw_spec.html#HwSpec.get_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.HwSpec.get_href "Link to this definition")

Get the URL of hardware specifications.

Parameters:

**hw\_spec\_details** ( _dict_) – details of the hardware specifications

Returns:

href of the hardware specifications

Return type:

str

**Example:**

```
hw_spec_details = client.hw_spec.get_details(hw_spec_id)
hw_spec_href = client.hw_spec.get_href(hw_spec_details)

```

_static_ get\_id( _hw\_spec\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/hw_spec.html#HwSpec.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.HwSpec.get_id "Link to this definition")

Get the ID of a hardware specifications asset.

Parameters:

**hw\_spec\_details** ( _dict_) – metadata of the hardware specifications

Returns:

unique ID of the hardware specifications

Return type:

str

**Example:**

```
asset_id = client.hardware_specifications.get_id(hw_spec_details)

```

get\_id\_by\_name( _hw\_spec\_name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/hw_spec.html#HwSpec.get_id_by_name) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.HwSpec.get_id_by_name "Link to this definition")

Get the unique ID of a hardware specification for the given name.

Parameters:

**hw\_spec\_name** ( _str_) – name of the hardware specification

Returns:

unique ID of the hardware specification

Return type:

str

**Example:**

```
asset_id = client.hardware_specifications.get_id_by_name(hw_spec_name)

```

_static_ get\_uid( _hw\_spec\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/hw_spec.html#HwSpec.get_uid) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.HwSpec.get_uid "Link to this definition")

Get the UID of a hardware specifications asset.

_Deprecated:_ Use `get_id(hw_spec_details)` instead.

Parameters:

**hw\_spec\_details** ( _dict_) – metadata of the hardware specifications

Returns:

unique ID of the hardware specifications

Return type:

str

**Example:**

```
asset_uid = client.hardware_specifications.get_uid(hw_spec_details)

```

get\_uid\_by\_name( _hw\_spec\_name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/hw_spec.html#HwSpec.get_uid_by_name) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.HwSpec.get_uid_by_name "Link to this definition")

Get the unique ID of a hardware specification for the given name.

_Deprecated:_ Use `get_id_by_name(hw_spec_name)` instead.

Parameters:

**hw\_spec\_name** ( _str_) – name of the hardware specification

Returns:

unique ID of the hardware specification

Return type:

str

**Example:**

```
asset_uid = client.hardware_specifications.get_uid_by_name(hw_spec_name)

```

list( _name=None_, _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/hw_spec.html#HwSpec.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.HwSpec.list "Link to this definition")

List hardware specifications in a table format.

Parameters:

- **name** ( _str_ _,_ _optional_) – unique ID of the hardware spec

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

pandas.DataFrame with listed hardware specifications

Return type:

pandas.DataFrame

**Example:**

```
client.hardware_specifications.list()

```

store( _meta\_props_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/hw_spec.html#HwSpec.store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.HwSpec.store "Link to this definition")

Create a hardware specification.

Parameters:

**meta\_props** ( _dict_) –

metadata of the hardware specification configuration. To see available meta names, use:

```
client.hardware_specifications.ConfigurationMetaNames.get()

```

Returns:

metadata of the created hardware specification

Return type:

dict

**Example:**

```
meta_props = {
    client.hardware_specifications.ConfigurationMetaNames.NAME: "custom hardware specification",
    client.hardware_specifications.ConfigurationMetaNames.DESCRIPTION: "Custom hardware specification creted with SDK",
    client.hardware_specifications.ConfigurationMetaNames.NODES:{"cpu":{"units":"2"},"mem":{"size":"128Gi"},"gpu":{"num_gpu":1}}
 }

client.hardware_specifications.store(meta_props)

```

_class_ metanames.HwSpecMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#HwSpecMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.HwSpecMetaNames "Link to this definition")

Set of MetaNames for Hardware Specifications Specs.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| NAME | str | Y | `Custom Hardware Specification` |
| DESCRIPTION | str | N | `my_description` |
| NODES | dict | N | `{}` |
| SPARK | dict | N | `{}` |
| DATASTAGE | dict | N | `{}` |

## Helpers [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#helpers "Link to this heading")

_class_ ibm\_watsonx\_ai.helpers.helpers.get\_credentials\_from\_config( _env\_name_, _credentials\_name_, _config\_path='./config.ini'_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/helpers/helpers.html#get_credentials_from_config) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.helpers.helpers.get_credentials_from_config "Link to this definition")

Bases:

Load credentials from the config file.

```
[DEV_LC]

credentials = { }
cos_credentials = { }

```

Parameters:

- **env\_name** ( _str_) – name of \[ENV\] defined in the config file

- **credentials\_name** ( _str_) – name of credentials

- **config\_path** ( _str_) – path to the config file


Returns:

loaded credentials

Return type:

dict

**Example:**

```
get_credentials_from_config(env_name='DEV_LC', credentials_name='credentials')

```

## Model definitions [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#model-definitions "Link to this heading")

_class_ client.ModelDefinition( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition "Link to this definition")

Store and manage model definitions.

ConfigurationMetaNames _=<ibm\_watsonx\_ai.metanames.ModelDefinitionMetaNamesobject>_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.ConfigurationMetaNames "Link to this definition")

MetaNames for model definition creation.

create\_revision( _model\_definition\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.create_revision) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.create_revision "Link to this definition")

Create a revision for the given model definition. Revisions are immutable once created.
The metadata and attachment of the model definition is taken and a revision is created out of it.

Parameters:

**model\_definition\_id** ( _str_) – ID of the model definition

Returns:

revised metadata of the stored model definition

Return type:

dict

**Example:**

```
model_definition_revision = client.model_definitions.create_revision(model_definition_id)

```

delete( _model\_definition\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.delete "Link to this definition")

Delete a stored model definition.

Parameters:

**model\_definition\_id** ( _str_) – unique ID of the stored model definition

Returns:

status (“SUCCESS” or “FAILED”)

Return type:

str

**Example:**

```
client.model_definitions.delete(model_definition_id)

```

download( _model\_definition\_id_, _filename=None_, _rev\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.download) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.download "Link to this definition")

Download the content of a model definition asset.

Parameters:

- **model\_definition\_id** ( _str_) – unique ID of the model definition asset to be downloaded

- **filename** ( _str_) – filename to be used for the downloaded file

- **rev\_id** ( _str_ _,_ _optional_) – revision ID


Returns:

path to the downloaded asset content

Return type:

str

**Example:**

```
client.model_definitions.download(model_definition_id, "model_definition_file")

```

get\_details( _model\_definition\_id=None_, _limit=None_, _get\_all=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.get_details "Link to this definition")

Get metadata of a stored model definition. If no model\_definition\_id is passed,
details for all model definitions are returned.

Parameters:

- **model\_definition\_id** ( _str_ _,_ _optional_) – unique ID of the model definition

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

metadata of model definition

Return type:

dict (if model\_definition\_id is not None)

**Example:**

get\_href( _model\_definition\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.get_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.get_href "Link to this definition")

Get the href of a stored model definition.

Parameters:

**model\_definition\_details** ( _dict_) – details of the stored model definition

Returns:

href of the stored model definition

Return type:

str

**Example:**

```
model_definition_id = client.model_definitions.get_href(model_definition_details)

```

get\_id( _model\_definition\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.get_id "Link to this definition")

Get the unique ID of a stored model definition asset.

Parameters:

**model\_definition\_details** ( _dict_) – metadata of the stored model definition asset

Returns:

unique ID of the stored model definition asset

Return type:

str

**Example:**

```
asset_id = client.model_definition.get_id(asset_details)

```

get\_revision\_details( _model\_definition\_id=None_, _rev\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.get_revision_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.get_revision_details "Link to this definition")

Get metadata of a model definition.

Parameters:

- **model\_definition\_id** ( _str_) – ID of the model definition

- **rev\_id** ( _str_ _,_ _optional_) – ID of the revision. If this parameter is not provided, it returns the latest revision. If there is no latest revision, it returns an error.


Returns:

metadata of the stored model definition

Return type:

dict

**Example:**

```
script_details = client.model_definitions.get_revision_details(model_definition_id, rev_id)

```

get\_uid( _model\_definition\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.get_uid) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.get_uid "Link to this definition")

Get the UID of the stored model.

_Deprecated:_ Use `get_id(model_definition_details)` instead.

Parameters:

**model\_definition\_details** ( _dict_) – details of the stored model definition

Returns:

UID of the stored model definition

Return type:

str

**Example:**

```
model_definition_uid = client.model_definitions.get_uid(model_definition_details)

```

list( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.list "Link to this definition")

Return the stored model definition assets in a table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records

Returns:

pandas.DataFrame with listed model definitions

Return type:

pandas.DataFrame

**Example:**

```
client.model_definitions.list()

```

list\_revisions( _model\_definition\_id=None_, _limit=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.list_revisions) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.list_revisions "Link to this definition")

Return the stored model definition assets in a table format.

Parameters:

- **model\_definition\_id** ( _str_) – unique ID of the model definition

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

pandas.DataFrame with listed model definitions

Return type:

pandas.DataFrame

**Example:**

```
client.model_definitions.list_revisions()

```

store( _model\_definition_, _meta\_props_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.store "Link to this definition")

Create a model definition.

Parameters:

- **meta\_props** ( _dict_) –

metadata of the model definition configuration. To see available meta names, use:





```
client.model_definitions.ConfigurationMetaNames.get()

```

- **model\_definition** ( _str_) – path to the content file to be uploaded


Returns:

metadata of the created model definition

Return type:

dict

**Example:**

```
client.model_definitions.store(model_definition, meta_props)

```

update( _model\_definition\_id_, _meta\_props=None_, _file\_path=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/model_definition.html#ModelDefinition.update) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ModelDefinition.update "Link to this definition")

Update the model definition with metadata, attachment, or both.

Parameters:

- **model\_definition\_id** ( _str_) – ID of the model definition

- **meta\_props** ( _dict_) – metadata of the model definition configuration to be updated

- **file\_path** ( _str_ _,_ _optional_) – path to the content file to be uploaded


Returns:

updated metadata of the model definition

Return type:

dict

**Example:**

```
model_definition_details = client.model_definition.update(model_definition_id, meta_props, file_path)

```

_class_ metanames.ModelDefinitionMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#ModelDefinitionMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.ModelDefinitionMetaNames "Link to this definition")

Set of MetaNames for Model Definition.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| NAME | str | Y |  | `my_model_definition` |
| DESCRIPTION | str | N |  | `my model_definition` |
| PLATFORM | dict | Y | `{'name(required)': 'string', 'versions(required)': ['versions']}` | `{'name': 'python', 'versions': ['3.10']}` |
| VERSION | str | Y |  | `1.0` |
| COMMAND | str | N |  | `python3 convolutional_network.py` |
| CUSTOM | dict | N |  | `{'field1': 'value1'}` |
| SPACE\_UID | str | N |  | `3c1ce536-20dc-426e-aac7-7284cf3befc6` |

## Package extensions [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#package-extensions "Link to this heading")

_class_ client.PkgExtn( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/pkg_extn.html#PkgExtn) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.PkgExtn "Link to this definition")

Store and manage software Packages Extension specs.

ConfigurationMetaNames _=<ibm\_watsonx\_ai.metanames.PkgExtnMetaNamesobject>_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.PkgExtn.ConfigurationMetaNames "Link to this definition")

MetaNames for Package Extensions creation.

delete( _pkg\_extn\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/pkg_extn.html#PkgExtn.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.PkgExtn.delete "Link to this definition")

Delete a package extension.

Parameters:

**pkg\_extn\_id** ( _str_) – unique ID of the package extension

Returns:

status (“SUCCESS” or “FAILED”) if deleted synchronously or dictionary with response

Return type:

str or dict

**Example:**

```
client.package_extensions.delete(pkg_extn_id)

```

download( _pkg\_extn\_id_, _filename_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/pkg_extn.html#PkgExtn.download) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.PkgExtn.download "Link to this definition")

Download a package extension.

Parameters:

- **pkg\_extn\_id** ( _str_) – unique ID of the package extension to be downloaded

- **filename** ( _str_) – filename to be used for the downloaded file


Returns:

path to the downloaded package extension content

Return type:

str

**Example:**

```
client.package_extensions.download(pkg_extn_id,"sample_conda.yml/custom_library.zip")

```

get\_details( _pkg\_extn\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/pkg_extn.html#PkgExtn.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.PkgExtn.get_details "Link to this definition")

Get package extensions details.

Parameters:

**pkg\_extn\_id** ( _str_) – unique ID of the package extension

Returns:

details of the package extension

Return type:

dict

**Example:**

```
pkg_extn_details = client.pkg_extn.get_details(pkg_extn_id)

```

_static_ get\_href( _pkg\_extn\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/pkg_extn.html#PkgExtn.get_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.PkgExtn.get_href "Link to this definition")

Get the URL of a stored package extension.

Parameters:

**pkg\_extn\_details** ( _dict_) – details of the package extension

Returns:

href of the package extension

Return type:

str

**Example:**

```
pkg_extn_details = client.package_extensions.get_details(pkg_extn_id)
pkg_extn_href = client.package_extensions.get_href(pkg_extn_details)

```

_static_ get\_id( _pkg\_extn\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/pkg_extn.html#PkgExtn.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.PkgExtn.get_id "Link to this definition")

Get the unique ID of a package extension.

Parameters:

**pkg\_extn\_details** ( _dict_) – details of the package extension

Returns:

unique ID of the package extension

Return type:

str

**Example:**

```
asset_id = client.package_extensions.get_id(pkg_extn_details)

```

get\_id\_by\_name( _pkg\_extn\_name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/pkg_extn.html#PkgExtn.get_id_by_name) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.PkgExtn.get_id_by_name "Link to this definition")

Get the ID of a package extension.

Parameters:

**pkg\_extn\_name** ( _str_) – name of the package extension

Returns:

unique ID of the package extension

Return type:

str

**Example:**

```
asset_id = client.package_extensions.get_id_by_name(pkg_extn_name)

```

list() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/pkg_extn.html#PkgExtn.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.PkgExtn.list "Link to this definition")

List the package extensions in a table format.

Returns:

pandas.DataFrame with listed package extensions

Return type:

pandas.DataFrame

```
client.package_extensions.list()

```

store( _meta\_props_, _file\_path_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/pkg_extn.html#PkgExtn.store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.PkgExtn.store "Link to this definition")

Create a package extension.

Parameters:

- **meta\_props** ( _dict_) –

metadata of the package extension. To see available meta names, use:





```
client.package_extensions.ConfigurationMetaNames.get()

```

- **file\_path** ( _str_) – path to the file to be uploaded as a package extension


Returns:

metadata of the package extension

Return type:

dict

**Example:**

```
meta_props = {
    client.package_extensions.ConfigurationMetaNames.NAME: "skl_pipeline_heart_problem_prediction",
    client.package_extensions.ConfigurationMetaNames.DESCRIPTION: "description scikit-learn_0.20",
    client.package_extensions.ConfigurationMetaNames.TYPE: "conda_yml"
}

pkg_extn_details = client.package_extensions.store(meta_props=meta_props, file_path="/path/to/file")

```

_class_ metanames.PkgExtnMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#PkgExtnMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.PkgExtnMetaNames "Link to this definition")

Set of MetaNames for Package Extensions Specs.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| NAME | str | Y | `Python 3.10 with pre-installed ML package` |
| DESCRIPTION | str | N | `my_description` |
| TYPE | str | Y | `conda_yml/custom_library` |

## Parameter Sets [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#parameter-sets "Link to this heading")

_class_ client.ParameterSets( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/parameter_sets.html#ParameterSets) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ParameterSets "Link to this definition")

Store and manage parameter sets.

ConfigurationMetaNames _=<ibm\_watsonx\_ai.metanames.ParameterSetsMetaNamesobject>_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ParameterSets.ConfigurationMetaNames "Link to this definition")

MetaNames for Parameter Sets creation.

create( _meta\_props_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/parameter_sets.html#ParameterSets.create) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ParameterSets.create "Link to this definition")

Create a parameter set.

Parameters:

**meta\_props** ( _dict_) –

metadata of the space configuration. To see available meta names, use:

```
client.parameter_sets.ConfigurationMetaNames.get()

```

Returns:

metadata of the stored parameter set

Return type:

dict

**Example:**

```
meta_props = {
    client.parameter_sets.ConfigurationMetaNames.NAME: "Example name",
    client.parameter_sets.ConfigurationMetaNames.DESCRIPTION: "Example description",
    client.parameter_sets.ConfigurationMetaNames.PARAMETERS: [\
        {\
            "name": "string",\
            "description": "string",\
            "prompt": "string",\
            "type": "string",\
            "subtype": "string",\
            "value": "string",\
            "valid_values": [\
                "string"\
            ]\
        }\
    ],
    client.parameter_sets.ConfigurationMetaNames.VALUE_SETS: [\
        {\
            "name": "string",\
            "values": [\
                {\
                    "name": "string",\
                    "value": "string"\
                }\
            ]\
        }\
    ]
}

parameter_sets_details = client.parameter_sets.create(meta_props)

```

delete( _parameter\_set\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/parameter_sets.html#ParameterSets.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ParameterSets.delete "Link to this definition")

Delete a parameter set.

Parameters:

**parameter\_set\_id** ( _str_) – unique ID of the parameter set

Returns:

status (“SUCCESS” or “FAILED”)

Return type:

str

**Example:**

```
client.parameter_sets.delete(parameter_set_id)

```

get\_details( _parameter\_set\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/parameter_sets.html#ParameterSets.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ParameterSets.get_details "Link to this definition")

Get parameter set details. If no parameter\_sets\_id is passed, details for all parameter sets
are returned.

Parameters:

**parameter\_set\_id** ( _str_ _,_ _optional_) – ID of the software specification

Returns:

metadata of the stored parameter set(s)

Return type:

- **dict** \- if parameter\_set\_id is not None

- **{“parameter\_sets”: \[dict\]}** \- if parameter\_set\_id is None


**Examples**

If parameter\_set\_id is None:

```
parameter_sets_details = client.parameter_sets.get_details()

```

If parameter\_set\_id is given:

```
parameter_sets_details = client.parameter_sets.get_details(parameter_set_id)

```

get\_id\_by\_name( _parameter\_set\_name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/parameter_sets.html#ParameterSets.get_id_by_name) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ParameterSets.get_id_by_name "Link to this definition")

Get the unique ID of a parameter set.

Parameters:

**parameter\_set\_name** ( _str_) – name of the parameter set

Returns:

unique ID of the parameter set

Return type:

str

**Example:**

```
asset_id = client.parameter_sets.get_id_by_name(parameter_set_name)

```

list( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/parameter_sets.html#ParameterSets.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ParameterSets.list "Link to this definition")

List parameter sets in a table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records

Returns:

pandas.DataFrame with listed parameter sets

Return type:

pandas.DataFrame

**Example:**

```
client.parameter_sets.list()

```

update( _parameter\_set\_id_, _new\_data_, _file\_path_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/parameter_sets.html#ParameterSets.update) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ParameterSets.update "Link to this definition")

Update parameter sets.

Parameters:

- **parameter\_set\_id** ( _str_) – unique ID of the parameter sets

- **new\_data** ( _str_ _,_ _list_) – new data for parameters

- **file\_path** ( _str_) – path to update


Returns:

metadata of the updated parameter sets

Return type:

dict

**Example for description**

```
new_description_data = "New description"
parameter_set_details = client.parameter_sets.update(parameter_set_id, new_description_data, "description")

```

**Example for parameters**

```
new_parameters_data = [\
    {\
        "name": "string",\
        "description": "new_description",\
        "prompt": "new_string",\
        "type": "new_string",\
        "subtype": "new_string",\
        "value": "new_string",\
        "valid_values": [\
            "new_string"\
        ]\
    }\
]
parameter_set_details = client.parameter_sets.update(parameter_set_id, new_parameters_data, "parameters")

```

**Example for value\_sets**

```
new_value_sets_data = [\
    {\
        "name": "string",\
        "values": [\
            {\
                "name": "string",\
                "value": "new_string"\
            }\
        ]\
    }\
]
parameter_set_details = client.parameter_sets.update_value_sets(parameter_set_id, new_value_sets_data, "value_sets")

```

_class_ metanames.ParameterSetsMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#ParameterSetsMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.ParameterSetsMetaNames "Link to this definition")

Set of MetaNames for Parameter Sets metanames.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| NAME | str | Y | `sample name` |
| DESCRIPTION | str | N | `sample description` |
| PARAMETERS | list | Y | `[{'name': 'string', 'description': 'string', 'prompt': 'string', 'type': 'string', 'subtype': 'string', 'value': 'string', 'valid_values': ['string']}]` |
| VALUE\_SETS | list | N | `[{'name': 'string', 'values': [{'name': 'string', 'value': 'string'}]}]` |

## Repository [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#repository "Link to this heading")

_class_ client.Repository( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository "Link to this definition")

Store and manage models, functions, spaces, pipelines, and experiments
using the Watson Machine Learning Repository.

To view ModelMetaNames, use:

```
client.repository.ModelMetaNames.show()

```

To view ExperimentMetaNames, use:

```
client.repository.ExperimentMetaNames.show()

```

To view FunctionMetaNames, use:

```
client.repository.FunctionMetaNames.show()

```

To view PipelineMetaNames, use:

```
client.repository.PipelineMetaNames.show()

```

To view AIServiceMetaNames, use:

```
client.repository.AIServiceMetaNames.show()

```

_class_ ModelAssetTypes( _DO\_DOCPLEX\_20\_1='do-docplex\_20.1'_, _DO\_OPL\_20\_1='do-opl\_20.1'_, _DO\_CPLEX\_20\_1='do-cplex\_20.1'_, _DO\_CPO\_20\_1='do-cpo\_20.1'_, _DO\_DOCPLEX\_22\_1='do-docplex\_22.1'_, _DO\_OPL\_22\_1='do-opl\_22.1'_, _DO\_CPLEX\_22\_1='do-cplex\_22.1'_, _DO\_CPO\_22\_1='do-cpo\_22.1'_, _WML\_HYBRID\_0\_1='wml-hybrid\_0.1'_, _PMML\_4\_2\_1='pmml\_4.2.1'_, _PYTORCH\_ONNX\_1\_12='pytorch-onnx\_1.12'_, _PYTORCH\_ONNX\_RT22\_2='pytorch-onnx\_rt22.2'_, _PYTORCH\_ONNX\_2\_0='pytorch-onnx\_2.0'_, _PYTORCH\_ONNX\_RT23\_1='pytorch-onnx\_rt23.1'_, _SCIKIT\_LEARN\_1\_1='scikit-learn\_1.1'_, _MLLIB\_3\_3='mllib\_3.3'_, _SPSS\_MODELER\_17\_1='spss-modeler\_17.1'_, _SPSS\_MODELER\_18\_1='spss-modeler\_18.1'_, _SPSS\_MODELER\_18\_2='spss-modeler\_18.2'_, _TENSORFLOW\_2\_9='tensorflow\_2.9'_, _TENSORFLOW\_RT22\_2='tensorflow\_rt22.2'_, _TENSORFLOW\_2\_12='tensorflow\_2.12'_, _TENSORFLOW\_RT23\_1='tensorflow\_rt23.1'_, _XGBOOST\_1\_6='xgboost\_1.6'_, _PROMPT\_TUNE\_1\_0='prompt\_tune\_1.0'_, _CUSTOM\_FOUNDATION\_MODEL\_1\_0='custom\_foundation\_model\_1.0'_, _CURATED\_FOUNDATION\_MODEL\_1\_0='curated\_foundation\_model\_1.0'_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.ModelAssetTypes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.ModelAssetTypes "Link to this definition")

Data class with supported model asset types.

create\_ai\_service\_revision( _ai\_service\_id_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.create_ai_service_revision) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.create_ai_service_revision "Link to this definition")

Create a new AI service revision.

Parameters:

**ai\_service\_id** ( _str_) – unique ID of the AI service

Returns:

revised metadata of the stored AI service

Return type:

dict

**Example:**

```
client.repository.create_ai_service_revision(ai_service_id)

```

create\_experiment\_revision( _experiment\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.create_experiment_revision) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.create_experiment_revision "Link to this definition")

Create a new experiment revision.

Parameters:

**experiment\_id** ( _str_) – unique ID of the stored experiment

Returns:

new revision details of the stored experiment

Return type:

dict

**Example:**

```
experiment_revision_artifact = client.repository.create_experiment_revision(experiment_id)

```

create\_function\_revision( _function\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.create_function_revision) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.create_function_revision "Link to this definition")

Create a new function revision.

Parameters:

**function\_id** ( _str_) – unique ID of the function

Returns:

revised metadata of the stored function

Return type:

dict

**Example:**

```
client.repository.create_function_revision(pipeline_id)

```

create\_model\_revision( _model\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.create_model_revision) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.create_model_revision "Link to this definition")

Create a revision for a given model ID.

Parameters:

**model\_id** ( _str_) – ID of the stored model

Returns:

revised metadata of the stored model

Return type:

dict

**Example:**

```
model_details = client.repository.create_model_revision(model_id)

```

create\_pipeline\_revision( _pipeline\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.create_pipeline_revision) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.create_pipeline_revision "Link to this definition")

Create a new pipeline revision.

Parameters:

**pipeline\_id** ( _str_) – unique ID of the pipeline

Returns:

details of the pipeline revision

Return type:

dict

**Example:**

```
client.repository.create_pipeline_revision(pipeline_id)

```

create\_revision( _artifact\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.create_revision) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.create_revision "Link to this definition")

Create a revision for passed artifact\_id.

Parameters:

**artifact\_id** ( _str_) – unique ID of a stored model, experiment, function, or pipelines

Returns:

artifact new revision metadata

Return type:

dict

**Example:**

```
details = client.repository.create_revision(artifact_id)

```

delete( _artifact\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.delete "Link to this definition")

Delete a model, experiment, pipeline, function, or AI service from the repository.

Parameters:

**artifact\_id** ( _str_) – unique ID of the stored model, experiment, function, pipeline, or AI service

Returns:

status “SUCCESS” if deletion is successful

Return type:

Literal\[“SUCCESS”\]

**Example:**

```
client.repository.delete(artifact_id)

```

download( _artifact\_id=None_, _filename='downloaded\_artifact.tar.gz'_, _rev\_id=None_, _format=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.download) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.download "Link to this definition")

Download the configuration file for an artifact with the specified ID.

Parameters:

- **artifact\_id** ( _str_) – unique ID of the model or function

- **filename** ( _str_ _,_ _optional_) – name of the file to which the artifact content will be downloaded

- **rev\_id** ( _str_ _,_ _optional_) – revision ID

- **format** ( _str_ _,_ _optional_) – format of the content, applicable for models


Returns:

path to the downloaded artifact content

Return type:

str

**Examples**

```
client.repository.download(model_id, 'my_model.tar.gz')
client.repository.download(model_id, 'my_model.json') # if original model was saved as json, works only for xgboost 1.3

```

get\_ai\_service\_details( _ai\_service\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_, _spec\_state=None_, _ai\_service\_name=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_ai_service_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_ai_service_details "Link to this definition")

Get the metadata of AI service(s). If neither AI service ID nor AI service name is specified,
all AI service metadata is returned.
If only AI service name is specified, metadata of AI services with the name is returned (if any).

Parameters:

- **ai\_service\_id** ( _str_ _,_ _optional_) – ID of the AI service

- **limit** ( _int_ _\|_ _None_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator, defaults to False

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks, defaults to False

- **spec\_state** ( _SpecStates_ _\|_ _None_ _,_ _optional_) – software specification state, can be used only when ai\_service\_id is None

- **ai\_service\_name** ( _str_ _,_ _optional_) – name of the AI service, can be used only when ai\_service\_id is None


Returns:

metadata of the AI service

Return type:

dict (if ID is not None) or {“resources”: \[dict\]} (if ID is None)

Note

In the current implementation setting, spec\_state=True might break the set limit and return less records than stated in the set limit.

**Examples:**

```
ai_service_details = client.repository.get_ai_service_details(ai_service_id)
ai_service_details = client.repository.get_ai_service_details(ai_service_name)
ai_service_details = client.repository.get_ai_service_details()
ai_service_details = client.repository.get_ai_service_details(limit=100)
ai_service_details = client.repository.get_ai_service_details(limit=100, get_all=True)
ai_service_details = []
for entry in client.repository.get_ai_service_details(limit=100, asynchronous=True, get_all=True):
    ai_service_details.extend(entry)

```

_static_ get\_ai\_service\_id( _ai\_service\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_ai_service_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_ai_service_id "Link to this definition")

Get the ID of a stored AI service.

Parameters:

**ai\_service\_details** ( _dict_) – metadata of the stored AI service

Returns:

ID of the stored AI service

Return type:

str

**Example:**

```
ai_service_details = client.repository.get_ai_service_details(ai_service_id)
ai_service_id = client.repository.get_ai_service_id(ai_service_details)

```

get\_ai\_service\_revision\_details( _ai\_service\_id_, _rev\_id_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_ai_service_revision_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_ai_service_revision_details "Link to this definition")

Get the metadata of a specific revision of a stored AI service.

Parameters:

- **ai\_service\_id** ( _str_) – definition of the stored AI service

- **rev\_id** ( _str_) – unique ID of the AI service revision


Returns:

metadata of the stored AI service revision

Return type:

dict

**Example:**

```
ai_service_revision_details = client.repository.get_ai_service_revision_details(ai_service_id, rev_id)

```

get\_details( _artifact\_id=None_, _spec\_state=None_, _artifact\_name=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_details "Link to this definition")

Get metadata of stored artifacts. If artifact\_id and artifact\_name are not specified,
the metadata of all models, experiments, functions, pipelines, and ai services is returned.
If only artifact\_name is specified, metadata of all artifacts with the name is returned.

Parameters:

- **artifact\_id** ( _str_ _,_ _optional_) – unique ID of the stored model, experiment, function, or pipeline

- **spec\_state** ( _SpecStates_ _,_ _optional_) – software specification state, can be used only when artifact\_id is None

- **artifact\_name** ( _str_ _,_ _optional_) – name of the stored model, experiment, function, pipeline, or ai service
can be used only when artifact\_id is None


Returns:

metadata of the stored artifact(s)

Return type:

- dict (if artifact\_id is not None)

- {“models”: dict, “experiments”: dict, “pipeline”: dict, “functions”: dict, “ai\_service”: dict} (if artifact\_id is None)


**Examples**

```
details = client.repository.get_details(artifact_id)
details = client.repository.get_details(artifact_name='Sample_model')
details = client.repository.get_details()

```

Example of getting all repository assets with deprecated software specifications:

```
from ibm_watsonx_ai.lifecycle import SpecStates

details = client.repository.get_details(spec_state=SpecStates.DEPRECATED)

```

get\_experiment\_details( _experiment\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_, _experiment\_name=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_experiment_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_experiment_details "Link to this definition")

Get metadata of the experiment(s). If neither experiment ID nor experiment name is specified,
all experiment metadata is returned.
If only experiment name is specified, metadata of experiments with the name is returned (if any).

Parameters:

- **experiment\_id** ( _str_ _,_ _optional_) – ID of the experiment

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks

- **experiment\_name** ( _str_ _,_ _optional_) – name of the experiment, can be used only when experiment\_id is None


Returns:

experiment metadata

Return type:

dict (if ID is not None) or {“resources”: \[dict\]} (if ID is None)

**Example:**

```
experiment_details = client.repository.get_experiment_details(experiment_id)
experiment_details = client.repository.get_experiment_details(experiment_name='Sample_experiment')
experiment_details = client.repository.get_experiment_details()
experiment_details = client.repository.get_experiment_details(limit=100)
experiment_details = client.repository.get_experiment_details(limit=100, get_all=True)
experiment_details = []
for entry in client.repository.get_experiment_details(limit=100, asynchronous=True, get_all=True):
    experiment_details.extend(entry)

```

_static_ get\_experiment\_href( _experiment\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_experiment_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_experiment_href "Link to this definition")

Get the href of a stored experiment.

Parameters:

**experiment\_details** ( _dict_) – metadata of the stored experiment

Returns:

href of the stored experiment

Return type:

str

**Example:**

```
experiment_details = client.repository.get_experiment_details(experiment_id)
experiment_href = client.repository.get_experiment_href(experiment_details)

```

_static_ get\_experiment\_id( _experiment\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_experiment_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_experiment_id "Link to this definition")

Get the unique ID of a stored experiment.

Parameters:

**experiment\_details** ( _dict_) – metadata of the stored experiment

Returns:

unique ID of the stored experiment

Return type:

str

**Example:**

```
experiment_details = client.repository.get_experiment_details(experiment_id)
experiment_id = client.repository.get_experiment_id(experiment_details)

```

get\_experiment\_revision\_details( _experiment\_id_, _rev\_id_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_experiment_revision_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_experiment_revision_details "Link to this definition")

Get metadata of a stored experiments revisions.

Parameters:

- **experiment\_id** ( _str_) – ID of the stored experiment

- **rev\_id** ( _str_) – rev\_id number of the stored experiment


Returns:

revision metadata of the stored experiment

Return type:

dict

Example:

```
experiment_details = client.repository.get_experiment_revision_details(experiment_id, rev_id)

```

get\_function\_details( _function\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_, _spec\_state=None_, _function\_name=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_function_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_function_details "Link to this definition")

Get metadata of function(s). If neither function ID nor function name is specified,
the metadata of all functions is returned.
If only function name is specified, metadata of functions with the name is returned (if any).

Parameters:

- **function\_id** – ID of the function

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks

- **spec\_state** ( _SpecStates_ _,_ _optional_) – software specification state, can be used only when function\_id is None

- **function\_name** ( _str_ _,_ _optional_) – name of the function, can be used only when function\_id is None


Type:

str, optional

Returns:

metadata of the function

Return type:

dict (if ID is not None) or {“resources”: \[dict\]} (if ID is None)

Note

In current implementation setting spec\_state=True may break set limit,
returning less records than stated by set limit.

**Examples**

```
function_details = client.repository.get_function_details(function_id)
function_details = client.repository.get_function_details(function_name='Sample_function')
function_details = client.repository.get_function_details()
function_details = client.repository.get_function_details(limit=100)
function_details = client.repository.get_function_details(limit=100, get_all=True)
function_details = []
for entry in client.repository.get_function_details(limit=100, asynchronous=True, get_all=True):
    function_details.extend(entry)

```

_static_ get\_function\_href( _function\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_function_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_function_href "Link to this definition")

Get the URL of a stored function.

Parameters:

**function\_details** ( _dict_) – details of the stored function

Returns:

href of the stored function

Return type:

str

**Example:**

```
function_details = client.repository.get_function_details(function_id)
function_url = client.repository.get_function_href(function_details)

```

_static_ get\_function\_id( _function\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_function_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_function_id "Link to this definition")

Get ID of stored function.

Parameters:

**function\_details** ( _dict_) – metadata of the stored function

Returns:

ID of stored function

Return type:

str

**Example:**

```
function_details = client.repository.get_function_details(function_id)
function_id = client.repository.get_function_id(function_details)

```

get\_function\_revision\_details( _function\_id_, _rev\_id_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_function_revision_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_function_revision_details "Link to this definition")

Get metadata of a specific revision of a stored function.

Parameters:

- **function\_id** ( _str_) – definition of the stored function

- **rev\_id** ( _str_) – unique ID of the function revision


Returns:

stored function revision metadata

Return type:

dict

**Example:**

```
function_revision_details = client.repository.get_function_revision_details(function_id, rev_id)

```

get\_id\_by\_name( _artifact\_name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_id_by_name) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_id_by_name "Link to this definition")

Get the ID of a stored artifact by name.

Parameters:

**artifact\_name** ( _str_) – name of the stored artifact

Returns:

ID of the stored artifact if exactly one with the ‘artifact\_name’ exists. Otherwise, raise an error.

Return type:

str

**Example:**

```
artifact_id = client.repository.get_id_by_name(artifact_name)

```

get\_model\_details( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_, _spec\_state=None_, _model\_name=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_model_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_model_details "Link to this definition")

Get metadata of stored models. If neither model ID nor model name is specified,
the metadata of all models is returned.
If only model name is specified, metadata of models with the name is returned (if any).

Parameters:

- **model\_id** ( _str_ _,_ _optional_) – ID of the stored model, definition, or pipeline

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks

- **spec\_state** ( _SpecStates_ _,_ _optional_) – software specification state, can be used only when model\_id is None

- **model\_name** ( _str_ _,_ _optional_) – name of the stored model, definition, or pipeline, can be used only when model\_id is None


Returns:

metadata of the stored model(s)

Return type:

dict (if ID is not None) or {“resources”: \[dict\]} (if ID is None)

Note

In current implementation setting spec\_state=True may break set limit,
returning less records than stated by set limit.

**Example:**

```
model_details = client.repository.get_model_details(model_id)
models_details = client.repository.get_model_details(model_name='Sample_model')
models_details = client.repository.get_model_details()
models_details = client.repository.get_model_details(limit=100)
models_details = client.repository.get_model_details(limit=100, get_all=True)
models_details = []
for entry in client.repository.get_model_details(limit=100, asynchronous=True, get_all=True):
    models_details.extend(entry)

```

_static_ get\_model\_href( _model\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_model_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_model_href "Link to this definition")

Get the URL of a stored model.

Parameters:

**model\_details** ( _dict_) – details of the stored model

Returns:

URL of the stored model

Return type:

str

**Example:**

```
model_url = client.repository.get_model_href(model_details)

```

_static_ get\_model\_id( _model\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_model_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_model_id "Link to this definition")

Get the ID of a stored model.

Parameters:

**model\_details** ( _dict_) – details of the stored model

Returns:

ID of the stored model

Return type:

str

**Example:**

```
model_id = client.repository.get_model_id(model_details)

```

get\_model\_revision\_details( _model\_id=None_, _rev\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_model_revision_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_model_revision_details "Link to this definition")

Get metadata of a stored model’s specific revision.

Parameters:

- **model\_id** ( _str_) – ID of the stored model, definition, or pipeline

- **rev\_id** ( _str_) – unique ID of the stored model revision


Returns:

metadata of the stored model(s)

Return type:

dict

**Example:**

```
model_details = client.repository.get_model_revision_details(model_id, rev_id)

```

get\_pipeline\_details( _pipeline\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_, _pipeline\_name=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_pipeline_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_pipeline_details "Link to this definition")

Get metadata of stored pipeline(s). If neither pipeline ID nor pipeline name is specified,
the metadata of all pipelines is returned.
If only pipeline name is specified, metadata of pipelines with the name is returned (if any).

Parameters:

- **pipeline\_id** ( _str_ _,_ _optional_) – ID of the pipeline

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks

- **pipeline\_name** ( _str_ _,_ _optional_) – name of the pipeline, can be used only when pipeline\_id is None


Returns:

metadata of pipeline(s)

Return type:

dict (if ID is not None) or {“resources”: \[dict\]} (if ID is None)

**Example:**

```
pipeline_details = client.repository.get_pipeline_details(pipeline_id)
pipeline_details = client.repository.get_pipeline_details(pipeline_name='Sample_pipeline')
pipeline_details = client.repository.get_pipeline_details()
pipeline_details = client.repository.get_pipeline_details(limit=100)
pipeline_details = client.repository.get_pipeline_details(limit=100, get_all=True)
pipeline_details = []
for entry in client.repository.get_pipeline_details(limit=100, asynchronous=True, get_all=True):
    pipeline_details.extend(entry)

```

_static_ get\_pipeline\_href( _pipeline\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_pipeline_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_pipeline_href "Link to this definition")

Get the href from pipeline details.

Parameters:

**pipeline\_details** ( _dict_) – metadata of the stored pipeline

Returns:

href of the pipeline

Return type:

str

**Example:**

```
pipeline_details = client.repository.get_pipeline_details(pipeline_id)
pipeline_href = client.repository.get_pipeline_href(pipeline_details)

```

_static_ get\_pipeline\_id( _pipeline\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_pipeline_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_pipeline_id "Link to this definition")

Get the pipeline ID from pipeline details.

Parameters:

**pipeline\_details** ( _dict_) – metadata of the stored pipeline

Returns:

unique ID of the pipeline

Return type:

str

**Example:**

```
pipeline_id = client.repository.get_pipeline_id(pipeline_details)

```

get\_pipeline\_revision\_details( _pipeline\_id=None_, _rev\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.get_pipeline_revision_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.get_pipeline_revision_details "Link to this definition")

Get metadata of a pipeline revision.

Parameters:

- **pipeline\_id** ( _str_) – ID of the stored pipeline

- **rev\_id** ( _str_) – revision ID of the stored pipeline


Returns:

revised metadata of the stored pipeline

Return type:

dict

**Example:**

```
pipeline_details = client.repository.get_pipeline_revision_details(pipeline_id, rev_id)

```

Note

rev\_id parameter is not applicable in Cloud platform.

list( _framework\_filter=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.list "Link to this definition")

Get and list stored models, pipelines, functions, experiments, and AI services in a table/DataFrame format.

Parameters:

**framework\_filter** ( _str_ _,_ _optional_) – get only the frameworks with the desired names

Returns:

DataFrame with listed names and IDs of stored models

Return type:

pandas.DataFrame

**Example:**

```
client.repository.list()
client.repository.list(framework_filter='prompt_tune')

```

list\_ai\_service\_revisions( _ai\_service\_id_, _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.list_ai_service_revisions) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.list_ai_service_revisions "Link to this definition")

Print all revisions for a given AI service ID in a table format.

Parameters:

- **ai\_service\_id** ( _str_) – unique ID of the stored AI service

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

pandas.DataFrame with listed revisions

Return type:

pandas.DataFrame

**Example:**

```
client.repository.list_ai_service_revisions(ai_service_id)

```

list\_ai\_services( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.list_ai_services) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.list_ai_services "Link to this definition")

Return stored AI services in a table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records

Returns:

pandas.DataFrame with listed AI services

Return type:

pandas.DataFrame

**Example:**

```
client.repository.list_ai_services()

```

list\_experiments( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.list_experiments) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.list_experiments "Link to this definition")

List stored experiments in a table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records

Returns:

pandas.DataFrame with listed experiments

Return type:

pandas.DataFrame

**Example:**

```
client.repository.list_experiments()

```

list\_experiments\_revisions( _experiment\_id=None_, _limit=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.list_experiments_revisions) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.list_experiments_revisions "Link to this definition")

Print all revisions for a given experiment ID in a table format.

Parameters:

- **experiment\_id** ( _str_) – unique ID of the stored experiment

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

pandas.DataFrame with listed revisions

Return type:

pandas.DataFrame

**Example:**

```
client.repository.list_experiments_revisions(experiment_id)

```

list\_functions( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.list_functions) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.list_functions "Link to this definition")

Return stored functions in a table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records

Returns:

pandas.DataFrame with listed functions

Return type:

pandas.DataFrame

**Example:**

```
client.repository.list_functions()

```

list\_functions\_revisions( _function\_id=None_, _limit=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.list_functions_revisions) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.list_functions_revisions "Link to this definition")

Print all revisions for a given function ID in a table format.

Parameters:

- **function\_id** ( _str_) – unique ID of the stored function

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

pandas.DataFrame with listed revisions

Return type:

pandas.DataFrame

**Example:**

```
client.repository.list_functions_revisions(function_id)

```

list\_models( _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.list_models) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.list_models "Link to this definition")

List stored models in a table format.

Parameters:

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

pandas.DataFrame with listed models or generator if asynchronous is set to True

Return type:

pandas.DataFrame \| Generator

**Example:**

```
client.repository.list_models()
client.repository.list_models(limit=100)
client.repository.list_models(limit=100, get_all=True)
[entry for entry in client.repository.list_models(limit=100, asynchronous=True, get_all=True)]

```

list\_models\_revisions( _model\_id=None_, _limit=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.list_models_revisions) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.list_models_revisions "Link to this definition")

Print all revisions for the given model ID in a table format.

Parameters:

- **model\_id** ( _str_) – unique ID of the stored model

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

pandas.DataFrame with listed revisions

Return type:

pandas.DataFrame

**Example:**

```
client.repository.list_models_revisions(model_id)

```

list\_pipelines( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.list_pipelines) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.list_pipelines "Link to this definition")

List stored pipelines in a table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records

Returns:

pandas.DataFrame with listed pipelines

Return type:

pandas.DataFrame

**Example:**

```
client.repository.list_pipelines()

```

list\_pipelines\_revisions( _pipeline\_id=None_, _limit=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.list_pipelines_revisions) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.list_pipelines_revisions "Link to this definition")

List all revision for a given pipeline ID in a table format.

Parameters:

- **pipeline\_id** ( _str_) – unique ID of the stored pipeline

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

pandas.DataFrame with listed revisions

Return type:

pandas.DataFrame

**Example:**

```
client.repository.list_pipelines_revisions(pipeline_id)

```

load( _artifact\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.load) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.load "Link to this definition")

Load a model from the repository to object in a local environment.

Note

The use of the load() method is restricted and not permitted for AutoAI models.

Parameters:

**artifact\_id** ( _str_) – ID of the stored model

Returns:

trained model

Return type:

object

**Example**

```
model = client.repository.load(model_id)

```

promote\_model( _model\_id_, _source\_project\_id_, _target\_space\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.promote_model) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.promote_model "Link to this definition")

Promote a model from a project to space. Supported only for IBM Cloud Pak® for Data.

_Deprecated:_ Use client.spaces.promote(asset\_id, source\_project\_id, target\_space\_id) instead.

store\_ai\_service( _ai\_service_, _meta\_props_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.store_ai_service) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.store_ai_service "Link to this definition")

Create an AI service asset.

Note

Supported for IBM watsonx.ai for IBM Cloud and IBM watsonx.ai software with IBM Cloud Pak® for Data (version 5.1.1 and later).

You can use one of the following as an ai\_service:

- filepath to gz file

- generator function that takes no argument or arguments that all have primitive python default values, and returns a generate function.


Parameters:

- **ai\_service** ( _str_ _\|_ _Callable_) – path to a file with an archived AI service function’s content or a generator function (as described above)

- **meta\_props** ( _dict_) – metadata for storing an AI service asset. To see available meta names
use `client.repository.AIServiceMetaNames.show()`


Returns:

metadata of the stored AI service

Return type:

dict

**Examples:**

The most simple use of an AI service is:

```
documentation_request = {
    "application/json": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "query": {"type": "string"},
            "parameters": {
                "properties": {
                    "max_new_tokens": {"type": "integer"},
                    "top_p": {"type": "number"},
                },
                "required": ["max_new_tokens", "top_p"],
            },
        },
        "required": ["query"],
    }
}

documentation_response = {
    "application/json": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "query": {"type": "string"},
            "result": {"type": "string"}
        },
        "required": ["query", "result"],
    }
}

meta_props = {
    client.repository.AIServiceMetaNames.NAME: "AI service example",
    client.repository.AIServiceMetaNames.DESCRIPTION: "This is AI service function",
    client.repository.AIServiceMetaNames.SOFTWARE_SPEC_ID: "53dc4cf1-252f-424b-b52d-5cdd9814987f",
    client.repository.AIServiceMetaNames.REQUEST_DOCUMENTATION: request_documentation,
    client.repository.AIServiceMetaNames.RESPONSE_DOCUMENTATION: response_documentation
    }

def deployable_ai_service(context, params={"k1":"v1"}, **kwargs):

    # imports
    from ibm_watsonx_ai import Credentials
    from ibm_watsonx_ai.foundation_models import ModelInference

    task_token = context.generate_token()

    outer_context = context
    url = "https://us-south.ml.cloud.ibm.com"
    project_id = "53dc4cf1-252f-424b-b52d-5cdd9814987f"

    def generate(context):
        task_token = outer_context.generate_token()
        payload = context.get_json()

        model = ModelInference(
            model_id="google/flan-t5-xl",
            credentials=Credentials(
                            url=url,
                            token=task_token
                            ),
            project_id=project_id)

        response = model.generate_text(payload['query'])
        response_body = {'query': payload['query'],
                         'result': response}

        return {'body': response_body}

    return generate

stored_ai_service_details = client.repository.store_ai_service(deployable_ai_service, meta_props)

```

store\_experiment( _meta\_props_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.store_experiment) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.store_experiment "Link to this definition")

Create an experiment.

Parameters:

**meta\_props** ( _dict_) –

metadata of the experiment configuration. To see available meta names, use:

```
client.repository.ExperimentMetaNames.get()

```

Returns:

metadata of the stored experiment

Return type:

dict

**Example:**

```
metadata = {
    client.repository.ExperimentMetaNames.NAME: 'my_experiment',
    client.repository.ExperimentMetaNames.EVALUATION_METRICS: ['accuracy'],
    client.repository.ExperimentMetaNames.TRAINING_REFERENCES: [\
        {'pipeline': {'href': pipeline_href_1}},\
        {'pipeline': {'href':pipeline_href_2}}\
    ]
}
experiment_details = client.repository.store_experiment(meta_props=metadata)
experiment_href = client.repository.get_experiment_href(experiment_details)

```

store\_function( _function_, _meta\_props_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.store_function) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.store_function "Link to this definition")

Create a function.

As a ‘function’ may be used one of the following:

- filepath to gz file

- ‘score’ function reference, where the function is the function which will be deployed

- generator function, which takes no argument or arguments which all have primitive python default values
and as result return ‘score’ function


Parameters:

- **function** ( _str_ _or_ _function_) – path to file with archived function content or function (as described above)

- **meta\_props** ( _str_ _or_ _dict_) – meta data or name of the function, to see available meta names
use `client.repository.FunctionMetaNames.show()`


Returns:

stored function metadata

Return type:

dict

**Examples**

The most simple use is (using score function):

```
meta_props = {
    client.repository.FunctionMetaNames.NAME: "function",
    client.repository.FunctionMetaNames.DESCRIPTION: "This is ai function",
    client.repository.FunctionMetaNames.SOFTWARE_SPEC_UID: "53dc4cf1-252f-424b-b52d-5cdd9814987f"}

def score(payload):
    values = [[row[0]*row[1]] for row in payload['values']]
    return {'fields': ['multiplication'], 'values': values}

stored_function_details = client.repository.store_function(score, meta_props)

```

Other, more interesting example is using generator function.
In this situation it is possible to pass some variables:

```
creds = {...}

def gen_function(credentials=creds, x=2):
    def f(payload):
        values = [[row[0]*row[1]*x] for row in payload['values']]
        return {'fields': ['multiplication'], 'values': values}
    return f

stored_function_details = client.repository.store_function(gen_function, meta_props)

```

store\_model( _model=None_, _meta\_props=None_, _training\_data=None_, _training\_target=None_, _pipeline=None_, _feature\_names=None_, _label\_column\_names=None_, _subtrainingId=None_, _round\_number=None_, _experiment\_metadata=None_, _training\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.store_model) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.store_model "Link to this definition")

Create a model.

[Here](https://ibm.github.io/watsonx-ai-python-sdk/save_models.html#save-models) you can explore how to save external models in correct format.

Parameters:

- **model** ( _str_ _(_ _for filename_ _or_ _path_ _) or_ _object_ _(_ _corresponding to model type_ _)_) –

Can be one of following:


  - The train model object:


    > - scikit-learn
    >
    > - xgboost
    >
    > - spark (PipelineModel)

  - path to saved model in format:


    > - tensorflow / keras (.tar.gz)
    >
    > - pmml (.xml)
    >
    > - scikit-learn (.tar.gz)
    >
    > - spss (.str)
    >
    > - spark (.tar.gz)
    >
    > - xgboost (.tar.gz)

  - directory containing model file(s):


    > - scikit-learn
    >
    > - xgboost
    >
    > - tensorflow

  - unique ID of the trained model


- **meta\_props** ( _dict_ _,_ _optional_) –

metadata of the models configuration. To see available meta names, use:





```
client.repository.ModelMetaNames.get()

```

- **training\_data** ( _spark dataframe_ _,_ _pandas dataframe_ _,_ _numpy.ndarray_ _or_ _array_ _,_ _optional_) – Spark DataFrame supported for spark models. Pandas dataframe, numpy.ndarray or array
supported for scikit-learn models

- **training\_target** ( _array_ _,_ _optional_) – array with labels required for scikit-learn models

- **pipeline** ( _object_ _,_ _optional_) – pipeline required for spark mllib models

- **feature\_names** ( _numpy.ndarray_ _or_ _list_ _,_ _optional_) – feature names for the training data in case of Scikit-Learn/XGBoost models,
this is applicable only in the case where the training data is not of type - pandas.DataFrame

- **label\_column\_names** ( _numpy.ndarray_ _or_ _list_ _,_ _optional_) – label column names of the trained Scikit-Learn/XGBoost models

- **round\_number** ( _int_ _,_ _optional_) – round number of a Federated Learning experiment that has been configured to save
intermediate models, this applies when model is a training id

- **experiment\_metadata** ( _dict_ _,_ _optional_) – metadata retrieved from the experiment that created the model

- **training\_id** ( _str_ _,_ _optional_) – Run id of AutoAI or TuneExperiment experiment.


Returns:

metadata of the created model

Return type:

dict

Note

- For a keras model, model content is expected to contain a .h5 file and an archived version of it.

- feature\_names is an optional argument containing the feature names for the training data
in case of Scikit-Learn/XGBoost models. Valid types are numpy.ndarray and list.
This is applicable only in the case where the training data is not of type - pandas.DataFrame.

- If the training\_data is of type pandas.DataFrame and feature\_names are provided,
feature\_names are ignored.

- For INPUT\_DATA\_SCHEMA meta prop use list even when passing single input data schema. You can provide
multiple schemas as dictionaries inside a list.


**Examples**

```
stored_model_details = client.repository.store_model(model, name)

```

In more complicated cases you should create proper metadata, similar to this one:

```
sw_spec_id = client.software_specifications.get_id_by_name('scikit-learn_0.23-py3.7')

metadata = {
    client.repository.ModelMetaNames.NAME: 'customer satisfaction prediction model',
    client.repository.ModelMetaNames.SOFTWARE_SPEC_ID: sw_spec_id,
    client.repository.ModelMetaNames.TYPE: 'scikit-learn_0.23'
}

```

In case when you want to provide input data schema of the model, you can provide it as part of meta:

```
sw_spec_id = client.software_specifications.get_id_by_name('spss-modeler_18.1')

metadata = {
    client.repository.ModelMetaNames.NAME: 'customer satisfaction prediction model',
    client.repository.ModelMetaNames.SOFTWARE_SPEC_ID: sw_spec_id,
    client.repository.ModelMetaNames.TYPE: 'spss-modeler_18.1',
    client.repository.ModelMetaNames.INPUT_DATA_SCHEMA: [{'id': 'test',\
                                                          'type': 'list',\
                                                          'fields': [{'name': 'age', 'type': 'float'},\
                                                                     {'name': 'sex', 'type': 'float'},\
                                                                     {'name': 'fbs', 'type': 'float'},\
                                                                     {'name': 'restbp', 'type': 'float'}]\
                                                          },\
                                                          {'id': 'test2',\
                                                           'type': 'list',\
                                                           'fields': [{'name': 'age', 'type': 'float'},\
                                                                      {'name': 'sex', 'type': 'float'},\
                                                                      {'name': 'fbs', 'type': 'float'},\
                                                                      {'name': 'restbp', 'type': 'float'}]\
    }]
}

```

`store_model()` method used with a local tar.gz file that contains a model:

```
stored_model_details = client.repository.store_model(path_to_tar_gz, meta_props=metadata, training_data=None)

```

`store_model()` method used with a local directory that contains model files:

```
stored_model_details = client.repository.store_model(path_to_model_directory, meta_props=metadata, training_data=None)

```

`store_model()` method used with the ID of a trained model:

```
stored_model_details = client.repository.store_model(trained_model_id, meta_props=metadata, training_data=None)

```

`store_model()` method used with a pipeline that was generated by an AutoAI experiment:

```
metadata = {
    client.repository.ModelMetaNames.NAME: 'AutoAI prediction model stored from object'
}
stored_model_details = client.repository.store_model(pipeline_model, meta_props=metadata, experiment_metadata=experiment_metadata)

```

```
metadata = {
    client.repository.ModelMetaNames.NAME: 'AutoAI prediction Pipeline_1 model'
}
stored_model_details = client.repository.store_model(model="Pipeline_1", meta_props=metadata, training_id = training_id)

```

Example of storing a prompt tuned model:

```
stored_model_details = client.repository.store_model(training_id = prompt_tuning_run_id)

```

Example of storing a custom foundation model:

```
sw_spec_id = client.software_specifications.get_id_by_name('watsonx-cfm-caikit-1.0')

metadata = {
    client.repository.ModelMetaNames.NAME: 'custom FM asset',
    client.repository.ModelMetaNames.SOFTWARE_SPEC_ID: sw_spec_id,
    client.repository.ModelMetaNames.TYPE: client.repository.ModelAssetTypes.CUSTOM_FOUNDATION_MODEL_1_0
}
stored_model_details = client.repository.store_model(model='mistralai/Mistral-7B-Instruct-v0.2', meta_props=metadata)

```

store\_pipeline( _meta\_props_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.store_pipeline) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.store_pipeline "Link to this definition")

Create a pipeline.

Parameters:

**meta\_props** ( _dict_) –

metadata of the pipeline configuration. To see available meta names, use:

```
client.repository.PipelineMetaNames.get()

```

Returns:

stored pipeline metadata

Return type:

dict

**Example:**

```
metadata = {
    client.repository.PipelineMetaNames.NAME: 'my_training_definition',
    client.repository.PipelineMetaNames.DOCUMENT: {"doc_type":"pipeline",
                                                       "version": "2.0",
                                                       "primary_pipeline": "dlaas_only",
                                                       "pipelines": [{"id": "dlaas_only",\
                                                                      "runtime_ref": "hybrid",\
                                                                      "nodes": [{"id": "training",\
                                                                                 "type": "model_node",\
                                                                                 "op": "dl_train",\
                                                                                 "runtime_ref": "DL",\
                                                                                 "inputs": [],\
                                                                                 "outputs": [],\
                                                                                 "parameters": {"name": "tf-mnist",\
                                                                                                "description": "Simple MNIST model implemented in TF",\
                                                                                                "command": "python3 convolutional_network.py --trainImagesFile ${DATA_DIR}/train-images-idx3-ubyte.gz --trainLabelsFile ${DATA_DIR}/train-labels-idx1-ubyte.gz --testImagesFile ${DATA_DIR}/t10k-images-idx3-ubyte.gz --testLabelsFile ${DATA_DIR}/t10k-labels-idx1-ubyte.gz --learningRate 0.001 --trainingIters 6000",\
                                                                                                "compute": {"name": "k80","nodes": 1},\
                                                                                                "training_lib_href": "/v4/libraries/64758251-bt01-4aa5-a7ay-72639e2ff4d2/content"\
                                                                                 },\
                                                                                 "target_bucket": "wml-dev-results"\
                                                                      }]\
                                                       }]
    }
}
pipeline_details = client.repository.store_pipeline(training_definition_filepath, meta_props=metadata)

```

update\_ai\_service( _ai\_service\_id_, _changes_, _update\_ai\_service=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.update_ai_service) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.update_ai_service "Link to this definition")

Updates existing AI service asset metadata.

Parameters:

- **ai\_service\_id** ( _str_) – ID of AI service to be updated

- **changes** ( _dict_) – elements that will be changed, where keys are AIServiceMetaNames

- **update\_ai\_service** – path to the file with an archived AI service function’s content or function that will be changed for a specific ai\_service\_id


**Example:**

```
metadata = {
    client.repository.AIServiceMetaNames.NAME: "updated_ai_service"
}

ai_service_details = client.repository.update_ai_service(ai_service_id, changes=metadata)

```

update\_experiment( _experiment\_id=None_, _changes=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.update_experiment) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.update_experiment "Link to this definition")

Updates existing experiment metadata.

Parameters:

- **experiment\_id** ( _str_) – ID of the experiment with the definition to be updated

- **changes** ( _dict_) – elements to be changed, where keys are ExperimentMetaNames


Returns:

metadata of the updated experiment

Return type:

dict

**Example:**

```
metadata = {
    client.repository.ExperimentMetaNames.NAME: "updated_exp"
}
exp_details = client.repository.update_experiment(experiment_id, changes=metadata)

```

update\_function( _function\_id_, _changes=None_, _update\_function=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.update_function) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.update_function "Link to this definition")

Updates existing function metadata.

Parameters:

- **function\_id** ( _str_) – ID of function which define what should be updated

- **changes** ( _dict_) – elements which should be changed, where keys are FunctionMetaNames

- **update\_function** ( _str_ _or_ _function_ _,_ _optional_) – path to file with archived function content or function which should be changed
for specific function\_id, this parameter is valid only for CP4D 3.0.0


**Example:**

```
metadata = {
    client.repository.FunctionMetaNames.NAME: "updated_function"
}

function_details = client.repository.update_function(function_id, changes=metadata)

```

update\_model( _model\_id=None_, _updated\_meta\_props=None_, _update\_model=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.update_model) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.update_model "Link to this definition")

Update an existing model.

Parameters:

- **model\_id** ( _str_) – ID of model to be updated

- **updated\_meta\_props** ( _dict_ _,_ _optional_) – new set of updated\_meta\_props to be updated

- **update\_model** ( _object_ _or_ _model_ _,_ _optional_) – archived model content file or path to directory that contains the archived model file
that needs to be changed for the specific model\_id


Returns:

updated metadata of the model

Return type:

dict

**Example:**

```
model_details = client.repository.update_model(model_id, update_model=updated_content)

```

update\_pipeline( _pipeline\_id=None_, _changes=None_, _rev\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/repository.html#Repository.update_pipeline) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Repository.update_pipeline "Link to this definition")

Update metadata of an existing pipeline.

Parameters:

- **pipeline\_id** ( _str_) – unique ID of the pipeline to be updated

- **changes** ( _dict_) – elements to be changed, where keys are PipelineMetaNames

- **rev\_id** ( _str_) – revision ID of the pipeline


Returns:

metadata of the updated pipeline

Return type:

dict

**Example:**

```
metadata = {
    client.repository.PipelineMetaNames.NAME: "updated_pipeline"
}
pipeline_details = client.repository.update_pipeline(pipeline_id, changes=metadata)

```

_class_ metanames.ModelMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#ModelMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.ModelMetaNames "Link to this definition")

Set of MetaNames for models.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| NAME | str | Y |  | `my_model` |
| DESCRIPTION | str | N |  | `my_description` |
| INPUT\_DATA\_SCHEMA | list | N | `{'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}` | `{'id': '1', 'type': 'struct', 'fields': [{'name': 'x', 'type': 'double', 'nullable': False, 'metadata': {}}, {'name': 'y', 'type': 'double', 'nullable': False, 'metadata': {}}]}` |
| TRAINING\_DATA\_REFERENCES | list | N | `[{'name(optional)': 'string', 'type(required)': 'string', 'connection(required)': {'endpoint_url(required)': 'string', 'access_key_id(required)': 'string', 'secret_access_key(required)': 'string'}, 'location(required)': {'bucket': 'string', 'path': 'string'}, 'schema(optional)': {'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}}]` | `[]` |
| TEST\_DATA\_REFERENCES | list | N | `[{'name(optional)': 'string', 'type(required)': 'string', 'connection(required)': {'endpoint_url(required)': 'string', 'access_key_id(required)': 'string', 'secret_access_key(required)': 'string'}, 'location(required)': {'bucket': 'string', 'path': 'string'}, 'schema(optional)': {'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}}]` | `[]` |
| OUTPUT\_DATA\_SCHEMA | dict | N | `{'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}` | `{'id': '1', 'type': 'struct', 'fields': [{'name': 'x', 'type': 'double', 'nullable': False, 'metadata': {}}, {'name': 'y', 'type': 'double', 'nullable': False, 'metadata': {}}]}` |
| LABEL\_FIELD | str | N |  | `PRODUCT_LINE` |
| TRANSFORMED\_LABEL\_FIELD | str | N |  | `PRODUCT_LINE_IX` |
| TAGS | list | N | `['string', 'string']` | `['string', 'string']` |
| SIZE | dict | N | `{'in_memory(optional)': 'string', 'content(optional)': 'string'}` | `{'in_memory': 0, 'content': 0}` |
| PIPELINE\_ID | str | N |  | `53628d69-ced9-4f43-a8cd-9954344039a8` |
| RUNTIME\_ID | str | N |  | `53628d69-ced9-4f43-a8cd-9954344039a8` |
| TYPE | str | Y |  | `mllib_2.1` |
| CUSTOM | dict | N |  | `{}` |
| DOMAIN | str | N |  | `Watson Machine Learning` |
| HYPER\_PARAMETERS | dict | N |  |  |
| METRICS | list | N |  |  |
| IMPORT | dict | N | `{'name(optional)': 'string', 'type(required)': 'string', 'connection(required)': {'endpoint_url(required)': 'string', 'access_key_id(required)': 'string', 'secret_access_key(required)': 'string'}, 'location(required)': {'bucket': 'string', 'path': 'string'}}` | `{'connection': {'endpoint_url': 'https://s3-api.us-geo.objectstorage.softlayer.net', 'access_key_id': '***', 'secret_access_key': '***'}, 'location': {'bucket': 'train-data', 'path': 'training_path'}, 'type': 's3'}` |
| TRAINING\_LIB\_ID | str | N |  | `53628d69-ced9-4f43-a8cd-9954344039a8` |
| MODEL\_DEFINITION\_ID | str | N |  | `53628d6_cdee13-35d3-s8989343` |
| SOFTWARE\_SPEC\_ID | str | N |  | `53628d69-ced9-4f43-a8cd-9954344039a8` |
| TF\_MODEL\_PARAMS | dict | N |  | `{'save_format': 'None', 'signatures': 'struct', 'options': 'None', 'custom_objects': 'string'}` |
| FAIRNESS\_INFO | dict | N |  | `{'favorable_labels': ['X']}` |
| MODEL\_LOCATION | dict | N |  | `{'connection_id': '53628d69-ced9-4f43-a8cd-9954344039a8', 'bucket': 'cos_sample_bucket', 'file_path': 'path/to/model/on/cos'}` |
| FRAMEWORK | str | N |  | `custom_foundation_model` |
| VERSION | str | N |  | `1.0` |

**Note:** project (MetaNames.PROJECT\_ID) and space (MetaNames.SPACE\_ID) meta names are not supported and considered as invalid. Instead use client.set.default\_space(<SPACE\_ID>) to set the space or client.set.default\_project(<PROJECT\_ID>).

_class_ metanames.ExperimentMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#ExperimentMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.ExperimentMetaNames "Link to this definition")

Set of MetaNames for experiments.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| NAME | str | Y |  | `Hand-written Digit Recognition` |
| DESCRIPTION | str | N |  | `Hand-written Digit Recognition training` |
| TAGS | list | N | `[{'value(required)': 'string', 'description(optional)': 'string'}]` | `[{'value': 'dsx-project.<project-guid>', 'description': 'DSX project guid'}]` |
| EVALUATION\_METHOD | str | N |  | `multiclass` |
| EVALUATION\_METRICS | list | N | `[{'name(required)': 'string', 'maximize(optional)': 'boolean'}]` | `[{'name': 'accuracy', 'maximize': False}]` |
| TRAINING\_REFERENCES | list | Y | `[{'pipeline(optional)': {'href(required)': 'string', 'data_bindings(optional)': [{'data_reference(required)': 'string', 'node_id(required)': 'string'}], 'nodes_parameters(optional)': [{'node_id(required)': 'string', 'parameters(required)': 'dict'}]}, 'training_lib(optional)': {'href(required)': 'string', 'compute(optional)': {'name(required)': 'string', 'nodes(optional)': 'number'}, 'runtime(optional)': {'href(required)': 'string'}, 'command(optional)': 'string', 'parameters(optional)': 'dict'}}]` | `[{'pipeline': {'href': '/v4/pipelines/6d758251-bb01-4aa5-a7a3-72339e2ff4d8'}}]` |
| SPACE\_UID | str | N |  | `3c1ce536-20dc-426e-aac7-7284cf3befc6` |
| LABEL\_COLUMN | str | N |  | `label` |
| CUSTOM | dict | N |  | `{'field1': 'value1'}` |

_class_ metanames.FunctionMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#FunctionMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.FunctionMetaNames "Link to this definition")

Set of MetaNames for AI functions.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| NAME | str | Y |  | `ai_function` |
| DESCRIPTION | str | N |  | `This is ai function` |
| SOFTWARE\_SPEC\_ID | str | N |  | `53628d69-ced9-4f43-a8cd-9954344039a8` |
| SOFTWARE\_SPEC\_UID | str | N |  | `53628d69-ced9-4f43-a8cd-9954344039a8` |
| INPUT\_DATA\_SCHEMAS | list | N | `[{'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}]` | `[{'id': '1', 'type': 'struct', 'fields': [{'name': 'x', 'type': 'double', 'nullable': False, 'metadata': {}}, {'name': 'y', 'type': 'double', 'nullable': False, 'metadata': {}}]}]` |
| OUTPUT\_DATA\_SCHEMAS | list | N | `[{'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}]` | `[{'id': '1', 'type': 'struct', 'fields': [{'name': 'multiplication', 'type': 'double', 'nullable': False, 'metadata': {}}]}]` |
| TAGS | list | N | `['string']` | `['tags1', 'tags2']` |
| TYPE | str | N |  | `python` |
| CUSTOM | dict | N |  | `{}` |
| SAMPLE\_SCORING\_INPUT | dict | N | `{'id(optional)': 'string', 'fields(optional)': 'array', 'values(optional)': 'array'}` | `{'input_data': [{'fields': ['name', 'age', 'occupation'], 'values': [['john', 23, 'student'], ['paul', 33, 'engineer']]}]}` |

_class_ metanames.PipelineMetanames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#PipelineMetanames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.PipelineMetanames "Link to this definition")

Set of MetaNames for pipelines.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| NAME | str | Y |  | `Hand-written Digit Recognitionu` |
| DESCRIPTION | str | N |  | `Hand-written Digit Recognition training` |
| SPACE\_ID | str | N |  | `3c1ce536-20dc-426e-aac7-7284cf3befc6` |
| SPACE\_UID | str | N |  | `3c1ce536-20dc-426e-aac7-7284cf3befc6` |
| TAGS | list | N | `[{'value(required)': 'string', 'description(optional)': 'string'}]` | `[{'value': 'dsx-project.<project-guid>', 'description': 'DSX project guid'}]` |
| DOCUMENT | dict | N | `{'doc_type(required)': 'string', 'version(required)': 'string', 'primary_pipeline(required)': 'string', 'pipelines(required)': [{'id(required)': 'string', 'runtime_ref(required)': 'string', 'nodes(required)': [{'id': 'string', 'type': 'string', 'inputs': 'list', 'outputs': 'list', 'parameters': {'training_lib_href': 'string'}}]}]}` | `{'doc_type': 'pipeline', 'version': '2.0', 'primary_pipeline': 'dlaas_only', 'pipelines': [{'id': 'dlaas_only', 'runtime_ref': 'hybrid', 'nodes': [{'id': 'training', 'type': 'model_node', 'op': 'dl_train', 'runtime_ref': 'DL', 'inputs': [], 'outputs': [], 'parameters': {'name': 'tf-mnist', 'description': 'Simple MNIST model implemented in TF', 'command': 'python3 convolutional_network.py --trainImagesFile ${DATA_DIR}/train-images-idx3-ubyte.gz --trainLabelsFile ${DATA_DIR}/train-labels-idx1-ubyte.gz --testImagesFile ${DATA_DIR}/t10k-images-idx3-ubyte.gz --testLabelsFile ${DATA_DIR}/t10k-labels-idx1-ubyte.gz --learningRate 0.001 --trainingIters 6000', 'compute': {'name': 'k80', 'nodes': 1}, 'training_lib_href': '/v4/libraries/64758251-bt01-4aa5-a7ay-72639e2ff4d2/content'}, 'target_bucket': 'wml-dev-results'}]}]}` |
| CUSTOM | dict | N |  | `{'field1': 'value1'}` |
| IMPORT | dict | N | `{'name(optional)': 'string', 'type(required)': 'string', 'connection(required)': {'endpoint_url(required)': 'string', 'access_key_id(required)': 'string', 'secret_access_key(required)': 'string'}, 'location(required)': {'bucket': 'string', 'path': 'string'}}` | `{'connection': {'endpoint_url': 'https://s3-api.us-geo.objectstorage.softlayer.net', 'access_key_id': '***', 'secret_access_key': '***'}, 'location': {'bucket': 'train-data', 'path': 'training_path'}, 'type': 's3'}` |
| RUNTIMES | list | N |  | `[{'id': 'id', 'name': 'tensorflow', 'version': '1.13-py3'}]` |
| COMMAND | str | N |  | `convolutional_network.py --trainImagesFile train-images-idx3-ubyte.gz --trainLabelsFile train-labels-idx1-ubyte.gz --testImagesFile t10k-images-idx3-ubyte.gz --testLabelsFile t10k-labels-idx1-ubyte.gz --learningRate 0.001 --trainingIters 6000` |
| COMPUTE | dict | N |  | `{'name': 'k80', 'nodes': 1}` |

_class_ metanames.AIServiceMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#AIServiceMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.AIServiceMetaNames "Link to this definition")

Set of MetaNames for AI services.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| NAME | str | Y |  | `ai_service` |
| DESCRIPTION | str | N |  | `This is AI service` |
| SOFTWARE\_SPEC\_ID | str | N |  | `53628d69-ced9-4f43-a8cd-9954344039a8` |
| REQUEST\_DOCUMENTATION | dict | N |  | `{'application/json': {'$schema': 'http://json-schema.org/draft-07/schema#', 'type': 'object', 'properties': {'query': {'type': 'string'}, 'parameters': {'properties': {'max_new_tokens': {'type': 'integer'}, 'top_p': {'type': 'number'}}, 'required': ['max_new_tokens', 'top_p']}}, 'required': ['query']}}` |
| RESPONSE\_DOCUMENTATION | dict | N |  | `{'application/json': {'$schema': 'http://json-schema.org/draft-07/schema#', 'type': 'object', 'properties': {'query': {'type': 'string'}, 'result': {'type': 'string'}}, 'required': ['query', 'result']}}` |
| TAGS | list | N | `['string']` | `['tags1', 'tags2']` |
| CODE\_TYPE | str | N |  | `python` |
| CUSTOM | dict | N |  | `{'key1': 'value1'}` |
| TOOLING | dict | N |  | `{'reference_format': True, 't1': 'u1'}` |

## Script [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#script "Link to this heading")

_class_ client.Script( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script "Link to this definition")

Store and manage script assets.

ConfigurationMetaNames _=<ibm\_watsonx\_ai.metanames.ScriptMetaNamesobject>_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.ConfigurationMetaNames "Link to this definition")

MetaNames for script assets creation.

create\_revision( _script\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script.create_revision) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.create_revision "Link to this definition")

Create a revision for the given script. Revisions are immutable once created.
The metadata and attachment at script\_id is taken and a revision is created out of it.

Parameters:

**script\_id** ( _str_) – ID of the script

Returns:

revised metadata of the stored script

Return type:

dict

**Example:**

```
script_revision = client.script.create_revision(script_id)

```

delete( _asset\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.delete "Link to this definition")

Delete a stored script asset.

Parameters:

**asset\_id** ( _str_) – ID of the script asset

Returns:

status (“SUCCESS” or “FAILED”) if deleted synchronously or dictionary with response

Return type:

str \| dict

**Example:**

```
client.script.delete(asset_id)

```

download( _asset\_id=None_, _filename=None_, _rev\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script.download) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.download "Link to this definition")

Download the content of a script asset.

Parameters:

- **asset\_id** ( _str_) – unique ID of the script asset to be downloaded

- **filename** ( _str_) – filename to be used for the downloaded file

- **rev\_id** ( _str_ _,_ _optional_) – revision ID


Returns:

path to the downloaded asset content

Return type:

str

**Example:**

```
client.script.download(asset_id, "script_file")

```

get\_details( _script\_id=None_, _limit=None_, _get\_all=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.get_details "Link to this definition")

Get script asset details. If no script\_id is passed, details for all script assets are returned.

Parameters:

- **script\_id** ( _str_ _,_ _optional_) – unique ID of the script

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

metadata of the stored script asset

Return type:

- **dict** \- if script\_id is not None

- **{“resources”: \[dict\]}** \- if script\_id is None


**Example:**

```
script_details = client.script.get_details(script_id)

```

_static_ get\_href( _asset\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script.get_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.get_href "Link to this definition")

Get the URL of a stored script asset.

Parameters:

**asset\_details** ( _dict_) – details of the stored script asset

Returns:

href of the stored script asset

Return type:

str

**Example:**

```
asset_details = client.script.get_details(asset_id)
asset_href = client.script.get_href(asset_details)

```

_static_ get\_id( _asset\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.get_id "Link to this definition")

Get the unique ID of a stored script asset.

Parameters:

**asset\_details** ( _dict_) – metadata of the stored script asset

Returns:

unique ID of the stored script asset

Return type:

str

**Example:**

```
asset_id = client.script.get_id(asset_details)

```

get\_revision\_details( _script\_id=None_, _rev\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script.get_revision_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.get_revision_details "Link to this definition")

Get metadata of the script revision.

Parameters:

- **script\_id** ( _str_) – ID of the script

- **rev\_id** ( _str_ _,_ _optional_) – ID of the revision. If this parameter is not provided, it returns the latest revision. If there is no latest revision, it returns an error.


Returns:

metadata of the stored script(s)

Return type:

list

**Example:**

```
script_details = client.script.get_revision_details(script_id, rev_id)

```

list( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.list "Link to this definition")

List stored scripts in a table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records

Returns:

pandas.DataFrame with listed scripts

Return type:

pandas.DataFrame

**Example:**

```
client.script.list()

```

list\_revisions( _script\_id=None_, _limit=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script.list_revisions) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.list_revisions "Link to this definition")

Print all revisions for the given script ID in a table format.

Parameters:

- **script\_id** ( _str_) – ID of the stored script

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

pandas.DataFrame with listed revisions

Return type:

pandas.DataFrame

**Example:**

```
client.script.list_revisions(script_id)

```

store( _meta\_props_, _file\_path_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script.store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.store "Link to this definition")

Create a script asset and upload content to it.

Parameters:

- **meta\_props** ( _dict_) – name to be given to the script asset

- **file\_path** ( _str_) – path to the content file to be uploaded


Returns:

metadata of the stored script asset

Return type:

dict

**Example:**

```
metadata = {
    client.script.ConfigurationMetaNames.NAME: 'my first script',
    client.script.ConfigurationMetaNames.DESCRIPTION: 'description of the script',
    client.script.ConfigurationMetaNames.SOFTWARE_SPEC_ID: '0cdb0f1e-5376-4f4d-92dd-da3b69aa9bda'
}

asset_details = client.script.store(meta_props=metadata, file_path="/path/to/file")

```

update( _script\_id=None_, _meta\_props=None_, _file\_path=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/script.html#Script.update) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Script.update "Link to this definition")

Update a script with metadata, attachment, or both.

Parameters:

- **script\_id** ( _str_) – ID of the script

- **meta\_props** ( _dict_ _,_ _optional_) – changes for the script matadata

- **file\_path** ( _str_ _,_ _optional_) – file path to the new attachment


Returns:

updated metadata of the script

Return type:

dict

**Example:**

```
script_details = client.script.update(script_id, meta, content_path)

```

_class_ metanames.ScriptMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#ScriptMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.ScriptMetaNames "Link to this definition")

Set of MetaNames for Script Specifications.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| NAME | str | Y | `Python script` |
| DESCRIPTION | str | N | `my_description` |
| SOFTWARE\_SPEC\_ID | str | Y | `53628d69-ced9-4f43-a8cd-9954344039a8` |

## Service instance [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#service-instance "Link to this heading")

_class_ client.ServiceInstance( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/service_instance.html#ServiceInstance) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ServiceInstance "Link to this definition")

Connect, get details, and check usage of a Watson Machine Learning service instance.

get\_api\_key() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/service_instance.html#ServiceInstance.get_api_key) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ServiceInstance.get_api_key "Link to this definition")

Get the API key of a Watson Machine Learning service.

Returns:

API key

Return type:

str

**Example:**

```
instance_details = client.service_instance.get_api_key()

```

get\_details() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/service_instance.html#ServiceInstance.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ServiceInstance.get_details "Link to this definition")

Get information about the Watson Machine Learning instance.

Returns:

metadata of the service instance

Return type:

dict

**Example:**

```
instance_details = client.service_instance.get_details()

```

get\_instance\_id() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/service_instance.html#ServiceInstance.get_instance_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ServiceInstance.get_instance_id "Link to this definition")

Get the instance ID of a Watson Machine Learning service.

Returns:

ID of the instance

Return type:

str

**Example:**

```
instance_details = client.service_instance.get_instance_id()

```

get\_password() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/service_instance.html#ServiceInstance.get_password) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ServiceInstance.get_password "Link to this definition")

Get the password for the Watson Machine Learning service. Applicable only for IBM Cloud Pak® for Data.

Returns:

password

Return type:

str

**Example:**

```
instance_details = client.service_instance.get_password()

```

get\_url() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/service_instance.html#ServiceInstance.get_url) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ServiceInstance.get_url "Link to this definition")

Get the instance URL of a Watson Machine Learning service.

Returns:

URL of the instance

Return type:

str

**Example:**

```
instance_details = client.service_instance.get_url()

```

get\_username() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/service_instance.html#ServiceInstance.get_username) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.ServiceInstance.get_username "Link to this definition")

Get the username for the Watson Machine Learning service. Applicable only for IBM Cloud Pak® for Data.

Returns:

username

Return type:

str

**Example:**

```
instance_details = client.service_instance.get_username()

```

## Set [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#set "Link to this heading")

_class_ client.Set( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/Set.html#Set) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Set "Link to this definition")

Set a space\_id or a project\_id to be used in the subsequent actions.

default\_project( _project\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/Set.html#Set.default_project) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Set.default_project "Link to this definition")

Set a project ID.

Parameters:

**project\_id** ( _str_) – ID of the project to be used

Returns:

status (“SUCCESS” if succeeded)

Return type:

str

**Example:**

```
client.set.default_project(project_id)

```

default\_space( _space\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/Set.html#Set.default_space) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Set.default_space "Link to this definition")

Set a space ID.

Parameters:

**space\_id** ( _str_) – ID of the space to be used

Returns:

status (“SUCCESS” if succeeded)

Return type:

str

**Example:**

```
client.set.default_space(space_id)

```

## Shiny (IBM Cloud Pak® for Data only) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#shiny-ibm-cloud-pak-for-data-only "Link to this heading")

**Warning!** Not supported for IBM Cloud.

_class_ client.Shiny( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny "Link to this definition")

Store and manage shiny assets.

ConfigurationMetaNames _=<ibm\_watsonx\_ai.metanames.ShinyMetaNamesobject>_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.ConfigurationMetaNames "Link to this definition")

MetaNames for Shiny Assets creation.

create\_revision( _shiny\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.create_revision) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.create_revision "Link to this definition")

Create a revision for the given shiny asset. Revisions are immutable once created.
The metadata and attachment at script\_id is taken and a revision is created out of it.

Parameters:

**shiny\_id** ( _str_) – ID of the shiny asset

Returns:

revised metadata of the stored shiny asset

Return type:

dict

**Example:**

```
shiny_revision = client.shiny.create_revision(shiny_id)

```

delete( _shiny\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.delete "Link to this definition")

Delete a stored shiny asset.

Parameters:

**shiny\_id** ( _str_) – unique ID of the shiny asset

Returns:

status (“SUCCESS” or “FAILED”) if deleted synchronously or dictionary with response

Return type:

str \| dict

**Example:**

```
client.shiny.delete(shiny_id)

```

download( _shiny\_id=None_, _filename=None_, _rev\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.download) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.download "Link to this definition")

Download the content of a shiny asset.

Parameters:

- **shiny\_id** ( _str_) – unique ID of the shiny asset to be downloaded

- **filename** ( _str_) – filename to be used for the downloaded file

- **rev\_id** ( _str_ _,_ _optional_) – ID of the revision


Returns:

path to the downloaded shiny asset content

Return type:

str

**Example:**

```
client.shiny.download(shiny_id, "shiny_asset.zip")

```

get\_details( _shiny\_id=None_, _limit=None_, _get\_all=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.get_details "Link to this definition")

Get shiny asset details. If no shiny\_id is passed, details for all shiny assets are returned.

Parameters:

- **shiny\_id** ( _str_ _,_ _optional_) – unique ID of the shiny asset

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

metadata of the stored shiny asset

Return type:

- **dict** \- if shiny\_id is not None

- **{“resources”: \[dict\]}** \- if shiny\_id is None


**Example:**

```
shiny_details = client.shiny.get_details(shiny_id)

```

_static_ get\_href( _shiny\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.get_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.get_href "Link to this definition")

Get the URL of a stored shiny asset.

Parameters:

**shiny\_details** ( _dict_) – details of the stored shiny asset

Returns:

href of the stored shiny asset

Return type:

str

**Example:**

```
shiny_details = client.shiny.get_details(shiny_id)
shiny_href = client.shiny.get_href(shiny_details)

```

_static_ get\_id( _shiny\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.get_id "Link to this definition")

Get the unique ID of a stored shiny asset.

Parameters:

**shiny\_details** ( _dict_) – metadata of the stored shiny asset

Returns:

unique ID of the stored shiny asset

Return type:

str

**Example:**

```
shiny_id = client.shiny.get_id(shiny_details)

```

get\_revision\_details( _shiny\_id=None_, _rev\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.get_revision_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.get_revision_details "Link to this definition")

Get metadata of the shiny\_id revision.

Parameters:

- **shiny\_id** ( _str_) – ID of the shiny asset

- **rev\_id** ( _str_ _,_ _optional_) – ID of the revision. If this parameter is not provided, it returns the latest revision. If there is no latest revision, it returns an error.


Returns:

stored shiny(s) metadata

Return type:

list

**Example:**

```
shiny_details = client.shiny.get_revision_details(shiny_id, rev_id)

```

_static_ get\_uid( _shiny\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.get_uid) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.get_uid "Link to this definition")

Get the Unique ID of a stored shiny asset.

_Deprecated:_ Use `get_id(shiny_details)` instead.

Parameters:

**shiny\_details** ( _dict_) – metadata of the stored shiny asset

Returns:

unique ID of the stored shiny asset

Return type:

str

**Example:**

```
shiny_id = client.shiny.get_uid(shiny_details)

```

list( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.list "Link to this definition")

List stored shiny assets in a table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records

Returns:

pandas.DataFrame with listed shiny assets

Return type:

pandas.DataFrame

**Example:**

```
client.shiny.list()

```

list\_revisions( _shiny\_id=None_, _limit=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.list_revisions) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.list_revisions "Link to this definition")

List all revisions for the given shiny asset ID in a table format.

Parameters:

- **shiny\_id** ( _str_) – ID of the stored shiny asset

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records


Returns:

pandas.DataFrame with listed shiny revisions

Return type:

pandas.DataFrame

**Example:**

```
client.shiny.list_revisions(shiny_id)

```

store( _meta\_props_, _file\_path_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.store "Link to this definition")

Create a shiny asset and upload content to it.

Parameters:

- **meta\_props** ( _dict_) – metadata of the shiny asset

- **file\_path** ( _str_) – path to the content file to be uploaded


Returns:

metadata of the stored shiny asset

Return type:

dict

**Example:**

```
meta_props = {
    client.shiny.ConfigurationMetaNames.NAME: "shiny app name"
}

shiny_details = client.shiny.store(meta_props, file_path="/path/to/file")

```

update( _shiny\_id=None_, _meta\_props=None_, _file\_path=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/shiny.html#Shiny.update) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Shiny.update "Link to this definition")

Update a shiny asset with metadata, attachment, or both.

Parameters:

- **shiny\_id** ( _str_) – ID of the shiny asset

- **meta\_props** ( _dict_ _,_ _optional_) – changes to the metadata of the shiny asset

- **file\_path** ( _str_ _,_ _optional_) – file path to the new attachment


Returns:

updated metadata of the shiny asset

Return type:

dict

**Example:**

```
script_details = client.script.update(shiny_id, meta, content_path)

```

## Software specifications [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#software-specifications "Link to this heading")

_class_ client.SwSpec( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec "Link to this definition")

Store and manage software specs.

ConfigurationMetaNames _=<ibm\_watsonx\_ai.metanames.SwSpecMetaNamesobject>_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.ConfigurationMetaNames "Link to this definition")

MetaNames for Software Specification creation.

add\_package\_extension( _sw\_spec\_id=None_, _pkg\_extn\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec.add_package_extension) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.add_package_extension "Link to this definition")

Add a package extension to a software specification’s existing metadata.

Parameters:

- **sw\_spec\_id** ( _str_) – unique ID of the software specification to be updated

- **pkg\_extn\_id** ( _str_) – unique ID of the package extension to be added to the software specification


Returns:

status

Return type:

str

**Example:**

```
client.software_specifications.add_package_extension(sw_spec_id, pkg_extn_id)

```

delete( _sw\_spec\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.delete "Link to this definition")

Delete a software specification.

Parameters:

**sw\_spec\_id** ( _str_) – unique ID of the software specification

Returns:

status (“SUCCESS” or “FAILED”)

Return type:

str

**Example:**

```
client.software_specifications.delete(sw_spec_id)

```

delete\_package\_extension( _sw\_spec\_id=None_, _pkg\_extn\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec.delete_package_extension) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.delete_package_extension "Link to this definition")

Delete a package extension from a software specification’s existing metadata.

Parameters:

- **sw\_spec\_id** ( _str_) – unique ID of the software specification to be updated

- **pkg\_extn\_id** ( _str_) – unique ID of the package extension to be deleted from the software specification


Returns:

status

Return type:

str

**Example:**

```
client.software_specifications.delete_package_extension(sw_spec_uid, pkg_extn_id)

```

get\_details( _sw\_spec\_id=None_, _state\_info=False_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.get_details "Link to this definition")

Get software specification details. If no sw\_spec\_id is passed, details for all software specifications
are returned.

Parameters:

- **sw\_spec\_id** ( _bool_) – ID of the software specification

- **state\_info** – works only when sw\_spec\_id is None, instead of returning details of software specs, it returns
the state of the software specs information (supported, unsupported, deprecated), containing suggested replacement
in case of unsupported or deprecated software specs


Returns:

metadata of the stored software specification(s)

Return type:

- **dict** \- if sw\_spec\_uid is not None

- **{“resources”: \[dict\]}** \- if sw\_spec\_uid is None


**Examples**

```
sw_spec_details = client.software_specifications.get_details(sw_spec_uid)
sw_spec_details = client.software_specifications.get_details()
sw_spec_state_details = client.software_specifications.get_details(state_info=True)

```

_static_ get\_href( _sw\_spec\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec.get_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.get_href "Link to this definition")

Get the URL of a software specification.

Parameters:

**sw\_spec\_details** ( _dict_) – details of the software specification

Returns:

href of the software specification

Return type:

str

**Example:**

```
sw_spec_details = client.software_specifications.get_details(sw_spec_id)
sw_spec_href = client.software_specifications.get_href(sw_spec_details)

```

_static_ get\_id( _sw\_spec\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.get_id "Link to this definition")

Get the unique ID of a software specification.

Parameters:

**sw\_spec\_details** ( _dict_) – metadata of the software specification

Returns:

unique ID of the software specification

Return type:

str

**Example:**

```
asset_id = client.software_specifications.get_id(sw_spec_details)

```

get\_id\_by\_name( _sw\_spec\_name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec.get_id_by_name) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.get_id_by_name "Link to this definition")

Get the unique ID of a software specification.

Parameters:

**sw\_spec\_name** ( _str_) – name of the software specification

Returns:

unique ID of the software specification

Return type:

str

**Example:**

```
asset_uid = client.software_specifications.get_id_by_name(sw_spec_name)

```

_static_ get\_uid( _sw\_spec\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec.get_uid) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.get_uid "Link to this definition")

Get the unique ID of a software specification.

_Deprecated:_ Use `get_id(sw_spec_details)` instead.

Parameters:

**sw\_spec\_details** ( _dict_) – metadata of the software specification

Returns:

unique ID of the software specification

Return type:

str

**Example:**

```
asset_uid = client.software_specifications.get_uid(sw_spec_details)

```

get\_uid\_by\_name( _sw\_spec\_name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec.get_uid_by_name) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.get_uid_by_name "Link to this definition")

Get the unique ID of a software specification.

_Deprecated:_ Use `get_id_by_name(self, sw_spec_name)` instead.

Parameters:

**sw\_spec\_name** ( _str_) – name of the software specification

Returns:

unique ID of the software specification

Return type:

str

**Example:**

```
asset_uid = client.software_specifications.get_uid_by_name(sw_spec_name)

```

list( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.list "Link to this definition")

List software specifications in a table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records

Returns:

pandas.DataFrame with listed software specifications

Return type:

pandas.DataFrame

**Example:**

```
client.software_specifications.list()

```

store( _meta\_props_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/sw_spec.html#SwSpec.store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.SwSpec.store "Link to this definition")

Create a software specification.

Parameters:

**meta\_props** ( _dict_) –

metadata of the space configuration. To see available meta names, use:

```
client.software_specifications.ConfigurationMetaNames.get()

```

Returns:

metadata of the stored space

Return type:

dict

**Example:**

```
meta_props = {
    client.software_specifications.ConfigurationMetaNames.NAME: "skl_pipeline_heart_problem_prediction",
    client.software_specifications.ConfigurationMetaNames.DESCRIPTION: "description scikit-learn_0.20",
    client.software_specifications.ConfigurationMetaNames.PACKAGE_EXTENSIONS_UID: [],
    client.software_specifications.ConfigurationMetaNames.SOFTWARE_CONFIGURATIONS: {},
    client.software_specifications.ConfigurationMetaNames.BASE_SOFTWARE_SPECIFICATION_ID: "guid"
}

sw_spec_details = client.software_specifications.store(meta_props)

```

_class_ metanames.SwSpecMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#SwSpecMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.SwSpecMetaNames "Link to this definition")

Set of MetaNames for Software Specifications Specs.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| NAME | str | Y |  | `Python 3.10 with pre-installed ML package` |
| DESCRIPTION | str | N |  | `my_description` |
| PACKAGE\_EXTENSIONS | list | N |  | `[{'guid': 'value'}]` |
| SOFTWARE\_CONFIGURATION | dict | N | `{'platform(required)': 'string'}` | `{'platform': {'name': 'python', 'version': '3.10'}}` |
| BASE\_SOFTWARE\_SPECIFICATION | dict | Y |  | `{'guid': 'BASE_SOFTWARE_SPECIFICATION_ID'}` |

## Spaces [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#spaces "Link to this heading")

_class_ client.Spaces( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces "Link to this definition")

Store and manage spaces.

ConfigurationMetaNames _=<ibm\_watsonx\_ai.metanames.SpacesMetaNamesobject>_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.ConfigurationMetaNames "Link to this definition")

MetaNames for spaces creation.

MemberMetaNames _=<ibm\_watsonx\_ai.metanames.SpacesMemberMetaNamesobject>_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.MemberMetaNames "Link to this definition")

MetaNames for space members creation.

create\_member( _space\_id_, _meta\_props_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.create_member) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.create_member "Link to this definition")

Create a member within a space.

Parameters:

- **space\_id** ( _str_) – ID of the space with the definition to be updated

- **meta\_props** ( _dict_) –

metadata of the member configuration. To see available meta names, use:





```
client.spaces.MemberMetaNames.get()

```


Returns:

metadata of the stored member

Return type:

dict

Note

- role can be any one of the following: “viewer”, “editor”, “admin”

- type can be any one of the following: “user”, “service”

- id can be one of the following: service-ID or IAM-userID


**Examples**

```
metadata = {
    client.spaces.MemberMetaNames.MEMBERS: [{"id":"IBMid-100000DK0B",\
                                             "type": "user",\
                                             "role": "admin" }]
}
members_details = client.spaces.create_member(space_id=space_id, meta_props=metadata)

```

```
metadata = {
    client.spaces.MemberMetaNames.MEMBERS: [{"id":"iam-ServiceId-5a216e59-6592-43b9-8669-625d341aca71",\
                                             "type": "service",\
                                             "role": "admin" }]
}
members_details = client.spaces.create_member(space_id=space_id, meta_props=metadata)

```

delete( _space\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.delete "Link to this definition")

Delete a stored space.

Parameters:

**space\_id** ( _str_) – ID of the space

Returns:

status “SUCCESS” if deletion is successful

Return type:

Literal\[“SUCCESS”\]

**Example:**

```
client.spaces.delete(space_id)

```

delete\_member( _space\_id_, _member\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.delete_member) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.delete_member "Link to this definition")

Delete a member associated with a space.

Parameters:

- **space\_id** ( _str_) – ID of the space

- **member\_id** ( _str_) – ID of the member


Returns:

status (“SUCCESS” or “FAILED”)

Return type:

str

**Example:**

```
client.spaces.delete_member(space_id,member_id)

```

get\_details( _space\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_, _space\_name=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.get_details "Link to this definition")

Get metadata of stored space(s).

Parameters:

- **space\_id** ( _str_ _,_ _optional_) – ID of the space

- **limit** ( _int_ _,_ _optional_) – applicable when space\_id is not provided, otherwise limit will be ignored

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks

- **space\_name** ( _str_ _,_ _optional_) – name of the stored space, can be used only when space\_id is None


Returns:

metadata of stored space(s)

Return type:

- **dict** \- if space\_id is not None

- **{“resources”: \[dict\]}** \- if space\_id is None


**Example:**

```
space_details = client.spaces.get_details(space_id)
space_details = client.spaces.get_details(space_name)
space_details = client.spaces.get_details(limit=100)
space_details = client.spaces.get_details(limit=100, get_all=True)
space_details = []
for entry in client.spaces.get_details(limit=100, asynchronous=True, get_all=True):
    space_details.extend(entry)

```

_static_ get\_id( _space\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.get_id "Link to this definition")

Get the space\_id from the space details.

Parameters:

**space\_details** ( _dict_) – metadata of the stored space

Returns:

ID of the stored space

Return type:

str

**Example:**

```
space_details = client.spaces.store(meta_props)
space_id = client.spaces.get_id(space_details)

```

get\_id\_by\_name( _space\_name_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.get_id_by_name) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.get_id_by_name "Link to this definition")

Get the ID of a stored space by name.

Parameters:

**space\_name** ( _str_) – name of the stored space

Returns:

ID of the stored space

Return type:

str

**Example:**

```
space_id = client.spaces.get_id_by_name(space_name)

```

get\_member\_details( _space\_id_, _member\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.get_member_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.get_member_details "Link to this definition")

Get metadata of a member associated with a space.

Parameters:

- **space\_id** ( _str_) – ID of that space with the definition to be updated

- **member\_id** ( _str_) – ID of the member


Returns:

metadata of the space member

Return type:

dict

**Example:**

```
member_details = client.spaces.get_member_details(space_id,member_id)

```

_static_ get\_uid( _space\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.get_uid) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.get_uid "Link to this definition")

Get the unique ID of the space.

> _Deprecated:_ Use `get_id(space_details)` instead.
>
> param space\_details:
>
> metadata of the space
>
> type space\_details:
>
> dict
>
> return:
>
> unique ID of the space
>
> rtype:
>
> str

**Example:**

```
space_details = client.spaces.store(meta_props)
space_uid = client.spaces.get_uid(space_details)

```

list( _limit=None_, _member=None_, _roles=None_, _space\_type=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.list "Link to this definition")

List stored spaces in a table format.

Parameters:

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **member** ( _str_ _,_ _optional_) – filters the result list, only includes spaces where the user with a matching user ID
is a member

- **roles** ( _str_ _,_ _optional_) – limit number of fetched records

- **space\_type** ( _str_ _,_ _optional_) – filter spaces by their type, available types are ‘wx’, ‘cpd’, and ‘wca’


Returns:

pandas.DataFrame with listed spaces

Return type:

pandas.DataFrame

**Example:**

```
client.spaces.list()

```

list\_members( _space\_id_, _limit=None_, _identity\_type=None_, _role=None_, _state=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.list_members) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.list_members "Link to this definition")

Print the stored members of a space in a table format.

Parameters:

- **space\_id** ( _str_) – ID of the space

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **identity\_type** ( _str_ _,_ _optional_) – filter the members by type

- **role** ( _str_ _,_ _optional_) – filter the members by role

- **state** ( _str_ _,_ _optional_) – filter the members by state


Returns:

pandas.DataFrame with listed members

Return type:

pandas.DataFrame

**Example:**

```
client.spaces.list_members(space_id)

```

promote( _asset\_id_, _source\_project\_id_, _target\_space\_id_, _rev\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.promote) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.promote "Link to this definition")

Promote an asset from a project to a space.

Parameters:

- **asset\_id** ( _str_) – ID of the stored asset

- **source\_project\_id** ( _str_) – source project, from which the asset is promoted

- **target\_space\_id** ( _str_) – target space, where the asset is promoted

- **rev\_id** ( _str_ _,_ _optional_) – revision ID of the promoted asset


Returns:

ID of the promoted asset

Return type:

str

**Examples**

```
promoted_asset_id = client.spaces.promote(asset_id, source_project_id=project_id, target_space_id=space_id)
promoted_model_id = client.spaces.promote(model_id, source_project_id=project_id, target_space_id=space_id)
promoted_function_id = client.spaces.promote(function_id, source_project_id=project_id, target_space_id=space_id)
promoted_data_asset_id = client.spaces.promote(data_asset_id, source_project_id=project_id, target_space_id=space_id)
promoted_connection_asset_id = client.spaces.promote(connection_id, source_project_id=project_id, target_space_id=space_id)

```

store( _meta\_props_, _background\_mode=True_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.store "Link to this definition")

Create a space. The instance associated with the space via COMPUTE will be used for billing purposes on
the cloud. Note that STORAGE and COMPUTE are applicable only for cloud.

Parameters:

- **meta\_props** ( _dict_) –

metadata of the space configuration. To see available meta names, use:





```
client.spaces.ConfigurationMetaNames.get()

```

- **background\_mode** ( _bool_ _,_ _optional_) – indicator if store() method will run in background (async) or (sync)


Returns:

metadata of the stored space

Return type:

dict

**Example:**

```
metadata = {
    client.spaces.ConfigurationMetaNames.NAME: "my_space",
    client.spaces.ConfigurationMetaNames.DESCRIPTION: "spaces",
    client.spaces.ConfigurationMetaNames.STORAGE: {"resource_crn": "provide crn of the COS storage"},
    client.spaces.ConfigurationMetaNames.COMPUTE: {"name": "test_instance",
                                                   "crn": "provide crn of the instance"},
    client.spaces.ConfigurationMetaNames.STAGE: {"production": True,
                                                 "name": "stage_name"},
    client.spaces.ConfigurationMetaNames.TAGS: ["sample_tag_1", "sample_tag_2"],
    client.spaces.ConfigurationMetaNames.TYPE: "cpd",
}
spaces_details = client.spaces.store(meta_props=metadata)

```

update( _space\_id_, _changes_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.update) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.update "Link to this definition")

Update existing space metadata. ‘STORAGE’ cannot be updated.
STORAGE and COMPUTE are applicable only for cloud.

Parameters:

- **space\_id** ( _str_) – ID of the space with the definition to be updated

- **changes** ( _dict_) – elements to be changed, where keys are ConfigurationMetaNames


Returns:

metadata of the updated space

Return type:

dict

**Example:**

```
metadata = {
    client.spaces.ConfigurationMetaNames.NAME:"updated_space",
    client.spaces.ConfigurationMetaNames.COMPUTE: {"name": "test_instance",
                                                   "crn": "v1:staging:public:pm-20-dev:us-south:a/09796a1b4cddfcc9f7fe17824a68a0f8:f1026e4b-77cf-4703-843d-c9984eac7272::"
    }
}
space_details = client.spaces.update(space_id, changes=metadata)

```

update\_member( _space\_id_, _member\_id_, _changes_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/spaces.html#Spaces.update_member) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Spaces.update_member "Link to this definition")

Update the metadata of an existing member.

Parameters:

- **space\_id** ( _str_) – ID of the space

- **member\_id** ( _str_) – ID of the member to be updated

- **changes** ( _dict_) – elements to be changed, where keys are ConfigurationMetaNames


Returns:

metadata of the updated member

Return type:

dict

**Example:**

```
metadata = {
    client.spaces.MemberMetaNames.MEMBER: {"role": "editor"}
}
member_details = client.spaces.update_member(space_id, member_id, changes=metadata)

```

_class_ metanames.SpacesMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#SpacesMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.SpacesMetaNames "Link to this definition")

Set of MetaNames for Platform Spaces Specs.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| NAME | str | Y | `my_space` |
| DESCRIPTION | str | N | `my_description` |
| STORAGE | dict | N | `{'type': 'bmcos_object_storage', 'resource_crn': '', 'delegated(optional)': 'false'}` |
| COMPUTE | dict | N | `{'name': 'name', 'crn': 'crn of the instance'}` |
| STAGE | dict | N | `{'production': True, 'name': 'name of the stage'}` |
| TAGS | list | N | `['sample_tag']` |
| TYPE | str | N | `cpd` |

_class_ metanames.SpacesMemberMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#SpacesMemberMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.SpacesMemberMetaNames "Link to this definition")

Set of MetaNames for Platform Spaces Member Specs.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| MEMBERS | list | N | `[{'id(required)': 'string', 'role(required)': 'string', 'type(required)': 'string', 'state(optional)': 'string'}]` | `[{'id': 'iam-id1', 'role': 'editor', 'type': 'user', 'state': 'active'}, {'id': 'iam-id2', 'role': 'viewer', 'type': 'user', 'state': 'active'}]` |
| MEMBER | dict | N |  | `{'id': 'iam-id1', 'role': 'editor', 'type': 'user', 'state': 'active'}` |

## Task Credentials [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#task-credentials "Link to this heading")

_class_ client.TaskCredentials( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/task_credentials.html#TaskCredentials) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TaskCredentials "Link to this definition")

Store and manage your task credentials.

delete( _task\_credentials\_id_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/task_credentials.html#TaskCredentials.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TaskCredentials.delete "Link to this definition")

Delete a software specification.

Parameters:

**task\_credentials\_id** ( _str_) – Unique Id of task credentials

Returns:

status “SUCCESS” if deletion is successful

Return type:

Literal\[“SUCCESS”\]

**Example:**

```
client.task_credentials.delete(task_credentials_id)

```

get\_details( _task\_credentials\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/task_credentials.html#TaskCredentials.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TaskCredentials.get_details "Link to this definition")

Get task credentials details. If no task\_credentials\_id is passed, details for all task credentials
will be returned.

Parameters:

- **task\_credentials\_id** ( _str_ _,_ _optional_) – ID of task credentials to be fetched

- **project\_id** ( _str_ _,_ _optional_) – ID of project to be used for filtering

- **space\_id** ( _str_ _,_ _optional_) – ID of space to be used for filtering


Returns:

created task credentials details

Return type:

dict (if task\_credentials\_id is not None) or {“resources”: \[dict\]} (if task\_credentials\_id is None)

**Example:**

```
task_credentials_details = client.task_credentials.get_details(task_credentials_id)

```

_static_ get\_id( _task\_credentials\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/task_credentials.html#TaskCredentials.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TaskCredentials.get_id "Link to this definition")

Get Unique Id of task credentials.

Parameters:

**task\_credentials\_details** ( _dict_) – metadata of the task credentials

Returns:

Unique Id of task credentials

Return type:

str

**Example:**

```
task_credentials_id = client.task_credentials.get_id(task_credentials_details)

```

list( _limit=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/task_credentials.html#TaskCredentials.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TaskCredentials.list "Link to this definition")

Lists task credentials in table format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records

Returns:

pandas.DataFrame with listed assets

Return type:

pandas.DataFrame

**Example:**

```
client.task_credentials.list()

```

store( _name=None_, _description=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/task_credentials.html#TaskCredentials.store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.TaskCredentials.store "Link to this definition")

Store current credentials using Task Credentials API to use with long run tasks. Supported only on Cloud.

Parameters:

- **name** ( _str_ _,_ _optional_) – Name of the task credentials. Defaults to Python API generated task credentials

- **description** ( _str_ _,_ _optional_) – Description of the task credentials. Defaults to Python API generated task credentials


Returns:

A dictionary containing metadata of the stored task credentials.

Return type:

dict

**Example:**

```
task_credentials_details = client.task_credentials.store()

```

## Training [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#training "Link to this heading")

_class_ client.Training( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training "Link to this definition")

Train new models.

cancel( _training\_id=None_, _hard\_delete=False_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training.cancel) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training.cancel "Link to this definition")

Cancel a training that is currently running. This method can delete metadata
details of a completed or canceled training run when hard\_delete parameter is set to True.

Parameters:

- **training\_id** ( _str_) – ID of the training

- **hard\_delete** ( _bool_ _,_ _optional_) –

specify True or False:


  - True \- to delete the completed or canceled training run

  - False \- to cancel the currently running training run


Returns:

status “SUCCESS” if cancelation is successful

Return type:

Literal\[“SUCCESS”\]

**Example:**

```
client.training.cancel(training_id)

```

get\_details( _training\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_, _training\_type=None_, _state=None_, _tag\_value=None_, _training\_definition\_id=None_, _\_internal=False_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training.get_details "Link to this definition")

Get metadata of training(s). If training\_id is not specified, the metadata of all model spaces are returned.

Parameters:

- **training\_id** ( _str_ _,_ _optional_) – unique ID of the training

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks

- **training\_type** ( _str_ _,_ _optional_) – filter the fetched list of trainings based on the training type \[“pipeline” or “experiment”\]

- **state** ( _str_ _,_ _optional_) – filter the fetched list of training based on their state:
\[queued, running, completed, failed\]

- **tag\_value** ( _str_ _,_ _optional_) – filter the fetched list of training based on their tag value

- **training\_definition\_id** ( _str_ _,_ _optional_) – filter the fetched trainings that are using the given training definition


Returns:

metadata of training(s)

Return type:

- **dict** \- if training\_id is not None

- **{“resources”: \[dict\]}** \- if training\_id is None


**Examples**

```
training_run_details = client.training.get_details(training_id)
training_runs_details = client.training.get_details()
training_runs_details = client.training.get_details(limit=100)
training_runs_details = client.training.get_details(limit=100, get_all=True)
training_runs_details = []
for entry in client.training.get_details(limit=100, asynchronous=True, get_all=True):
    training_runs_details.extend(entry)

```

_static_ get\_href( _training\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training.get_href) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training.get_href "Link to this definition")

Get the training href from the training details.

Parameters:

**training\_details** ( _dict_) – metadata of the created training

Returns:

training href

Return type:

str

**Example:**

```
training_details = client.training.get_details(training_id)
run_url = client.training.get_href(training_details)

```

_static_ get\_id( _training\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training.get_id "Link to this definition")

Get the training ID from the training details.

Parameters:

**training\_details** ( _dict_) – metadata of the created training

Returns:

unique ID of the training

Return type:

str

**Example:**

```
training_details = client.training.get_details(training_id)
training_id = client.training.get_id(training_details)

```

get\_metrics( _training\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training.get_metrics) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training.get_metrics "Link to this definition")

Get metrics of a training run.

Parameters:

**training\_id** ( _str_) – ID of the training

Returns:

metrics of the training run

Return type:

list of dict

**Example:**

```
training_status = client.training.get_metrics(training_id)

```

get\_status( _training\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training.get_status) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training.get_status "Link to this definition")

Get the status of a created training.

Parameters:

**training\_id** ( _str_) – ID of the training

Returns:

training\_status

Return type:

dict

**Example:**

```
training_status = client.training.get_status(training_id)

```

list( _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training.list "Link to this definition")

List stored trainings in a table format.

Parameters:

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

pandas.DataFrame with listed experiments

Return type:

pandas.DataFrame

**Examples**

```
client.training.list()
training_runs_df = client.training.list(limit=100)
training_runs_df = client.training.list(limit=100, get_all=True)
training_runs_df = []
for entry in client.training.list(limit=100, asynchronous=True, get_all=True):
    training_runs_df.extend(entry)

```

list\_intermediate\_models( _training\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training.list_intermediate_models) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training.list_intermediate_models "Link to this definition")

Print the intermediate\_models in a table format.

Parameters:

**training\_id** ( _str_) – ID of the training

Note

This method is not supported for IBM Cloud Pak® for Data.

**Example:**

```
client.training.list_intermediate_models()

```

monitor\_logs( _training\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training.monitor_logs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training.monitor_logs "Link to this definition")

Print the logs of a training created.

Parameters:

**training\_id** ( _str_) – training ID

Note

This method is not supported for IBM Cloud Pak® for Data.

**Example:**

```
client.training.monitor_logs(training_id)

```

monitor\_metrics( _training\_id=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training.monitor_metrics) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training.monitor_metrics "Link to this definition")

Print the metrics of a created training.

Parameters:

**training\_id** ( _str_) – ID of the training

Note

This method is not supported for IBM Cloud Pak® for Data.

**Example:**

```
client.training.monitor_metrics(training_id)

```

run( _meta\_props_, _asynchronous=True_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/training.html#Training.run) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#client.Training.run "Link to this definition")

Create a new Machine Learning training.

Parameters:

- **meta\_props** ( _dict_) –

metadata of the training configuration. To see available meta names, use:





```
client.training.ConfigurationMetaNames.show()

```

- **asynchronous** ( _bool_ _,_ _optional_) –


  - True \- training job is submitted and progress can be checked later

  - False \- method will wait till job completion and print training stats


Returns:

metadata of the training created

Return type:

dict

Note

You can provide one of the following values for training:

- client.training.ConfigurationMetaNames.EXPERIMENT

- client.training.ConfigurationMetaNames.PIPELINE

- client.training.ConfigurationMetaNames.MODEL\_DEFINITION


**Examples**

Example of meta\_props for creating a training run in IBM Cloud Pak® for Data version 3.0.1 or above:

```
metadata = {
    client.training.ConfigurationMetaNames.NAME: 'Hand-written Digit Recognition',
    client.training.ConfigurationMetaNames.DESCRIPTION: 'Hand-written Digit Recognition Training',
    client.training.ConfigurationMetaNames.PIPELINE: {
        "id": "4cedab6d-e8e4-4214-b81a-2ddb122db2ab",
        "rev": "12",
        "model_type": "string",
        "data_bindings": [\
            {\
                "data_reference_name": "string",\
                "node_id": "string"\
            }\
        ],
        "nodes_parameters": [\
            {\
                "node_id": "string",\
                "parameters": {}\
            }\
        ],
        "hardware_spec": {
            "id": "4cedab6d-e8e4-4214-b81a-2ddb122db2ab",
            "rev": "12",
            "name": "string",
            "num_nodes": "2"
        }
    },
    client.training.ConfigurationMetaNames.TRAINING_DATA_REFERENCES: [{\
        'type': 's3',\
        'connection': {},\
        'location': {'href': 'v2/assets/asset1233456'},\
        'schema': { 'id': 't1', 'name': 'Tasks', 'fields': [ { 'name': 'duration', 'type': 'number' } ]}\
    }],
    client.training.ConfigurationMetaNames.TRAINING_RESULTS_REFERENCE: {
        'id' : 'string',
        'connection': {
            'endpoint_url': 'https://s3-api.us-geo.objectstorage.service.networklayer.com',
            'access_key_id': '***',
            'secret_access_key': '***'
        },
        'location': {
            'bucket': 'wml-dev-results',
            'path' : "path"
        }
        'type': 's3'
    }
}

```

Example of a Federated Learning training job:

```
aggregator_metadata = {
    client.training.ConfigurationMetaNames.NAME: 'Federated_Learning_Tensorflow_MNIST',
    client.training.ConfigurationMetaNames.DESCRIPTION: 'MNIST digit recognition with Federated Learning using Tensorflow',
    client.training.ConfigurationMetaNames.TRAINING_DATA_REFERENCES: [],
    client.training.ConfigurationMetaNames.TRAINING_RESULTS_REFERENCE: {
        'type': results_type,
        'name': 'outputData',
        'connection': {},
        'location': { 'path': '/projects/' + PROJECT_ID + '/assets/trainings/'}
    },
    client.training.ConfigurationMetaNames.FEDERATED_LEARNING: {
        'model': {
            'type': 'tensorflow',
            'spec': {
            'id': untrained_model_id
        },
        'model_file': untrained_model_name
    },
    'fusion_type': 'iter_avg',
    'metrics': 'accuracy',
    'epochs': 3,
    'rounds': 10,
    'remote_training' : {
        'quorum': 1.0,
        'max_timeout': 3600,
        'remote_training_systems': [ { 'id': prime_rts_id }, { 'id': nonprime_rts_id} ]
    },
    'hardware_spec': {
        'name': 'S'
    },
    'software_spec': {
        'name': 'runtime-22.1-py3.9'
    }
}

aggregator = client.training.run(aggregator_metadata, asynchronous=True)
aggregator_id = client.training.get_id(aggregator)

```

_class_ metanames.TrainingConfigurationMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#TrainingConfigurationMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#metanames.TrainingConfigurationMetaNames "Link to this definition")

Set of MetaNames for trainings.

Available MetaNames:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| MetaName | Type | Required | Schema | Example value |
| TRAINING\_DATA\_REFERENCES | list | Y | `[{'name(optional)': 'string', 'type(required)': 'string', 'connection(required)': {'endpoint_url(required)': 'string', 'access_key_id(required)': 'string', 'secret_access_key(required)': 'string'}, 'location(required)': {'bucket': 'string', 'path': 'string'}, 'schema(optional)': {'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}}]` | `[{'connection': {'endpoint_url': 'https://s3-api.us-geo.objectstorage.softlayer.net', 'access_key_id': '***', 'secret_access_key': '***'}, 'location': {'bucket': 'train-data', 'path': 'training_path'}, 'type': 's3', 'schema': {'id': '1', 'fields': [{'name': 'x', 'type': 'double', 'nullable': 'False'}]}}]` |
| TRAINING\_RESULTS\_REFERENCE | dict | Y | `{'name(optional)': 'string', 'type(required)': 'string', 'connection(required)': {'endpoint_url(required)': 'string', 'access_key_id(required)': 'string', 'secret_access_key(required)': 'string'}, 'location(required)': {'bucket': 'string', 'path': 'string'}}` | `{'connection': {'endpoint_url': 'https://s3-api.us-geo.objectstorage.softlayer.net', 'access_key_id': '***', 'secret_access_key': '***'}, 'location': {'bucket': 'test-results', 'path': 'training_path'}, 'type': 's3'}` |
| TEST\_DATA\_REFERENCES | list | N | `[{'name(optional)': 'string', 'type(required)': 'string', 'connection(required)': {'endpoint_url(required)': 'string', 'access_key_id(required)': 'string', 'secret_access_key(required)': 'string'}, 'location(required)': {'bucket': 'string', 'path': 'string'}, 'schema(optional)': {'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}}]` | `[{'connection': {'endpoint_url': 'https://s3-api.us-geo.objectstorage.softlayer.net', 'access_key_id': '***', 'secret_access_key': '***'}, 'location': {'bucket': 'train-data', 'path': 'training_path'}, 'type': 's3', 'schema': {'id': '1', 'fields': [{'name': 'x', 'type': 'double', 'nullable': 'False'}]}}]` |
| TEST\_OUTPUT\_DATA | dict | N | `{'name(optional)': 'string', 'type(required)': 'string', 'connection(required)': {'endpoint_url(required)': 'string', 'access_key_id(required)': 'string', 'secret_access_key(required)': 'string'}, 'location(required)': {'bucket': 'string', 'path': 'string'}, 'schema(optional)': {'id(required)': 'string', 'fields(required)': [{'name(required)': 'string', 'type(required)': 'string', 'nullable(optional)': 'string'}]}}` | `[{'connection': {'endpoint_url': 'https://s3-api.us-geo.objectstorage.softlayer.net', 'access_key_id': '***', 'secret_access_key': '***'}, 'location': {'bucket': 'train-data', 'path': 'training_path'}, 'type': 's3', 'schema': {'id': '1', 'fields': [{'name': 'x', 'type': 'double', 'nullable': 'False'}]}}]` |
| TAGS | list | N | `['string']` | `['string']` |
| PIPELINE | dict | N |  | `{'id': '3c1ce536-20dc-426e-aac7-7284cf3befc6', 'rev': '1', 'modeltype': 'tensorflow_1.1.3-py3', 'data_bindings': [{'data_reference_name': 'string', 'node_id': 'string'}], 'node_parameters': [{'node_id': 'string', 'parameters': {}}], 'hardware_spec': {'id': '4cedab6d-e8e4-4214-b81a-2ddb122db2ab', 'rev': '12', 'name': 'string', 'num_nodes': '2'}, 'hybrid_pipeline_hardware_specs': [{'node_runtime_id': 'string', 'hardware_spec': {'id': '4cedab6d-e8e4-4214-b81a-2ddb122db2ab', 'rev': '12', 'name': 'string', 'num_nodes': '2'}}]}` |
| EXPERIMENT | dict | N |  | `{'id': '3c1ce536-20dc-426e-aac7-7284cf3befc6', 'rev': 1, 'description': 'test experiment'}` |
| PROMPT\_TUNING | dict | N |  | `{'task_id': 'generation', 'base_model': {'model_id': 'google/flan-t5-xl'}}` |
| FINE\_TUNING | dict | N |  | `{'task_id': 'generation', 'base_model': {'model_id': 'bigscience/bloom-560m'}}` |
| AUTO\_UPDATE\_MODEL | bool | N |  | `False` |
| FEDERATED\_LEARNING | dict | N |  | `3c1ce536-20dc-426e-aac7-7284cf3befc6` |
| SPACE\_UID | str | N |  | `3c1ce536-20dc-426e-aac7-7284cf3befc6` |
| MODEL\_DEFINITION | dict | N |  | `{'id': '4cedab6d-e8e4-4214-b81a-2ddb122db2ab', 'rev': '12', 'model_type': 'string', 'hardware_spec': {'id': '4cedab6d-e8e4-4214-b81a-2ddb122db2ab', 'rev': '12', 'name': 'string', 'num_nodes': '2'}, 'software_spec': {'id': '4cedab6d-e8e4-4214-b81a-2ddb122db2ab', 'rev': '12', 'name': '...'}, 'command': 'string', 'parameters': {}}` |
| DESCRIPTION | str | Y |  | `tensorflow model training` |
| NAME | str | Y |  | `sample training` |

## Enums [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html\#module-ibm_watsonx_ai.utils.autoai.enums "Link to this heading")

_class_ ibm\_watsonx\_ai.utils.autoai.enums.ClassificationAlgorithms( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#ClassificationAlgorithms) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms "Link to this definition")

Bases: `Enum`

Classification algorithms that AutoAI can use for IBM Cloud.

DT _='DecisionTreeClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.DT "Link to this definition")EX\_TREES _='ExtraTreesClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.EX_TREES "Link to this definition")GB _='GradientBoostingClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.GB "Link to this definition")LGBM _='LGBMClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.LGBM "Link to this definition")LR _='LogisticRegression'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.LR "Link to this definition")RF _='RandomForestClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.RF "Link to this definition")SnapBM _='SnapBoostingMachineClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.SnapBM "Link to this definition")SnapDT _='SnapDecisionTreeClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.SnapDT "Link to this definition")SnapLR _='SnapLogisticRegression'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.SnapLR "Link to this definition")SnapRF _='SnapRandomForestClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.SnapRF "Link to this definition")SnapSVM _='SnapSVMClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.SnapSVM "Link to this definition")XGB _='XGBClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithms.XGB "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#ClassificationAlgorithmsCP4D) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D "Link to this definition")

Bases: `Enum`

Classification algorithms that AutoAI can use for IBM Cloud Pak® for Data(CP4D).
The SnapML estimators (SnapDT, SnapRF, SnapSVM, SnapLR) are supported
on IBM Cloud Pak® for Data version 4.0.2 and later.

DT _='DecisionTreeClassifierEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.DT "Link to this definition")EX\_TREES _='ExtraTreesClassifierEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.EX_TREES "Link to this definition")GB _='GradientBoostingClassifierEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.GB "Link to this definition")LGBM _='LGBMClassifierEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.LGBM "Link to this definition")LR _='LogisticRegressionEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.LR "Link to this definition")RF _='RandomForestClassifierEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.RF "Link to this definition")SnapBM _='SnapBoostingMachineClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.SnapBM "Link to this definition")SnapDT _='SnapDecisionTreeClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.SnapDT "Link to this definition")SnapLR _='SnapLogisticRegression'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.SnapLR "Link to this definition")SnapRF _='SnapRandomForestClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.SnapRF "Link to this definition")SnapSVM _='SnapSVMClassifier'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.SnapSVM "Link to this definition")XGB _='XGBClassifierEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ClassificationAlgorithmsCP4D.XGB "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.DataConnectionTypes [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#DataConnectionTypes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.DataConnectionTypes "Link to this definition")

Bases: `object`

Supported types of DataConnection.

CA _='connection\_asset'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.DataConnectionTypes.CA "Link to this definition")CN _='container'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.DataConnectionTypes.CN "Link to this definition")DS _='data\_asset'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.DataConnectionTypes.DS "Link to this definition")FS _='fs'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.DataConnectionTypes.FS "Link to this definition")GH _='github'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.DataConnectionTypes.GH "Link to this definition")S3 _='s3'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.DataConnectionTypes.S3 "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.Directions [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#Directions) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Directions "Link to this definition")

Bases: `object`

Possible metrics directions

ASCENDING _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Directions.ASCENDING "Link to this definition")DESCENDING _='descending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Directions.DESCENDING "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.DocumentsSamplingTypes [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#DocumentsSamplingTypes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.DocumentsSamplingTypes "Link to this definition")

Bases: `object`

Types of training data sampling.

BENCHMARK\_DRIVEN _='benchmark\_driven'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.DocumentsSamplingTypes.BENCHMARK_DRIVEN "Link to this definition")RANDOM _='random'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.DocumentsSamplingTypes.RANDOM "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.ForecastingAlgorithms( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#ForecastingAlgorithms) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithms "Link to this definition")

Bases: `Enum`

Forecasting algorithms that AutoAI can use for IBM watsonx.ai software with IBM Cloud Pak® for Data.

ARIMA _='ARIMA'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithms.ARIMA "Link to this definition")BATS _='BATS'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithms.BATS "Link to this definition")ENSEMBLER _='Ensembler'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithms.ENSEMBLER "Link to this definition")HW _='HoltWinters'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithms.HW "Link to this definition")LR _='LinearRegression'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithms.LR "Link to this definition")RF _='RandomForest'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithms.RF "Link to this definition")SVM _='SVM'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithms.SVM "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.ForecastingAlgorithmsCP4D( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#ForecastingAlgorithmsCP4D) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithmsCP4D "Link to this definition")

Bases: `Enum`

Forecasting algorithms that AutoAI can use for IBM Cloud.

ARIMA _='ARIMA'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithmsCP4D.ARIMA "Link to this definition")BATS _='BATS'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithmsCP4D.BATS "Link to this definition")ENSEMBLER _='Ensembler'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithmsCP4D.ENSEMBLER "Link to this definition")HW _='HoltWinters'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithmsCP4D.HW "Link to this definition")LR _='LinearRegression'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithmsCP4D.LR "Link to this definition")RF _='RandomForest'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithmsCP4D.RF "Link to this definition")SVM _='SVM'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingAlgorithmsCP4D.SVM "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.ForecastingPipelineTypes( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#ForecastingPipelineTypes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes "Link to this definition")

Bases: `Enum`

Forecasting pipeline types that AutoAI can use for IBM Cloud Pak® for Data(CP4D).

ARIMA _='ARIMA'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ARIMA "Link to this definition")ARIMAX _='ARIMAX'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ARIMAX "Link to this definition")ARIMAX\_DMLR _='ARIMAX\_DMLR'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ARIMAX_DMLR "Link to this definition")ARIMAX\_PALR _='ARIMAX\_PALR'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ARIMAX_PALR "Link to this definition")ARIMAX\_RAR _='ARIMAX\_RAR'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ARIMAX_RAR "Link to this definition")ARIMAX\_RSAR _='ARIMAX\_RSAR'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ARIMAX_RSAR "Link to this definition")Bats _='Bats'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.Bats "Link to this definition")DifferenceFlattenEnsembler _='DifferenceFlattenEnsembler'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.DifferenceFlattenEnsembler "Link to this definition")ExogenousDifferenceFlattenEnsembler _='ExogenousDifferenceFlattenEnsembler'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ExogenousDifferenceFlattenEnsembler "Link to this definition")ExogenousFlattenEnsembler _='ExogenousFlattenEnsembler'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ExogenousFlattenEnsembler "Link to this definition")ExogenousLocalizedFlattenEnsembler _='ExogenousLocalizedFlattenEnsembler'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ExogenousLocalizedFlattenEnsembler "Link to this definition")ExogenousMT2RForecaster _='ExogenousMT2RForecaster'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ExogenousMT2RForecaster "Link to this definition")ExogenousRandomForestRegressor _='ExogenousRandomForestRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ExogenousRandomForestRegressor "Link to this definition")ExogenousSVM _='ExogenousSVM'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.ExogenousSVM "Link to this definition")FlattenEnsembler _='FlattenEnsembler'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.FlattenEnsembler "Link to this definition")HoltWinterAdditive _='HoltWinterAdditive'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.HoltWinterAdditive "Link to this definition")HoltWinterMultiplicative _='HoltWinterMultiplicative'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.HoltWinterMultiplicative "Link to this definition")LocalizedFlattenEnsembler _='LocalizedFlattenEnsembler'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.LocalizedFlattenEnsembler "Link to this definition")MT2RForecaster _='MT2RForecaster'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.MT2RForecaster "Link to this definition")RandomForestRegressor _='RandomForestRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.RandomForestRegressor "Link to this definition")SVM _='SVM'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.SVM "Link to this definition")_static_ get\_exogenous() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#ForecastingPipelineTypes.get_exogenous) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.get_exogenous "Link to this definition")

Get a list of pipelines that use supporting features (exogenous pipelines).

Returns:

list of pipelines using supporting features

Return type:

list\[ [ForecastingPipelineTypes](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes "ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes")\]

_static_ get\_non\_exogenous() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#ForecastingPipelineTypes.get_non_exogenous) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes.get_non_exogenous "Link to this definition")

Get a list of pipelines that are not using supporting features (non-exogenous pipelines).

Returns:

list of pipelines that do not use supporting features

Return type:

list\[ [ForecastingPipelineTypes](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes "ibm_watsonx_ai.utils.autoai.enums.ForecastingPipelineTypes")\]

_class_ ibm\_watsonx\_ai.utils.autoai.enums.ImputationStrategy( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#ImputationStrategy) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy "Link to this definition")

Bases: `Enum`

Missing values imputation strategies.

BEST\_OF\_DEFAULT\_IMPUTERS _='best\_of\_default\_imputers'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy.BEST_OF_DEFAULT_IMPUTERS "Link to this definition")CUBIC _='cubic'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy.CUBIC "Link to this definition")FLATTEN\_ITERATIVE _='flatten\_iterative'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy.FLATTEN_ITERATIVE "Link to this definition")LINEAR _='linear'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy.LINEAR "Link to this definition")MEAN _='mean'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy.MEAN "Link to this definition")MEDIAN _='median'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy.MEDIAN "Link to this definition")MOST\_FREQUENT _='most\_frequent'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy.MOST_FREQUENT "Link to this definition")NEXT _='next'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy.NEXT "Link to this definition")NO\_IMPUTATION _='no\_imputation'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy.NO_IMPUTATION "Link to this definition")PREVIOUS _='previous'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy.PREVIOUS "Link to this definition")VALUE _='value'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.ImputationStrategy.VALUE "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.Metrics [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#Metrics) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics "Link to this definition")

Bases: `object`

Supported types of classification and regression metrics in AutoAI.

ACCURACY\_AND\_DISPARATE\_IMPACT\_SCORE _='accuracy\_and\_disparate\_impact'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.ACCURACY_AND_DISPARATE_IMPACT_SCORE "Link to this definition")ACCURACY\_SCORE _='accuracy'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.ACCURACY_SCORE "Link to this definition")AVERAGE\_PRECISION\_SCORE _='average\_precision'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.AVERAGE_PRECISION_SCORE "Link to this definition")EXPLAINED\_VARIANCE\_SCORE _='explained\_variance'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.EXPLAINED_VARIANCE_SCORE "Link to this definition")F1\_SCORE _='f1'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.F1_SCORE "Link to this definition")F1\_SCORE\_MACRO _='f1\_macro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.F1_SCORE_MACRO "Link to this definition")F1\_SCORE\_MICRO _='f1\_micro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.F1_SCORE_MICRO "Link to this definition")F1\_SCORE\_WEIGHTED _='f1\_weighted'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.F1_SCORE_WEIGHTED "Link to this definition")LOG\_LOSS _='neg\_log\_loss'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.LOG_LOSS "Link to this definition")MEAN\_ABSOLUTE\_ERROR _='neg\_mean\_absolute\_error'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.MEAN_ABSOLUTE_ERROR "Link to this definition")MEAN\_SQUARED\_ERROR _='neg\_mean\_squared\_error'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.MEAN_SQUARED_ERROR "Link to this definition")MEAN\_SQUARED\_LOG\_ERROR _='neg\_mean\_squared\_log\_error'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.MEAN_SQUARED_LOG_ERROR "Link to this definition")MEDIAN\_ABSOLUTE\_ERROR _='neg\_median\_absolute\_error'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.MEDIAN_ABSOLUTE_ERROR "Link to this definition")PRECISION\_SCORE _='precision'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.PRECISION_SCORE "Link to this definition")PRECISION\_SCORE\_MACRO _='precision\_macro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.PRECISION_SCORE_MACRO "Link to this definition")PRECISION\_SCORE\_MICRO _='precision\_micro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.PRECISION_SCORE_MICRO "Link to this definition")PRECISION\_SCORE\_WEIGHTED _='precision\_weighted'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.PRECISION_SCORE_WEIGHTED "Link to this definition")R2\_AND\_DISPARATE\_IMPACT\_SCORE _='r2\_and\_disparate\_impact'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.R2_AND_DISPARATE_IMPACT_SCORE "Link to this definition")R2\_SCORE _='r2'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.R2_SCORE "Link to this definition")RECALL\_SCORE _='recall'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.RECALL_SCORE "Link to this definition")RECALL\_SCORE\_MACRO _='recall\_macro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.RECALL_SCORE_MACRO "Link to this definition")RECALL\_SCORE\_MICRO _='recall\_micro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.RECALL_SCORE_MICRO "Link to this definition")RECALL\_SCORE\_WEIGHTED _='recall\_weighted'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.RECALL_SCORE_WEIGHTED "Link to this definition")ROC\_AUC\_SCORE _='roc\_auc'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.ROC_AUC_SCORE "Link to this definition")ROOT\_MEAN\_SQUARED\_ERROR _='neg\_root\_mean\_squared\_error'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.ROOT_MEAN_SQUARED_ERROR "Link to this definition")ROOT\_MEAN\_SQUARED\_LOG\_ERROR _='neg\_root\_mean\_squared\_log\_error'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Metrics.ROOT_MEAN_SQUARED_LOG_ERROR "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.MetricsToDirections( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#MetricsToDirections) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections "Link to this definition")

Bases: `Enum`

Map of metrics directions.

ACCURACY _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.ACCURACY "Link to this definition")AVERAGE\_PRECISION _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.AVERAGE_PRECISION "Link to this definition")EXPLAINED\_VARIANCE _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.EXPLAINED_VARIANCE "Link to this definition")F1 _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.F1 "Link to this definition")F1\_MACRO _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.F1_MACRO "Link to this definition")F1\_MICRO _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.F1_MICRO "Link to this definition")F1\_WEIGHTED _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.F1_WEIGHTED "Link to this definition")NEG\_LOG\_LOSS _='descending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.NEG_LOG_LOSS "Link to this definition")NEG\_MEAN\_ABSOLUTE\_ERROR _='descending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.NEG_MEAN_ABSOLUTE_ERROR "Link to this definition")NEG\_MEAN\_SQUARED\_ERROR _='descending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.NEG_MEAN_SQUARED_ERROR "Link to this definition")NEG\_MEAN\_SQUARED\_LOG\_ERROR _='descending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.NEG_MEAN_SQUARED_LOG_ERROR "Link to this definition")NEG\_MEDIAN\_ABSOLUTE\_ERROR _='descending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.NEG_MEDIAN_ABSOLUTE_ERROR "Link to this definition")NEG\_ROOT\_MEAN\_SQUARED\_ERROR _='descending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.NEG_ROOT_MEAN_SQUARED_ERROR "Link to this definition")NEG\_ROOT\_MEAN\_SQUARED\_LOG\_ERROR _='descending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.NEG_ROOT_MEAN_SQUARED_LOG_ERROR "Link to this definition")NORMALIZED\_GINI\_COEFFICIENT _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.NORMALIZED_GINI_COEFFICIENT "Link to this definition")PRECISION _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.PRECISION "Link to this definition")PRECISION\_MACRO _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.PRECISION_MACRO "Link to this definition")PRECISION\_MICRO _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.PRECISION_MICRO "Link to this definition")PRECISION\_WEIGHTED _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.PRECISION_WEIGHTED "Link to this definition")R2 _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.R2 "Link to this definition")RECALL _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.RECALL "Link to this definition")RECALL\_MACRO _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.RECALL_MACRO "Link to this definition")RECALL\_MICRO _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.RECALL_MICRO "Link to this definition")RECALL\_WEIGHTED _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.RECALL_WEIGHTED "Link to this definition")ROC\_AUC _='ascending'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.MetricsToDirections.ROC_AUC "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.PipelineTypes [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#PipelineTypes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PipelineTypes "Link to this definition")

Bases: `object`

Supported types of Pipelines.

LALE _='lale'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PipelineTypes.LALE "Link to this definition")SKLEARN _='sklearn'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PipelineTypes.SKLEARN "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.PositiveLabelClass [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#PositiveLabelClass) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass "Link to this definition")

Bases: `object`

Metrics that need positive label definition for binary classification.

AVERAGE\_PRECISION\_SCORE _='average\_precision'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.AVERAGE_PRECISION_SCORE "Link to this definition")F1\_SCORE _='f1'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.F1_SCORE "Link to this definition")F1\_SCORE\_MACRO _='f1\_macro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.F1_SCORE_MACRO "Link to this definition")F1\_SCORE\_MICRO _='f1\_micro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.F1_SCORE_MICRO "Link to this definition")F1\_SCORE\_WEIGHTED _='f1\_weighted'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.F1_SCORE_WEIGHTED "Link to this definition")PRECISION\_SCORE _='precision'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.PRECISION_SCORE "Link to this definition")PRECISION\_SCORE\_MACRO _='precision\_macro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.PRECISION_SCORE_MACRO "Link to this definition")PRECISION\_SCORE\_MICRO _='precision\_micro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.PRECISION_SCORE_MICRO "Link to this definition")PRECISION\_SCORE\_WEIGHTED _='precision\_weighted'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.PRECISION_SCORE_WEIGHTED "Link to this definition")RECALL\_SCORE _='recall'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.RECALL_SCORE "Link to this definition")RECALL\_SCORE\_MACRO _='recall\_macro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.RECALL_SCORE_MACRO "Link to this definition")RECALL\_SCORE\_MICRO _='recall\_micro'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.RECALL_SCORE_MICRO "Link to this definition")RECALL\_SCORE\_WEIGHTED _='recall\_weighted'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PositiveLabelClass.RECALL_SCORE_WEIGHTED "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.PredictionType [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#PredictionType) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PredictionType "Link to this definition")

Bases: `object`

Supported types of learning.

BINARY _='binary'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PredictionType.BINARY "Link to this definition")CLASSIFICATION _='classification'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PredictionType.CLASSIFICATION "Link to this definition")FORECASTING _='forecasting'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PredictionType.FORECASTING "Link to this definition")MULTICLASS _='multiclass'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PredictionType.MULTICLASS "Link to this definition")REGRESSION _='regression'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PredictionType.REGRESSION "Link to this definition")TIMESERIES\_ANOMALY\_PREDICTION _='timeseries\_anomaly\_prediction'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.PredictionType.TIMESERIES_ANOMALY_PREDICTION "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.RAGMetrics [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#RAGMetrics) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RAGMetrics "Link to this definition")

Bases: `object`

Supported types of AutoAI RAG metrics

ANSWER\_CORRECTNESS _='answer\_correctness'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RAGMetrics.ANSWER_CORRECTNESS "Link to this definition")CONTEXT\_CORRECTNESS _='context\_correctness'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RAGMetrics.CONTEXT_CORRECTNESS "Link to this definition")FAITHFULNESS _='faithfulness'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RAGMetrics.FAITHFULNESS "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.RegressionAlgorithms( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#RegressionAlgorithms) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms "Link to this definition")

Bases: `Enum`

Regression algorithms that AutoAI can use for IBM Cloud.

DT _='DecisionTreeRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms.DT "Link to this definition")EX\_TREES _='ExtraTreesRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms.EX_TREES "Link to this definition")GB _='GradientBoostingRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms.GB "Link to this definition")LGBM _='LGBMRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms.LGBM "Link to this definition")LR _='LinearRegression'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms.LR "Link to this definition")RF _='RandomForestRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms.RF "Link to this definition")RIDGE _='Ridge'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms.RIDGE "Link to this definition")SnapBM _='SnapBoostingMachineRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms.SnapBM "Link to this definition")SnapDT _='SnapDecisionTreeRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms.SnapDT "Link to this definition")SnapRF _='SnapRandomForestRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms.SnapRF "Link to this definition")XGB _='XGBRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithms.XGB "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.RegressionAlgorithmsCP4D( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#RegressionAlgorithmsCP4D) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D "Link to this definition")

Bases: `Enum`

Regression algorithms that AutoAI can use for IBM Cloud Pak® for Data(CP4D).
The SnapML estimators (SnapDT, SnapRF, SnapBM) are supported
on IBM Cloud Pak® for Data version 4.0.2 and later.

DT _='DecisionTreeRegressorEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D.DT "Link to this definition")EX\_TREES _='ExtraTreesRegressorEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D.EX_TREES "Link to this definition")GB _='GradientBoostingRegressorEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D.GB "Link to this definition")LGBM _='LGBMRegressorEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D.LGBM "Link to this definition")LR _='LinearRegressionEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D.LR "Link to this definition")RF _='RandomForestRegressorEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D.RF "Link to this definition")RIDGE _='RidgeEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D.RIDGE "Link to this definition")SnapBM _='SnapBoostingMachineRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D.SnapBM "Link to this definition")SnapDT _='SnapDecisionTreeRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D.SnapDT "Link to this definition")SnapRF _='SnapRandomForestRegressor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D.SnapRF "Link to this definition")XGB _='XGBRegressorEstimator'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RegressionAlgorithmsCP4D.XGB "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.RunStateTypes [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#RunStateTypes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RunStateTypes "Link to this definition")

Bases: `object`

Supported types of AutoAI fit/run.

COMPLETED _='completed'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RunStateTypes.COMPLETED "Link to this definition")FAILED _='failed'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.RunStateTypes.FAILED "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.SamplingTypes [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#SamplingTypes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.SamplingTypes "Link to this definition")

Bases: `object`

Types of training data sampling.

FIRST\_VALUES _='first\_n\_records'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.SamplingTypes.FIRST_VALUES "Link to this definition")LAST\_VALUES _='truncate'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.SamplingTypes.LAST_VALUES "Link to this definition")RANDOM _='random'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.SamplingTypes.RANDOM "Link to this definition")STRATIFIED _='stratified'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.SamplingTypes.STRATIFIED "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.TShirtSize [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#TShirtSize) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TShirtSize "Link to this definition")

Bases: `object`

Possible sizes of the AutoAI POD.
Depending on the POD size, AutoAI can support different data set sizes.

- S - small (2vCPUs and 8GB of RAM)

- M - Medium (4vCPUs and 16GB of RAM)

- L - Large (8vCPUs and 32GB of RAM))

- XL - Extra Large (16vCPUs and 64GB of RAM)


L _='l'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TShirtSize.L "Link to this definition")M _='m'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TShirtSize.M "Link to this definition")S _='s'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TShirtSize.S "Link to this definition")XL _='xl'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TShirtSize.XL "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.TimeseriesAnomalyPredictionAlgorithms( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#TimeseriesAnomalyPredictionAlgorithms) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TimeseriesAnomalyPredictionAlgorithms "Link to this definition")

Bases: `Enum`

Timeseries Anomaly Prediction algorithms that AutoAI can use for IBM Cloud.

Forecasting _='Forecasting'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TimeseriesAnomalyPredictionAlgorithms.Forecasting "Link to this definition")Relationship _='Relationship'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TimeseriesAnomalyPredictionAlgorithms.Relationship "Link to this definition")Window _='Window'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TimeseriesAnomalyPredictionAlgorithms.Window "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.TimeseriesAnomalyPredictionPipelineTypes( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#TimeseriesAnomalyPredictionPipelineTypes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TimeseriesAnomalyPredictionPipelineTypes "Link to this definition")

Bases: `Enum`

Timeseries Anomaly Prediction pipeline types that AutoAI can use for IBM Cloud.

PointwiseBoundedBATS _='PointwiseBoundedBATS'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TimeseriesAnomalyPredictionPipelineTypes.PointwiseBoundedBATS "Link to this definition")PointwiseBoundedBATSForceUpdate _='PointwiseBoundedBATSForceUpdate'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TimeseriesAnomalyPredictionPipelineTypes.PointwiseBoundedBATSForceUpdate "Link to this definition")PointwiseBoundedHoltWintersAdditive _='PointwiseBoundedHoltWintersAdditive'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TimeseriesAnomalyPredictionPipelineTypes.PointwiseBoundedHoltWintersAdditive "Link to this definition")WindowLOF _='WindowLOF'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TimeseriesAnomalyPredictionPipelineTypes.WindowLOF "Link to this definition")WindowNN _='WindowNN'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TimeseriesAnomalyPredictionPipelineTypes.WindowNN "Link to this definition")WindowPCA _='WindowPCA'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.TimeseriesAnomalyPredictionPipelineTypes.WindowPCA "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.Transformers [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#Transformers) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers "Link to this definition")

Bases: `object`

Supported types of congito transformers names in AutoAI.

ABS _='abs'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.ABS "Link to this definition")CBRT _='cbrt'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.CBRT "Link to this definition")COS _='cos'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.COS "Link to this definition")CUBE _='cube'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.CUBE "Link to this definition")DIFF _='diff'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.DIFF "Link to this definition")DIVIDE _='divide'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.DIVIDE "Link to this definition")FEATUREAGGLOMERATION _='featureagglomeration'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.FEATUREAGGLOMERATION "Link to this definition")ISOFORESTANOMALY _='isoforestanomaly'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.ISOFORESTANOMALY "Link to this definition")LOG _='log'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.LOG "Link to this definition")MAX _='max'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.MAX "Link to this definition")MINMAXSCALER _='minmaxscaler'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.MINMAXSCALER "Link to this definition")NXOR _='nxor'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.NXOR "Link to this definition")PCA _='pca'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.PCA "Link to this definition")PRODUCT _='product'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.PRODUCT "Link to this definition")ROUND _='round'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.ROUND "Link to this definition")SIGMOID _='sigmoid'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.SIGMOID "Link to this definition")SIN _='sin'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.SIN "Link to this definition")SQRT _='sqrt'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.SQRT "Link to this definition")SQUARE _='square'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.SQUARE "Link to this definition")STDSCALER _='stdscaler'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.STDSCALER "Link to this definition")SUM _='sum'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.SUM "Link to this definition")TAN _='tan'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.Transformers.TAN "Link to this definition")_class_ ibm\_watsonx\_ai.utils.autoai.enums.VisualizationTypes [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/utils/autoai/enums.html#VisualizationTypes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.VisualizationTypes "Link to this definition")

Bases: `object`

Types of visualization options.

INPLACE _='inplace'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.VisualizationTypes.INPLACE "Link to this definition")PDF _='pdf'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#ibm_watsonx_ai.utils.autoai.enums.VisualizationTypes.PDF "Link to this definition")