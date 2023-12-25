<h1>
<img src="plexiglass/assets/plexiglass_safellama.png" width="100" height="100"><br>
Plexiglass</h1>
<!-- <p align="center"> -->

[**Quickstart**](#quickstart) | [**Installation**](#installation) |
[**Documentation**](https://safellama.github.io/plexiglass/build/html/index.html) | [**Code of Conduct**](#code-of-conduct)

<a href="https://badge.fury.io/py/plexiglass"><img src="https://badge.fury.io/py/plexiglass.svg" alt="PyPI version" height="18"></a>
<img alt="GitHub License" src="https://img.shields.io/github/license/safellama/plexiglass">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/plexiglass">
</p>

Plexiglass is a toolkit for detecting and protecting against vulnerabilities in Large Language Models (LLMs).

It is a simple command line interface (CLI) tool which allows users to quickly test LLMs against adversarial attacks such as prompt injection, jailbreaking and more. 

Plexiglass also allows security, bias and toxicity benchmarking of multiple LLMs by scraping latest adversarial prompts such as [jailbreakchat.com](https://www.jailbreakchat.com/) and [wiki_toxic](https://huggingface.co/datasets/OxAISH-AL-LLM/wiki_toxic/viewer/default/train?p=1). See more at [modes](#modes).

## Quickstart

Please follow this [quickstart guide](https://safellama.github.io/plexiglass/build/html/quick-start.html) in the documentation.

## Installation

The first experimental release is version `0.0.1`.

To download the package from PyPi:

`pip install --upgrade plexiglass`

## Modes

Plexiglass has two modes: `llm-chat` and `llm-scan`.

`llm-chat` allows you to converse with the LLM and measure predefined metrics, such as toxicity, from its responses.

`llm-scan` runs benchmarks using open-source datasets to identify and assess various vulnerabilities in the LLM.

## Feature Request
To request new features, please submit an [issue](https://github.com/enochkan/plexiglass/issues)

## Local Development

[Join us in #plexiglass on Discord.](https://discord.gg/sHuzVV8tQv)

## Contributors

<!-- Copy-paste in your Readme.md file -->

<a href="https://github.com/kortex-labs/plexiglass/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kortex-labs/plexiglass" />
</a>

### Code of Conduct

Read our [Code of Conduct](https://safellama.github.io/plexiglass/build/html/code-of-conduct.html).

Made with [contrib.rocks](https://contrib.rocks).
