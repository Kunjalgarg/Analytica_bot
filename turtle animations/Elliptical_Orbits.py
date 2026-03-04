

import pygame, math, sys

# ---------- Config ----------
WIDTH, HEIGHT = 1000, 700
FPS = 60
BG_COLOR = (10, 10, 25)
SUN_COLOR = (255, 200, 50)
TRAIL_LENGTH = 200  # number of previous positions to keep for trail

# Gravitational parameter GM (arbitrary units). Change to scale orbital speeds.
GM = 1.0

# Center (focus) on screen
FOCUS_X, FOCUS_Y = WIDTH // 2, HEIGHT // 2

# Planets configuration: each dict has a, e, color, size, M0 (initial mean anomaly), time_scale
# a = semi-major axis (pixels), e = eccentricity (0..<1), time_scale scales orbital period
planets = [
    # small fast orbit
    {"name": "Mercury-like", "a": 80,  "e": 0.205, "color": (200,180,120), "size": 4, "M0": 0.0, "time_scale": 3.0},
    # Earth-like
    {"name": "Earth-like",   "a": 160, "e": 0.0167,"color": (100,160,255), "size": 6, "M0": 1.0, "time_scale": 1.0},
    # more eccentric orbit
    {"name": "Eccentric",    "a": 260, "e": 0.6,   "color": (255,120,120), "size": 6, "M0": 2.5, "time_scale": 0.6},
    # far, slower
    {"name": "Outer",        "a": 380, "e": 0.2,   "color": (160,255,180), "size": 8, "M0": 4.0, "time_scale": 0.4},
]

# Precompute derived params and storage
for p in planets:
    a = p["a"]
    e = p["e"]
    p["b"] = a * math.sqrt(max(0.0, 1 - e * e))   # semi-minor axis
    # mean motion n = sqrt(GM / a^3) -> radians per unit time
    # We will apply time_scale to speed up/slow down each planet (user-friendly)
    p["n"] = math.sqrt(GM / (a ** 3)) * p["time_scale"]
    p["t"] = 0.0  # elapsed time for this planet
    p["trail"] = []  # list of previous (x,y) positions for drawing trail

# ---------- Kepler solver ----------
def solve_kepler(M, e, iters=30, tol=1e-10):
    """
    Solve Kepler's equation M = E - e*sin(E) for eccentric anomaly E.
    Uses Newton-Raphson starting from E = M (good for small e) and iterations.
    """
    # Normalize M to -pi..pi for better convergence
    M = (M + math.pi) % (2 * math.pi) - math.pi
    E = M if e < 0.8 else math.pi  # initial guess
    for _ in range(iters):
        f = E - e * math.sin(E) - M
        fp = 1 - e * math.cos(E)
        if abs(fp) < 1e-14:
            break
        dE = -f / fp
        E += dE
        if abs(dE) < tol:
            break
    return E

# ---------- Pygame setup ----------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elliptical Orbits (Keplerian) - Press ESC to quit")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

def draw_text(surf, text, x, y, color=(220,220,220)):
    img = font.render(text, True, color)
    surf.blit(img, (x, y))

# ---------- Main loop ----------
running = True
global_time = 0.0  # simulation time
paused = False

while running:
    dt = clock.tick(FPS) / 1000.0  # real seconds per frame
    # scale simulation time to make motion visible; user can change factor if needed
    sim_dt = dt * 1.0  # change 1.0 -> 2.0 to speed up all orbits globally

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_UP:
                # speed up global sim time
                sim_dt *= 1.5
            elif event.key == pygame.K_DOWN:
                sim_dt *= 0.67

    if not paused:
        global_time += sim_dt

    screen.fill(BG_COLOR)

    # draw focus (sun) at center
    pygame.draw.circle(screen, SUN_COLOR, (FOCUS_X, FOCUS_Y), 12)
    draw_text(screen, "Focus (central mass)", FOCUS_X + 16, FOCUS_Y - 6)

    # draw each planet and its orbit
    for p in planets:
        a = p["a"]
        b = p["b"]
        e = p["e"]
        n = p["n"]
        size = p["size"]
        color = p["color"]
        M0 = p["M0"]

        # advance the planet's internal clock (we choose to drive with global_time scaled)
        # compute mean anomaly M = n * t + M0
        # we could use p["t"] += sim_dt * p["time_scale"] but n already includes time_scale
        M = n * global_time + M0

        # solve for eccentric anomaly E
        E = solve_kepler(M, e)

        # coordinates in orbital plane, focus at origin:
        x_orb = a * (math.cos(E) - e)
        y_orb = b * math.sin(E)

        # convert to screen coords (translate focus to FOCUS_X, FOCUS_Y)
        screen_x = int(FOCUS_X + x_orb)
        screen_y = int(FOCUS_Y + y_orb)

        # store trail
        p["trail"].append((screen_x, screen_y))
        if len(p["trail"]) > TRAIL_LENGTH:
            p["trail"].pop(0)

        # draw orbit ellipse outline (approximate with pygame.ellipse at centered rect)
        # The ellipse centered at (FOCUS_X + c, FOCUS_Y) with width 2a and height 2b
        c = a * e  # focal distance
        ellipse_rect = pygame.Rect(FOCUS_X - a + c, FOCUS_Y - b, 2 * a, 2 * b)
        pygame.draw.ellipse(screen, (80, 80, 120), ellipse_rect, 1)

        if len(p["trail"]) > 1:
            for idx in range(1, len(p["trail"])):
                alpha = int(255 * (idx / len(p["trail"])))
                tx, ty = p["trail"][idx]
                radius = max(1, int(size * (idx / len(p["trail"]))))
                # use color blended toward background for simple fade effect (no alpha)
                fade_color = tuple(int(c2 * (idx / len(p["trail"]))) for c2 in color)
                pygame.draw.circle(screen, fade_color, (tx, ty), 1)

        # draw planet
        pygame.draw.circle(screen, color, (screen_x, screen_y), size)

        # label
        draw_text(screen, p["name"], screen_x + 8, screen_y - 6)

    # UI help
    draw_text(screen, "Space: Pause/Resume   ESC: Quit", 10, 10)
    draw_text(screen, "Trails length: {}".format(TRAIL_LENGTH), 10, 30)
    draw_text(screen, "GM and a are in arbitrary units; 'a' is in pixels.", 10, 50)

    pygame.display.flip()

pygame.quit()
sys.exit()
