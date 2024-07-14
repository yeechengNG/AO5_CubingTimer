import time
import threading
import sys

class InspectionTimer:
    def __init__(self):
        self.start_time = None
        self._running = False
        self._update_thread = None

    def start_inspection(self):
        """Starts the inspection timer."""
        self.start_time = time.time()
        self._running = True
        self._update_thread = threading.Thread(target=self._update_inspection_timer)
        self._update_thread.start()

    def stop(self):
        """Stops the timer."""
        self._running = False
        if self._update_thread is not None and threading.current_thread() != self._update_thread:
            self._update_thread.join()

    def _update_inspection_timer(self):
        """Updates the inspection timer display in real-time."""
        inspection_duration = 15
        start_time = time.time()

        while self._running:
            elapsed = time.time() - start_time

            if elapsed >= inspection_duration:
                self._running = False
                break

            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            timer_display = f"\rInspection Time: {minutes:02d}:{seconds:02d}"
            sys.stdout.write(timer_display.ljust(30))
            sys.stdout.flush()

            # Check for specific times to show warnings
            if int(elapsed) == 8:
                self._show_warning(8)
            elif int(elapsed) == 12:
                self._show_warning(12)

            time.sleep(0.1)  # Update every 0.1 seconds

        # Ensure final display when inspection time ends exactly at 15 seconds
        if elapsed >= inspection_duration:
            sys.stdout.write("\rInspection Time: 00:15\n")
            sys.stdout.flush()

        self.stop()

    def _show_warning(self, elapsed):
        """Shows a warning message for the current elapsed time."""
        warning_display = f"\rWarning: {elapsed} SECONDS!"
        sys.stdout.write(warning_display.ljust(30))
        sys.stdout.flush()
