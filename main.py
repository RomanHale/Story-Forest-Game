from StateMachine import ForestGame

def main():
    game=ForestGame.create()
    print(f"The gamestate is {game.state.name}.")
    game.loop()

if __name__ == "__main__":
     main()