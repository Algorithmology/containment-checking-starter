"""Perform an experiment to study efficiency of containment checking for collections."""

import timeit

import typer
from rich.console import Console

from containmentcheck.analyze import calculate_average_values
from containmentcheck.approach import ContainmentCheckApproach
from containmentcheck.containment import (
    containment_check_list,
    containment_check_set,
    containment_check_tuple,
)
from containmentcheck.generate import (
    generate_random_container,
    generate_random_number,
)
from containmentcheck.util import human_readable_boolean

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for rich text output
console = Console()


# TODO: Make sure that you understand how each of these functions work

# TODO: Make sure that you add all of the needed documentation to the functions

# TODO: Make sure that you add type annotations to all functions


def perform_containment_check_benchmark(
    containment_check_lambda,
):
    """Run an experiment using the timeit package for the specific function."""
    # set the number of runs inside of a benchmark
    # TODO: you may want to consider making this a parameter to the tool
    number_runs = 10
    # set the number of repeats for running an entire benchmark
    # NOTE: you may want to consider making this a parameter to the tool
    number_repeats = 3
    # use the timeit module to evaluate performance with the current configuration
    # reference to learn about the timeit module:
    # https://docs.python.org/3/library/timeit.html
    # key insights:
    # --> each benchmark run will have a total of number_runs and timeit will report the total across number_runs
    # --> each of the entire benchmark run will be repeated a total of number_repeats times
    # TODO: Read the reference for using the lambda function:
    # https://stackoverflow.com/questions/5086430/how-to-pass-parameters-of-a-function-when-using-timeit-timer
    execution_times = timeit.Timer(containment_check_lambda).repeat(
        repeat=number_repeats, number=number_runs
    )
    # TODO: display the results of the benchmarking campaign
    # see the examples of the expected output to understand how to format the benchmark results


@cli.command()
def containmentcheck(
    size: int = typer.Option(5),
    maximum: int = typer.Option(25),
    exceed: bool = typer.Option(False),
    approach: ContainmentCheckApproach = ContainmentCheckApproach.list,
) -> None:
    """Conduct an experiment to measure the performance of containment checking."""
    # create the starting data container and random number
    random_container = None
    # generate a random value that goes up to the maximum value;
    # if the value of exceed is True then generate a number beyond the maximum
    random_number = generate_random_number(maximum, exceed)
    # display diagnostic details about the configuration of the experiment
    console.print(
        "Conducting an experiment to measure the performance of containment checking!\n"
    )
    console.print(f"Type of the data container: {approach}")
    console.print(f"Size of the data container: {size}")
    console.print(
        f"Maximum value for a number in the data container: {maximum}"
    )
    console.print(
        f"Should the value to search for exceed the maximum number? {human_readable_boolean(exceed)}"
    )
    console.print()
    # conduct an experiment for containment checking with the list data structure
    if approach.value == ContainmentCheckApproach.list:
        # generate the container of inputs consisting of random integer values
        random_container = generate_random_container(
            size, maximum, make_tuple=False
        )
        # create the containment check lambda function
        containment_check_lambda = lambda: containment_check_list(
            random_container,  # type: ignore
            random_number,
        )
        perform_containment_check_benchmark(containment_check_lambda)
    # conduct an experiment for containment checking with the tuple data structure
    elif approach.value == ContainmentCheckApproach.tuple:
        # generate the container of inputs consisting of random integer values
        random_container = generate_random_container(
            size, maximum, make_tuple=True
        )
        # create the containment check lambda function
        containment_check_lambda = lambda: containment_check_tuple(
            random_container,  # type: ignore
            random_number,
        )
        perform_containment_check_benchmark(containment_check_lambda)
    # conduct an experiment for containment checking with the set data structure
    elif approach.value == ContainmentCheckApproach.set:
        # generate the container of inputs consisting of random integer values
        random_container = generate_random_container(
            size, maximum, make_tuple=False
        )
        # generate a random value that goes up to the maximum value;
        containment_check_lambda = lambda: containment_check_set(
            random_container,  # type: ignore
            random_number,
        )
        perform_containment_check_benchmark(containment_check_lambda)
