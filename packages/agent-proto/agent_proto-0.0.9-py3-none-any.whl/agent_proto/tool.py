"""
Tool module.
A tool is a pydantic object that embodies an specific feature that can be executed by the agent. It's structure defines the signature of the function that will be implemented on the `run` method, which will contain the core logic of the feature, it automatically handles the schema definition that is needed by the agent to infer which function to call based on user's natural language input.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Any, Dict, Generic, Literal, TypeVar

from pydantic import BaseModel
from typing_extensions import Required, TypeAlias, TypedDict

from .utils import setup_logging

FunctionParameters: TypeAlias = Dict[str, object]
logger = setup_logging(__name__)

T = TypeVar("T")


class FunctionSchema(TypedDict, total=False):
    """
    Represents the parameters of a function.

    Attributes:
        type (Literal["object"]): The type of the parameters.
        properties (Dict[str, object]): The properties of the parameters.
        required (List[str]): The required properties of the parameters.
    """

    type: Required[Literal["object"]]
    title: Required[str]
    description: Required[str]
    properties: Required[Dict[str, object]]
    required: Required[list[str]]


class FunctionDefinition(TypedDict, total=False):
    """
    Represents the definition of a function.

    Attributes:
        name (str): The name of the function.
        description (str): The description of the function.
        parameters (FunctionParameters): The parameters of the function.
    """

    name: Required[str]
    description: Required[str]
    parameters: Required[FunctionParameters]


class ToolDefinition(TypedDict, total=False):
    """
    Represents the definition of a tool.

    Attributes:
        type (Literal["function"]): The type of the tool.
        function (FunctionDefinition): The definition of the function.
    """

    type: Required[Literal["function"]]
    function: Required[FunctionDefinition]


class Model(BaseModel):
    """
    This class represents a model used in the application.
    """

    model_config = {"extra": "allow", "arbitrary_types_allowed": True}

    @classmethod
    @lru_cache
    def definition(cls) -> FunctionSchema:
        _schema = cls.model_json_schema()
        assert isinstance(
            cls.__doc__, str
        ), "All models must have a docstring explaining its purpose"
        return {
            "type": "object",
            "title": cls.__name__,
            "description": cls.__doc__,
            "properties": _schema.get("properties", {}),
            "required": _schema.get("required", []),
        }


class ToolOutput(Model):
    """
    Represents a response from a tool.

    Attributes:
        content (Any): The content of the response.
        [TODO] Implement output parser class to handle the output `content` of the tools.
        role (str): The role of the response.
    """

    content: Any
    role: str


class Tool(Model, ABC):
    """
    Represents a tool used in the application.

    This class provides a base implementation for defining tools.
    Subclasses should override the `run` method to provide the specific
    functionality of the tool.

    Attributes:
        None

    Methods:
        run: Executes the tool and returns the result. [TODO] Add the output parser here.
        __call__: Executes the tool and returns the result as a ToolOutput object.

    """

    @abstractmethod
    async def run(self) -> Any:
        """
        This method is responsible for executing the tool.

        Returns:
            ToolResponse: The response from the tool execution.
        """
        raise NotImplementedError

    async def __call__(self) -> ToolOutput:
        """
        This method is intended to be called by the agent.
        It execute the underlying logic of the tool and returns and object with the result as the `content` attribute and the name of the tool as the `role` attribute in order to be compatible with the `message` format used by the agent and easily distinguishable from other messages to be consumed from the client application. It has a `robust` decorator that catches any exception, handles logging and retries the execution of the tool if it fails on an exponential backoff fashion.
        """
        response = await self.run()
        return ToolOutput(content=response, role=self.__class__.__name__.lower())


class BaseTool(Tool, Generic[T], ABC):
    @abstractmethod
    async def response(self) -> T:
        raise NotImplementedError
