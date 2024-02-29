class Element:
    """
    An element object that represents an element of Infinite Craft.

    ## Attributes:
        `name` (`str`): Name of the element
        `emoji` (`str`): Emoji of the element. Could be `None` if not found in the emoji cache
        `first_discovery` (`bool`): Whether the current element was a first discovery or not
    
    It is not recommended to use this class to make an Element.
    """

    def __init__(self, *, name: str, emoji: str, is_first_discovery: bool) -> None:
        self.name = name
        self.emoji = emoji
        self.is_first_discovery = is_first_discovery
    
    def __str__(self) -> None:
        if self.emoji:
            return self.emoji + " " + self.name
        else:
            return self.name
    
    def __repr__(self) -> None:
        return f"Element(name={repr(self.name)}, emoji={repr(self.emoji)}, is_first_discovery={repr(self.is_first_discovery)})"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Element) and __value.name == self.name:
            return True
        else:
            return False