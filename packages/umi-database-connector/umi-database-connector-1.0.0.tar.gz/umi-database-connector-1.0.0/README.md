# UMI database connector
This is a python wrapper for streamlining the querying process for our python services.

## Class DatabaseConnector
A singleton that manages the MongoDB client and connections to different databases on the same cluster

### Class method:

#### Query method:
1. find(query: Dict) -> List or Cursor
2. update(query: Dict) -> Dict
3. TODO delete(query: Dict) -> Dict

#### Query object structure:
