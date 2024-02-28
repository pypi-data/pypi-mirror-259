# `neon_client`: an api wrapper for the [Neon API](https://api-docs.neon.tech/reference/getting-started-with-neon-api).

`neon_client` is a Python wrapper designed to simplify interactions with the [Neon API](https://api-docs.neon.tech/reference/getting-started-with-neon-api). It provides a convenient way for developers to integrate their Python applications with the Neon platform, offering methods to manage API keys, projects, branches, databases, endpoints, roles, and operations programmatically.

With `neon_client`, you can automate tasks, streamline workflows, and build powerful integrations with ease.


## Installation

```bash
$ pip install neon-client
```

**Please Note**: this repository is a work in progress.  The package is not yet available on PyPi.  The above command will not work.


## Usage

```python
from neon_client import NeonAPI

# Initialize the client.
neon = NeonAPI(api_key='your_api_key')
```

Remember that you should never expose your api_key and handle it carefully since it gives access to sensitive data. It's better to set it as an environment variable (e.g. `NEON_API_KEY` + accompanying `neon_client.from_environ()`).

-------

### Methods of the `NeonAPI` class:

- `me()`: Returns the current user.

**Manage API keys**:

- `api_keys()`: Returns a list of API keys.
- `api_key_create(**json)`: Creates an API key.
- `api_key_delete(key_id)`: Deletes a given API key.

**Manage projects**:

- `projects()`: Returns a list of projects.
- `project(project_id)`: Returns a specific project.
- `project_create(project_id, **json)`: Creates a new project. 
- `project_update(project_id, **json)`: Updates a given project.
- `project_delete(project_id)`: Deletes a given project.
- `project_permissions(project_id)`: Returns a list of permissions for a given project.
- `project_permissions_grant(project_id, **json)`: Grant permissions to a given project.
- `project_permissions_revoke(project_id, **json)`: Revoke permissions from a given project.

**Manage branches**:

- `branches(project_id)`: Returns a list of branches for a given project.
- `branch(project_id, branch_id)`: Returns a specific branch.
- `branch_create(project_id, **json)`: Creates a new branch.
- `branch_update(project_id, branch_id, **json)`: Updates a given branch.
- `branch_delete(project_id, branch_id)`: Deletes a given branch.
- `branch_set_as_primary(project_id, branch_id)`: Sets a given branch as primary.

**Manage databases**:

- `databases(project_id, branch_id)`: Returns a list of databases for a given project and branch.
- `database(project_id, branch_id, database_id)`: Returns a specific database.
- `database_create(project_id, branch_id, **json)`: Creates a new database.
- `database_update(project_id, branch_id, **json)`: Updates a given database.
- `database_delete(project_id, branch_id, database_id)`: Deletes a given database.

**Manage endpoints**:

- `endpoints(project_id, branch_id)`: Returns a list of endpoints for a given project and branch.
- `endpoint_create(project_id, branch_id, **json)`: Creates a new endpoint.
- `endpoint_update(project_id, branch_id, endpoint_id, **json)`: Updates a given endpoint.
- `endpoint_delete(project_id, branch_id, endpoint_id)`: Deletes a given endpoint.
- `endpoint_start(project_id, branch_id, endpoint_id)`: Starts a given endpoint.
- `endpoint_suspend(project_id, branch_id, endpoint_id)`: Suspends a given endpoint.

**Manage roles**:

- `roles(project_id, branch_id)`: Returns a list of roles for a given project and branch.
- `role(project_id, branch_id, role_name)`: Returns a specific role.
- `role_create(project_id, branch_id, role_name)`: Creates a new role.
- `role_delete(project_id, branch_id, role_name)`: Deletes a given role.
- `role_password_reveal(project_id, branch_id, role_name)`: Reveals the password for a given role.
- `role_password_reset(project_id, branch_id, role_name)`: Resets the password for a given role.

**Manage operations**:

- `operations(project_id)`: Returns a list of operations for a given project.
- `operation(project_id, operation_id)`: Returns a specific operation.

**Experimental**:

- `consumption()`: Returns a list of project consumption metrics.


View the [Neon API documentation](https://api-docs.neon.tech/reference/getting-started-with-neon-api) for more information on the available endpoints and their parameters.


## Development

Installation is simple with `pipenv`. Just run the following command in the root directory of the repository:

```bash
$ pipenv install --dev
```

This will install all the necessary dependencies for development.

To run the tests, use the following command:

```bash
$ make test
```

The tests don't require an internet connection, as they are mocked using the `pytest-vcr` library. To record new cassettes, use the following command:

```bash
$ make record
```

This will record new cassettes for the tests. Make sure to commit these cassettes along with your changes.

## License & Copyright

[MIT licensed](./LICENSE).
