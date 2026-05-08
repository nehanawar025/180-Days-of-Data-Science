## Async - Await

<b>Synchronous Waiter:</b>
Takes order from table 1 -> stand in the kitchen waiting for table 1's food -> bring the food -> then go to table 2 for order.

<b>Asynchronous Waiter:</b>
One waiter many table, no idle waiting.
Python's `async`/ `await` is like that.

<b>Key Rule:</b>
`await` will always be inside `async def` 


## Things I learned

```py

async def func():
    pass

result = func() # Nothing run. Only returns coroutine object.
```

`func()` will not call the function, it will only return a coroutine object.

Coroutine functions can pause their execution and let other code run, and then resume where they left off.

To run a coroutine object, `await` keyword is needed.

```py

async def func():
    pass

result = await func() # Now it runs.
```

### Some Examples to understand better

#### Easy Example

<b>Bad usage(Synchronous):</b>

```py

import asyncio

async def make_tea():
    print("Put Kettle on")
    await asyncio.sleep(3) # 'await' pauses make_tea() and give control to event loop to do other tasks for 3 seconds.
    print("Tea is ready") # after 3 seconds this will print.

async def make_toast():
    print("Putting bread in toaster")
    await asyncio.sleep(2) # pauses make_toast for 2 sec
    print("Toast is ready") # after 2 sec pause this prints

async def main():
    await make_tea()
    await make_toast()

asyncio.run(main())

```
<br>

#### Execution Order for bad usage:

1. `asyncio.run(main())` → starts thestarts the event loop and calls `main()` 

2. Inside `main()`, `await make_tea()` starts `make_tea()`
- `print("Put Kettle on")` prints
- `await asyncio.sleep(3)` pause for 3 sec
- `print("Tea is ready")` prints
- `make_tea()` returns

3. `main()` moves to `await make_toast()`
- `print("Putting bread in toaster")` prints
- `await asyncio.sleep(2)` pauses 2 sec
- `print("Toast is ready")` prints
- return `make_toast()`

4. `main()` finishes and `asyncio.run()` cleans up.

<br>

<b>Good usage(Asynchronous):</b>

```py

import asyncio

async def make_tea():
    print("Put Kettle on")
    await asyncio.sleep(3) 
    print("Tea is ready") 

async def make_toast():
    print("Putting bread in toaster")
    await asyncio.sleep(2) 
    print("Toast is ready") 

async def main():
    await asyncio.gather(make_tea(), make_toast())

asyncio.run(main())

```
<br>

#### Execution Order for good usage:

1. `asyncio.run(main())` → starts the event loop and calls `main()` 

2. Inside `main()`, both `make_tea()` and `make_toast()` starts together.
- `print("Put Kettle on")`  and `print("Putting bread in toaster")` both executes

- `await asyncio.sleep(3)` pause for 3 sec and `await asyncio.sleep(2)` pauses 2 sec

- `make_toast()` sleep finishes(on 2nd second) then it resumes and `print("Toast is ready")` prints then return `make_toast()`

- `make_tea()` sleep finishes(on 3rd second) then it resumes and `print("Tea is ready")` prints then return `make_tea()`

3. `gather()` finishes, `main()` returns and `asyncio.run()` cleans up