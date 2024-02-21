import logic
import pygame

def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    BACKGROUND = pygame.image.load("images/board.png")
    
    PLAYERS = ["X", "O"]

    player = "X"

    BLUE = (0, 0, 128)
    FONT = pygame.font.Font(None, 200)

    pygame.display.set_caption("Tic Tac Toe")
    pygame.mixer.music.load("audio/music.mp3")
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(loops=-1)

    click = pygame.mixer.Sound("audio/click.wav")

    running = True

    game_over = False

    switch = lambda player: "X" if player == "O" else "O"

    board = logic.gen_board()

    screen.blit(BACKGROUND, (0, 0))

    # give access to width, height and screen directly
    def draw_text(text):
        """ draw win message to the screen """
        font = pygame.font.Font(None, 90)
        text = font.render(text, True, pygame.Color("white"))
        rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        screen.blit(text, rect)

    while running:
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not game_over:
                    TEXT = FONT.render(player, True, BLUE)

                    pos = pygame.mouse.get_pos()
                    pos = logic.convert(pos)

                    valid = logic.move(pos, player, board)

                    if valid:
                        screen.blit(TEXT, logic.get_box(pos))
                        click.play()

                        state = logic.check_board(board, PLAYERS)
                        
                        if state in PLAYERS:
                            game_over = True
                            screen.fill("black")
                            draw_text(f"Winner: {state}")
                            pygame.mixer_music.fadeout(100)
                        
                        elif not state:
                            game_over = True
                            screen.fill("black")
                            draw_text("Tie!")
                            pygame.mixer_music.fadeout(100)
                    
                    player = switch(player)

            keys = pygame.key.get_pressed()

            # reset the game if game_over condition is met
            if keys[pygame.K_SPACE] and game_over:
                game_over = False
                board = logic.gen_board()
                player = "X"
                screen.blit(BACKGROUND, (0,0))
                pygame.mixer.music.play(loops=-1)           

if __name__ == "__main__":
    main()
