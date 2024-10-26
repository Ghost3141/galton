# import pygame
# import random
# import sys

# # Constants
# WIDTH, HEIGHT = 800, 600
# BALL_RADIUS = 5
# NUM_BALLS = 20
# NUM_BINS = 20
# BIN_WIDTH = WIDTH // NUM_BINS
# PEG_RADIUS = 4
# PEG_ROWS = 10
# GRAVITY = 0.5
# HORIZONTAL_STEP = 20

# # Colors
# COLORS = {
#     'background': (0, 0, 0),        # Black background
#     'peg': (30, 144, 255),          # Dodger Blue
#     'bin': (100, 149, 237),         # Steel Blue
#     'bin_outline': (0, 0, 139),     # Dark Blue
#     'ball': (70, 130, 180),         # Steel Blue
# }

# # Initialize Pygame
# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Galton Board")

# # Create pegs
# pegs = []
# for row in range(PEG_ROWS):
#     for col in range(row + 1):
#         x = WIDTH // 2 + (col - row / 2) * 40
#         y = 100 + row * 40
#         pegs.append((x, y))

# # Create bins
# bins = [0] * NUM_BINS

# def draw_bins():
#     for i in range(NUM_BINS):
#         pygame.draw.rect(screen, COLORS['bin_outline'], (i * BIN_WIDTH, HEIGHT - 50, BIN_WIDTH, 50), 1)
#         for j in range(bins[i]):
#             pygame.draw.circle(screen, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, HEIGHT - 50 - (j * 3)), BALL_RADIUS)

# def drop_ball():
#     x = WIDTH // 2
#     y = 0
#     downward_speed = 0
#     path = []

#     while y < HEIGHT - 50:
#         path.append((int(x), int(y)))

#         # Draw everything
#         screen.fill(COLORS['background'])
#         draw_bins()

#         # Draw pegs
#         for peg in pegs:
#             pygame.draw.circle(screen, COLORS['peg'], (int(peg[0]), int(peg[1])), PEG_RADIUS)

#         # Draw the ball
#         pygame.draw.circle(screen, COLORS['ball'], (int(x), int(y)), BALL_RADIUS)

#         # Draw the path
#         if len(path) > 1:
#             for i in range(len(path) - 1):
#                 pygame.draw.line(screen, COLORS['ball'], path[i], path[i + 1], 2)

#         # Update ball position
#         downward_speed += GRAVITY
#         y += downward_speed

#         # Check for peg collisions
#         collided = False
#         for peg in pegs:
#             if (peg[0] - PEG_RADIUS < x < peg[0] + PEG_RADIUS and
#                     peg[1] - PEG_RADIUS < y < peg[1] + PEG_RADIUS):
#                 collided = True
#                 if random.random() < 0.5:
#                     x += HORIZONTAL_STEP  # Move right
#                 else:
#                     x -= HORIZONTAL_STEP  # Move left
#                 break  # Exit after first collision

#         # If not colliding with any peg, update y position
#         if not collided:
#             y += downward_speed

#         # Ensure ball stays within bounds
#         x = max(min(x, WIDTH - BALL_RADIUS), BALL_RADIUS)

#         pygame.display.flip()
#         pygame.time.delay(20)

#     # Determine the bin the ball lands in
#     bin_index = min(max(0, x // BIN_WIDTH), NUM_BINS - 1)
#     collect_ball(bin_index)

# def collect_ball(bin_index):
#     # Animate the ball moving into the bin
#     target_x = bin_index * BIN_WIDTH + BIN_WIDTH // 2
#     y = HEIGHT - 50
#     while y > HEIGHT - (bins[bin_index] + 1) * 3:
#         screen.fill(COLORS['background'])
#         draw_bins()

#         # Draw pegs
#         for peg in pegs:
#             pygame.draw.circle(screen, COLORS['peg'], (int(peg[0]), int(peg[1])), PEG_RADIUS)

#         # Draw the ball moving into the bin
#         pygame.draw.circle(screen, COLORS['ball'], (int(target_x), int(y)), BALL_RADIUS)

#         y -= 1
#         pygame.display.flip()
#         pygame.time.delay(10)

#     # Update the bin count
#     bins[bin_index] += 1

# def drop_multiple_balls():
#     for _ in range(NUM_BALLS):
#         drop_ball()
#         pygame.display.flip()
#         pygame.time.delay(50)

# # Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             drop_multiple_balls()

#     screen.fill(COLORS['background'])
#     draw_bins()

#     # Draw pegs
#     for peg in pegs:
#         pygame.draw.circle(screen, COLORS['peg'], (int(peg[0]), int(peg[1])), PEG_RADIUS)

#     pygame.display.flip()

# pygame.quit()
# sys.exit()
##########################################################################################
# import pygame as pg
# from random import randrange
# import pymunk.pygame_util
# pymunk.pygame_util.positive_y_is_up = False

# RES = WIDTH, HEIGHT = 1200, 1000
# FPS = 60

# pg.init()
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# space = pymunk.Space()
# space.gravity = 0, 8000
# ball_mass, ball_radius = 1, 7
# segment_thickness = 6

# a, b, c, d = 10, 100, 18, 40
# x1, x2, x3, x4 = a, WIDTH // 2 - c, WIDTH // 2 + c, WIDTH - a
# y1, y2, y3, y4, y5 = b, HEIGHT // 4 - d, HEIGHT // 4, HEIGHT // 2 - 1.5 * b, HEIGHT - 4 * b
# L1, L2, L3, L4 = (x1, -100), (x1, y1), (x2, y2), (x2, y3)
# R1, R2, R3, R4 = (x4, -100), (x4, y1), (x3, y2), (x3, y3)
# B1, B2 = (0, HEIGHT), (WIDTH, HEIGHT)


# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
#     ball_body = pymunk.Body(ball_mass, ball_moment)
#     ball_body.position = randrange(x1, x4), randrange(-y1, y1)
#     ball_shape = pymunk.Circle(ball_body, ball_radius)
#     ball_shape.elasticity = 0.1
#     ball_shape.friction = 0.1
#     space.add(ball_body, ball_shape)
#     return ball_body


# def create_segment(from_, to_, thickness, space, color):
#     segment_shape = pymunk.Segment(space.static_body, from_, to_, thickness)
#     segment_shape.color = pg.color.THECOLORS[color]
#     space.add(segment_shape)


# def create_peg(x, y, space, color):
#     circle_shape = pymunk.Circle(space.static_body, radius=10, offset=(x, y))
#     circle_shape.color = pg.color.THECOLORS[color]
#     circle_shape.elasticity = 0.1
#     circle_shape.friction = 0.5
#     space.add(circle_shape)


# # pegs
# peg_y, step = y4, 60
# for i in range(10):
#     peg_x = -1.5 * step if i % 2 else -step
#     for j in range(WIDTH // step + 2):
#         create_peg(peg_x, peg_y, space, 'darkslateblue')
#         if i == 9:
#             create_segment((peg_x, peg_y + 50), (peg_x, HEIGHT), segment_thickness, space, 'darkslategray')
#         peg_x += step
#     peg_y += 0.5 * step

# platforms = (L1, L2), (L2, L3), (L3, L4), (R1, R2), (R2, R3), (R3, R4)
# for platform in platforms:
#     create_segment(*platform, segment_thickness, space, 'darkolivegreen')
# create_segment(B1, B2, 20, space, 'darkslategray')

# # balls
# balls = [([randrange(256) for i in range(3)], create_ball(space)) for j in range(600)]

# while True:
#     surface.fill(pg.Color('black'))

#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             exit()

#     space.step(1 / FPS)
#     space.debug_draw(draw_options)

#     # [pg.draw.circle(surface, color, ball.position, ball_radius) for color, ball in balls]
#     [pg.draw.circle(surface, color, (int(ball.position[0]), int(ball.position[1])),
#                     ball_radius) for color, ball in balls]

#     pg.display.flip()
#     clock.tick(FPS)
#######################################################################################################3
# import pygame as pg
# from random import randrange
# import pymunk
# import pymunk.pygame_util

# # Initialize Pygame and Pymunk
# pg.init()
# pymunk.pygame_util.positive_y_is_up = False

# # Constants
# RES = WIDTH, HEIGHT = 1200, 1000
# FPS = 60
# BALL_RADIUS = 7
# PEG_RADIUS = 10
# SEGMENT_THICKNESS = 6
# NUM_BINS = 30
# BIN_WIDTH = WIDTH // NUM_BINS

# # Nord Color Scheme
# COLORS = {
#     'background': (0, 0, 0),          # Black
#     'ball': (38, 70, 83),            # Nord Blue
#     'peg': (47, 54, 64),             # Nord Gray
#     'bin_outline': (68, 91, 100),     # Nord Light Gray
#     'bin_fill': (95, 129, 138),       # Nord Lighter Gray
# }

# # Create Pygame surface and clock
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# # Create a physics space
# space = pymunk.Space()
# space.gravity = 0, 8000  # Gravity

# # Create a static ground
# def create_static_body(space):
#     static_body = space.static_body
#     pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# # Create a ball
# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
#     ball_body = pymunk.Body(1, ball_moment)
#     ball_body.position = randrange(100, WIDTH - 100), -BALL_RADIUS
#     ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
#     ball_shape.elasticity = 0.5
#     ball_shape.friction = 0.5
#     space.add(ball_body, ball_shape)
#     return ball_body

# # Create a peg
# def create_peg(x, y, space):
#     peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
#     peg_body.position = x, y
#     peg_shape = pymunk.Circle(peg_body, PEG_RADIUS)
#     peg_shape.elasticity = 0.5
#     peg_shape.friction = 0.5
#     space.add(peg_body, peg_shape)

# # Create pegs in a grid
# def create_pegs(space):
#     peg_y = 200
#     step_x = 60
#     step_y = 30
#     for row in range(10):
#         for col in range(10):
#             create_peg(300 + col * step_x + (row % 2) * (step_x / 2), peg_y + row * step_y, space)

# # Create bins to collect balls
# bins = [0] * NUM_BINS
# bin_positions = [(i * BIN_WIDTH + BIN_WIDTH // 2, HEIGHT - 50) for i in range(NUM_BINS)]

# # Initialize the board
# create_static_body(space)
# create_pegs(space)

# # Main loop
# balls = []
# for _ in range(1000):  # Drop 100 balls
#     balls.append(create_ball(space))

# while True:
#     surface.fill(COLORS['background'])
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # Step the physics simulation
#     space.step(1 / FPS)

#     # Draw pegs
#     space.debug_draw(draw_options)

#     # Draw bins
#     for i in range(NUM_BINS):
#         bin_rect = pg.Rect(i * BIN_WIDTH + 1, HEIGHT - 50, BIN_WIDTH - 2, 50)  # Thinner bins
#         pg.draw.rect(surface, COLORS['bin_outline'], bin_rect, 1)
#         pg.draw.rect(surface, COLORS['bin_fill'], bin_rect.move(1, 1), 1)  # Fill with lighter gray

#     # Draw balls
#     for ball in balls:
#         # Check if the ball is in a bin
#         bin_index = int(ball.position[0] // BIN_WIDTH)
#         if ball.position[1] >= HEIGHT - 50 and 0 <= bin_index < NUM_BINS:
#             bins[bin_index] += 1
#             balls.remove(ball)  # Remove ball after it lands in a bin
#         else:
#             pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

#     # Draw bin contents
#     for i in range(NUM_BINS):
#         for j in range(bins[i]):
#             pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, HEIGHT - 50 - (j * 3)), BALL_RADIUS)

#     pg.display.flip()
#     clock.tick(FPS)
################################################################################################################################3
##randomising the pegs
# import pygame as pg
# from random import randrange, sample
# import pymunk
# import pymunk.pygame_util

# # Initialize Pygame and Pymunk
# pg.init()
# pymunk.pygame_util.positive_y_is_up = False

# # Constants
# RES = WIDTH, HEIGHT = 600, 600  # Compact dimensions
# FPS = 60
# BALL_RADIUS = 5  # Smaller ball size
# PEG_RADIUS = 7
# SEGMENT_THICKNESS = 4
# NUM_BINS = 15  # Number of bins to fit the width
# BIN_WIDTH = WIDTH // NUM_BINS

# # Nord Color Scheme
# COLORS = {
#     'background': (0, 0, 0),          # Black
#     'ball': (38, 70, 83),            # Nord Blue
#     'peg': (47, 54, 64),             # Nord Gray
#     'bin_outline': (68, 91, 100),     # Nord Light Gray
#     'bin_fill': (95, 129, 138),       # Nord Lighter Gray
# }

# # Create Pygame surface and clock
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# # Create a physics space
# space = pymunk.Space()
# space.gravity = 0, 8000  # Gravity

# # Create static walls right beside the last peg column
# def create_walls(space):
#     wall_thickness = 5
#     # Left wall
#     left_wall = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), wall_thickness)
#     left_wall.elasticity = 1.0
#     space.add(left_wall)
    
#     # Right wall (aligned with the last peg)
#     right_wall = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
#     right_wall.elasticity = 1.0
#     space.add(right_wall)

# # Create a static ground
# def create_static_body(space):
#     static_body = space.static_body
#     pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# # Create a ball
# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
#     ball_body = pymunk.Body(1, ball_moment)
    
#     # Generate x position based on exponential-like distribution
#     x_position = int(WIDTH * (1 - (1 - randrange(0, 100) / 100) ** 2))

#     ball_body.position = x_position, -BALL_RADIUS
#     ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
#     ball_shape.elasticity = 0.5
#     ball_shape.friction = 0.5
#     space.add(ball_body, ball_shape)
#     return ball_body

# # Create a peg
# def create_peg(x, y, space):
#     peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
#     peg_body.position = x, y
#     peg_shape = pymunk.Circle(peg_body, PEG_RADIUS)
#     peg_shape.elasticity = 0.5
#     peg_shape.friction = 0.5
#     space.add(peg_body, peg_shape)

# # Create random pegs with lower density and layer offsets
# def create_random_pegs(space):
#     peg_y_start = 100
#     step_y = 50  # Increased vertical spacing between rows
#     num_rows = 6  # Fewer rows of pegs
#     num_pegs_per_row = 8  # Fewer pegs per row

#     for row in range(num_rows):
#         # Randomly select unique x positions for the pegs with an offset for each row
#         x_positions = sample(range(0, WIDTH - 20, 60), num_pegs_per_row)  # Avoid edge collisions
#         # Apply an offset for each row
#         offset = row * 10  # Increase offset with each row
#         for x in x_positions:
#             create_peg(x + 20 + offset, peg_y_start + row * step_y, space)  # Added offset to fit pegs

# # Create bins to collect balls
# bins = [0] * NUM_BINS

# # Initialize the board
# create_walls(space)  # Create side walls
# create_static_body(space)
# create_random_pegs(space)

# # Main loop
# balls = []
# for _ in range(1000):  # Drop 1000 balls
#     balls.append(create_ball(space))

# while True:
#     surface.fill(COLORS['background'])
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # Step the physics simulation
#     space.step(1 / FPS)

#     # Draw pegs
#     space.debug_draw(draw_options)

#     # Draw bins
#     for i in range(NUM_BINS):
#         bin_rect = pg.Rect(i * BIN_WIDTH + 1, HEIGHT - 50, BIN_WIDTH - 2, 50)  # Thinner bins
#         pg.draw.rect(surface, COLORS['bin_outline'], bin_rect, 1)
#         pg.draw.rect(surface, COLORS['bin_fill'], bin_rect.move(1, 1), 1)  # Fill with lighter gray

#     # Draw balls
#     for ball in balls:
#         # Check if the ball is in a bin
#         bin_index = int(ball.position[0] // BIN_WIDTH)
#         if ball.position[1] >= HEIGHT - 50 and 0 <= bin_index < NUM_BINS:
#             bins[bin_index] += 1
#             balls.remove(ball)  # Remove ball after it lands in a bin
#         else:
#             pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

#     # Draw bin contents
#     for i in range(NUM_BINS):
#         for j in range(bins[i]):
#             pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, HEIGHT - 50 - (j * 3)), BALL_RADIUS)

#     pg.display.flip()
#     clock.tick(FPS)
#######################################################################################################################################
###using / pattern of pegs
# import pygame as pg
# from random import randrange
# import pymunk
# import pymunk.pygame_util

# # Initialize Pygame and Pymunk
# pg.init()
# pymunk.pygame_util.positive_y_is_up = False

# # Constants
# RES = WIDTH, HEIGHT = 600, 600  # Compact dimensions
# FPS = 60
# BALL_RADIUS = 5  # Smaller ball size
# PEG_RADIUS = 7
# SEGMENT_THICKNESS = 4
# NUM_BINS = 15  # Number of bins to fit the width
# BIN_WIDTH = WIDTH // NUM_BINS

# # Nord Color Scheme
# COLORS = {
#     'background': (0, 0, 0),          # Black
#     'ball': (38, 70, 83),            # Nord Blue
#     'peg': (47, 54, 64),             # Nord Gray
#     'bin_outline': (68, 91, 100),     # Nord Light Gray
#     'bin_fill': (95, 129, 138),       # Nord Lighter Gray
# }

# # Create Pygame surface and clock
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# # Create a physics space
# space = pymunk.Space()
# space.gravity = 0, 8000  # Gravity

# # Create static walls right beside the last peg column
# def create_walls(space):
#     wall_thickness = 5
#     # Left wall
#     left_wall = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), wall_thickness)
#     left_wall.elasticity = 1.0
#     space.add(left_wall)
    
#     # Right wall (aligned with the last peg)
#     right_wall = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
#     right_wall.elasticity = 1.0
#     space.add(right_wall)

# # Create a static ground
# def create_static_body(space):
#     static_body = space.static_body
#     pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# # Create a ball
# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
#     ball_body = pymunk.Body(1, ball_moment)

#     # Generate x position based on exponential-like distribution
#     x_position = int(WIDTH * (1 - (1 - randrange(0, 100) / 100) ** 2))

#     ball_body.position = x_position, -BALL_RADIUS
#     ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
#     ball_shape.elasticity = 0.5
#     ball_shape.friction = 0.5
#     space.add(ball_body, ball_shape)
#     return ball_body

# # Create a peg
# def create_peg(x, y, space):
#     peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
#     peg_body.position = x, y
#     peg_shape = pymunk.Circle(peg_body, PEG_RADIUS)
#     peg_shape.elasticity = 0.5
#     peg_shape.friction = 0.5
#     space.add(peg_body, peg_shape)

# # Create pegs in a slanted line pattern
# def create_slanted_pegs(space):
#     num_rows = 8
#     num_pegs_per_row = 15
#     vertical_spacing = 40
#     horizontal_spacing = WIDTH // (num_pegs_per_row - 1)

#     for row in range(num_rows):
#         # Calculate offset for slant
#         offset = row * 10  # Slight offset for each row
#         for col in range(num_pegs_per_row):
#             x_position = col * horizontal_spacing + (row % 2) * (horizontal_spacing // 2) + offset
#             y_position = row * vertical_spacing
#             create_peg(x_position, y_position + 100, space)  # Added 100 to avoid overlap with the top

# # Create bins to collect balls
# bins = [0] * NUM_BINS

# # Initialize the board
# create_walls(space)  # Create side walls
# create_static_body(space)
# create_slanted_pegs(space)

# # Main loop
# balls = []
# for _ in range(500):  # Drop 1000 balls
#     balls.append(create_ball(space))

# while True:
#     surface.fill(COLORS['background'])
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # Step the physics simulation
#     space.step(1 / FPS)

#     # Draw pegs
#     space.debug_draw(draw_options)

#     # Draw bins
#     for i in range(NUM_BINS):
#         bin_rect = pg.Rect(i * BIN_WIDTH + 1, HEIGHT - 50, BIN_WIDTH - 2, 50)  # Thinner bins
#         pg.draw.rect(surface, COLORS['bin_outline'], bin_rect, 1)
#         pg.draw.rect(surface, COLORS['bin_fill'], bin_rect.move(1, 1), 1)  # Fill with lighter gray

#     # Draw balls
#     for ball in balls:
#         # Check if the ball is in a bin
#         bin_index = int(ball.position[0] // BIN_WIDTH)
#         if ball.position[1] >= HEIGHT - 50 and 0 <= bin_index < NUM_BINS:
#             bins[bin_index] += 1
#             balls.remove(ball)  # Remove ball after it lands in a bin
#         else:
#             pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

#     # Draw bin contents
#     for i in range(NUM_BINS):
#         for j in range(bins[i]):
#             pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, HEIGHT - 50 - (j * 3)), BALL_RADIUS)

#     pg.display.flip()
#     clock.tick(FPS)

##############################################################################################################33
#using /center\ pattern
# import pygame as pg
# from random import randrange
# import pymunk
# import pymunk.pygame_util

# # Initialize Pygame and Pymunk
# pg.init()
# pymunk.pygame_util.positive_y_is_up = False

# # Constants
# RES = WIDTH, HEIGHT = 600, 600  # Compact dimensions
# FPS = 60
# BALL_RADIUS = 5  # Smaller ball size
# PEG_RADIUS = 7
# SEGMENT_THICKNESS = 4
# NUM_BINS = 15  # Number of bins to fit the width
# BIN_WIDTH = WIDTH // NUM_BINS

# # Nord Color Scheme
# COLORS = {
#     'background': (0, 0, 0),          # Black
#     'ball': (38, 70, 83),            # Nord Blue
#     'peg': (47, 54, 64),             # Nord Gray
#     'bin_outline': (68, 91, 100),     # Nord Light Gray
#     'bin_fill': (95, 129, 138),       # Nord Lighter Gray
# }

# # Create Pygame surface and clock
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# # Create a physics space
# space = pymunk.Space()
# space.gravity = 0, 8000  # Gravity

# # Create static walls right beside the last peg column
# def create_walls(space):
#     wall_thickness = 5
#     # Left wall
#     left_wall = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), wall_thickness)
#     left_wall.elasticity = 1.0
#     space.add(left_wall)
    
#     # Right wall (aligned with the last peg)
#     right_wall = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
#     right_wall.elasticity = 1.0
#     space.add(right_wall)

# # Create a static ground
# def create_static_body(space):
#     static_body = space.static_body
#     pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# # Create a ball
# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
#     ball_body = pymunk.Body(1, ball_moment)

#     # Generate x position based on exponential-like distribution
#     x_position = int(WIDTH * (1 - (1 - randrange(0, 100) / 100) ** 2))

#     ball_body.position = x_position, -BALL_RADIUS
#     ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
#     ball_shape.elasticity = 0.5
#     ball_shape.friction = 0.5
#     space.add(ball_body, ball_shape)
#     return ball_body

# # Create a peg
# def create_peg(x, y, space):
#     peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
#     peg_body.position = x, y
#     peg_shape = pymunk.Circle(peg_body, PEG_RADIUS)
#     peg_shape.elasticity = 0.5
#     peg_shape.friction = 0.5
#     space.add(peg_body, peg_shape)

# # Create pegs in a center (V) pattern
# def create_center_pegs(space):
#     num_rows = 8
#     vertical_spacing = 50
#     max_pegs_in_row = 15

#     for row in range(num_rows):
#         # Determine number of pegs in the current row
#         num_pegs = max_pegs_in_row - row if row < max_pegs_in_row // 2 else row + 1
#         # Calculate the horizontal spacing based on the row
#         horizontal_spacing = WIDTH / (num_pegs + 1)

#         for col in range(num_pegs):
#             x_position = (col + 1) * horizontal_spacing
#             # Adjust x position for the center V shape
#             if row >= max_pegs_in_row // 2:
#                 x_position = WIDTH - x_position  # Mirror for the lower half
#             y_position = row * vertical_spacing + 100  # Added 100 to avoid overlap with the top
#             create_peg(x_position, y_position, space)

# # Create bins to collect balls
# bins = [0] * NUM_BINS

# # Initialize the board
# create_walls(space)  # Create side walls
# create_static_body(space)
# create_center_pegs(space)

# # Main loop
# balls = []
# for _ in range(500):  # Drop 1000 balls
#     balls.append(create_ball(space))

# while True:
#     surface.fill(COLORS['background'])
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # Step the physics simulation
#     space.step(1 / FPS)

#     # Draw pegs
#     space.debug_draw(draw_options)

#     # Draw bins
#     for i in range(NUM_BINS):
#         bin_rect = pg.Rect(i * BIN_WIDTH + 1, HEIGHT - 50, BIN_WIDTH - 2, 50)  # Thinner bins
#         pg.draw.rect(surface, COLORS['bin_outline'], bin_rect, 1)
#         pg.draw.rect(surface, COLORS['bin_fill'], bin_rect.move(1, 1), 1)  # Fill with lighter gray

#     # Draw balls
#     for ball in balls:
#         # Check if the ball is in a bin
#         bin_index = int(ball.position[0] // BIN_WIDTH)
#         if ball.position[1] >= HEIGHT - 50 and 0 <= bin_index < NUM_BINS:
#             bins[bin_index] += 1
#             balls.remove(ball)  # Remove ball after it lands in a bin
#         else:
#             pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

#     # Draw bin contents
#     for i in range(NUM_BINS):
#         for j in range(bins[i]):
#             pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, HEIGHT - 50 - (j * 3)), BALL_RADIUS)

#     pg.display.flip()
#     clock.tick(FPS)
######################################################################################################################
# import pygame as pg
# from random import randrange
# import pymunk
# import pymunk.pygame_util

# # Initialize Pygame and Pymunk
# pg.init()
# pymunk.pygame_util.positive_y_is_up = False

# # Constants
# RES = WIDTH, HEIGHT = 600, 600  # Compact dimensions
# FPS = 60
# BALL_RADIUS = 5  # Smaller ball size
# PEG_RADIUS = 7
# SEGMENT_THICKNESS = 4
# NUM_BINS = 15  # Number of bins to fit the width
# BIN_WIDTH = WIDTH // NUM_BINS

# # Nord Color Scheme
# COLORS = {
#     'background': (0, 0, 0),          # Black
#     'ball': (38, 70, 83),            # Nord Blue
#     'peg': (47, 54, 64),             # Nord Gray
#     'bin_outline': (68, 91, 100),     # Nord Light Gray
#     'bin_fill': (95, 129, 138),       # Nord Lighter Gray
# }

# # Create Pygame surface and clock
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# # Create a physics space
# space = pymunk.Space()
# space.gravity = 0, 8000  # Gravity

# # Create static walls right beside the last peg column
# def create_walls(space):
#     wall_thickness = 5
#     # Left wall
#     left_wall = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), wall_thickness)
#     left_wall.elasticity = 1.0
#     space.add(left_wall)
    
#     # Right wall (aligned with the last peg)
#     right_wall = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
#     right_wall.elasticity = 1.0
#     space.add(right_wall)

# # Create a static ground
# def create_static_body(space):
#     static_body = space.static_body
#     pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# # Create a ball
# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
#     ball_body = pymunk.Body(1, ball_moment)

#     # Generate x position based on exponential-like distribution
#     x_position = int(WIDTH * (1 - (1 - randrange(0, 100) / 100) ** 2))

#     ball_body.position = x_position, -BALL_RADIUS
#     ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
#     ball_shape.elasticity = 0.5
#     ball_shape.friction = 0.5
#     space.add(ball_body, ball_shape)
#     return ball_body

# # Create a peg
# def create_peg(x, y, space):
#     peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
#     peg_body.position = x, y
#     peg_shape = pymunk.Circle(peg_body, PEG_RADIUS)
#     peg_shape.elasticity = 0.5
#     peg_shape.friction = 0.5
#     space.add(peg_body, peg_shape)

# # Create pegs in a "\center/" pattern
# def create_center_slash_pegs(space):
#     num_rows = 8
#     vertical_spacing = 50
#     max_pegs_in_row = NUM_BINS  # Maximum pegs in the top row

#     for row in range(num_rows):
#         # Determine the number of pegs in the current row
#         num_pegs = max_pegs_in_row - row if row < max_pegs_in_row // 2 else row + 1
#         # Calculate the horizontal spacing based on the row
#         horizontal_spacing = WIDTH / (max_pegs_in_row + 1)

#         for col in range(num_pegs):
#             if row < num_rows // 2:
#                 x_position = (col + 1) * horizontal_spacing
#             else:
#                 x_position = WIDTH - (col + 1) * horizontal_spacing  # Mirror for the lower half
            
#             y_position = row * vertical_spacing + 100  # Added 100 to avoid overlap with the top
#             create_peg(x_position, y_position, space)

# # Create bins to collect balls
# bins = [0] * NUM_BINS

# # Initialize the board
# create_walls(space)  # Create side walls
# create_static_body(space)
# create_center_slash_pegs(space)

# # Main loop
# balls = []
# for _ in range(1000):  # Drop 1000 balls
#     balls.append(create_ball(space))

# while True:
#     surface.fill(COLORS['background'])
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # Step the physics simulation
#     space.step(1 / FPS)

#     # Draw pegs
#     space.debug_draw(draw_options)

#     # Draw bins
#     for i in range(NUM_BINS):
#         bin_rect = pg.Rect(i * BIN_WIDTH + 1, HEIGHT - 50, BIN_WIDTH - 2, 50)  # Thinner bins
#         pg.draw.rect(surface, COLORS['bin_outline'], bin_rect, 1)
#         pg.draw.rect(surface, COLORS['bin_fill'], bin_rect.move(1, 1), 1)  # Fill with lighter gray

#     # Draw balls
#     for ball in balls:
#         # Check if the ball is in a bin
#         bin_index = int(ball.position[0] // BIN_WIDTH)
#         if ball.position[1] >= HEIGHT - 50 and 0 <= bin_index < NUM_BINS:
#             bins[bin_index] += 1
#             balls.remove(ball)  # Remove ball after it lands in a bin
#         else:
#             pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

#     # Draw bin contents
#     for i in range(NUM_BINS):
#         for j in range(bins[i]):
#             pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, HEIGHT - 50 - (j * 3)), BALL_RADIUS)

#     pg.display.flip()
#     clock.tick(FPS)
#######################################################################################################################
####exponential
#Exponential-like Positioning: The x-position of the balls is calculated using a cubic function: x_position = int(WIDTH * (1 - (1 - randrange(0, 100) / 100) ** 3)). This gives a stronger bias toward the center bins, creating an exponential-like distribution.
#chat gpt modified
# import pygame as pg
# import numpy as np
# import pymunk
# import pymunk.pygame_util

# # Initialize Pygame and Pymunk
# pg.init()
# pymunk.pygame_util.positive_y_is_up = False

# # Constants
# RES = WIDTH, HEIGHT = 800, 1200  # Set frame size
# FPS = 60
# BALL_RADIUS = 5  # Ball size
# PEG_RADIUS = 7
# NUM_BINS = 15  # Number of bins
# BIN_WIDTH = WIDTH // NUM_BINS  # Width of each bin
# BIN_Y_POSITION = HEIGHT - 100  # Position of the bins
# PEG_Y_POSITION = HEIGHT - 700  # Position of the pegs

# # Color Scheme
# COLORS = {
#     'background': (0, 0, 0),          # Black
#     'ball': (38, 70, 83),            # Ball color
#     'peg': (47, 54, 64),             # Peg color
#     'bin_outline': (68, 91, 100),     # Bin outline color
#     'bin_fill': (95, 129, 138),       # Bin fill color
# }

# # Create Pygame surface and clock
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# # Create a physics space
# space = pymunk.Space()
# space.gravity = 0, 8000  # Gravity

# # Create static walls
# def create_walls(space):
#     wall_thickness = 5
#     left_wall = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), wall_thickness)
#     left_wall.elasticity = 1.0
#     space.add(left_wall)

#     right_wall = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
#     right_wall.elasticity = 1.0
#     space.add(right_wall)

# # Create a static ground
# def create_static_body(space):
#     static_body = space.static_body
#     pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# # Create a ball with exponential distribution for x-position
# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
#     ball_body = pymunk.Body(1, ball_moment)

#     # Generate x position using an exponential distribution
#     lambda_param = 1 / (WIDTH / 2)  # Adjust lambda for desired spread
#     x_position = int(np.random.exponential(scale=1/lambda_param) * WIDTH / 3)

#     # Clamp x_position to ensure it stays within bounds
#     x_position = min(max(x_position, 0), WIDTH - BALL_RADIUS)

#     ball_body.position = x_position, -BALL_RADIUS
#     ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
#     ball_shape.elasticity = 0.5
#     ball_shape.friction = 0.5
#     space.add(ball_body, ball_shape)
#     return ball_body

# # Create a peg
# def create_peg(x, y, space):
#     peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
#     peg_body.position = x, y
#     peg_shape = pymunk.Circle(peg_body, PEG_RADIUS)
#     peg_shape.elasticity = 0.5
#     peg_shape.friction = 0.5
#     space.add(peg_body, peg_shape)

# # Create pegs in a "\center/" pattern
# def create_center_slash_pegs(space):
#     num_rows = 8
#     vertical_spacing = 50
#     max_pegs_in_row = NUM_BINS + 5  # More pegs in the top rows

#     for row in range(num_rows):
#         num_pegs = max_pegs_in_row - row if row < num_rows // 2 else row + 1
#         horizontal_spacing = WIDTH / (max_pegs_in_row + 1)

#         for col in range(num_pegs):
#             if row < num_rows // 2:
#                 x_position = (col + 1) * horizontal_spacing
#             else:
#                 x_position = WIDTH - (col + 1) * horizontal_spacing

#             y_position = row * vertical_spacing + 100
#             create_peg(x_position, y_position, space)

# # Create bins to collect balls
# bins = [0] * NUM_BINS

# # Initialize the board
# create_walls(space)
# create_static_body(space)
# create_center_slash_pegs(space)

# # Main loop
# balls = []
# for _ in range(1000):  # Drop 1000 balls
#     balls.append(create_ball(space))

# while True:
#     surface.fill(COLORS['background'])
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # Step the physics simulation
#     space.step(1 / FPS)

#     # Draw pegs
#     space.debug_draw(draw_options)

#     # Draw bins
#     for i in range(NUM_BINS):
#         bin_rect = pg.Rect(i * BIN_WIDTH + 1, BIN_Y_POSITION, BIN_WIDTH - 2, 50)
#         pg.draw.rect(surface, COLORS['bin_outline'], bin_rect, 1)
#         pg.draw.rect(surface, COLORS['bin_fill'], bin_rect.move(1, 1), 1)

#     # Draw balls
#     for ball in balls:
#         bin_index = int(ball.position[0] // BIN_WIDTH)
#         if ball.position[1] >= BIN_Y_POSITION and 0 <= bin_index < NUM_BINS:
#             bins[bin_index] += 1
#             balls.remove(ball)
#         else:
#             pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

#     # Draw bin contents
#     for i in range(NUM_BINS):
#         for j in range(bins[i]):
#             pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, BIN_Y_POSITION - (j * 3)), BALL_RADIUS)

#     pg.display.flip()
#     clock.tick(FPS)




######################################################################################################################3
##potential log normal

# import pygame as pg
# from random import randrange
# import numpy as np
# import pymunk
# import pymunk.pygame_util

# # Initialize Pygame and Pymunk
# pg.init()
# pymunk.pygame_util.positive_y_is_up = False

# # Constants
# RES = WIDTH, HEIGHT = 900, 1100  # Updated dimensions
# FPS = 60
# BALL_RADIUS = 5  # Smaller ball size
# PEG_RADIUS = 7
# SEGMENT_THICKNESS = 4
# NUM_BINS = 15  # Number of bins to fit the width
# BIN_WIDTH = WIDTH // NUM_BINS

# # Nord Color Scheme
# COLORS = {
#     'background': (0, 0, 0),          # Black
#     'ball': (38, 70, 83),            # Nord Blue
#     'peg': (47, 54, 64),             # Nord Gray
#     'bin_outline': (68, 91, 100),     # Nord Light Gray
#     'bin_fill': (95, 129, 138),       # Nord Lighter Gray
# }

# # Create Pygame surface and clock
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# # Create a physics space
# space = pymunk.Space()
# space.gravity = 0, 8000  # Gravity

# # Create static walls
# def create_walls(space):
#     wall_thickness = 5
#     left_wall = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), wall_thickness)
#     left_wall.elasticity = 1.0
#     space.add(left_wall)
    
#     right_wall = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
#     right_wall.elasticity = 1.0
#     space.add(right_wall)

# # Create a static ground
# def create_static_body(space):
#     static_body = space.static_body
#     pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# # Create a ball with log-normal distribution for x-position
# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
#     ball_body = pymunk.Body(1, ball_moment)

#     # Generate x position using a log-normal distribution
#     mean = np.log(WIDTH / 2)  # Center the mean
#     sigma = 0.5  # Standard deviation for spread
#     x_position = int(np.random.lognormal(mean, sigma))

#     # Clamp x_position to be within bounds
#     x_position = min(max(x_position, 0), WIDTH)

#     ball_body.position = x_position, -BALL_RADIUS
#     ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
#     ball_shape.elasticity = 0.5
#     ball_shape.friction = 0.5
#     space.add(ball_body, ball_shape)
#     return ball_body

# # Create a peg
# def create_peg(x, y, space):
#     peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
#     peg_body.position = x, y
#     peg_shape = pymunk.Circle(peg_body, PEG_RADIUS)
#     peg_shape.elasticity = 0.5
#     peg_shape.friction = 0.5
#     space.add(peg_body, peg_shape)

# # Create pegs in a "\center/" pattern
# def create_center_slash_pegs(space):
#     num_rows = 8
#     vertical_spacing = 50
#     max_pegs_in_row = NUM_BINS  # Maximum pegs in the top row

#     for row in range(num_rows):
#         num_pegs = max_pegs_in_row - row if row < max_pegs_in_row // 2 else row + 1
#         horizontal_spacing = WIDTH / (max_pegs_in_row + 1)

#         for col in range(num_pegs):
#             if row < num_rows // 2:
#                 x_position = (col + 1) * horizontal_spacing
#             else:
#                 x_position = WIDTH - (col + 1) * horizontal_spacing
            
#             y_position = row * vertical_spacing + 100
#             create_peg(x_position, y_position, space)

# # Create bins to collect balls
# bins = [0] * NUM_BINS

# # Initialize the board
# create_walls(space)
# create_static_body(space)
# create_center_slash_pegs(space)

# # Main loop
# balls = []
# for _ in range(800):  # Drop 1000 balls
#     balls.append(create_ball(space))

# while True:
#     surface.fill(COLORS['background'])
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # Step the physics simulation
#     space.step(1 / FPS)

#     # Draw pegs
#     space.debug_draw(draw_options)

#     # Draw bins
#     for i in range(NUM_BINS):
#         bin_rect = pg.Rect(i * BIN_WIDTH + 1, HEIGHT - 50, BIN_WIDTH - 2, 50)
#         pg.draw.rect(surface, COLORS['bin_outline'], bin_rect, 1)
#         pg.draw.rect(surface, COLORS['bin_fill'], bin_rect.move(1, 1), 1)

#     # Draw balls
#     for ball in balls:
#         bin_index = int(ball.position[0] // BIN_WIDTH)
#         if ball.position[1] >= HEIGHT - 50 and 0 <= bin_index < NUM_BINS:
#             bins[bin_index] += 1
#             balls.remove(ball)
#         else:
#             pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

#     # Draw bin contents
#     for i in range(NUM_BINS):
#         for j in range(bins[i]):
#             pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, HEIGHT - 50 - (j * 3)), BALL_RADIUS)

#     pg.display.flip()
#     clock.tick(FPS)

#####################################################################################################################
##cauchy?
# import pygame as pg
# from random import random
# import pymunk
# import pymunk.pygame_util

# # Initialize Pygame and Pymunk
# pg.init()
# pymunk.pygame_util.positive_y_is_up = False

# # Constants
# RES = WIDTH, HEIGHT = 800, 1100  
# FPS = 60
# BALL_RADIUS = 5
# PEG_RADIUS = 7
# SEGMENT_THICKNESS = 4
# NUM_BINS = 15  # Number of bins
# BIN_HEIGHT = 40  # Height of each bin
# BIN_WIDTH = WIDTH // NUM_BINS  # Width of each bin base
# CHANNEL_WIDTH = 40  # Width of the channel
# BIN_Y_POSITION = HEIGHT - 100  # Position of the bins
# PEG_Y_POSITION = HEIGHT - 700  # Y position for the pegs

# # Color Scheme
# COLORS = {
#     'background': (0, 0, 0),
#     'ball': (38, 70, 83),
#     'peg': (47, 54, 64),
#     'bin_outline': (68, 91, 100),
#     'bin_fill': (95, 129, 138),
# }

# # Create Pygame surface and clock
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# # Create a physics space
# space = pymunk.Space()
# space.gravity = 0, 8000

# # Create static walls
# def create_walls(space):
#     wall_thickness = 5
#     left_wall = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), wall_thickness)
#     left_wall.elasticity = 1.0
#     space.add(left_wall)
    
#     right_wall = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
#     right_wall.elasticity = 1.0
#     space.add(right_wall)

# # Create a static ground
# def create_static_body(space):
#     static_body = space.static_body
#     pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# # Create a ball
# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
#     ball_body = pymunk.Body(1, ball_moment)

#     # Centered position in the channel
#     x_position = WIDTH // 2
#     ball_body.position = x_position, -BALL_RADIUS
#     ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
#     ball_shape.elasticity = 0.5
#     ball_shape.friction = 0.5
#     space.add(ball_body, ball_shape)
#     return ball_body

# # Create a peg
# def create_peg(x, y, space):
#     peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
#     peg_body.position = x, y
#     peg_shape = pymunk.Circle(peg_body, PEG_RADIUS)
#     peg_shape.elasticity = 0.5
#     peg_shape.friction = 0.5
#     space.add(peg_body, peg_shape)

# # Create rectangular bins arrangement
# def create_bins():
#     for i in range(NUM_BINS):
#         x = i * BIN_WIDTH
#         pg.draw.rect(surface, COLORS['bin_fill'], (x, BIN_Y_POSITION, BIN_WIDTH, BIN_HEIGHT))
#         pg.draw.rect(surface, COLORS['bin_outline'], (x, BIN_Y_POSITION, BIN_WIDTH, BIN_HEIGHT), 2)

# # Create asymmetric triangle peg arrangement
# def create_asymmetric_triangle_pegs(space):
#     num_rows = 8
#     vertical_spacing = 50
#     max_pegs_in_row = NUM_BINS + 5

#     for row in range(num_rows):
#         if row < num_rows // 2:
#             num_pegs = max_pegs_in_row - row * 2
#         else:
#             num_pegs = max_pegs_in_row - row

#         horizontal_spacing = WIDTH / (num_pegs + 1)

#         for col in range(num_pegs):
#             x_position = (col + 1) * horizontal_spacing
#             y_position = PEG_Y_POSITION - (row * vertical_spacing)  # Position pegs above the bins
#             create_peg(x_position, y_position, space)

# # Create bins to collect balls
# bins = [0] * NUM_BINS

# # Initialize the board
# create_walls(space)
# create_static_body(space)
# create_asymmetric_triangle_pegs(space)

# # Create a channel for dropping balls
# def create_drop_channel():
#     pg.draw.rect(surface, COLORS['bin_outline'], (WIDTH // 2 - CHANNEL_WIDTH // 2, 0, CHANNEL_WIDTH, 100), 1)

# # Main loop
# balls = []
# for _ in range(500):  # Drop 1000 balls
#     balls.append(create_ball(space))

# while True:
#     surface.fill(COLORS['background'])
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # Step the physics simulation
#     space.step(1 / FPS)

#     # Draw pegs
#     space.debug_draw(draw_options)

#     # Draw bins
#     create_bins()

#     # Draw drop channel
#     create_drop_channel()

#     # Draw balls
#     for ball in balls:
#         bin_index = int(ball.position[0] // BIN_WIDTH)
#         if ball.position[1] >= BIN_Y_POSITION and 0 <= bin_index < NUM_BINS:
#             bins[bin_index] += 1
#             balls.remove(ball)
#         else:
#             pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

#     # Draw bin contents
#     for i in range(NUM_BINS):
#         for j in range(bins[i]):
#             pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, BIN_Y_POSITION + BIN_HEIGHT - (j * 3)), BALL_RADIUS)

#     pg.display.flip()
#     clock.tick(FPS)
############################################################################################################################################33
# # An interesting curve
# import pygame as pg
# import numpy as np
# import pymunk
# import pymunk.pygame_util

# # Initialize Pygame and Pymunk
# pg.init()
# pymunk.pygame_util.positive_y_is_up = False

# # Constants
# RES = WIDTH, HEIGHT = 800, 1200  # Set frame size
# FPS = 60
# BALL_RADIUS = 5  # Ball size
# PEG_RADIUS = 7
# NUM_BINS = 15  # Number of bins
# BIN_WIDTH = WIDTH // NUM_BINS  # Width of each bin
# BIN_Y_POSITION = HEIGHT - 100  # Position of the bins
# PEG_Y_POSITION = HEIGHT - 700  # Position of the pegs

# # Color Scheme
# COLORS = {
#     'background': (0, 0, 0),          # Black
#     'ball': (38, 70, 83),            # Ball color
#     'peg': (47, 54, 64),             # Peg color
#     'bin_outline': (68, 91, 100),     # Bin outline color
#     'bin_fill': (95, 129, 138),       # Bin fill color
# }

# # Create Pygame surface and clock
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# # Create a physics space
# space = pymunk.Space()
# space.gravity = 0, 8000  # Gravity

# # Create static walls
# def create_walls(space):
#     wall_thickness = 5
#     left_wall = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), wall_thickness)
#     left_wall.elasticity = 1.0
#     space.add(left_wall)

#     right_wall = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
#     right_wall.elasticity = 1.0
#     space.add(right_wall)

# # Create a static ground
# def create_static_body(space):
#     static_body = space.static_body
#     pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# # Create a ball with log-normal distribution for x-position
# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
#     ball_body = pymunk.Body(1, ball_moment)

#     # Generate x position using a log-normal distribution
#     mean = np.log(WIDTH / 4)  # Centered towards the left
#     sigma = 0.5  # Standard deviation for spread
#     x_position = int(np.random.lognormal(mean, sigma))

#     # Clamp x_position to be within bounds
#     x_position = min(max(x_position, 0), WIDTH)

#     ball_body.position = x_position, -BALL_RADIUS
#     ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
#     ball_shape.elasticity = 0.5
#     ball_shape.friction = 0.5
#     space.add(ball_body, ball_shape)
#     return ball_body

# # Create a peg
# def create_peg(x, y, space):
#     peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
#     peg_body.position = x, y
#     peg_shape = pymunk.Circle(peg_body, PEG_RADIUS)
#     peg_shape.elasticity = 0.5
#     peg_shape.friction = 0.5
#     space.add(peg_body, peg_shape)

# # Create pegs in a "\center/" pattern
# def create_center_slash_pegs(space):
#     num_rows = 8
#     vertical_spacing = 50
#     max_pegs_in_row = NUM_BINS + 5  # More pegs in the top rows

#     for row in range(num_rows):
#         num_pegs = max_pegs_in_row - row if row < num_rows // 2 else row + 1
#         horizontal_spacing = WIDTH / (max_pegs_in_row + 1)

#         for col in range(num_pegs):
#             if row < num_rows // 2:
#                 x_position = (col + 1) * horizontal_spacing
#             else:
#                 x_position = WIDTH - (col + 1) * horizontal_spacing

#             y_position = row * vertical_spacing + 100
#             create_peg(x_position, y_position, space)

# # Create bins to collect balls
# bins = [0] * NUM_BINS

# # Initialize the board
# create_walls(space)
# create_static_body(space)
# create_center_slash_pegs(space)

# # Main loop
# balls = []
# for _ in range(1000):  # Drop 1000 balls
#     balls.append(create_ball(space))

# while True:
#     surface.fill(COLORS['background'])
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # Step the physics simulation
#     space.step(1 / FPS)

#     # Draw pegs
#     space.debug_draw(draw_options)

#     # Draw bins
#     for i in range(NUM_BINS):
#         bin_rect = pg.Rect(i * BIN_WIDTH + 1, BIN_Y_POSITION, BIN_WIDTH - 2, 50)
#         pg.draw.rect(surface, COLORS['bin_outline'], bin_rect, 1)
#         pg.draw.rect(surface, COLORS['bin_fill'], bin_rect.move(1, 1), 1)

#     # Draw balls
#     for ball in balls:
#         bin_index = int(ball.position[0] // BIN_WIDTH)
#         if ball.position[1] >= BIN_Y_POSITION and 0 <= bin_index < NUM_BINS:
#             bins[bin_index] += 1
#             balls.remove(ball)
#         else:
#             pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

#     # Draw bin contents
#     for i in range(NUM_BINS):
#         for j in range(bins[i]):
#             pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, BIN_Y_POSITION - (j * 3)), BALL_RADIUS)

#     pg.display.flip()
#     clock.tick(FPS)
#####################################################################################################################################3
#aesthetic bell curve 
# import pygame as pg
# import numpy as np
# import pymunk
# import pymunk.pygame_util

# # Initialize Pygame and Pymunk
# pg.init()
# pymunk.pygame_util.positive_y_is_up = False

# # Constants
# RES = WIDTH, HEIGHT = 800, 1200  # Set frame size
# FPS = 60
# BALL_RADIUS = 5  # Ball size
# PEG_LENGTH_A = 10  # Length of side A
# PEG_LENGTH_B = 5  # Length of side B
# PEG_LENGTH_C = 15  # Length of side C
# NUM_BINS = 15  # Number of bins
# BIN_WIDTH = WIDTH // NUM_BINS  # Width of each bin
# BIN_Y_POSITION = HEIGHT - 100  # Position of the bins
# PEG_Y_POSITION = HEIGHT - 700  # Position of the pegs

# # Color Scheme
# COLORS = {
#     'background': (0, 0, 0),          # Black
#     'ball': (38, 70, 83),            # Ball color
#     'peg': (47, 54, 64),             # Peg color
#     'bin_outline': (68, 91, 100),     # Bin outline color
#     'bin_fill': (95, 129, 138),       # Bin fill color
# }

# # Create Pygame surface and clock
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# # Create a physics space
# space = pymunk.Space()
# space.gravity = 0, 8000  # Gravity

# # Create static walls
# def create_walls(space):
#     wall_thickness = 5
#     left_wall = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), wall_thickness)
#     left_wall.elasticity = 1.0
#     space.add(left_wall)

#     right_wall = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
#     right_wall.elasticity = 1.0
#     space.add(right_wall)

# # Create a static ground
# def create_static_body(space):
#     static_body = space.static_body
#     pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# # Create a ball with exponential distribution for x-position
# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
#     ball_body = pymunk.Body(1, ball_moment)

#     # Generate x position based on a normal distribution
#     x_position = WIDTH // 2  # Drop from the center

#     ball_body.position = x_position, -BALL_RADIUS
#     ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
#     ball_shape.elasticity = 0.5
#     ball_shape.friction = 0.5
#     space.add(ball_body, ball_shape)
#     return ball_body

# # Create a triangular peg based on side lengths
# def create_peg(x, y, space, length_a, length_b, length_c):
#     peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
#     peg_body.position = x, y
    
#     # Calculate triangle vertices
#     angle_A = np.arccos((length_b**2 + length_c**2 - length_a**2) / (2 * length_b * length_c))
#     angle_B = np.arccos((length_a**2 + length_c**2 - length_b**2) / (2 * length_a * length_c))
    
#     vertex_A = (0, 0)  # Starting point at the top
#     vertex_B = (length_b * np.cos(angle_A), length_b * np.sin(angle_A))
#     vertex_C = (length_c * np.cos(np.pi - angle_B), length_c * np.sin(np.pi - angle_B))

#     vertices = [vertex_A, vertex_B, vertex_C]

#     peg_shape = pymunk.Poly(peg_body, vertices)
#     peg_shape.elasticity = 0.5
#     peg_shape.friction = 0.5
#     space.add(peg_body, peg_shape)

# # Create pegs in a "\center/" pattern
# def create_center_slash_pegs(space):
#     num_rows = 8
#     vertical_spacing = 50
#     max_pegs_in_row = NUM_BINS + 5  # More pegs in the top rows

#     for row in range(num_rows):
#         num_pegs = max_pegs_in_row - row if row < num_rows // 2 else row + 1
#         horizontal_spacing = WIDTH / (max_pegs_in_row + 1)

#         for col in range(num_pegs):
#             if row < num_rows // 2:
#                 x_position = (col + 1) * horizontal_spacing
#             else:
#                 x_position = WIDTH - (col + 1) * horizontal_spacing

#             y_position = row * vertical_spacing + 100
#             create_peg(x_position, y_position, space, PEG_LENGTH_A, PEG_LENGTH_B, PEG_LENGTH_C)

# # Create bins to collect balls
# bins = [0] * NUM_BINS

# # Initialize the board
# create_walls(space)
# create_static_body(space)
# create_center_slash_pegs(space)

# # Main loop
# balls = []
# for _ in range(600):  # Drop 600 balls
#     balls.append(create_ball(space))

# while True:
#     surface.fill(COLORS['background'])
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # Step the physics simulation
#     space.step(1 / FPS)

#     # Draw pegs
#     space.debug_draw(draw_options)

#     # Draw bins
#     for i in range(NUM_BINS):
#         bin_rect = pg.Rect(i * BIN_WIDTH + 1, BIN_Y_POSITION, BIN_WIDTH - 2, 50)
#         pg.draw.rect(surface, COLORS['bin_outline'], bin_rect, 1)
#         pg.draw.rect(surface, COLORS['bin_fill'], bin_rect.move(1, 1), 1)

#     # Draw balls
#     for ball in balls:
#         bin_index = int(ball.position[0] // BIN_WIDTH)
#         if ball.position[1] >= BIN_Y_POSITION and 0 <= bin_index < NUM_BINS:
#             bins[bin_index] += 1
#             balls.remove(ball)
#         else:
#             pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

#     # Draw bin contents
#     for i in range(NUM_BINS):
#         for j in range(bins[i]):
#             pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, BIN_Y_POSITION - (j * 3)), BALL_RADIUS)

#     pg.display.flip()
#     clock.tick(FPS)

###################################################################################################################################333
##log normal?
# import pygame as pg
# import numpy as np
# import pymunk
# import pymunk.pygame_util

# # Initialize Pygame and Pymunk
# pg.init()
# pymunk.pygame_util.positive_y_is_up = False

# # Constants
# RES = WIDTH, HEIGHT = 800, 1200
# FPS = 60
# BALL_RADIUS = 5
# PEG_LENGTH_A = 20  # Length of side A
# PEG_LENGTH_B = 25  # Length of side B
# PEG_LENGTH_C = 40  # Length of side C
# NUM_BINS = 15
# BIN_WIDTH = WIDTH // NUM_BINS
# BIN_Y_POSITION = HEIGHT - 100

# # Peg arrangement parameters
# ROWS = 8      # Number of rows of pegs
# COLS = 10     # Number of columns of pegs
# PEG_Y_POSITION = 200  # Y position of the first layer of pegs

# # Drop origin parameter (1 to 9)
# DROP_ORIGIN = 5  # Adjust this value between 1 and 9

# # Calculate the x-position based on DROP_ORIGIN
# def calculate_drop_position(origin):
#     return int((origin - 1) * (WIDTH / 8)) + BIN_WIDTH // 2

# # Color Scheme
# COLORS = {
#     'background': (0, 0, 0),          # Black
#     'ball': (38, 70, 83),            # Ball color
#     'peg': (47, 54, 64),             # Peg color
#     'bin_outline': (68, 91, 100),     # Bin outline color
#     'bin_fill': (95, 129, 138),       # Bin fill color
# }

# # Create Pygame surface and clock
# surface = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# draw_options = pymunk.pygame_util.DrawOptions(surface)

# # Create a physics space
# space = pymunk.Space()
# space.gravity = 0, 8000  # Gravity

# # Create static walls
# def create_walls(space):
#     wall_thickness = 5
#     left_wall = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), wall_thickness)
#     left_wall.elasticity = 1.0
#     space.add(left_wall)

#     right_wall = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
#     right_wall.elasticity = 1.0
#     space.add(right_wall)

# # Create a static ground
# def create_static_body(space):
#     static_body = space.static_body
#     pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# # Create a ball with drop position based on DROP_ORIGIN
# def create_ball(space):
#     ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
#     ball_body = pymunk.Body(1, ball_moment)

#     # Calculate x position based on drop origin
#     x_position = calculate_drop_position(DROP_ORIGIN)

#     ball_body.position = x_position, -BALL_RADIUS
#     ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
#     ball_shape.elasticity = 0.5
#     ball_shape.friction = 0.5
#     space.add(ball_body, ball_shape)
#     return ball_body

# # Create a triangular peg based on side lengths
# def create_peg(x, y, space, length_a, length_b, length_c):
#     peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
#     peg_body.position = x, y
    
#     # Calculate triangle vertices
#     angle_A = np.arccos((length_b**2 + length_c**2 - length_a**2) / (2 * length_b * length_c))
#     angle_B = np.arccos((length_a**2 + length_c**2 - length_b**2) / (2 * length_a * length_c))

#     vertex_A = (0, 0)  # Top vertex
#     vertex_B = (length_b * np.cos(angle_A), length_b * np.sin(angle_A))
#     vertex_C = (length_c * np.cos(np.pi - angle_B), length_c * np.sin(np.pi - angle_B))

#     vertices = [vertex_A, vertex_B, vertex_C]

#     peg_shape = pymunk.Poly(peg_body, vertices)
#     peg_shape.elasticity = 0.5
#     peg_shape.friction = 0.5
#     space.add(peg_body, peg_shape)

# # Create a rectangular arrangement of pegs
# def create_rectangular_pegs(space, rows, cols):
#     horizontal_spacing = WIDTH / (cols + 1)
#     vertical_spacing = 50  # Space between rows

#     for row in range(rows):
#         for col in range(cols):
#             x_position = (col + 1) * horizontal_spacing
#             y_position = PEG_Y_POSITION + row * vertical_spacing
#             create_peg(x_position, y_position, space, PEG_LENGTH_A, PEG_LENGTH_B, PEG_LENGTH_C)

# # Create bins to collect balls
# bins = [0] * NUM_BINS

# # Initialize the board
# create_walls(space)
# create_static_body(space)
# create_rectangular_pegs(space, ROWS, COLS)

# # Main loop
# balls = []
# for _ in range(600):  # Drop 600 balls
#     balls.append(create_ball(space))

# while True:
#     surface.fill(COLORS['background'])
    
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # Step the physics simulation
#     space.step(1 / FPS)

#     # Draw pegs
#     space.debug_draw(draw_options)

#     # Draw bins
#     for i in range(NUM_BINS):
#         bin_rect = pg.Rect(i * BIN_WIDTH + 1, BIN_Y_POSITION, BIN_WIDTH - 2, 50)
#         pg.draw.rect(surface, COLORS['bin_outline'], bin_rect, 1)
#         pg.draw.rect(surface, COLORS['bin_fill'], bin_rect.move(1, 1), 1)

#     # Draw balls
#     for ball in balls:
#         bin_index = int(ball.position[0] // BIN_WIDTH)
#         if ball.position[1] >= BIN_Y_POSITION and 0 <= bin_index < NUM_BINS:
#             bins[bin_index] += 1
#             balls.remove(ball)
#         else:
#             pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

#     # Draw bin contents
#     for i in range(NUM_BINS):
#         for j in range(bins[i]):
#             pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, BIN_Y_POSITION - (j * 3)), BALL_RADIUS)

#     pg.display.flip()
#     clock.tick(FPS)
##########################################################################################################################333
import pygame as pg
import numpy as np
import pymunk
import pymunk.pygame_util

# Initialize Pygame and Pymunk
pg.init()
pymunk.pygame_util.positive_y_is_up = False

# Constants
RES = WIDTH, HEIGHT = 800, 1200
FPS = 60
BALL_RADIUS = 5
PEG_LENGTH_A = 40  # Length of side A
PEG_LENGTH_B = 40  # Length of side B
PEG_LENGTH_C = 50  # Length of side C
NUM_BINS = 15
BIN_WIDTH = WIDTH // NUM_BINS
BIN_Y_POSITION = HEIGHT - 100

# Peg arrangement parameters
ROWS = 8      # Number of rows of pegs
COLS = 10     # Number of columns of pegs
PEG_Y_POSITION = 200  # Y position of the first layer of pegs

# Drop origin parameter (1 to 9)
DROP_ORIGIN = 5  # Adjust this value between 1 and 9

# Calculate the x-position based on DROP_ORIGIN
def calculate_drop_position(origin):
    return int((origin - 1) * (WIDTH / 8)) + BIN_WIDTH // 2

# Color Scheme
COLORS = {
    'background': (0, 0, 0),          # Black
    'ball': (38, 70, 83),            # Ball color
    'peg': (47, 54, 64),             # Peg color
    'bin_outline': (68, 91, 100),     # Bin outline color
    'bin_fill': (95, 129, 138),       # Bin fill color
}

# Create Pygame surface and clock
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

# Create a physics space
space = pymunk.Space()
space.gravity = 0, 8000  # Gravity

# Create static walls
def create_walls(space):
    wall_thickness = 5
    left_wall = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), wall_thickness)
    left_wall.elasticity = 1.0
    space.add(left_wall)

    right_wall = pymunk.Segment(space.static_body, (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    right_wall.elasticity = 1.0
    space.add(right_wall)

# Create a static ground
def create_static_body(space):
    static_body = space.static_body
    pymunk.Segment(static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20).elasticity = 0.5

# Create a ball with drop position based on DROP_ORIGIN
def create_ball(space):
    ball_moment = pymunk.moment_for_circle(1, 0, BALL_RADIUS)
    ball_body = pymunk.Body(1, ball_moment)

    # Calculate x position based on drop origin
    x_position = calculate_drop_position(DROP_ORIGIN)

    ball_body.position = x_position, -BALL_RADIUS
    ball_shape = pymunk.Circle(ball_body, BALL_RADIUS)
    ball_shape.elasticity = 0.5
    ball_shape.friction = 0.5
    space.add(ball_body, ball_shape)
    return ball_body

# Create a triangular peg based on side lengths
def create_peg(x, y, space, length_a, length_b, length_c):
    peg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    peg_body.position = x, y
    
    # Calculate triangle vertices
    angle_A = np.arccos((length_b**2 + length_c**2 - length_a**2) / (2 * length_b * length_c))
    angle_B = np.arccos((length_a**2 + length_c**2 - length_b**2) / (2 * length_a * length_c))

    vertex_A = (0, 0)  # Top vertex
    vertex_B = (length_b * np.cos(angle_A), length_b * np.sin(angle_A))
    vertex_C = (length_c * np.cos(np.pi - angle_B), length_c * np.sin(np.pi - angle_B))

    vertices = [vertex_A, vertex_B, vertex_C]

    peg_shape = pymunk.Poly(peg_body, vertices)
    peg_shape.elasticity = 0.5
    peg_shape.friction = 0.5
    space.add(peg_body, peg_shape)

# Create a rectangular arrangement of pegs
def create_rectangular_pegs(space, rows, cols):
    horizontal_spacing = WIDTH / (cols + 1)
    vertical_spacing = 50  # Space between rows

    for row in range(rows):
        for col in range(cols):
            x_position = (col + 1) * horizontal_spacing
            y_position = PEG_Y_POSITION + row * vertical_spacing
            create_peg(x_position, y_position, space, PEG_LENGTH_A, PEG_LENGTH_B, PEG_LENGTH_C)

# Create bins to collect balls
bins = [0] * NUM_BINS

# Initialize the board
create_walls(space)
create_static_body(space)
create_rectangular_pegs(space, ROWS, COLS)

# Main loop
balls = []
for _ in range(600):  # Drop 600 balls
    balls.append(create_ball(space))

while True:
    surface.fill(COLORS['background'])
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # Step the physics simulation
    space.step(1 / FPS)

    # Draw pegs
    space.debug_draw(draw_options)

    # Draw bins
    for i in range(NUM_BINS):
        bin_rect = pg.Rect(i * BIN_WIDTH + 1, BIN_Y_POSITION, BIN_WIDTH - 2, 50)
        pg.draw.rect(surface, COLORS['bin_outline'], bin_rect, 1)
        pg.draw.rect(surface, COLORS['bin_fill'], bin_rect.move(1, 1), 1)

    # Draw balls
    for ball in balls:
        bin_index = int(ball.position[0] // BIN_WIDTH)
        if ball.position[1] >= BIN_Y_POSITION and 0 <= bin_index < NUM_BINS:
            bins[bin_index] += 1
            balls.remove(ball)
        else:
            pg.draw.circle(surface, COLORS['ball'], (int(ball.position[0]), int(ball.position[1])), BALL_RADIUS)

    # Draw bin contents
    for i in range(NUM_BINS):
        for j in range(bins[i]):
            pg.draw.circle(surface, COLORS['ball'], (i * BIN_WIDTH + BIN_WIDTH // 2, BIN_Y_POSITION - (j * 3)), BALL_RADIUS)

    pg.display.flip()
    clock.tick(FPS)
