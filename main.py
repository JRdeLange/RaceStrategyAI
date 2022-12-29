from track import Track
from car import Car
from race_control import RaceControl
from renderer import Renderer
import utils


def main():
    track = Track()
    track.gen_drivers(20)
    track.cars_to_grid(20)
    race_control = RaceControl(track)
    renderer = Renderer(track)
    while True:
        track.tick()
        race_control.tick()
        renderer.tick()


if __name__ == "__main__":
    main()
