"""
Message Broker Implementation for Publish/Subscribe Pattern

This module provides a simple implementation of the publish/subscribe pattern
for message passing between components. It allows components to subscribe to
specific message types and receive notifications when messages of those types
are published.

Classes:
    MsgType: Enum of supported message types
    MsgBroker: Central message broker that manages subscriptions and message distribution
    MsgSubscriber: Wrapper for callback functions that handle messages
"""

from enum import Enum
import threading
import logging
import traceback
from typing import Callable, Dict, List, Any, Optional, Set, Union

class MsgType(Enum):
    """Enumeration of supported message types."""
    fatal = "fatal"
    fault = "fault"     # Critical messages requiring immediate attention
    alarm = "alarm"     # Informational messages
    info = "info"       # Status updates
    custom = "custom"   # Custom message types

class MsgBroker:
    """
    Message broker that manages subscriptions and distributes messages.

    This class implements the publish/subscribe pattern, allowing components
    to subscribe to specific message types and receive notifications when
    messages of those types are published.
    """

    def __init__(self):
        """Initialize a new message broker."""
        # Use a dictionary to store subscribers by message type
        self._subscribers: Dict[MsgType, List[MsgSubscriber]] = {
            msg_type: [] for msg_type in MsgType
        }
        # Track subscribers across all message types for easier removal
        self._all_subscribers: Set[MsgSubscriber] = set()
        # Lock for thread safety
        self._lock = threading.Lock()

    def addSubscriber(self, subscriber: 'MsgSubscriber', msg_type: Union[MsgType, List[MsgType]]) -> bool:
        """
        Add a subscriber for the specified message type(s).

        Args:
            subscriber: The subscriber to add
            msg_type: A message type or list of message types to subscribe to

        Returns:
            bool: True if the subscriber was added successfully

        Raises:
            ValueError: If msg_type is not a valid MsgType
        """
        if not isinstance(subscriber, MsgSubscriber):
            raise TypeError("subscriber must be an instance of MsgSubscriber")

        # Convert single message type to list for uniform processing
        msg_types = [msg_type] if isinstance(msg_type, MsgType) else msg_type

        # Validate message types
        for mt in msg_types:
            if not isinstance(mt, MsgType):
                raise ValueError(f"Invalid message type: {mt}")

        with self._lock:
            # Add subscriber to each specified message type
            for mt in msg_types:
                if subscriber not in self._subscribers[mt]:
                    self._subscribers[mt].append(subscriber)

            # Add to the set of all subscribers
            self._all_subscribers.add(subscriber)

            return True

    def removeSubscriber(self, subscriber: 'MsgSubscriber',
                         msg_type: Optional[Union[MsgType, List[MsgType]]] = None) -> bool:
        """
        Remove a subscriber from specified message type(s) or all message types.

        Args:
            subscriber: The subscriber to remove
            msg_type: Optional message type(s) to unsubscribe from.
                      If None, removes from all message types.

        Returns:
            bool: True if the subscriber was removed from at least one message type
        """
        if not isinstance(subscriber, MsgSubscriber):
            logging.warning(f"Attempted to remove non-MsgSubscriber object: {subscriber}")
            return False

        removed = False

        with self._lock:
            if msg_type is None:
                # Remove from all message types
                for sub_list in self._subscribers.values():
                    if subscriber in sub_list:
                        sub_list.remove(subscriber)
                        removed = True

                # Remove from the set of all subscribers
                if subscriber in self._all_subscribers:
                    self._all_subscribers.remove(subscriber)
            else:
                # Convert single message type to list for uniform processing
                msg_types = [msg_type] if isinstance(msg_type, MsgType) else msg_type

                # Validate message types
                for mt in msg_types:
                    if not isinstance(mt, MsgType):
                        logging.warning(f"Invalid message type in removal: {mt}")
                        continue

                    # Remove from specified message type
                    if subscriber in self._subscribers[mt]:
                        self._subscribers[mt].remove(subscriber)
                        removed = True

                # Check if subscriber is still subscribed to any message type
                still_subscribed = any(subscriber in sub_list for sub_list in self._subscribers.values())
                if not still_subscribed and subscriber in self._all_subscribers:
                    self._all_subscribers.remove(subscriber)

        if removed:
            logging.debug(f"Removed subscriber: {subscriber}")
        else:
            logging.debug(f"Subscriber not found for removal: {subscriber}")

        return removed

    def publish(self, msg_type: MsgType, message: Dict) -> int:
        """
        Publish a message to all subscribers of the specified message type.

        Args:
            msg_type: The type of message to publish
            content: The message content
            source: Optional source identifier

        Returns:
            int: Number of subscribers that received the message

        Raises:
            ValueError: If msg_type is not a valid MsgType
        """
        if not isinstance(msg_type, MsgType):
            raise ValueError(f"msg_type 消息类型必须为MsgType枚举类型!")

        if not isinstance(message, Dict):
            raise ValueError(f"message消息格式错误,必须为字典类型!")

        count = 0

        # Get a copy of the subscriber list to avoid issues if the list changes during iteration
        with self._lock:
            subscribers = self._subscribers[msg_type].copy()

        # Notify all subscribers
        for subscriber in subscribers:
            try:
                subscriber.invoke(message)
                count += 1
            except Exception as e:
                logging.error(f"Error notifying subscriber: {e}")
                logging.debug(traceback.format_exc())

        return count

    def getSubscriberCount(self, msg_type: Optional[MsgType] = None) -> int:
        """
        Get the number of subscribers for a specific message type or all message types.

        Args:
            msg_type: Optional message type to count subscribers for.
                     If None, returns the total number of unique subscribers.

        Returns:
            int: Number of subscribers
        """
        with self._lock:
            if msg_type is None:
                return len(self._all_subscribers)
            elif isinstance(msg_type, MsgType):
                return len(self._subscribers[msg_type])
            else:
                raise ValueError(f"Invalid message type: {msg_type}")

class MsgSubscriber:
    """
    Wrapper for callback functions that handle messages.

    This class wraps a callback function and provides a method to invoke it
    with a message. It also provides equality methods to allow for subscriber
    removal by identity.
    """

    def __init__(self, callback: Callable[[Dict] , None], name: Optional[str] = None):
        """
        Initialize a new message subscriber.

        Args:
            callback: The function to call when a message is received
            name: Optional name for the subscriber (useful for debugging)

        Raises:
            TypeError: If callback is not callable
        """
        if not callable(callback):
            raise TypeError("callback must be callable")

        self._callback = callback
        self.name = name or f"Subscriber-{id(self)}"

    def invoke(self, msg: Dict) -> None:
        """
        Invoke the callback function with the given message.

        Args:
            msg: The message to pass to the callback

        Raises:
            Exception: If the callback raises an exception
        """
        try:
            self._callback(msg)
        except Exception as e:
            logging.error(f"Error in subscriber {self.name}: {e}")
            logging.debug(traceback.format_exc())
            raise

    def __eq__(self, other: object) -> bool:
        """Check if two subscribers are equal (same callback)."""
        if not isinstance(other, MsgSubscriber):
            return False
        return self._callback == other._callback

    def __hash__(self) -> int:
        """Hash based on the callback function."""
        return hash(self._callback)

    def __str__(self) -> str:
        """String representation of the subscriber."""
        return f"MsgSubscriber({self.name})"

# Test code
if __name__ == "__main__":
    import time

    def test_notify_system():
        print("\n=== Testing Notification System ===")

        # Create message broker
        broker = MsgBroker()

        # Message handlers
        def handle_alarm(msg):
            print(f"ALARM: {msg.content} from {msg.source}")

        def handle_info(msg):
            print(f"INFO: {msg.content} from {msg.source}")

        def handle_status(msg):
            print(f"STATUS: {msg.content} from {msg.source}")

        def handle_all(msg):
            print(f"ALL: {msg.content} from {msg.source}")

        # Create subscribers
        alarm_subscriber = MsgSubscriber(handle_alarm, "AlarmHandler")
        info_subscriber = MsgSubscriber(handle_info, "InfoHandler")
        status_subscriber = MsgSubscriber(handle_status, "StatusHandler")
        all_subscriber = MsgSubscriber(handle_all, "AllHandler")

        # Add subscribers
        broker.addSubscriber(alarm_subscriber, MsgType.fatal)
        broker.addSubscriber(info_subscriber, MsgType.info)
        broker.addSubscriber(status_subscriber, MsgType.alarm)
        broker.addSubscriber(all_subscriber, [MsgType.alarm, MsgType.info, MsgType.fatal])

        # Test publishing messages
        print("\n--- Publishing messages ---")
        broker.publish(MsgType.alarm, "System overheating", "TempSensor")
        broker.publish(MsgType.info, "User logged in", "AuthSystem")

        # Test subscriber removal
        print("\n--- After removing info subscriber ---")
        broker.removeSubscriber(info_subscriber)
        broker.publish(MsgType.info, "This should not go to InfoHandler", "AuthSystem")

        # Test error handling
        print("\n--- Testing error handling ---")
        def faulty_handler(msg):
            raise ValueError("Simulated error in handler")

        faulty_subscriber = MsgSubscriber(faulty_handler, "FaultyHandler")
        broker.addSubscriber(faulty_subscriber, MsgType.alarm)

        try:
            broker.publish(MsgType.alarm, "This will cause an error in FaultyHandler", "ErrorTest")
            print("Error was caught by the broker")
        except Exception as e:
            print(f"Error propagated to caller: {e}")

        # Test subscriber counts
        print("\n--- Subscriber counts ---")
        print(f"Alarm subscribers: {broker.getSubscriberCount(MsgType.alarm)}")
        print(f"Info subscribers: {broker.getSubscriberCount(MsgType.info)}")
        print(f"Total unique subscribers: {broker.getSubscriberCount()}")

        print("\n=== Notification System Test Complete ===")

    # Run the test
    test_notify_system()
