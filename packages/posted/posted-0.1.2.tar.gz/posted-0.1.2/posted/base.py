"""
Base module for the `posted` package.

This module contains the base class for message brokers, 'MsgBrokerBase', which defines 
the interface for message brokers.
"""

from abc import ABC
from functools import partial
from typing import Any, Callable, Mapping
from i2.util import mk_sentinel


_mk_sentinel = partial(
    mk_sentinel, boolean_value=False, repr_=lambda x: x.__name__, module=__name__
)
NoMsg = _mk_sentinel('NoMsg')


class MsgBrokerBase(ABC):
    """
    Base class for message brokers. Subclasses must implement the 'write', 'read',
    'subscribe', and 'unsubscribe' methods.
    """

    _config: Mapping[str, Any]

    def __init__(self, **config):
        self._config = config

    def write(self, message: Any, channel: str):
        """
        Write a message to the channel.
        
        :param message: The message to write.
        :param channel: The channel to write to.
        """
        raise NotImplementedError("The 'write' method must be implemented in subclass.")

    def read(self, channel: str):
        """
        Read a message from the channel.

        :param channel: The channel to read from.
        :return: The message read from the channel.
        """
        raise NotImplementedError("The 'read' method must be implemented in subclass.")

    def subscribe(self, channel: str, callback: Callable[[Any], None]):
        """
        Subscribe to a channel.

        :param channel: The channel to subscribe to.
        :param callback: The callback to call when a message is received on the channel.
        """
        raise NotImplementedError(
            "The 'subscribe' method must be implemented in subclass."
        )

    def unsubscribe(self, channel: str):
        """
        Unsubscribe from a channel.

        :param channel: The channel to unsubscribe from.
        """
        raise NotImplementedError(
            "The 'unsubscribe' method must be implemented in subclass."
        )
