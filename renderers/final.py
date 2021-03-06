from rgbmatrix import graphics
from utils import get_font
from renderers.teams import TeamsRenderer
import ledcolors.scoreboard

class Final:
  def __init__(self, canvas, game, scoreboard, scroll_pos):
    self.canvas = canvas
    self.font = get_font()
    self.game = game
    self.scoreboard = scoreboard
    self.text_color = graphics.Color(*ledcolors.scoreboard.text)
    self.scroll_pos = scroll_pos

  def render(self):
    TeamsRenderer(self.canvas, self.scoreboard.home_team, self.scoreboard.away_team).render()
    self.__render_final_inning()
    return self.__render_scroll_text()

  def __render_scroll_text(self):
    scroll_text = "W: %s %s-%s L: %s %s-%s" % (
      self.game.winning_pitcher, self.game.winning_pitcher_wins, self.game.winning_pitcher_losses,
      self.game.losing_pitcher, self.game.losing_pitcher_wins, self.game.losing_pitcher_losses)
    return graphics.DrawText(self.canvas, self.font, self.scroll_pos, 31, self.text_color, scroll_text)

  def __render_final_inning(self):
    color = graphics.Color(*ledcolors.scoreboard.text)
    text = "FINAL " + str(self.scoreboard.inning.number)
    text_x = self.__center_text_pos(text, 32)
    graphics.DrawText(self.canvas, self.font, text_x, 20, color, text)

  def __center_text_pos(self, text, canvas_width):
    return ((canvas_width - (len(text) * 4)) / 2)
