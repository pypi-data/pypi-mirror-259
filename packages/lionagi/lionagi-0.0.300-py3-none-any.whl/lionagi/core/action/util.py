import inspect

from lionagi.core.schema import Tool


def func_to_tool(func_, parser=None, docstring_style="google"):
    """
    Transforms a given function into a Tool object, equipped with a schema derived
    from its docstring. This process involves parsing the function's docstring based
    on a specified style ('google' or 'reST') to extract relevant metadata and
    parameters, which are then used to construct a comprehensive schema for the Tool.
    This schema facilitates the integration of the function with systems or
    frameworks that rely on structured metadata for automation, documentation, or
    interface generation purposes.

    The function to be transformed can be any callable that adheres to the
    specified docstring conventions. The resulting Tool object encapsulates the
    original function, allowing it to be utilized within environments that require
    objects with structured metadata.

    Args:
        func_ (Callable): The function to be transformed into a Tool object. This
                          function should have a docstring that follows the
                          specified docstring style for accurate schema generation.
        parser (Optional[Any]): An optional parser object associated with the Tool.
                                This parameter is currently not utilized in the
                                transformation process but is included for future
                                compatibility and extension purposes.
        docstring_style (str): The format of the docstring to be parsed, indicating
                               the convention used in the function's docstring.
                               Supports 'google' for Google-style docstrings and
                               'reST' for reStructuredText-style docstrings. The
                               chosen style affects how the docstring is parsed and
                               how the schema is generated.

    Returns:
        Tool: An object representing the original function wrapped as a Tool, along
              with its generated schema. This Tool object can be used in systems that
              require detailed metadata about functions, facilitating tasks such as
              automatic documentation generation, user interface creation, or
              integration with other software tools.

    Examples:
        >>> def example_function_google(param1: int, param2: str) -> bool:
        ...     '''
        ...     An example function using Google style docstrings.
        ...
        ...     Args:
        ...         param1 (int): The first parameter, demonstrating an integer input_.
        ...         param2 (str): The second parameter, demonstrating a string input_.
        ...
        ...     Returns:
        ...         bool: A boolean value, illustrating the return type.
        ...     '''
        ...     return True
        ...
        >>> tool_google = func_to_tool(example_function_google, docstring_style='google')
        >>> print(isinstance(tool_google, Tool))
        True

        >>> def example_function_reST(param1: int, param2: str) -> bool:
        ...     '''
        ...     An example function using reStructuredText (reST) style docstrings.
        ...
        ...     :param param1: The first parameter, demonstrating an integer input_.
        ...     :type param1: int
        ...     :param param2: The second parameter, demonstrating a string input_.
        ...     :type param2: str
        ...     :returns: A boolean value, illustrating the return type.
        ...     :rtype: bool
        ...     '''
        ...     return True
        ...
        >>> tool_reST = func_to_tool(example_function_reST, docstring_style='reST')
        >>> print(isinstance(tool_reST, Tool))
        True

    Note:
        The transformation process relies heavily on the accuracy and completeness of
        the function's docstring. Functions with incomplete or incorrectly formatted
        docstrings may result in incomplete or inaccurate Tool schemas.
    """
    schema = _func_to_schema(func_, docstring_style)
    return Tool(func=func_, parser=parser, schema_=schema)


def _extract_docstring_details_google(func):
    """
    Extracts the function description and parameter descriptions from the
    docstring following the Google style format.

    Args:
        func (Callable): The function from which to extract docstring details.

    Returns:
        Tuple[str, Dict[str, str]]: A tuple containing the function description
        and a dictionary with parameter names as keys and their descriptions as values.

    Examples:
        >>> def example_function(param1: int, param2: str):
        ...     '''Example function.
        ...
        ...     Args:
        ...         param1 (int): The first parameter.
        ...         param2 (str): The second parameter.
        ...     '''
        ...     pass
        >>> description, params = _extract_docstring_details_google(example_function)
        >>> description
        'Example function.'
        >>> params == {'param1': 'The first parameter.', 'param2': 'The second parameter.'}
        True
    """
    docstring = inspect.getdoc(func)
    if not docstring:
        return "No description available.", {}
    lines = docstring.split("\n")
    func_description = lines[0].strip()

    param_start_pos = 0
    lines_len = len(lines)

    params_description = {}
    for i in range(1, lines_len):
        if (
            lines[i].startswith("Args")
            or lines[i].startswith("Arguments")
            or lines[i].startswith("Parameters")
        ):
            param_start_pos = i + 1
            break

    current_param = None
    for i in range(param_start_pos, lines_len):
        if lines[i] == "":
            continue
        elif lines[i].startswith(" "):
            param_desc = lines[i].split(":", 1)
            if len(param_desc) == 1:
                params_description[current_param] += " " + param_desc[0].strip()
                continue
            param, desc = param_desc
            param = param.split("(")[0].strip()
            params_description[param] = desc.strip()
            current_param = param
        else:
            break
    return func_description, params_description


def _extract_docstring_details_rest(func):
    """
    Extracts the function description and parameter descriptions from the
    docstring following the reStructuredText (reST) style format.

    Args:
        func (Callable): The function from which to extract docstring details.

    Returns:
        Tuple[str, Dict[str, str]]: A tuple containing the function description
        and a dictionary with parameter names as keys and their descriptions as values.

    Examples:
        >>> def example_function(param1: int, param2: str):
        ...     '''Example function.
        ...
        ...     :param param1: The first parameter.
        ...     :type param1: int
        ...     :param param2: The second parameter.
        ...     :type param2: str
        ...     '''
        ...     pass
        >>> description, params = _extract_docstring_details_rest(example_function)
        >>> description
        'Example function.'
        >>> params == {'param1': 'The first parameter.', 'param2': 'The second parameter.'}
        True
    """
    docstring = inspect.getdoc(func)
    if not docstring:
        return "No description available.", {}
    lines = docstring.split("\n")
    func_description = lines[0].strip()

    params_description = {}
    current_param = None
    for line in lines[1:]:
        line = line.strip()
        if line.startswith(":param"):
            param_desc = line.split(":", 2)
            _, param, desc = param_desc
            param = param.split()[-1].strip()
            params_description[param] = desc.strip()
            current_param = param
        elif line.startswith(" "):
            params_description[current_param] += " " + line

    return func_description, params_description


def _extract_docstring_details(func, style="google"):
    """
    Extracts the function description and parameter descriptions from the
    docstring of the given function using either Google style or reStructuredText
    (reST) style format.

    Args:
        func (Callable): The function from which to extract docstring details.
        style (str): The style of docstring to parse ('google' or 'reST').

    Returns:
        Tuple[str, Dict[str, str]]: A tuple containing the function description
        and a dictionary with parameter names as keys and their descriptions as values.

    Raises:
        ValueError: If an unsupported style is provided.

    Examples:
        >>> def example_function(param1: int, param2: str):
        ...     '''Example function.
        ...
        ...     Args:
        ...         param1 (int): The first parameter.
        ...         param2 (str): The second parameter.
        ...     '''
        ...     pass
        >>> description, params = _extract_docstring_details(example_function, style='google')
        >>> description
        'Example function.'
        >>> params == {'param1': 'The first parameter.', 'param2': 'The second parameter.'}
        True
    """
    if style == "google":
        func_description, params_description = _extract_docstring_details_google(func)
    elif style == "reST":
        func_description, params_description = _extract_docstring_details_rest(func)
    else:
        raise ValueError(
            f'{style} is not supported. Please choose either "google" or "reST".'
        )
    return func_description, params_description


def _python_to_json_type(py_type):
    """
    Converts a Python type to its JSON type equivalent.

    Args:
        py_type (str): The name of the Python type.

    Returns:
        str: The corresponding JSON type.

    Examples:
        >>> _python_to_json_type('str')
        'string'
        >>> _python_to_json_type('int')
        'number'
    """
    type_mapping = {
        "str": "string",
        "int": "number",
        "float": "number",
        "list": "array",
        "tuple": "array",
        "bool": "boolean",
        "dict": "object",
    }
    return type_mapping.get(py_type, "object")


def _func_to_schema(func, style="google"):
    """
    Generates a schema description for a given function, using typing hints and
    docstrings. The schema includes the function's name, description, and parameters.

    Args:
        func (Callable): The function to generate a schema for.
        style (str): The docstring format ('google' or 'reST').

    Returns:
        Dict[str, Any]: A schema describing the function.

    Examples:
        >>> def example_function(param1: int, param2: str) -> bool:
        ...     '''Example function.
        ...
        ...     Args:
        ...         param1 (int): The first parameter.
        ...         param2 (str): The second parameter.
        ...     '''
        ...     return True
        >>> schema = _func_to_schema(example_function)
        >>> schema['function']['name']
        'example_function'
    """
    # Extracting function name and docstring details
    func_name = func.__name__
    func_description, params_description = _extract_docstring_details(func, style)

    # Extracting parameters with typing hints
    sig = inspect.signature(func)
    parameters = {
        "type": "object",
        "properties": {},
        "required": [],
    }

    for name, param in sig.parameters.items():
        # Default type to string and update if type hint is available
        param_type = "string"
        if param.annotation is not inspect.Parameter.empty:
            param_type = _python_to_json_type(param.annotation.__name__)

        # Extract parameter description from docstring, if available
        param_description = params_description.get(name, "No description available.")

        # Assuming all parameters are required for simplicity
        parameters["required"].append(name)
        parameters["properties"][name] = {
            "type": param_type,
            "description": param_description,
        }

    # Constructing the schema
    schema = {
        "type": "function",
        "function": {
            "name": func_name,
            "description": func_description,
            "parameters": parameters,
        },
    }

    return schema
