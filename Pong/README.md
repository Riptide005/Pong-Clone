# 2D Arcade Physics Engine & Pong Clone

Made a simple Pong Clone mainly using documentation online. Tried and tested and broke the game multiple times before landing on a stable working model. Its not anything special just old school pong. Maybe in the future I may add more mechanics like power ups or random speed shifting etc.

![Pong Gameplay](gameplay.mp4)
<video src="gameplay.mp4" width="800" autoplay loop muted></video>

## Features
- **Finite State Machine (FSM):** Structured engine flow handling explicit transitions between `MENU`, `INITIALIZE` (1-second pre-round buffer) and `PLAYING` game loops.
- **Dynamic Physics & AABB Collisions:** Custom rectangle intersection routines using Axis-Aligned Bounding Box (AABB) math with strict directional locks to completely mitigate the infinite-overlap glitch.
- **Hardware Decoupling:** Implements a fixed-rate execution clock throttling physics updates to a uniform 60 FPS, ensuring identical gameplay speed regardless of host processor execution performance.
- **Deterministic Server/Resets:** Integrated randomization matrices via standard distributions to handle coin-toss round serves alongside instantaneous global state resets.

## Controls
- **Player 1:** `W` (Up) / `S` (Down)
- **Player 2:** `I` (Up) / `K` (Down)
- **Menu:** `Spacebar` (Start Game)
- **Hidden:** Theres a hidden cheat code (😉) in the files for instant victory mainly something I used for debugging purposes. Natively it is disabled but the key binds are G for Player 1 victory, V for Player 2 victory.

## Installation & Execution
Ensure you have Python 3 and Pygame installed locally:
```bash
pip install pygame
python pong.py