# Rubik's_ScramblerTimer (last update: 14/7/2024)

Rubik's_ScramblerTimer is a Python-based Rubik's Cube timer inspired by CS Timer, designed to facilitate timing solves and generating scrambles.

## Features

- **Inspection Timer**: Allows for a 15-second inspection phase before solving.
- **Solving Timer**: Accurately times solves with milliseconds precision.
- **Penalty Options**: Supports penalties like +2 and DNF (Did Not Finish).
- **Scramble Generation**: Generates random scrambles for 3x3 Rubik's Cube solving.

## Libraries Used

- `time` and `threading`: For timing operations and managing threads.
- `sys`, `termios`, `tty`, `select`: For handling terminal input and output.
- `random`: For generating random scrambles.

## Possible Improvements

- **Statistical Analysis**: Introduce average of 5 solves (AO5) and average of 12 solves (AO12) to provide quick insights into recent performance trends. Calculate Best Potential Average (BPA) and Worst Potential Average (WPA) to assess optimal and suboptimal session averages, respectively.

### User Interface
- **Graphical User Interface (GUI)**: Develop a user-friendly GUI to enhance user experience and simplify interaction with the timer.

### Customization
- **Cube Size Selection**: Allow users to choose different cube sizes (e.g., 3x3, 2x2, 4x4) and customize settings accordingly.
- **Specific Scramble Generation**: Enhance scramble generation capabilities to support specific algorithms or user-defined scramble sequences.

### Performance Optimization
- **Code Optimization**: Optimize the codebase for faster scramble generation and smoother timer operations, ensuring minimal delay between solves.


## Python Skills Demonstrated

- Multithreading and synchronization using `threading` module.
- Input handling and terminal interaction using `sys`, `termios`, `tty`, and `select`.
- Time manipulation and formatting with the `time` module.
- Randomization and list operations with the `random` module.

## Inspiration

Rubik's_ScramblerTimer draws inspiration from CS Timer, aiming to provide a simple yet effective tool for cubers to time their solves and improve their speedcubing skills.

Feel free to contribute to this project by forking and submitting pull requests!

