from pydantic import BaseModel

"""
环境搭建
pip install opyrator
"""


class Input(BaseModel):
    message: str


class Output(BaseModel):
    message: str


def hello_world(input: Input) -> Output:
    """Returns the `message` of the input data."""
    return Output(message=input.message)


