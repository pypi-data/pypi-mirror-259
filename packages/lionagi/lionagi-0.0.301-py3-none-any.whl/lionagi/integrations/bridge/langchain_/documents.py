from typing import Union, Callable, List, Dict, Any, TypeVar
from lionagi.core.schema import DataNode


from lionagi.util import SysUtil

T = TypeVar("T", bound="DataNode")


def to_langchain_document(datanode: T, **kwargs: Any) -> Any:
    from langchain.schema import Document as LangchainDocument

    dnode = datanode.to_dict()
    SysUtil.change_dict_key(dnode, old_key="content", new_key="page_content")
    SysUtil.change_dict_key(dnode, old_key="lc_id", new_key="id_")
    dnode = {**dnode, **kwargs}
    return LangchainDocument(**dnode)


def langchain_loader(
    loader: Union[str, Callable],
    loader_args: List[Any] = [],
    loader_kwargs: Dict[str, Any] = {},
) -> Any:
    """
    Loads data using a specified langchain_ loader.

    Args:
        loader (Union[str, Callable]): The name of the loader function or the loader function itself.
        loader_args (List[Any]): Positional arguments to pass to the loader function.
        loader_kwargs (Dict[str, Any]): Keyword arguments to pass to the loader function.

    Returns:
        Any: The data loaded by the loader function.

    Raises:
        ValueError: If the specified loader is invalid or if the loader fails to load data.

    Examples:
        >>> data = langchain_loader("json_loader", loader_args=["data.json"])
        >>> isinstance(data, dict)
        True
    """
    try:
        if isinstance(loader, str):
            try:
                import langchain.document_loaders as document_loaders

                loader = getattr(document_loaders, loader)
            except ImportError as e:
                raise ValueError(
                    f"Unable to import {loader} from langchain_.document_loaders. "
                    f"Some dependency of LangChain are not installed. Error: {e}"
                )
        else:
            loader = loader
    except Exception as e:
        raise ValueError(f"Invalid loader: {loader}. Error: {e}")

    try:
        loader_obj = loader(*loader_args, **loader_kwargs)
        data = loader_obj.load()
        return data
    except Exception as e:
        raise ValueError(f"Failed to load. Error: {e}")


def langchain_text_splitter(
    data: Union[str, List],
    splitter: Union[str, Callable],
    splitter_args: List[Any] = None,
    splitter_kwargs: Dict[str, Any] = None,
) -> List[str]:
    splitter_args = splitter_args or []
    splitter_kwargs = splitter_kwargs or {}

    import langchain.text_splitter as text_splitter

    try:
        if isinstance(splitter, str):
            splitter = getattr(text_splitter, splitter)
        else:
            splitter = splitter
    except Exception as e:
        raise ValueError(f"Invalid text splitter: {splitter}. Error: {e}")

    try:
        splitter_obj = splitter(*splitter_args, **splitter_kwargs)
        if isinstance(data, str):
            chunk = splitter_obj.split_text(data)
        else:
            chunk = splitter_obj.split_documents(data)
        return chunk
    except Exception as e:
        raise ValueError(f"Failed to split. Error: {e}")


# def langchain_code_splitter(doc: str,
#                             language: str,
#                             splitter_args: List[Any] = [],
#                             splitter_kwargs: Dict[str, Any] = {}) -> List[Any]:
#     """
#     Splits code into smaller chunks using a RecursiveCharacterTextSplitter specific to a language.
#
#     Parameters:
#         doc (str): The code document to be split.
#         language (str): The programming language of the code.
#         splitter_args (List[Any]): Positional arguments to pass to the splitter.
#         splitter_kwargs (Dict[str, Any]): Keyword arguments to pass to the splitter.
#
#     Returns:
#         List[Any]: A list of Documents, each representing a chunk of the original code.
#
#     Raises:
#         ValueError: If the splitter fails to split the code document.
#     """
#     from langchain_.text_splitter import RecursiveCharacterTextSplitter
#
#     try:
#         splitter = RecursiveCharacterTextSplitter.from_language(
#             language=language, *splitter_args, **splitter_kwargs
#             )
#         docs = splitter.create_documents([doc])
#         return docs
#     except Exception as e:
#         raise ValueError(f'Failed to split. Error: {e}')
