from track import Track
from car import Car
from renderer import Renderer
import utils


def main():
    track = Track()
    track.gen_drivers(20)
    track.cars_to_grid(20)
    renderer = Renderer(track)
    while True:
        track.tick()
        renderer.tick()


if __name__ == "__main__":
    main()
