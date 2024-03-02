import os
import json
import toml
import importlib.util
import inspect
import ast
import re

class FunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.functions = []

    def visit_FunctionDef(self, node):
        self.functions.append(node)

def extract_function_code(module_path, function_name):
    spec = importlib.util.spec_from_file_location("module.name", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    function = getattr(module, function_name)
    return inspect.getsource(function)

def extract_functions_from_module(module_path):
    with open(module_path, "r") as f:
        tree = ast.parse(f.read(), filename=module_path)
        visitor = FunctionVisitor()
        visitor.visit(tree)
        functions = [ast.unparse(func) for func in visitor.functions]
        return functions

def extract_function_code_from_imports(module_path, function_name):
    with open(module_path, "r") as f:
        tree = ast.parse(f.read(), filename=module_path)
        for node in tree.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    try:
                        module = importlib.import_module(alias.name)
                        source_path = inspect.getsourcefile(module)
                        if source_path:
                            functions = extract_functions_from_module(source_path)
                            for func_code in functions:
                                if function_name in func_code:
                                    return func_code
                    except ImportError:
                        pass
            elif isinstance(node, ast.ImportFrom):
                try:
                    module = importlib.import_module(node.module)
                    source_path = inspect.getsourcefile(module)
                    if source_path:
                        functions = extract_functions_from_module(source_path)
                        for func_code in functions:
                            if function_name in func_code:
                                return func_code
                except ImportError:
                    pass
    return None

def extract_register_function(folder_path):
    pipeline_file_path = os.path.join(folder_path, "pipeline.py")
    
    if os.path.exists(pipeline_file_path):
        with open(pipeline_file_path, "r") as f:
            lines = f.readlines()
            register_function_lines = []
            found_register_function = False
            for line in lines:
                if found_register_function:
                    if line.strip():  # Check if line is not empty
                        register_function_lines.append(line.rstrip())
                    else:
                        break
                elif "def register(" in line:
                    found_register_function = True
                    register_function_lines.append(line.rstrip())
            if register_function_lines:
                register_function = "\n".join(register_function_lines)
                return register_function.strip()

    return None

def extract_node_name(node_code):
    match = re.search(r"Node\(name='(.+?)'", node_code)
    if match:
        return match.group(1)
    return None

def extract_node_inputs(node_code):
    inputs = []
    for keyword in node_code.keywords:
        if keyword.arg == "inputs" and isinstance(keyword.value, ast.List):
            for input_elt in keyword.value.elts:
                input_str = ast.unparse(input_elt)
                if isinstance(input_str, str):
                    inputs.append(input_str)
    return inputs

def extract_node_description(function_code):
    if function_code:
        match = re.search(r'"""(.*?)"""', function_code, re.DOTALL)
        if match:
            return match.group(1).strip()
    return None

def extract_register_description(register_function_code):
    if register_function_code:
        match = re.search(r'"""(.*?)"""', register_function_code, re.DOTALL)
        if match:
            return match.group(1).strip()
    return None

def extract_nodes_info(folder_path):
    pipeline_file_path = os.path.join(folder_path, "pipeline.py")
    
    if os.path.exists(pipeline_file_path):
        with open(pipeline_file_path, "r") as f:
            tree = ast.parse(f.read(), filename=pipeline_file_path)
            
            nodes = []
            for node_def in tree.body:
                if isinstance(node_def, ast.FunctionDef) and node_def.name == "register":
                    for node_assign in node_def.body:
                        if isinstance(node_assign, ast.Assign):
                            for target in node_assign.targets:
                                if isinstance(target, ast.Name) and target.id == "nodes":
                                    for node_list_elt in node_assign.value.elts:
                                        if isinstance(node_list_elt, ast.Call):
                                            node_name = None
                                            node_function = None
                                            node_inputs = []
                                            
                                            for arg in node_list_elt.args:
                                                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                                                    node_name = arg.value
                                            
                                            for keyword in node_list_elt.keywords:
                                                if keyword.arg == "function" and isinstance(keyword.value, ast.Name):
                                                    node_function = keyword.value.id
                                                    # Extract function code
                                                    function_code = None
                                                    if node_function != "register":
                                                        function_code = extract_function_code(pipeline_file_path, node_function)
                                                        if not function_code:
                                                            function_code = extract_function_code_from_imports(pipeline_file_path, node_function)
                                                    node_function = function_code if function_code else node_function
                                                elif keyword.arg == "inputs" and isinstance(keyword.value, ast.List):
                                                    for input_elt in keyword.value.elts:
                                                        if isinstance(input_elt, ast.Constant) and isinstance(input_elt.value, str):
                                                            node_inputs.append(input_elt.value)
                                            
                                            node_description = extract_node_description(function_code)
                                            
                                            nodes.append({
                                                "name": extract_node_name(ast.unparse(node_list_elt)),  # Extract node name
                                                "function": node_function,
                                                "inputs": extract_node_inputs(node_list_elt),
                                                "description": node_description if node_description else ""  # Use empty string if no description found
                                            })
                                            
            return nodes
    
    return None

def extract_register_info(folder_path):
    pipeline_file_path = os.path.join(folder_path, "pipeline.py")
    
    if os.path.exists(pipeline_file_path):
        with open(pipeline_file_path, "r") as f:
            tree = ast.parse(f.read(), filename=pipeline_file_path)
            for node_def in tree.body:
                if isinstance(node_def, ast.FunctionDef) and node_def.name == "register":
                    register_function_code = ast.unparse(node_def)
                    register_description = extract_register_description(register_function_code)
                    return register_description
    
    return None

def extract_data_classes_info(current_directory):
    data_classes_info = []
    data_file_path = os.path.join(current_directory, "data.py")
    if os.path.exists(data_file_path):
        with open(data_file_path, 'r') as f:
            tree = ast.parse(f.read(), filename=data_file_path)
            for node in tree.body:
                if isinstance(node, ast.ClassDef):
                    class_description = ast.get_docstring(node)
                    class_code = ast.unparse(node)
                    
                    class_name_match = re.search(r"name\s*=\s*'([^']*)'", class_code)
                    class_name = class_name_match.group(1) if class_name_match else "Unknown"
                    
                    data_classes_info.append({
                        "name": class_name,
                        "description": class_description if class_description else "",
                        "code": class_code
                    })
    return data_classes_info

def main():
    current_directory = os.getcwd()
    toml_file_path = os.path.join(current_directory, "project.toml")

    with open(toml_file_path, "r") as f:
        toml_data = toml.load(f)
        project_name = toml_data["project"]["name"]
        place = toml_data["project"]["place"]

    place_path = os.path.join(current_directory, place)

    if not os.path.exists(place_path):
        print(f"Der angegebene Ordner '{place}' existiert nicht.")
        return

    pipeline_folders = [folder for folder in os.listdir(place_path) if os.path.isdir(os.path.join(place_path, folder))]

    data = {
        "ProjectName": project_name,
        "DataClasses": extract_data_classes_info(current_directory),
        "Pipelines": {}
    }

    for folder in pipeline_folders:
        folder_path = os.path.join(place_path, folder)
        register_function = extract_register_function(folder_path)
        register_description = extract_register_description(register_function)
        nodes_info = extract_nodes_info(folder_path)
        data["Pipelines"][folder] = {
            "RegisterFunction": {
                "Function": register_function,
                "Description": register_description if register_description else ""
            },
            "Nodes": nodes_info
        }

    json_file_path = os.path.join(current_directory, "info.json")
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("JSON-Datei erfolgreich erstellt.")


if __name__ == "__main__":
    main()
