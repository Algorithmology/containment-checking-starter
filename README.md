# 🔬 Containment Checking

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## ✨ Table of Contents

<!---toc start-->

* [🔬 Containment Checking](#-containment-checking)
  * [✨ Table of Contents](#-table-of-contents)
  * [🏁 Introduction](#-introduction)
  * [🤝 Seeking Assistance](#-seeking-assistance)
  * [🛫 Project Overview](#-project-overview)
  * [🎉 Program Specifications](#-program-specifications)

<!---toc end-->

## 🏁 Introduction

If you are a student completing this project as part of a class at Allegheny
College, you can check the schedule on the course web site for the due date or
ask the course instructor for more information about the due date. Please note
that the content provided in the `README.md` file for this GitHub repository is
an overview of the project and thus may not include the details for every step
needed to successfully complete every project deliverable. This means that you
may need to schedule a meeting during the course instructor's office hours to
discuss aspects of this project. Finally, it is important to point out that
your repository for this project was created from the GitHub repository
template called
[containment-checking-starter](https://github.com/Algorithmology/containment-checking-starter);
you can check this repository for any updates to this project's documentation
or source code!

## 🤝 Seeking Assistance

Even though the course instructor will have covered all of the concepts central
to this project before you start to work on it, please note that not every
detail needed to successfully complete the assignment will have been covered
during prior classroom sessions. This is by design as an important skill that
you must practice as an algorithm engineer is to search for and then understand
and ultimately apply the technical content found in additional resources.

## 🛫 Project Overview

This project invites you to implement and use a program called
`containmentcheck` that conducts an experiment to evaluate the performance of
containment checking using the `in` operator for different types of data
containers (i.e., "collections") like tuples and lists. When you run the
completed version of the `containmentcheck` program it will allow you to
specify the size of the container, the maximum value of the integer values
stored in the container, the type of data container, and whether or not the
searching algorithm should look for a value that does or does not exceed the
maximum value in the list. If you configure it correctly, the
`containmentcheck` program will total and average time for using the `in`
operator for the automatically generated lists. Specifically,
`containmentcheck` will use the
[timeit](https://docs.python.org/3/library/timeit.html) package to measure the
performance of the `in` operator for different data containers, following one
of the approaches outlined in the article called [measure execution time with
timeit in Python](https://note.nkmk.me/en/python-timeit-measure/). As you
complete this engineering effort you will experimentally evaluate the claims in
the following articles about the best way to determine if a specific value
exists inside of a data container.

- [Membership testing](https://switowski.com/blog/membership-testing)
- [Python speed](https://wiki.python.org/moin/PythonSpeed)
- [Using key in list to check if key is contained in list](https://docs.quantifiedcode.com/python-anti-patterns/performance/using_key_in_list_to_check_if_key_is_contained_in_a_list.html)
- [Why is a set faster than a list in Python?](https://www.quora.com/Why-is-a-set-faster-than-a-list-in-Python)

After cloning this repository to your computer, please take the following steps
to get started on the project:

- To install the necessary software for running the `containmentcheck` program that
you will create as a part of this project, you should install the
[`devenv`](https://devenv.sh/getting-started/) tool, bearing in mind that it is
not necessary for you to install the `cachix` program referenced by these
installation instructions. Please note that students who are using Windows 11
should first install Windows subsystem for Linux (`wsl2`) before attempting to
install `devenv`. Once you have installed `devenv` and cloned this repository to
your computer, you can `cd` into the directory that contains the
`pyproject.toml` file and then type `devenv shell`. It is important to note that
the first time you run this command it may complete numerous steps and take a
considerable amount of time.
- Once this command completes correctly, you will have a Python development
environment that contains Python `3.11.6` and Poetry `1.7.1`! You can verify
that you have the correct version of these two programs by typing:
  - `python --version` (note that you should see `3.11.6`)
  - `poetry --version` (note that you should see `1.7.1`)
- If some aspect of the installation with `devenv` did not work correctly, then
please resolve what is wrong before proceeding further! Alternatively, you may
install the aforementioned versions of Python and Poetry on your laptop. With
that said, please make sure that you only use the specified versions of Python
and Poetry to complete this project. This means that, to ensure that the results
from running the micro-benchmarks are consistent and, as best as is possible,
comparable to the results from other computers, you should use exactly the
specified version of either Python or Poetry.
- Before moving to the next step, you may need to again type `poetry install` in
order to avoid the appearance of warnings when you next run the `containmentcheck`
program. Now you can type the command `poetry run containmentcheck --help` and
explore how to use the program.

## 🎉 Program Specifications

Before implementing the program so that it adheres to the following
requirements and produces the expected output, please note that the program
will not work unless you add the required source code at the designated `TODO`
markers. With that said, after you complete a correct implementation of all the
`containmentcheck`'s features you can run it with the command `poetry run
containmentcheck --size 32000000 --maximum 50000000 --approach list` and see
that it produces output like the following. It is worth noting that your
invocation of the program will likely produce different results than those
provided because of the fact that your laptop may have different software and
hardware, and thus different performance characteristics, than the one used to
run `containmentcheck`. With that said, a finished version of
`containmentcheck` should report both the total and average time for use the
`in` operator for the specified data container and searching approach.

```text
✨ Conducting an experiment to measure the performance of containment checking!
         Type of the data container: list
         Size of the data container: 32000000
         Maximum value for a number in the data container: 50000000
         Should the value to search for exceed the maximum number? No

🧮 Total time for running 10 runs in 3 benchmark campaigns:
[0.016107587000078638, 0.016178363999642897, 0.016164254000614164]

🧮 Average time for running 10 runs in 3 benchmark campaigns:
[0.0016107587000078639, 0.0016178363999642897, 0.0016164254000614164]
```

Please note that your implementation of the `containmentcheck` program should
work for three data container types and be configurable for all of the
parameters including (i) container type, (ii) container size, and (iii) maximum
value for a number in the container, and (iv) whether or not the searched value
will exceed the maximum value. If you study the files in the `containmentcheck/`
directory you will see that they have many `TODO` markers that designate the
functions you must implement so as to ensure that `containmentcheck` runs the
desired experiment and produces the correct output. Once you complete a task
associated with a `TODO` marker, make sure that you delete it and revise the
prompt associated with the marker into a meaningful comment. Specifically, you
will need to implement the Python functions such as the following:

- `def generate_random_number(maximum: int, exceed: bool = False) -> int`:
  automatically create a random number starting at zero and going up to the
  `maximum` value. When `exceed` is `true` the function should generate a number
  that is greater than the specified maximum value.

- `def generate_random_container(size: int, maximum: int, make_tuple: bool =
  False) -> Union[List[int], Tuple[int, ...]]`: automatically generate a data
  container that must be either of type `List` or type `Tuple`, ensuring that it
  contains exactly `size` numbers that are never bigger than the specified
  `maximum`.

- `def containment_check_list(thelist: List[int], number: int) -> bool`: use the
  `in` operator to perform containment checking for the provided list.

- `def containment_check_tuple(thetuple: Tuple[int], number: int) -> bool`: use
  the `in` operator to perform containment checking for the provided tuple.

- `def containment_check_set(thelist: List[int], number: int) -> bool`: after
  converting the provided list to a set, use the `in` operator to perform
  containment checking for the set. This function will allow you to
  experimentally evaluate the [conventional
  wisdom](https://docs.quantifiedcode.com/python-anti-patterns/performance/using_key_in_list_to_check_if_key_is_contained_in_a_list.html)
  that a developer can improve the performance of their Python program by
  converting a `list` to a `set` before using the `in` operator.

Ultimately, you should design your own experiment and state and run experiments
to answer your own research questions, focusing on the following key issues:

- The data container: `set`, `list`, and `tuple`
- The size of the data container: small values (e.g., 1 million numbers) to big
  values (e.g., 32 million numbers)
- Whether or not the value that it being searched for is `in` the list
- The maximum value of the numbers that are inside of the data container

Please make sure that, during the second week of this assignment, you meet with
the course instructor to receive feedback on the design of your experiment
before you embark on conducting the experiments and analyzing the data. Finally,
here are other issues that you should keep in mind as you work on the
`containmentcheck` program:

- You must implement test cases for all of the untested modules, excepting the
`main` module, while further ensuring that the test achieve the desired level
of code coverage.
- If you have already installed the
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs the
automated grading checks provided by
[GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
repository's base directory, run the automated grading checks by typing
`gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all of the required responses to the technical
writing prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
labels from all of the provided source code. This means that instead of only
deleting the `TODO` marker from the code you should delete the `TODO` marker
and the entire prompt and then add your own comments to demonstrate that you
understand all of the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
labels from every line of the `writing/reflection.md` file. This means that you
should not simply delete the `TODO` marker but instead delete the entire prompt
so that your reflection is a document that contains polished technical writing
that is suitable for publication on your professional web site.
