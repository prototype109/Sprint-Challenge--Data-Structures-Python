class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.current_index = 0

    def append(self, item):
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        else:
            self.buffer[self.current_index] = item
            if self.current_index < len(self.buffer) - 1:
                self.current_index += 1
            else:
                self.current_index = 0
    def get(self):
        return self.buffer

# my_buffer = RingBuffer(3)
# my_buffer.append(1)
# my_buffer.append(2)
# my_buffer.append(3)
# my_buffer.append(4)
# print(my_buffer.get())