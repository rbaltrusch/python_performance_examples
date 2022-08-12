# Contributions to the repository

Welcome to the python performance repo and thanks for considering to contribute! Every contribution is welcome, no matter how small or large.

## Setting up your branch

To setup your local development environment, first clone the repository:

```
git clone https://github.com/rbaltrusch/python_performance_examples
```

Then install the dependencies of the example to be worked on:

```
cd source/<exampledir>
python -m pip install -r requirements.txt
```

### Github Actions

After pushing to your branch, you should be able to see whether the existing workflows still pass. Make sure that all workflows that passed before your changes are still passing, otherwise your pull request will need to fix those failures first after being submitted.

## Pull requests

The general procedure for submitting pull requests that can be easily reviewed and accepted is detailed in the [pull request template](.github/pull_request_template.md).
Please go through the points specified in the template before submitting your pull request to avoid a lengthy back-and-forth between reviews and refactoring your changes.

### Pull requests without issues

If what you are improving on in your pull request is not detailed in any issue, it would be great if you could submit an issue first and then submit your pull request, referencing that issue.

## Contact

For any questions or feedback, please raise an issue or reach out to me by email: richard@baltrusch.net.
