enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside fuunction: {enemies}")

increase_enemies()
print(f"enemies outside fuunction: {enemies}")


# Global Constants

PI = 3.14159
