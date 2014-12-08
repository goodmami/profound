
import sys
from delphin.codecs import simplemrs
from delphin.mrs.query import find_quantifier

def pronoun_match(ep, m):
    q = m.get_ep(find_quantifier(m, ep.nodeid))
    if q is not None and \
       q.pred in ('pronoun_q_rel', 'which_q_rel', 'free_relative_q_rel'):
        return True
    elif ep.pred in ('generic_entity_rel', 'place_n_rel'):
        # time_n_rel is used for "when', but also "tomorrow"
        return True
    return False

def overt(ep):
    if ep.properties.get('PRONTYPE', '').lower() == 'zero_pron':
        return False
    return True

def construct_match_string(xmrs, matches):
    matches.sort(key=lambda x: (x.cfrom, x.cto))
    if not xmrs.surface:
        matchdict = {(m.cfrom, m.pred.string): m for m in matches}
        s = []
        for ep in xmrs.eps:
            if (ep.cfrom, ep.pred.string) in matchdict:
                s.append(red(ep.pred.string))
            else:
                s.append(ep.pred.string)
        return ' '.join(s)
    else:
        surface = xmrs.surface
        s = []
        pos = 0
        for match in matches:
            s.append(surface[pos:match.cfrom])
            if overt(match):
                s.append(red(surface[match.cfrom:match.cto]))
                pos = match.cto
            else:
                s.append(red('{}'))
                pos = match.cfrom
        s.append(surface[pos:])
        return ''.join(s)

def red(s):
    return '\x1b[31m{}\x1b[39;49m'.format(s)

if __name__ == '__main__':
    for m in simplemrs.load(sys.stdin):
        matches = []
        for ep in m.eps:
            if pronoun_match(ep, m):
                matches.append(ep)
        print(construct_match_string(m, matches))

