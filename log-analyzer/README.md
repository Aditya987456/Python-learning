# Log Analyzer

A small CLI-based log analyzer built while learning Python.

Instead of only practicing Python syntax, I’m using the language to build small utilities and gradually make them more practical.

## What it does

The Log Analyzer reads a `.log` file and analyzes the logs.

It currently:

- Counts total log entries
- Counts `INFO`, `WARNING`, and `ERROR` logs
- Finds unique errors
- Calculates the frequency of each error
- Finds the most common error

## Example

Input (`app.log`):

```text
INFO: Server started
INFO: User logged in
WARNING: Slow response
ERROR: Database connection failed
ERROR: Database connection failed
ERROR: Server crashed
ERROR: Server crashed
ERROR: Server crashed