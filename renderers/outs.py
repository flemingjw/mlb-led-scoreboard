import ledcolors.scoreboard

class OutsRenderer:
  """Renders the out circles on the scoreboard."""

  def __init__(self, canvas, outs):
    self.canvas = canvas
    self.outs = outs

  def render(self):
    out_px = []
    out_px.append({'x': 2, 'y': 27})
    out_px.append({'x': 6, 'y': 27})
    out_px.append({'x': 10, 'y': 27})
    for out in range(len(out_px)):
      self.__render_out_circle(out_px[out])
      # Fill in the circle if that out has occurred
      if (self.outs.number > out):
        self.canvas.SetPixel(
            out_px[out]['x'], out_px[out]['y'], *ledcolors.scoreboard.text)

  def __render_out_circle(self, out):
    offset = 1
    for x in range(-offset, offset + 1):
      for y in range(-offset, offset + 1):
        # The dead center is filled in only if that many outs has occurred, and happens above
        # after this circle is rendered
        if x == 0 and y == 0:
          continue
        self.canvas.SetPixel(out['x'] + x, out['y'] + y, *ledcolors.scoreboard.text)
