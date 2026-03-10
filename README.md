# AI File Agent

A simple AI agent capable of performing file operations within a restricted working directory using the Gemini API.

Built as a small educational project on [Boot.Dev](https://www.boot.dev) to learn the basics of working with an agent that uses tools for file operations.


## What it can do

The agent can:
- list files and directories,
- read files,
- write to files,
- run Python scripts.

---

## Limitations
All operations are restricted to the configured `WORKING_DIR`.

The agent only works inside that directory and should not have access to files outside of it.

---

## Learning Goals

The goal of this project was to build a simple proof of concept and better understand:

- how to build an AI agent that can interact with the filesystem safely,
- how to build an agent loop that feeds tool results back into the model so it can take multiple actions in a single request,
- the limitations of a simple tool-using agent

---

## Notes

❗ ***This is a simple educational project. This agent can run arbitrary Python code and is intended for learning purposes only.***
