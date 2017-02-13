from ansible import errors

# Return the hostname from a URL
# TODO: strip http(s) from the start of the string
def split_url(s, char='/'):
  return s.split(char, 1)[0]

# Convert an integer to a hex value padded to a given width
def to_hex(a, width=4):
  if not isinstance(a, int):
    raise errors.AnsibleFilterError("to_hex can only be called on integers (got '{}')".format(a))

  if not isinstance(width, int):
    raise errors.AnsibleFilterError("to_hex expects 'width' parameter to be integer")

  return format(a, '0{}x'.format(width))

# Strip leading slash
def lstrip_slash(s):
  if s.startswith('/'):
    return s[1:]

# Strip trailing slash
def rstrip_slash(s):
  if s.endswith('/'):
    return s[:-1]

class FilterModule(object):
  ''' ansible-lanparty string filters '''

  def filters(self):
    return {
      'split_url': split_url,
      'to_hex': to_hex,
      'lstrip_slash': lstrip_slash,
      'rstrip_slash': rstrip_slash
    }
