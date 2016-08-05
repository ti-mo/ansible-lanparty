# Filters for lp-gw

from ansible import errors


def to_hex(a, width=4):
  if not isinstance(a, int):
    raise errors.AnsibleFilterError("to_hex can only be called on integers (got '{}')".format(a))

  if not isinstance(width, int):
    raise errors.AnsibleFilterError("to_hex expects 'width' parameter to be integer")

  return format(a, '0{}x'.format(width))


class FilterModule(object):
  ''' lp-gw hex int/string operations '''

  def filters(self):
    return {
      'to_hex': to_hex
    }
