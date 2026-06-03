# Lesson 0.0: A real Python (not the system one)

Module 0: Project setup and CI skeleton

## Concept
macOS ships its own Python at `/usr/bin/python3` (Apple's system Python, version 3.9). It is there
for the operating system's own needs, it is old, and Apple can change or remove it on an update. The
rule on a Mac: never build your projects on the system Python. The clean fix is Homebrew, the
standard macOS package manager, used to install a current Python that you control, on a path that
survives OS updates. We installed Python 3.12 with `brew install python@3.12`, then rebuilt the
project venv on it. (3.12 rather than the newest release, because PySpark and some data tools lag
the latest Python by a version.) There is also no bare `python` or `pip` command globally, and that
is fine: those live inside the activated venv.

## Talking point
"I run projects on a Homebrew managed Python, never the macOS system Python, and pin the version per project."
