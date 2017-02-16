from ansible import errors

# Strip trailing slash
def append(l, item):
  try:
    l.append(item)
  except Exception as e:
    raise errors.AnsibleFilterError('Error in append: %s' % e)

  return l

# Filter empty strings from a list
def filter_empty(l):
  return [x for x in l if len(x) > 0]

class FilterModule(object):
  ''' ansible-lanparty list filters '''

  def filters(self):
    return {
      'append': append,
      'filter_empty': filter_empty
    }
