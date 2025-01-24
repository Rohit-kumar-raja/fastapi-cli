Here's a draft for the documentation of your command-line interface (CLI) tool, focusing on the structure and usage of the provided commands: 

---

# **FastAPI CLI (fpcli) Documentation**

The `fpcli` tool is designed to streamline the development process of FastAPI projects by providing a set of commands to generate common components and manage project structure efficiently.

## **Installation**

To use the CLI, ensure you have Python 3.12 installed and install the tool via `setup.py`:

```bash
python setup.py install
```

You can also install shell completion for easier use:

```bash
fpcli --install-completion
```

---

## **Command Overview**

Below is a list of the available commands along with their descriptions and usage examples.

### Global Options

- `--install-completion`  
  Installs shell completion for the current shell.  
  Example:  
  ```bash
  fpcli --install-completion
  ```

- `--show-completion`  
  Displays shell completion script for manual installation or customization.  
  Example:  
  ```bash
  fpcli --show-completion
  ```

- `--help`  
  Displays help information about the CLI or a specific command.  
  Example:  
  ```bash
  fpcli --help
  ```

---

### **Commands**

#### **`make:controller`**
Generate a FastAPI controller file within a specific app.

**Usage:**  
```bash
fpcli make:controller <controller_name> --app <app_name>
```

**Example:**  
```bash
fpcli make:controller user_controller --app users
```

---

#### **`make:model`**
Generate a Beanie ODM model file within a specific app.

**Usage:**  
```bash
fpcli make:model <model_name> --app <app_name>
```

**Example:**  
```bash
fpcli make:model UserModel --app users
```

---

#### **`make:validator`**
Generate a Pydantic validator file within a specific app.

**Usage:**  
```bash
fpcli make:validator <validator_name> --app <app_name>
```

**Example:**  
```bash
fpcli make:validator UserValidator --app users
```

---

#### **`make:service`**
Generate a service class file within a specific app.

**Usage:**  
```bash
fpcli make:service <service_name> --app <app_name>
```

**Example:**  
```bash
fpcli make:service UserService --app users
```

---

#### **`make:middleware`**
Generate a middleware file within a specific app.

**Usage:**  
```bash
fpcli make:middleware <middleware_name> --app <app_name>
```

**Example:**  
```bash
fpcli make:middleware AuthMiddleware --app common
```

---

#### **`make:seeder`**
Generate a seeder file within a specific app.

**Usage:**  
```bash
fpcli make:seeder <seeder_name> --app <app_name>
```

**Example:**  
```bash
fpcli make:seeder UserSeeder --app users
```

---

#### **`startapp`**
Create a new app structure for FastAPI with top-level files (e.g., `urls.py`, `models.py`).

**Usage:**  
```bash
fpcli startapp <app_name>
```

**Example:**  
```bash
fpcli startapp users
```

---

#### **`make:routes`**
Generate a route file with user-defined routes in a specific app.

**Usage:**  
```bash
fpcli make:routes <route_file_name> --app <app_name> --routes <routes_list>
```

- `<routes_list>`: A string of comma-separated HTTP methods, e.g., `'GET,POST,PUT'`.

**Example:**  
```bash
fpcli make:routes user_routes --app users --routes "GET,POST"
```

---

## **Testing and Debugging**

To run the provided test file:

```bash
python test.py
```

To debug, use the `--help` option to inspect specific commands:

```bash
fpcli <command> --help
```



This documentation provides an overview of `fpcli` commands and their uses. Customize and expand as needed for your development workflow. 