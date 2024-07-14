import sys
import select
import termios
import tty
import threading
import time
from solve import SolvingTimer
from scramble import ScrambleGenerator
from inspection import InspectionTimer

def solve():
    generator = ScrambleGenerator()
    inspection_timer = InspectionTimer()
    solving_timer = SolvingTimer()

    # Generate scramble
    scramble = generator.generate_scramble()
    print(f"Generated scramble: {scramble}\n")

    print("Press any key to start Inspection...")
    wait_for_keypress()

    # Start inspection timer
    print("\n")  # Add a newline
    inspection_timer.start_inspection()

    try:
        # Suppress keypresses during inspection
        suppression_thread = threading.Thread(target=suppress_keypresses, args=(inspection_timer,))
        suppression_thread.start()

        # Wait for inspection timer to complete (15 seconds)
        inspection_timer._update_thread.join()
        suppression_thread.join()  # Ensure suppression thread finishes

    except KeyboardInterrupt:
        pass
    finally:
        inspection_timer.stop()

    # Print a newline after inspection timer ends
    print("\nInspection time ended\n")

    # Start solving timer immediately after inspection timer ends
    solving_timer.start_solving()

    try:
        while solving_timer._running:
            if solving_timer._check_keypress():
                solving_timer._key_pressed = True
                break

    except KeyboardInterrupt:
        pass

    finally:
        solving_timer.stop()

        # Prompt user for +2, DNF, or Enter (no penalty)
        print("Press '+2' for +2 penalty, 'DNF' for DNF, or press Enter for no penalty: ", end="", flush=True)
        key = sys.stdin.readline().strip()
        if key == '+2':
            solving_timer.apply_plus_two()
            final_time = solving_timer.get_solving_time() + 2.0
            print(f"\nFinal Time: {solving_timer._format_time(final_time)}")
        elif key == 'DNF':
            print(f"\nFinal Time: DNF")
        else:
            final_time = solving_timer.get_solving_time()
            if final_time is None:
                print(f"\nFinal Time: DNF")
            else:
                print(f"\nFinal Time: {solving_timer._format_time(final_time)}")

def wait_for_keypress():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def suppress_keypresses(timer):
    # Suppresses keypresses during the inspection timer
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while timer._running:
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    solve()
