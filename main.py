from track import Track
from car import Car
from race_control import RaceControl
from renderer import Renderer
from test_ai import TestAI
import utils


def main():
    track = Track()
    track.gen_drivers(20)
    track.cars_to_grid(20)
    race_control = RaceControl(track)
    renderer = Renderer(track)
    test_ai = TestAI(track, race_control)

    while renderer.running:
        track.tick()
        race_control.tick()
        test_ai.tick()
        renderer.tick()


if __name__ == "__main__":
    main()
