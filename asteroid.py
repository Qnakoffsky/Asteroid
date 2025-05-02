class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.radius = radius
        self.x = x
        self.y = y
    def draw(self, surface)
        pygame.draw.circle(surface, color, (self.x, self.y), self.radius, 2)
    def update(self, dt)
        self.position += (self.velocity * dt)
