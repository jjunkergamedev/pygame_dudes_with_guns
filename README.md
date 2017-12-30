# pygame_dudes_with_guns
Making a game with Sass.

## Code Conventions

In general, try to follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

Data files will be in .json format. Load them in using ast.literal_eval. Save them out using json.dumps(data, indent=3).

## Goals

Start with: A 2D top down zelda-style game where the player can pick up items including different types of guns, navigate through a maze to the end, and fight against several types of enemies. There should be several screens in a dungeon that the player can move back and forth between.

#### Milestone 1: Player Movement

A player sprite can be controlled and moved by the player. There is a Goal that you can navigate to in order to win.

#### Milestone 2: Walls

Walls. The player collides with the walls, so you have to go around them. We should have a simple grid-based level editor to place the walls.

#### Milestone 3: Keys and Doors

There are collectible items: keys. You need the blue key to open a blue door, and the red key to open a red door.

#### Milestone 4: Guns and Destructible Walls

There is a collectible gun that can be picked up. Its bullets deal damage to certain vulnerable wall segments. When the segment takes enough damage it is removed.

#### Milestone 5: An Enemy

One type of enemy: A stationary enemy that fires at the player when they are in line of sight.

#### Milestone 6: More Guns and Enemies

Add more types of guns and enemies. Haven't decided what yet.
