"""
Simple test script for the notify module.
"""

# Import the module directly
from libs.notify import MsgType, MsgBroker, MsgSubscriber

def test_notify_system():
    # print("\n=== Testing Notification System ===")
    
    # Create message broker
    broker = MsgBroker()
    
    # Message handlers
    def handle_alarm(msg):
        # print(f"ALARM: {msg.content} from {msg.source}")
    
    def handle_info(msg):
        # print(f"INFO: {msg.content} from {msg.source}")
    
    def handle_status(msg):
        # print(f"STATUS: {msg.content} from {msg.source}")
    
    def handle_all(msg):
        # print(f"ALL: {msg.content} from {msg.source}")
    
    # Create subscribers
    alarm_subscriber = MsgSubscriber(handle_alarm, "AlarmHandler")
    info_subscriber = MsgSubscriber(handle_info, "InfoHandler")
    status_subscriber = MsgSubscriber(handle_status, "StatusHandler")
    all_subscriber = MsgSubscriber(handle_all, "AllHandler")
    
    # Add subscribers
    broker.addSubscriber(alarm_subscriber, MsgType.alarm)
    broker.addSubscriber(info_subscriber, MsgType.info)
    broker.addSubscriber(status_subscriber, MsgType.status)
    broker.addSubscriber(all_subscriber, [MsgType.alarm, MsgType.info, MsgType.status])
    
    # Test publishing messages
    # print("\n--- Publishing messages ---")
    broker.publish(MsgType.alarm, "System overheating", "TempSensor")
    broker.publish(MsgType.info, "User logged in", "AuthSystem")
    broker.publish(MsgType.status, "Processing complete", "TaskManager")
    
    # Test subscriber removal
    # print("\n--- After removing info subscriber ---")
    broker.removeSubscriber(info_subscriber)
    broker.publish(MsgType.info, "This should not go to InfoHandler", "AuthSystem")
    
    # Test error handling
    # print("\n--- Testing error handling ---")
    def faulty_handler(msg):
        raise ValueError("Simulated error in handler")
    
    faulty_subscriber = MsgSubscriber(faulty_handler, "FaultyHandler")
    broker.addSubscriber(faulty_subscriber, MsgType.alarm)
    
    try:
        broker.publish(MsgType.alarm, "This will cause an error in FaultyHandler", "ErrorTest")
        # print("Error was caught by the broker")
    except Exception as e:
        # print(f"Error propagated to caller: {e}")
    
    # Test subscriber counts
    # print("\n--- Subscriber counts ---")
    # print(f"Alarm subscribers: {broker.getSubscriberCount(MsgType.alarm)}")
    # print(f"Info subscribers: {broker.getSubscriberCount(MsgType.info)}")
    # print(f"Status subscribers: {broker.getSubscriberCount(MsgType.status)}")
    # print(f"Total unique subscribers: {broker.getSubscriberCount()}")
    
    # print("\n=== Notification System Test Complete ===")

if __name__ == "__main__":
    test_notify_system()
