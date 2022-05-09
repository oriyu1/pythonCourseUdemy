# %%

import dataclasses
import inspect
from dataclasses import dataclass, field, astuple, asdict
from pprint import pprint

# import attr


class ManualComment:
    def __init__(self, id: int, text: str):
        self.id: int = id
        self.text: str = text


# For immutable

    # self.__id: int = id
    # self.__text: str = text

    # @property
    # def id(self):
    #     return self.__id


    # @property
    # def text(self):
    #     return self.__text


    def __repr__(self):
        return "{}(id={}, text={})".format(self.__class__.__name__, self.id, self.text)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) == (other.id, other.text)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __hash__(self):
        return hash((self.__class__, self.id, self.text))

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) < (other.id, other.text)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) <= (other.id, other.text)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) > (other.id, other.text)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) >= (other.id, other.text)
        else:
            return NotImplemented


# Here implemented by dataclass - much shorter
@dataclass(frozen=True, order=True)
class Comment:
    id: int   # equivalent to id: int = field()
    text: str # equivalent to text: str = field(default="")
    # text: str = "" # Here with default value

    # replies: list[int] = [] # error - mutable cannot be default - 
    # we do not want all instances of this class to share the same list
    replies: list[int] = field(default_factory=list, repr=False, compare=False)

# Another option is to use an external library that has some more features

# @attr.s(frozen=True, order=True, slots=True)
# class AttrComment:
#     id: int = 0
#     text: str = ""

# %%
def main():
    comment = Comment(1, "I just subscribed!",[1,2,3])
    # comment.id = 3  # can't immutable
    print(comment)
    
    #print(astuple(comment))
    #print(asdict(comment))
    

    # This to see all the functions written in this class, 
    # by default its "eq" "init" "repr"
    # "frozen=True" is to make it immutable - its add "hash" and "setatt"
    # its good idea to use frozen so people can use them as keys in dictioanries
    # "order=True" is for ordering... ""
    
    #pprint(inspect.getmembers(Comment, inspect.isfunction))

    # if we want to make a copy of an immutable data class, with something changed in it 
    # we can use "replace"

    #copy = dataclasses.replace(comment, id=3)
    #print(copy)



if __name__ == '__main__':
    main()
# %%
