from typing import Callable


def feeder (get_next_item: Callable[[], str]) -> None:
    pass


def async_query(on_success: Callable[[int], None],
                on_failure: Callable[[int, Exception], None])-> None:
    pass

async_query('alamin', 'anamika')