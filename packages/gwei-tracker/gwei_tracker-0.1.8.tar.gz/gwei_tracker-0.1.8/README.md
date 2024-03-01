This module takes the ethereum gas price data at the time of execution and converts it to a png file.

```python
# Example
from gwei_tracker import capture_image
import asyncio

async def main():
    await capture_image("Your-api")
    

asyncio.run(main())
```