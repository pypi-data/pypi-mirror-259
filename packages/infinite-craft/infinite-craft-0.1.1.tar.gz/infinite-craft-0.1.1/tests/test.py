import random
import asyncio
from infinitecraft import InfiniteCraft, Logger

d = "tests/discoveries.json"
e = "tests/emoji_cache.json"

game = InfiniteCraft(
    manual_control=True,
    discoveries_storage=d,
    emoji_cache=e,
)

async def main():
    print("function started")

    await game.start()

    for x in range(10):
        async with game:

            first = random.choice(game.discoveries)
            second = random.choice(game.discoveries)

            print(f"Mixing {first} and {second}...")
            result = await game.pair(first, second)
            print(f"Result: {result}! (first discovery? {str(result.is_first_discovery).lower()})")
    
    await game.close()
    print("function ended")


asyncio.run(main())