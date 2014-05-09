import asyncio
import sys


@asyncio.coroutine
def get_anagram(words):
    # Very trivial client: connects to a server, sends a string,
    # receives a string back and prints it.
    reader, writer = yield from asyncio.open_connection('localhost', 42000)
    writer.write(words.encode('utf-8'))
    answer = yield from reader.readline()
    print(answer.decode('utf-8'))
    writer.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(get_anagram(sys.argv[1]))
