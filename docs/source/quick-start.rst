Quick Start Guide
=================


Basics
------

Plexiglass has two main components: a CLI tool and a Python module. 
The CLI tool has two modes: `llm-chat` and `llm-test` (not implemented yet).

The `llm-chat` mode is used to chat with an LLM and measure metrics based on the LLM's response.

.. code-block:: shell

    plx --mode llm-chat --metrics toxicity

You can also pass in multiple metrics to measure at once:

.. code-block:: shell

    plx --mode llm-chat --metrics toxicity --metrics pii
  