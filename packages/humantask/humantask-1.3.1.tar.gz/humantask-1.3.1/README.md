# [HumanTask.ai](https://www.humantask.ai) - Python Package

> ⚠️ **This package is in private beta.** If you want to try it out, [join the waitlist](https://docs.google.com/forms/d/e/1FAIpQLSf-kk7AFk1u8tz5Bsl1WpxZQFXvP6TNUKZw5IvGqKRWLhWhUg/viewform).


## Installation

```bash
pip install openai
```


## Usage

When you run a `humantask`, it will return **ONCE AND ONLY ONCE** the task is completed by a human. You **can** kill the process anytime and run it back, once the task is completed you will get the answer.

### Synchronous

```python
import os
from humantask import HumanTask

humantask = HumanTask(
    # This is the default and can be omitted
    api_key=os.environ.get("HUMANTASK_API_KEY"),
)

answer = humantask.run(
    # Put your task parameters here
)
# wait until the task is completed by a human
```

### Asynchronous

```python
import os
import asyncio
from humantask import AsyncHumanTask

humantask = AsyncHumanTask(
    # This is the default and can be omitted
    api_key=os.environ.get("HUMANTASK_API_KEY"),
)

async def main():
    answer = await humantask.run(
        # Put your task parameters here
    )
    # wait until the task is completed by a human

asyncio.run(main())
```