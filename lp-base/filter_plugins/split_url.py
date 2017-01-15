# Filters for lp-base

class FilterModule(object):
  ''' lp-base filters '''

  def filters(self):
    return {
      'split_url': split_url
    }

def split_url(s, char='/'):
  return s.split(char, 1)[0]
