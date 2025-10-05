from .seq import Seq

class FastaReader:
  def __init__(self, path:str):
    self.path = path

  def check(self):
    with open(self.path) as f:
      beginning = f.readline().strip()
      if beginning.startswith('>'):
        print('its fasta file')
        return True
      else:
        print('it is not fasta file')
        return False

  def read(self):
    seq = []
    title = None
    with open(self.path) as f:
      for x in f:
        x = x.strip()
        if not x:
          continue
        if x.startswith('>'):
          if title is not None:
            yield Seq(''.join(seq), title)
          title = x[1:]
          seq = []
        else:
          seq.append(x)
      if title is not None: #for latest seq
        yield Seq(''.join(seq), title)

    
  
          