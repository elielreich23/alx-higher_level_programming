#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, __value):
        return self.real != __value
    
    def __ne__(self, __value):
        return self.real == __value