from typing import Any

def coalesce(*arguments: Any) -> Any:
    """Returns the first value in the argument list that is not null."""
    for argument in arguments:
        if argument is not None:
            return argument
        
    return None