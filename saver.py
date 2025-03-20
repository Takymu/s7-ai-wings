from smolagents import Tool

class Memory(Tool):
    name = "saving responses tool"
    description = """
    This tool save responses until there are enough responses, 
    in this case you will informed about it by return value"""
    
    inputs = {
        "response": {
            "type": "tuple",
            "description": """ tuple should consist of 3 elements
            element 1 is user emotion (e.g. positive or negative or neutral), 
            element 2 is theme of the user's response (one or two words),
            element 3 is summary of the user's response (sentence or two)""",
        }
    }

    output_type = "string"

    def __init__(self, maxlen: int):
        self.response_list = []
        self.maxlen = maxlen

    def forward(self, response: tuple):
        self.response_list.append(response)
        print('response appended: ', response)
        if len(self.response_list) <= self.maxlen:
            return 'we need more responses, add them from this page or go on another'
        else:
            return 'it is enough of responses, you can stop adding them and provide final answer'

    def get_response_list(self):
        return self.response_list