# Contributing to Odin

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to Odin and its packages, which are hosted in the [Green Fox Academy Organization](https://github.com/green-fox-academy) on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[I don't want to read this whole thing, I just have a question!!!](#i-dont-want-to-read-this-whole-thing-i-just-have-a-question)

[How Can I Contribute?](#how-can-i-contribute)
  * [Your First Code Contribution](#your-first-code-contribution)
  * [Pull Requests](#pull-requests)

[Styleguides:](#styleguides)
  * [Git Commit Messages](#git-commit-messages)
  * [HTML & CSS Styleguide](#styleguide-for-html-and-css) 
  * [JavaScript Styleguide](#javascript-styleguide)
  * [TypeScript Styleguide](#typescript-styleguide)
  * [Java Styleguide](#java-styleguide)
  * [Documentation Styleguide](#documentation-styleguide)

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces inside A66.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [SLACK or EMAIL ADDRESS]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/

## I don't want to read this whole thing I just have a question!!!

> **Note:** Please don't file an issue to ask a question. You'll get faster results by using the resources below.

* [Join the Green Fox Academy Slack Team](https://green-fox-academy.slack.com/)
    * Even though Slack is a chat service, sometimes it takes several hours for maintainers to respond &mdash; please be patient!
    * Use the `huli` channel for general questions or discussion about Odin

## How Can I Contribute?

### Your First Code Contribution

Unsure where to begin contributing to Odin? You can start by looking through these `beginner` and `intermediate` issues:

* Beginner issues - issues which should only require a few lines of code, and a test or two.
* Intermediate issues - issues which should be a bit more involved than `beginner` issues.

### Pull Requests

The process described here has several goals:

- Maintain Odin's quality
- Fix issues that are important to users
- Engage the community in working toward the best possible Odin
- Enable a sustainable system for Odin's maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Follow all instructions in [the template](PULL_REQUEST_TEMPLATE.md)
2. Follow the [styleguides](#styleguides)
3. After you submit your pull request, verify that all [status checks](https://help.github.com/articles/about-status-checks/) are passing 

If a status check is failing, and you believe that the failure is unrelated to your change, please leave a comment on the pull request explaining why you believe the failure is unrelated. A maintainer will re-run the status check for you. If we conclude that the failure was a false positive, then we will open an issue to track that problem with our status check suite.

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

### Design Decisions

Coming soon...

## Styleguides

### Git Commit Messages

We follow the [AngularJS Commit Message Conventions](https://gist.github.com/stephenparish/9941e89d80e2bc58a153).

### Styleguide for HTML and CSS

We follow the styleguide of [Google]( https://google.github.io/styleguide/htmlcssguide.html)

#### Exceptions
 - HTML
   - Optional Tags
 - CSS
   - Declaration Order

#### Additions
 - HTML
   - Self closing slashes `/` for `void` HTML tags are optional in HTML5, be consistent, either use it in every `void` tag or in none
     - we will democratically agree to use it nowhere
       - list of `void` tags in HTML5: https://www.w3.org/TR/html-markup/syntax.html#syntax-elements
         ```html
         <!-- Good -->
         <link name="value">
         <img src="value">

         <!-- Bad -->
         <link name="value"></link>
         <img src="value"/>
         ```
 - CSS
   - Use `::` instead of `:` on pseudo element selectors. Eg.:
     ```css
     /* Good */
     .my-class::after {
       content: "apple";
     }

     /* Bad */
     .my-class:after {
       content: "apple";
     }
     ```

### JavaScript Styleguide

We follow the styleguide of [AirBnB](https://github.com/airbnb/javascript).

### TypeScript Styleguide

We follow the styleguide of [AirBnB](https://github.com/airbnb/javascript).
Always start with `use strict` as habit.

### Java Styleguide

We follow the styleguide of [Google](https://google.github.io/styleguide/javaguide.html).


### Documentation Styleguide

Use [Markdown](https://daringfireball.net/projects/markdown).
