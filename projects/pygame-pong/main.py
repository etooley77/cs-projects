import asyncio

from game import Game

game = Game()

if __name__ == "__main__":
    asyncio.run(game.run())