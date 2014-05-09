from random import shuffle
import asyncio


# This just makes sure that the first sleep() is longer than the second,
# and that one longer than the third one (and eventually will all be the same)
def _sleep_times():
    yield 8
    yield 5
    yield 3
    yield 2
    while True:
        yield 1
sleep_times = _sleep_times()

@asyncio.coroutine
def anagram(sentence):
    # This bit is just a poor man's anagram generator
    words = [list(w) for w in sentence.split()]
    for word in words:
        shuffle(word)

    # Here's the interesting bit: some slow I/O!
    # Could be reading a huge anagram list,
    # or querying a remote anagram-generating service
    yield from asyncio.sleep(next(sleep_times))

    # Finally, just return the anagrammed sentence back
    return " ".join("".join(w) for w in words)

@asyncio.coroutine
def handler(reader, writer):
    # Server handler: reads a sentence from the client...
    while True:
        line = (yield from reader.read(8*1024)).decode('utf-8').strip()
        if not line:
            break
        print("Got:", line)

        # ... relinquishes control to a coroutine that will eventually generate
        # the anagram...
        anagrammed = yield from anagram(line)

        # ... and, when that's finished and the handler coroutine is running again,
        # writes it back to the client
        writer.write((anagrammed + '\n').encode('utf-8'))
        print("Wrote:", anagrammed)

@asyncio.coroutine
def anagram_server():
    yield from asyncio.start_server(handler, 'localhost', 42000)


loop = asyncio.get_event_loop()
# Start the server...
loop.run_until_complete(anagram_server())
# And keep serving.
loop.run_forever()
