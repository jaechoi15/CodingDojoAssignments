# You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.
# You will create two classes. One class should be Call, the other CallCenter.

from datetime import datetime

class Call(object):
    NUM_CALLS = 0

    def __init__(self, caller_name, caller_number, call_reason):
        self.unique_id = Call.NUM_CALLS
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.call_time = datetime.now()
        self.call_reason = call_reason

        Call.NUM_CALLS += 1
    
    def displayInfo(self):
        print "Unique ID:", self.unique_id
        print "Caller Name:", self.caller_name
        print "Caller Phone Number:", str(self.caller_number)
        print "Time of Call:", self.call_time.strftime("%I:%M:%S")
        print "Reason for Call:", self.call_reason
        return self

print "*"*10 + "Call #1" + "*"*10
call1 = Call("Jae", "123-456-7890", "unknown")
call1.displayInfo()

print "*"*10 + "Call #2" + "*"*10
call2 = Call("Choi", "444-456-7890", "unknown")
call2.displayInfo()

class CallCenter(object):  
    def __init__(self):
        self.calls = []

    def get_queue_size(self):
        return len(self.calls)
    
    def add(self, a_call):
        self.calls.append(a_call)
        return self
    
    def remove(self):
        self.queue.size -= 1
        return self
    
    def info(self):
        print self.caller_name
        print self.caller_number
        print self.get_queue_size
        return self

center = CallCenter()
center.add(call1).add(call2)

print center.get_queue_size()



