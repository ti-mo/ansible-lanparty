from ansible import errors

# Strip trailing slash
def append(l, item):
  try:
    l.append(item)
  except Exception as e:
    raise errors.AnsibleFilterError('Error in append: %s' % e)

  return l

class FilterModule(object):
  ''' ansible-lanparty list filters '''

  def filters(self):
    return {
      'append': append
    }
