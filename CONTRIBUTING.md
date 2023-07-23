---

# Contributing to Panthon

First off, thank you for considering contributing to Panthon. It's people like you that make Panthon such a great tool.

## Getting Started

* Make sure you have a [GitHub account](https://github.com/signup/free)
* Submit a ticket for your issue, assuming one does not already exist.
    * Clearly describe the issue including steps to reproduce when it is a bug.
    * Make sure you fill in the earliest version that you know has the issue.
* Fork the repository on GitHub.

## Making Changes

* Create a topic branch from where you want to base your work.
    * This is usually the main branch.
    * Only target release branches if you are certain your fix must be on that branch.
    * To quickly create a topic branch based on main; `git branch fix/main/my_contribution main`. Then checkout the new branch with `git checkout fix/main/my_contribution`.
    * Please avoid working directly on the `main` branch.
* Make commits of logical units.
* Check for unnecessary whitespace with `git diff --check` before committing.
* Make sure your commit messages are in the proper format.

```    
    Example of commit message format

    Short (50 chars or less) summary of changes

    More detailed explanatory text, if necessary.  Wrap it to about 72
    characters or so. In some contexts, the first line is treated as the
    subject of an email and the rest of the text as the body.  The blank
    line separating the summary from the body is critical (unless you omit
    the body entirely); tools like rebase can get confused if you run the
    two together.

    Further paragraphs come after blank lines.

    - Bullet points are okay, too

    - Typically a hyphen or asterisk is used for the bullet, followed by a
      single space, with blank lines in between, but conventions vary here
```

* Make sure you have added the necessary tests for your changes.
* Run _all_ the tests to assure nothing else was accidentally broken.

## Submitting Changes

* Push your changes to a topic branch in your fork of the repository.
* Submit a pull request to the repository in the OpenAI organization.
* The core team looks at Pull Requests on a regular basis.
* After feedback has been given we expect responses within two weeks. After two weeks we may close the pull request if it isn't showing any activity.

## Coding conventions

Start reading our code and you'll get the hang of it. We optimize for readability:

  * We indent using four spaces (soft tabs)
  * We ALWAYS put spaces after list items and method parameters (`[1, 2, 3]`, not `[1,2,3]`), around operators (`x += 1`, not `x+=1`), and around hash arrows.
  * This is open source software. Consider the people who will read your code, and make it look nice for them. It's sort of like driving a car: Perhaps you love doing donuts when you're alone, but with passengers the goal is to make the ride as smooth as possible.

Thanks! ❤️ ❤️ ❤️

Panthon Team

---
