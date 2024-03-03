"""
Defines function retry_function_call
"""
import time
from typing import Any, Callable, Iterable

from joes_giant_toolbox.custom_exceptions import MaxRetriesExceededError


def retry_function_call(  # pylint: disable=too-many-arguments
    func: Callable,
    func_args: tuple,
    func_kwargs: dict,
    retry_pattern_seconds: Iterable[int | float],
    exceptions_to_handle: tuple,
    verbose: bool = False,
) -> Any:
    """
    Retries function (if it fails) according to retry pattern

    Args:
        func (Callable): The function to run
        func_args (tuple): (unnamed) arguments to pass to the function
        func_kwargs (dict): keyword (named) arguments to pass to the function
        retry_pattern_seconds (Iterable): Number of seconds to wait between failed function calls
        exceptions_to_handle (tuple): Exceptions which trigger a retry (others simply raise)
        verbose (bool): Print debugging information to standard out

    Returns:
        Any: If function executes without error, returns the function result

    Raises:
        MaxRetriesExceededError: if `retry_pattern_seconds` is exhausted successful function call

    Example:
        >>> import random
        >>> def random_failer(fail_prob: float) -> str:
        ...     '''Function which fails randomly with probability `fail_prob`'''
        ...     if random.uniform(0, 1) < fail_prob:
        ...         raise random.choice([ValueError, MemoryError])
        ...     return "function ran successfully"
        >>> func_output = retry_function_call(
        ...        random_failer,
        ...        func_args=(0.8,),
        ...        func_kwargs={},
        ...        retry_pattern_seconds=(0.1, 1, 2, 5),
        ...        exceptions_to_handle=(ValueError,),
        ...    )
        >>> print("Function output:", func_output)
    """
    for wait_n_seconds in retry_pattern_seconds:
        try:
            return func(*func_args, **func_kwargs)
        except Exception as err:  # pylint: disable=broad-exception-caught
            if verbose:
                print(f"received error {type(err)}")
            if type(err) in exceptions_to_handle:
                if verbose:
                    print(f"waiting {wait_n_seconds:,} seconds then retrying")
                time.sleep(wait_n_seconds)
            else:
                raise err

    raise MaxRetriesExceededError("Exhausted retry_pattern_seconds")


if __name__ == "__main__":
    import random

    def random_failer(fail_prob: float) -> str:
        """Function which fails randomly with probability `fail_prob`"""
        if random.uniform(0, 1) < fail_prob:
            raise random.choice([ValueError, MemoryError])
        return "function ran successfully"

    func_output = retry_function_call(  # pylint: disable=invalid-name
        random_failer,
        func_args=tuple(),
        func_kwargs={"fail_prob": 0.5},
        retry_pattern_seconds=(0.1, 1, 2, 5),
        exceptions_to_handle=(ValueError,),
        verbose=True,
    )
    print("Function output:", func_output)
