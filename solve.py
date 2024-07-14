import time
import threading
import sys
import termios
import tty

class SolvingTimer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.penalty = ""
        self._running = False
        self._key_pressed = False

    def start_solving(self):
        # Starts the solving timer
        self.start_time = time.time()
        self._running = True
        self._update_thread = threading.Thread(target=self._update_solving_timer)
        self._update_thread.start()

    def stop(self):
        # Stops the timer
        self._running = False
        if self._update_thread is not None and threading.current_thread() != self._update_thread:
            self._update_thread.join()

        # Apply penalty if set
        if self.penalty == "+2":
            self.end_time += 2.0
        elif self.penalty == "DNF":
            self.end_time = None

    def apply_plus_two(self):
        # Applies +2 penalty
        self.penalty = "+2"

    def apply_dnf(self):
        # Marks the solve as DNF
        self.penalty = "DNF"

    def get_solving_time(self):
        # Returns the solving time in seconds
        if self.end_time is None:
            return None
        else:
            return self.end_time - self.start_time

    def _update_solving_timer(self):
        # Updates the solving timer display in real-time
        while self._running:
            elapsed = time.time() - self.start_time

            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            milliseconds = int((elapsed % 1) * 1000)
            milliseconds_tens = milliseconds // 10
            milliseconds_units = milliseconds % 10

            timer_display = f"\rSolving Time: {minutes:02d}:{seconds:02d}.{milliseconds_tens}{milliseconds_units}"
            sys.stdout.write(timer_display.ljust(40))
            sys.stdout.flush()

            if self._key_pressed:
                break

            time.sleep(0.01)

        self.end_time = time.time()

    def _format_time(self, elapsed):
        """Formats the elapsed time into mm:ss.ms format."""
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed % 1) * 1000)
        milliseconds_tens = milliseconds // 10
        milliseconds_units = milliseconds % 10
        return f"{minutes:02d}:{seconds:02d}.{milliseconds_tens}{milliseconds_units}"

    def _check_keypress(self):
        # Checks for user input (any key) to stop the timer early
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            return True
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    timer = SolvingTimer()
    print("Press any key to start the solving timer, then press any key to stop.")

    try:
        input("Press Enter to start the solving timer...")
        timer.start_solving()

        while timer._running:
            if timer._check_keypress():
                timer._key_pressed = True
                break
    except KeyboardInterrupt:
        pass
    finally:
        timer.stop()

        # Prompt user for +2, DNF, or Enter (no penalty)
        print("\nPress '+' for +2, 'd' for DNF, or press Enter for no penalty:")
        key = sys.stdin.read(1)
        if key == '+':
            timer.apply_plus_two()
        elif key == 'd':
            timer.apply_dnf()

        # Get final solving time
        solving_time = timer.get_solving_time()
        if solving_time is None:
            formatted_time = "DNF"
        else:
            formatted_time = timer._format_time(solving_time)

        # Display final time with penalty (if any)
        print(f"Final time: {formatted_time}")

