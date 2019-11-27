import time

from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class Timer:
    """
    Time functions.

    # Example

    ```python
    import time
    print("Hello")

    with Timer():
            time.sleep(10)
    print("Done")

    ```
    output:

    "Hello"
    "Timer took 10 seconds"
    "Done"

    """

    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        logger.info(f"Timer {self.name} took: {self.interval} seconds")
