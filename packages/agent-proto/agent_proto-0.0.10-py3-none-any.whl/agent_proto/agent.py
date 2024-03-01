"""
Agent module.
it can be run locally and interacted with via a chat interface.
The agent can be used to run tools based on user input.
The agent is trained to provide useful responses and guidance to the user.
"""

from abc import ABC, abstractmethod
from typing import AsyncIterator, Generic, Iterable, Literal, Optional, Type, TypeVar

from pydantic import BaseModel

from .proxy import LazyProxy
from .tool import Tool, ToolDefinition, ToolOutput

T_co = TypeVar("T_co", covariant=True)


class RawMessage(BaseModel, Generic[T_co]):
    """
    Represents a message with a role and content.

    Attributes:
        role (str): The role of the message.
        content (str): The content of the message.
    """

    role: Literal["user", "assistant", "function", "tool", "system", "error"]
    content: T_co


class Message(RawMessage[str]):
    """
    Represents a message with a role and content.

    Attributes:
        role (str): The role of the message.
        content (str): The content of the message.
    """

    role: Literal["user", "assistant", "function", "tool", "system", "error"]
    content: str


class BaseAgent(BaseModel, LazyProxy[T_co], ABC):
    """
    Abstract base class for agents.
    """

    messages: list[Message]
    model: str
    tools: Iterable[Type[Tool]]

    @abstractmethod
    async def chat(
        self, *, message: str, stream: bool = True
    ) -> AsyncIterator[Message] | Message:
        """
        Chat with the agent.

        Args:
            message (str): The message to send to the agent.
            stream (bool, optional): Whether to stream the messages or not. Defaults to True.

        Returns:
            AsyncIterator[Message] | Message: An async iterator of messages or a single message.
        """
        raise NotImplementedError

    @abstractmethod
    async def run(
        self, *, message: str, definitions: Optional[Iterable[ToolDefinition]] = None
    ) -> ToolOutput:
        """
        Run the agent.

        Args:
            message (str): The message to run the agent with.

        Returns:
            ToolOutput: The output of the agent's run.
        """
        raise NotImplementedError

    @abstractmethod
    def __load__(self) -> T_co:
        """
        Load the agent.

        Returns:
            T_co: The agent.
        """
        raise NotImplementedError
