#imports
import pygame as pg
import time

#imports end

#window def

window = pg.display.set_mode((300 + (2 * 20), 300 + (2 * 20)))
window.fill([0, 0, 0])
pg.display.set_caption("Tic Tac Toe")
pg.display.update()
#font init
pg.font.init()
font = pg.font.SysFont("Arial", 15)
#sound init
pg.mixer.init()
click_sound = pg.mixer.Sound('click.wav')
victory_sound = pg.mixer.Sound('victory.wav')
tie_sound = pg.mixer.Sound('tie.wav')


def build_board():
    bar_color = [255, 255, 255]
    height = 300
    width = 5
    #horizontal
    pg.draw.rect(window, bar_color, pg.Rect(20, 100 + 20, height, width))
    pg.draw.rect(window, bar_color, pg.Rect(20, 200 + 20, height, width))
    #vertical
    pg.draw.rect(window, bar_color, pg.Rect(100 + 20, 20, width, height))
    pg.draw.rect(window, bar_color, pg.Rect(200 + 20, 20, width, height))




def cross(top_left):
    x = top_left[0]
    y = top_left[1]
    pg.draw.polygon(window, [30, 170, 30], [[x + 0, y + 0], [x + 10, y + 0], [x + 90, y + 80], [x + 80, y + 80]])
    pg.draw.polygon(window, [30, 170, 30], [[x + 80, y + 0], [x + 90, y + 0], [x + 10, y + 80], [x + 0, y + 80]])
def circle(center):
    pg.draw.circle(window, [200, 30, 30], center, 40)

def win(game_l):
    def line_win(game_l):

        y = [270, 170, 60]
        for line in game_l:
            if sum(line) == 3:
                pg.draw.rect(window, [255, 0, 0], pg.Rect(20, y[game_l.index(line)], 300, 10))
                print("The green player wins horizontally!")
                return [True, game_l.index(line)]
            elif sum(line) == 12:
                pg.draw.rect(window, [255, 0, 0], pg.Rect(20, y[game_l.index(line)], 300, 10))
                print("The red player wins horizontally!")
                return [True, game_l.index(line)]
        return [False]

    def column_win(game_l):
        c1 = game_l[0][0] + game_l[1][0] + game_l[2][0]
        c2 = game_l[0][1] + game_l[1][1] + game_l[2][1]
        c3 = game_l[0][2] + game_l[1][2] + game_l[2][2]
        c_list = [c1, c2, c3]
        for c in c_list:
            if c == 3:
                print("The green player wins vertically!")
                pg.draw.rect(window, [255, 0, 0], pg.Rect(c_list.index(3) * 100 + 60, 20, 10, 300))
                return [True, c_list.index(3)]
            elif c == 12:
                print("The red player wins vertically!")
                pg.draw.rect(window, [255, 0, 0], pg.Rect(c_list.index(12) * 100 + 60, 20, 10, 300))
                return [True, c_list.index(12)]

        return [False]


    def diagonals_win(game_l):
        d_20_02 = game_l[0][0] + game_l[1][1] + game_l[2][2]
        d_22_00 = game_l[0][2] + game_l[1][1] + game_l[2][0]
        d_list = [d_20_02, d_22_00]
        for d in d_list:
            if d == 3:
                if d_list.index(3) == 1:
                    pg.draw.polygon(window, [255, 0, 0], [[20, 25], [25, 20], [315, 310], [310, 315]])
                elif d_list.index(3) == 0:
                    pg.draw.polygon(window, [255, 0, 0], [[310, 25], [315, 30], [25, 315], [20, 310]])
                print("The green player wins diagonally!")
                return [True, d_list.index(3)]
            elif d == 12:
                if d_list.index(12) == 1:
                    pg.draw.polygon(window, [255, 0, 0], [[20, 25], [25, 20], [315, 310], [310, 315]])
                elif d_list.index(12) == 0:
                    pg.draw.polygon(window, [255, 0, 0], [[310, 25], [315, 30], [25, 315], [20, 310]])
                print("The red player wins diagonally!")
                return [True, d_list.index(12)]
        return [False]

    ifwin = [line_win(game_l)[0], column_win(game_l)[0], diagonals_win(game_l)[0]]
    if True in ifwin:
        return True
    else:
        return False

def screen_test():
    for c in circle_center_list:
        circle(c)

    for i in cross_list:
        cross(i)

def update_screen(window, game_l, green_selector, red_selector, who_is_playing):
    window.fill([0, 0, 0])
    build_board()
    #upper txt
    #don't show this when the game is over
    window.blit(
        font.render("Playing: ", False, (255, 255, 255)),
        (100, 2)
    )
    #upper rect o show who is playing
    if who_is_playing == "green":
        #green rect
        pg.draw.rect(window, [30, 100, 30], pg.Rect(160, 4, 60, 10))
    elif who_is_playing == "red":
        #red rect
        pg.draw.rect(window, [100, 30, 30], pg.Rect(160, 4, 60, 10))

    if not green_selector == red_selector:
        pg.draw.rect(window, [30, 100, 30], rects_list[green_selector[0]][green_selector[1]])
        pg.draw.rect(window, [100, 30, 30], rects_list[red_selector[0]][red_selector[1]])
    else:
        pg.draw.rect(window, [50, 50, 50], rects_list[green_selector[0]][green_selector[1]])
    line_n = -1
    for line in game_l:
        line_n += 1
        column_n = -1
        for column in line:
            column_n += 1
            if column == 1:
                cross(cross_list[line_n][column_n])
            elif column == 4:
                circle(circle_center_list[line_n][column_n])

    pg.display.update()

def movimentation_calc(selector_pos, key):
    if key == pg.K_w or key == pg.K_UP:
        if not selector_pos[0] == 2:
            selector_pos[0] += 1
    elif key == pg.K_s or key == pg.K_DOWN:
        if not selector_pos[0] == 0:
            selector_pos[0] -= 1

    if key == pg.K_d or key == pg.K_RIGHT:
        if not selector_pos[1] == 2:
            selector_pos[1] += 1
    elif key == pg.K_a or key == pg.K_LEFT:
        if not selector_pos[1] == 0:
            selector_pos[1] -= 1
    return selector_pos

#this is just to help draw the crosses
cross_list = [
    [[20, 234], [125, 234], [230, 234]],
    [[20, 132], [125, 132], [230, 132]],
    [[20, 30], [125, 30], [230, 30]]
    ]
#this is just to help draw the circles
circle_center_list = [
    [[65, 274], [170, 274], [275, 274]],
    [[65, 172], [170, 172], [275, 172]],
    [[65, 70], [170, 70], [275, 70]]
]

# if the value is 0, is a free space in the game, if is 1 is a green one and if is 4 is a red one
game_l = [[0, 0, 0], #lower
          [0, 0, 0],  #midle
          [0, 0, 0]]  #upper
#this is just to help draw the selectors
rects_list = [
    [pg.Rect(20, 225, 100, 95), pg.Rect(125, 225, 95, 95), pg.Rect(225, 225, 95, 95)], #lower
    [pg.Rect(20, 125, 100, 95), pg.Rect(125, 125, 95, 95), pg.Rect(225, 125, 95, 95)], #midle
    [pg.Rect(20, 20, 100, 100), pg.Rect(125, 20, 95, 100), pg.Rect(225, 20, 95, 100)]     #upper
]

#red and green slelector position
green_player_selector = [2, 0]
red_player_selector = [0, 2]

who_is_playing = "green"

green_moviments_list = [pg.K_w, pg.K_s, pg.K_a, pg.K_d]
red_moviments_list = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]

sound_on = True

#1st display
update_screen(window, game_l, green_player_selector, red_player_selector, who_is_playing)
#main loop
while True:
    events = pg.event.get()
    #this delay is optional
    time.sleep(0.005)
    for event in events:
        e_type = event.type
        if e_type == pg.QUIT:
            pg.quit()
        elif e_type == pg.KEYDOWN:
            if event.key in green_moviments_list:
                # calculation of movement of the green selector with verification of permission var
                green_player_selector = movimentation_calc(green_player_selector, event.key)
            elif event.key in red_moviments_list:
                # calculation of movement of the red selector with verification of permission var
                red_player_selector = movimentation_calc(red_player_selector, event.key)

            elif event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                if who_is_playing == "green" and event.key == pg.K_SPACE:
                    # if the selected square is not occupied now is red
                    if game_l[green_player_selector[0]][green_player_selector[1]] == 0:
                        game_l[green_player_selector[0]][green_player_selector[1]] = 1
                        # play the click sound if the sound is on
                        if sound_on:
                            click_sound.play()
                        who_is_playing = "red"
                elif who_is_playing == "red" and event.key == pg.K_RETURN:
                    #if the selected square is not occupied now is red
                    if game_l[red_player_selector[0]][red_player_selector[1]] == 0:
                        game_l[red_player_selector[0]][red_player_selector[1]] = 4
                        #play the click sound if the sound is on
                        if sound_on:
                            click_sound.play()
                        who_is_playing = "green"
            elif event.key == pg.K_ESCAPE:
                # turn the sound on/off if the key esk was pressed
                sound_on = False if sound_on else True

            else:
                print("Not a good key, bro!")

            #update the screen
            update_screen(window, game_l, green_player_selector, red_player_selector, who_is_playing)

            # see if the game ends without a win
            if not 0 in game_l[0] + game_l[1] + game_l[2]:
                if sound_on:
                    tie_sound.play()
                time.sleep(3)
                pg.quit()

            # see if the game ends whit a win
            if win(game_l) == True:
                #show a screen update to show the win red lines
                pg.display.update()
                time.sleep(1)
                window.fill([0, 0, 0])
                #show the trophy
                trophy = pg.image.load("trophy.jpg")
                #play the win sound if the sound is on
                if sound_on:
                    victory_sound.play()
                window.blit(trophy, [0, 0])
                pg.display.update()
                time.sleep(3)
                pg.quit()
