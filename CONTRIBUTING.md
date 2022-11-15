## How to contribute to the OBO Repository

Thank you for taking the time to contribute. We appreciate it!

There are two ways to contribute to this effort. The first way is to use this project's [Issues Page](https://github.com/OBOFoundry/OBOFoundry.github.io/issues), which we use as a forum to discuss both major and minor issues related to developing the OBO repository, procedures and associated web interface. Examples of the type of issues that can be submitted are:

- Issues to do with the website and other technical issues
- Issues relating to metadata about individual ontologies
- Issues regarding OBO as a whole

Please refer to the FAQ section [faq/how-do-i-edit-metadata.md](faq/how-do-i-edit-metadata.md) on making Pull Requests.

<a name="issue_resolution"></a>

## Issue Resolution

Once a pull request or issue have been submitted, anyone can comment or vote on an issue to express their opinion following the Apache voting system. Quick summary:

- **+1** something you agree with
- **-1** if you have a strong objection to an issue, which will be taken very seriously. A -1 vote should provide an alternative solution.
- **+0** or **-0** for neutral comments or weak opinions.
- It's okay to have input without voting
- Silence gives assent

A pull request with at least two **+1** votes, no **-1** votes, and that has been open for at least 3 days, is ready to be merged. The merge should be done by someone from a different organization than the submitter. (We sometimes waive the 3 days for cosmetic-only changes -- use good judgment.)

If an issue gets any **-1** votes, the comments on the issue need to reach consensus before the issue can be resolved one way or the other. There isn't any strict time limit on a contentious issue.

The project will strive for full consensus on everything until it runs into a problem with that model.

## Python Code Style

All Python code in this repository should conform to `black` and `isort`. You
can automatically apply them with `tox -e lint`.
