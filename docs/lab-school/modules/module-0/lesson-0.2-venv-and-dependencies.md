# Lesson 0.2: Virtual environments and dependencies

Module 0: Project setup and CI skeleton

## Concept
A virtualenv (venv) is the Python version of `node_modules` plus `package.json`. By default Python
installs packages globally on your machine, so two projects fight over the same versions (the
classic "it works on my machine" problem). A venv gives one project its own private Python and its
own private package folder, isolated from the system and from every other project. `requirements.txt`
is the `package.json` equivalent: the recipe of what to install. You commit the recipe, not the
cooked meal, which is why `.venv/` is gitignored but `requirements.txt` is tracked. Same instinct as
never committing `node_modules`.

## Talking point
"Each project gets an isolated venv with a pinned requirements file, so it installs the same way on
my machine and in CI."
