import random

class ScrambleGenerator:
    def __init__(self):
        self.moves = ["U", "D", "L", "R", "F", "B"]
        self.modifiers = ["", "'", "2"]

    def generate_scramble(self, length=20):
        scramble = []
        previous_move = ""
        
        for _ in range(length):
            move = random.choice(self.moves)
            
            # Ensure no move is repeated consecutively
            while move == previous_move:
                move = random.choice(self.moves)
                
            modifier = random.choice(self.modifiers)
            scramble.append(move + modifier)
            previous_move = move
        
        return " ".join(scramble)

if __name__ == "__main__":
    generator = ScrambleGenerator()
    print(generator.generate_scramble())
