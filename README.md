pygrunn2014-snippets
====================

Code snippets from my talk at PyGrunn 2014: A first look at asyncio

Slides for the talk available at http://isnomore.net/f/pygrunn-2014-asyncio.pdf

## Anagram client/server

This is a very simple example:

- A server that listens on a port for client connections; it reads a
  sentence, "calculates" an anagram of each of its words and writes
  that back to the client.

- A client that connects to the server, sends it a sentence, waits for
  it to return an anagram version of the sentence, and prints it.

#### Usage:

Run the server:

    [rbp@stamppotje:pygrunn2014-snippets]$ python3 anagram_server.py

Then run several instances of the client, passing the sentence (in
inverted commas) as a command-line parameter:

    [rbp@stamppotje:pygrunn2014-snippets]$ python3 anagram_client.py 'To be or not to be'


    [rbp@stamppotje:pygrunn2014-snippets]$ python3 anagram_client.py 'My kingdom for a horse'


The idea is that the server will receive the first sentence first, but
will take longer to process it (see the _sleep_time
generator). It will then receive, process and answer the second
request before answering the first one, therefore exemplifying
asynchronous I/O.

The expected output is something like this:


```
[rbp@stamppotje:pygrunn2014-snippets]$ python3 anagram_server.py
Got: To be or not to be
Got: My kingdom for a horse
Wrote: My ogndmki for a hsero
Wrote: oT be ro nto ot eb

[-----]

[rbp@stamppotje:pygrunn2014-snippets]$ python3 anagram_client.py 'To be or not to be'
oT be ro nto ot eb

[-----]

[rbp@stamppotje:pygrunn2014-snippets]$ python3 anagram_client.py 'My kingdom for a horse'
My ogndmki for a hsero

```
