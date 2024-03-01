"""Defines class DataBatcher"""


class DataBatcher:
    """Breaks a provided iterable up into batches according to a
    provided batching pattern

    Example:
    >>> mydata = [1,2,3,4,5,6,7,8,9,10,11,12]
    >>> mybatcher = DataBatcher(mydata, batch_pattern=(1,2,4))
    >>> for batch in mybatcher:
    ...     print(batch)
    (1,)
    (2, 3)
    (4, 5, 6, 7)
    (8, 9, 10, 11, 12)
    >>> mybatcher_fixed_size = DataBatcher(mydata, fixed_batch_size=5)
    >>> for batch in mybatcher_fixed_size:
    ...     print(batch)
    (1, 2, 3, 4, 5)
    (6, 7, 8, 9, 10)
    (11, 12)
    """

    def __init__(
        self,
        data,
        batch_pattern=None,
        fixed_batch_size: int | None = None,
    ) -> None:
        """Initial setup of DataBatcher class

        Note:
            Exactly one of `batch_pattern` or `fixed_batch_size` must be specified

        Args:
            data (Any): Any python iterable (list, tuple, set, str, dict etc.)
            batch_pattern (tuple[int, ...]): A list of integers describing sequence of batch sizes
                If `batch_pattern` is exhausted before `data`, the final batch contains everything
                remaining in `data`
                Omit this argument if using a fixed batch size
            fixed_batch_size(int): Return this number of datapoints in each batch
                Omit this argument if using a batching pattern
        """
        if (batch_pattern is None and fixed_batch_size is None) or (
            batch_pattern is not None and fixed_batch_size is not None
        ):
            raise ValueError(
                "Exactly one of `batch_pattern` or `fixed_batch_size` must be specified"
            )
        self._data = iter(data)
        if fixed_batch_size is not None:
            n_full_batches, n_remainder = divmod(len(data), fixed_batch_size)
            batch_pattern = tuple([fixed_batch_size] * n_full_batches + [n_remainder])
        self._batch_size = iter(batch_pattern)

    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        """Returns the next batch of data"""
        result = []
        try:
            batch_size: int = next(self._batch_size)
            for _ in range(batch_size):
                try:
                    result.append(next(self._data))
                except StopIteration:
                    break
        except StopIteration:  # nothing left in batch_pattern
            while self._data:
                try:
                    result.append(next(self._data))
                except StopIteration:
                    break
        if len(result) == 0:
            raise StopIteration
        return tuple(result)


if __name__ == "__main__":
    my_data = list(range(20))
    my_batch_pattern = (1, 2, 4, 1)
    print("my data:", my_data)
    print("my batch pattern:", my_batch_pattern)
    test_data_batcher = DataBatcher(my_data, my_batch_pattern)
    for batch in test_data_batcher:
        print(batch)
