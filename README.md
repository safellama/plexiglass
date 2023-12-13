<h1 align="center">
<img src="plexiglass/assets/plexiglass.png" width="80" height="80"><br>
Plexiglass</h1>
<p align="center">
<!-- Wondering if your AI model is safe enough to use? Plexiglass is your sparring partner to bolster your model's defenses!<br><br> -->
<a href="https://badge.fury.io/py/plexiglass"><img src="https://badge.fury.io/py/plexiglass.svg" alt="PyPI version" height="18"></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-apache2.0-yellow.svg" alt="license MIT" height="18"></a>
</p>
<!-- <p align="center">A Python Machine Learning Security Toolbox for Adversarial Attacks. Works with LLMs, DNNs, and other machine learning algorithms.</p> -->

## What is Plexiglass?

Plexiglass is a toolbox designed to test vulnerabilities and safeguard LLMs.

Plexiglass uses [litellm](https://github.com/BerriAI/litellm) under the hood. 

Simply [install](#Installation) and run `plx --help` to get started.

Here's a demo:
![alt](plexiglass/assets/demo_fast.gif)

We are working tirelessly to include more frameworks and attack/ defense mechanisms for testing. Please read our [docs](https://kortex-labs.github.io/plexiglass/build/html/index.html) for the latest updates.

> [!IMPORTANT]
> We are looking for contributors! Fork the repo to get started. Contribution guide is coming soon.

> [!NOTE]
> Plexiglass is open-source: Please leave a star to support the project! ⭐

## Installation

The first experimental release is version `0.0.1`.

To download the package from PyPi:

`pip install --upgrade plexiglass`

## Modes

Plexiglass has two modes: `llm-chat` and `llm-scan`.

`llm-chat` allows you to converse with the LLM and measure predefined metrics, such as toxicity, from its responses.

`llm-scan` runs tests to identify and assess various vulnerabilities in the LLM.

## Feature Request
To request new features, please submit an [issue](https://github.com/enochkan/plexiglass/issues)

## Local Development

To get started

```python
make develop
```

this will clean, build, and install the package locally for development purpose.

## Contributors

<!-- Copy-paste in your Readme.md file -->

<a href="https://github.com/kortex-labs/plexiglass/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kortex-labs/plexiglass" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
