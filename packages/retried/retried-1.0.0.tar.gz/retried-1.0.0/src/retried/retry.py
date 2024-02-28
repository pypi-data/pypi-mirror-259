from functools import partial
from functools import wraps
from itertools import cycle
from itertools import repeat
import logging
import time
import typing as t


logger = logging.getLogger(__name__)


T = t.TypeVar('T')
Ts = t.Union[t.Type[T], tuple[t.Type[T], ...]]

DelayT = float
DelaysT = t.Iterator[DelayT]


def retry(
    retries: t.Optional[int] = None,
    *,
    exceptions: Ts[Exception] = Exception,
    error_callback: t.Callable[
        [int, t.Optional[Exception], DelayT], None
    ] = lambda i, e, d: logger.warning(f'try-{i} -> {e!r}. sleep {d} seconds'),
    sleeper: t.Callable[[DelayT], None] = time.sleep,
    delays: DelaysT = repeat(0),
    first_delay: t.Optional[DelayT] = None,
):
    delays = cycle(delays)
    if first_delay is None:
        first_delay = next(delays)

    def _error_callback(index: int, exception: Exception, delay: DelayT):
        error_callback(index, exception, delay)
        sleeper(delay)

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            function_retrying = partial(f, *args, **kwargs)
            try:
                # execute once
                return function_retrying()
            except exceptions as e:
                # start retrying
                i = 0
                _error_callback(i, e, first_delay)
                # retrying
                while True:
                    try:
                        return function_retrying()
                    except exceptions as e:
                        # check first
                        if i == retries:
                            raise e from None
                        # then ++
                        i += 1
                        delay = next(delays)
                        _error_callback(i, e, delay)

        return wrapper

    return decorator


if __name__ == '__main__':
    from random import random

    logging.basicConfig(level=logging.DEBUG, format='%(levelname)-7s %(message)s')

    class Error(Exception):
        pass

    @retry(
        retries=2,
        exceptions=(ValueError, ZeroDivisionError, Error),
        error_callback=lambda i, e, d: print(i),
        delays=cycle([0, 1 / 3, 2 / 3]),
        first_delay=1.5,
    )
    def f():
        1 / 0  # type: ignore[reportUnusedExpression]

        if random() < 0.2:
            return

        if random() < 0.8:
            # return
            1 / 0  # type: ignore[reportUnusedExpression]
        if random() < 0.8:
            raise Error('??')

    f()
