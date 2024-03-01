from __future__ import annotations

import concurrent.futures
import multiprocessing
import threading

from threading import Thread
from functools import wraps
from multiprocessing import cpu_count as mp_cpu_count
from os import cpu_count as os_cpu_count
from typing import Any, Callable, List, TypeVar
from typing_extensions import Annotated, Doc, ParamSpec, TypeAlias, final



_T = TypeVar('_T')
_R = TypeVar('_R')
_PSpec = ParamSpec('_PSpec')
F: TypeAlias = Callable[_PSpec, _T]


def cpu_cores() -> int:
    return os_cpu_count() or mp_cpu_count()

@final
class ParallelExec:
    @staticmethod
    def processor(
        funcs:
            List[Callable[...,Any]],
        join: Annotated[
            bool,
            Doc(
                """
                If True, the main process will wait until other processes or functions
                have finished executing. Else the main process continues regardless.
                """
            ),
        ] = False,
    ) -> Callable[[F[Any,_R]], F[Any,_R]]:
        """
        Used as a decorator for a function that groups all the tasks above.

        **example:**
            if __name__ == '__main__'
                @ParallelExec.processor([func1, func2, func3], join=True)
                def run_all(): pass

                some_tasks()

                run_all()

                other_tasks()
        """

        def decorator(func: F[Any,_R]) -> F[Any,_R]:
            @wraps(func)
            def wrapper(*a: _PSpec.args, **kwa: _PSpec.kwargs) -> _R:
                processes = [multiprocessing.Process(target=f) for f in funcs]
                for process in processes:
                    process.start()
                    if join:
                        process.join()
                return func(*a, **kwa)
            return wrapper
        return decorator

    @staticmethod
    def cores_bound_processor(
        callables:
            List[Callable[...,Any]],
        max_workers: Annotated[
            int,
            Doc(
                """
                The number of the CPU cores, if you override this you'll decrease
                performance.
                """
            ),
        ] = cpu_cores(),
    ) -> None:
        """
        This will run the tasks using as many processes as the current machine's CPU allows.
        If a CPU has 16 cores, it will run 16 processes; if 4, then 4, and so on.
        To override the max value and run as many processes as needed, set max_workers
        to the desired number.

        **usage:**

        from parallelexec import ParallelExec

        def func() -> None: ...

        def func2() -> None: ...

        def func3() -> None: ...

        if __name__ == "__main__":
            ParallelExec.cores_limited_processor([func,func2,func3])
                """
        with concurrent.futures.ProcessPoolExecutor(
            max_workers=max_workers
        ) as executor:
            futures = [executor.submit(callable_func) for callable_func in callables]
            concurrent.futures.wait(futures)

    @staticmethod
    def thread(
        join: Annotated[
            bool,
            Doc(
                """
                If True, the main process will wait until all threaded functions
                have finished executing. Else, the main process continues regardless.
                """
            ),
        ] = False
    ) -> Any:
        """
        Use this as a wrapper for each function you want to run in a separate thread.

        **example**

        @ParallelExec.thread(join=True)

        def f() -> None: ...

        """

        def decorator(fn: F[Any,_R]) -> F[Any,_R]:
            @wraps(fn)
            def execute(*a: _PSpec.args, **kwa: _PSpec.kwargs) -> Any:
                f = threading.Thread(target=fn, args=a, kwargs=kwa)
                f.start()
                if join:
                    f.join()
                return f
            return execute
        return decorator
