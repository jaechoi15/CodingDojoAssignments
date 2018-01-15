# You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.
# You will create two classes. One class should be Call, the other CallCenter.

class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    
    def display(self):
        print "Unique ID:", self.unique_id
        print "Caller Name:", self.caller_name
        print "Caller Phone Number:", self.caller_phone_number
        print "Time of Call:", self.time_of_call
        print "Reason for Call:", self.reason_for_call
        print ""
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self

    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self

    def info(self):
        for call in self.calls:
            print "Caller Name:", call.caller_name
            print "Caller Phone Number:", call.caller_phone_number
            print "Queue Size:", self.queue_size
            print ""
        return self

call1 = Call(1, "LeBron", 7031234567, 1000, "King James")
call2 = Call(2, "Carmelo", 1234567890, 1000, "Hoodie Melo")
call3 = Call(3, "Chris", 34534534534, 1200, "CP3")

callCenter1 = CallCenter()
callCenter1.add(call1).add(call2).add(call3).info()