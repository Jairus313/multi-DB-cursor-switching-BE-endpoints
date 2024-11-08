# multi-DB-cursor-switching-BE-endpoints

## Agenda of the project.

I have been ask to build and FastAPI app with SQLAlchemy as ORM(pretty basic app) but here's the catch and it's actually the DB design. So the data for the each individual user will be present in different DBs and it needs to be queried from the endpoint where cursor of the DB switches by itself depending upon the user askes, meaning we will a master DB which stores the high-level data of the all user and anything specific about the user will be saved in their own DB. Here's bit schema design to make things clear.

```sh
    master_db.root_schema.user_table
    --------------------------------
    user_name
    user_db_url
    user_db_host
    user_db_name
    user_db_username
    user_db_password


    <user_name>.root_schema.user_info
    --------------------------------
    user_firstname
    user_lastname

```

### Example:

**Root DB:**

<div style="overflow-x:auto;">
  
| user_name  | user_db_url       | user_db_host   | user_db_name    | user_db_username | user_db_password |
|------------|-------------------|----------------|-----------------|------------------|------------------|
| john_doe   | db1.example.com   | 192.168.1.101 | john_doe_db     | john_doe_user    | password123      |
| jane_smith | db2.example.com   | 192.168.1.102 | jane_smith_db   | jane_smith_user  | securepass456    |

</div>

**User1 DB:**

<div style="overflow-x:auto;">
  
**john_doe.root_schema.user_info**

| user_firstname | user_lastname |
| -------------- | ------------- |
| John           | Doe           |

</div>

**User2 DB:**

<div style="overflow-x:auto;">

**jane_smith.root_schema.user_info**

| user_firstname | user_lastname |
| -------------- | ------------- |
| Jane           | Smith         |

</div>

Hope this clears the requirement. Let's building it.
