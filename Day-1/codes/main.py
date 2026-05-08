import asyncio
from datetime import datetime

bad_start_time = datetime.now()

async def make_tea():
    print("Put Kettle on")
    await asyncio.sleep(5) # 'await' pauses make_tea() and give control to event loop to do other tasks for 3 seconds.
    print("Tea is ready") # after 3 seconds this will print.

async def make_toast():
    print("Putting bread in toaster")
    await asyncio.sleep(3) # pauses make_toast for 2 sec
    print("Toast is ready") # after 2 sec pause this prints

async def main():
    await make_tea()
    await make_toast()

asyncio.run(main())

bad_end_time = datetime.now()

bad_duration = bad_end_time - bad_start_time
print(f"Without gather() Duration: {bad_duration}")


print()
# Good usage

good_start_time = datetime.now()

async def make_tea():
    print("Put Kettle on")
    await asyncio.sleep(5) 
    print("Tea is ready") 

async def make_toast():
    print("Putting bread in toaster")
    await asyncio.sleep(3) 
    print("Toast is ready") 

async def main():
    await asyncio.gather(make_tea(), make_toast())

asyncio.run(main())


good_end_time = datetime.now()

good_duration = good_end_time - good_start_time
print(f"With gather() Duration: {good_duration}")
