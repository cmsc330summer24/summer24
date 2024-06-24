import re

def lex(program):
  res = [
    #(re.compile("^(-?[0-9]+)"), lambda x: ("NUM",x.group(1))),
    (re.compile("^win"),        lambda x: (("TROOF", True),3)),
    (re.compile("^fail"),       lambda x: (("TROOF", False),4)),
    (re.compile("^sum"),        lambda x: ("SUM",3)),
    (re.compile("^diffrint"),   lambda x: ("DIFFRINT",8)),
    (re.compile("^diff"),       lambda x: ("DIFF",4)),
    (re.compile("^produkt"),    lambda x: ("PRODUKT",7)),
    (re.compile("^quoshunt"),   lambda x: ("QUOSHUNT",8)),
    (re.compile("^of"),         lambda x: ("OF",2)),
    (re.compile("^an"),         lambda x: ("AN",2)),
    (re.compile("^a"),          lambda x: ("A",1)),
    (re.compile("^mod"),        lambda x: ("MOD",3)),
    (re.compile("^biggr"),      lambda x: ("BIGGR",5)),
    (re.compile("^smallr"),     lambda x: ("SMALLR",6)),
    (re.compile("^either"),     lambda x: ("EITHER",6)),
    (re.compile("^both"),       lambda x: ("BOTH",4)),
    (re.compile("^not"),        lambda x: ("NOT",3)),
    (re.compile("^saem"),       lambda x: ("SAEM",4)),
    (re.compile("^\("),         lambda x: ("(",1)),
    (re.compile("^\)"),         lambda x: (")",1)),
    (re.compile("^itz"),        lambda x: ("ITZ",3)),
    (re.compile("^i"),          lambda x: ("I",1)),
    (re.compile("^has"),        lambda x: ("HAS",3)),
    (re.compile("^\n"),         lambda x: ("NL",1)),
    #(re.compile("^(\s+)"),      lambda x: (None)),
    (re.compile("^oic"),        lambda x: ("OIC",3)),
    (re.compile("^o"),          lambda x: ("O",1)),
    (re.compile("^\?"),         lambda x: ("?",1)),
    (re.compile("^rly"),        lambda x: ("RLY",3)),
    (re.compile("^ya"),         lambda x: ("YA",2)),
    (re.compile("^no"),         lambda x: ("NO",2)),
    (re.compile("^wai"),        lambda x: ("WAI",3)),
    (re.compile("^,"),          lambda x: (",",1)),
    #(re.compile("^([a-z0-9]+)"), lambda x: ("ID",x.group(1)))
  ]
  numre = re.compile("^(-?[0-9]+)")
  wsre = re.compile("^(\s+)") 
  idre = re.compile("^([a-z0-9]+)") 
  def lexer(string,toks):
    if string == "":
      return toks
    matched = numre.match(string)
    if matched:
      num = matched.group(1)
      numlen = len(num)
      return lexer(string[numlen:],toks + [("NUM",int(num))])
    for (regex,f) in res:
      matched = regex.match(string)
      if matched:
        (tok,tlen) = f(matched)
        return lexer(string[tlen:],toks + [tok])

    matched = wsre.match(string)
    if matched:
      ws = matched.group(1)
      return lexer(string[1:],toks)
    matched = idre.match(string)
    if matched:
      var = matched.group(1)
      varlen = len(var)
      return lexer(string[varlen:],toks + [("ID",var)])
  return lexer(program,[])

class Ast:
  def __init__(self,t,a1,a2,a3):
    self.type  = t
    self.arg1  = a1
    self.arg2  = a2
    self.arg3  = a3
  
  def __str__(self):
    t  = "type: " + str(self.type)
    a1 = "arg1: " + str(self.arg1)
    a2 = "arg2: " + str(self.arg2)
    a3 = "arg3: " + str(self.arg3)
    ret = ""
    if t:
      ret += t + "\n"
    if a1:
      ret += a1 + "\n"
    if a2:
      ret += a2 + "\n"
    if a3:
      ret += a3 + "\n"
    return ret

def parse(toks):
  (tree,rest) = parse_a(toks)
  if rest == []:
    return tree
  else:
    raise Exception("Extra tokens found")

def parse_a(toks):
  if ["I","HAS","A"] == toks[:3]:
    if type(toks[3]) == tuple and toks[3][0] == "ID" and toks[4] == "ITZ":
      (tree,rest) = parse_a(toks[5:])
      if rest[0] == "NL":
        (body,rest) = parse_a(rest[1:])
        return (Ast("HAS",toks[3][1],tree,body),rest)
      raise Exception("expecting newline after the has expression")
    raise Exception("expected a variable after the 'has a' portion")
  return parse_b(toks)

def parse_b(toks):
  if (toks[0] == "SUM" or toks[0] == "DIFF") and toks[1] == "OF":
    (e1,rest) = parse_b(toks[2:])
    if rest[0] == "AN":
      (e2,rest) = parse_b(rest[1:])
      return Ast(toks[0],e1,e2,None),rest
    raise Exception("missing AN keyword")
  else:
    return parse_c(toks)

def parse_c(toks):
  if (toks[0] == "QUOSHUNT" or toks[0] == "PRODUKT") and toks[1] == "OF":
    (e1,rest) = parse_c(toks[2:])
    if rest[0] == "AN":
      (e2,rest) = parse_c(rest[1:])
      return Ast(toks[0],e1,e2,None),rest
    raise Exception("missing AN keyword")
  else:
    return parse_d(toks)

def parse_d(toks):
  if (toks[0] == "MOD") and toks[1] == "OF":
    (e1,rest) = parse_d(toks[2:])
    if rest[0] == "AN":
      (e2,rest) = parse_d(rest[1:])
      return Ast(toks[0],e1,e2,None),rest
    raise Exception("missing AN keyword")
  else:
    return parse_e(toks)

def parse_e(toks):
  if (toks[0] == "BIGGR" or toks[0] == "SMALLR") and toks[1] == "OF":
    (e1,rest) = parse_e(toks[2:])
    if rest[0] == "AN":
      (e2,rest) = parse_e(rest[1:])
      return Ast(toks[0],e1,e2,None),rest
    raise Exception("missing AN keyword")
  else:
    return parse_f(toks)

def parse_f(toks):
  if (toks[0] == "EITHER") and toks[1] == "OF":
    (e1,rest) = parse_f(toks[2:])
    if rest[0] == "AN":
      (e2,rest) = parse_f(rest[1:])
      return Ast(toks[0],e1,e2,None),rest
    raise Exception("missing AN keyword")
  else:
    return parse_g(toks)

def parse_g(toks):
  if (toks[0] == "BOTH") and toks[1] == "OF":
    (e1,rest) = parse_g(toks[2:])
    if rest[0] == "AN":
      (e2,rest) = parse_g(rest[1:])
      return Ast(toks[0],e1,e2,None),rest
    raise Exception("missing AN keyword")
  else:
    return parse_h(toks)

def parse_h(toks):
  if (toks[0] == "NOT"):
    (e1,rest) = parse_h(toks[1:])
    return (Ast(toks[0],e1,None,None),rest)
  else:
    return parse_i(toks)

def parse_i(toks):
  if (toks[0] == "DIFFRINT") and toks[1] == "OF":
    (e1,rest) = parse_i(toks[2:])
    if rest[0] == "AN":
      (e2,rest) = parse_i(rest[1:])
      return Ast(toks[0],e1,e2,None)
    raise Exception("missing AN keyword")
  elif (toks[0] == "BOTH") and toks[1] == "SAEM" and toks[2] == "OF":
    (e1,rest) = parse_i(toks[3:])
    if rest[0] == "AN":
      (e2,rest) = parse_i(rest[1:])
      return (Ast("SAEM",e1,e2,None),rest)
    raise Exception("missing AN keyword")
  else:
    return parse_j(toks)

def parse_j(toks):
  if toks[0] == "(":
    (e1,r) = parse_a(toks[1:])
    if r[0] == ")":
      if len(r) > 9 and [",","O","RLY","?","NL","YA","RLY","NL"] == r[1:9]:
        (e2,r) = parse_a(r[9:])
        if len(r) > 3 and ["NL","NO","WAI","NL"] == r[:4]:
          (e3,r) = parse_a(r[4:])
          if len(r) > 1 and r[0] == "NL" and r[1] == "OIC":
            return (Ast("IF",e1,e2,e3),r[2:])
          raise Exception("no end of RLY block found")
        raise Exception("no 'no wai' clause found")
      return e1,r[1:]
    raise Exception("missing closing ')'")
  elif type(toks[0]) == tuple:
    return Ast(toks[0][0],toks[0][1],None,None),toks[1:]
  raise Exception("malformed sentence")

def interp(tree):
  def lookup(x,e):
    if e == []:
      raise Exception("unbound var")
    (var,val) = e[0]
    if var == x:
      return val
    return lookup(x,e[1:])
  def evaluate(x,env):
    if x.type == "NUM" or x.type == "TROOF":
      return x.arg1
    if x.type == "ID":
      return lookup(x.arg1,env)
    if x.type == "SUM":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      if type(e1) == type(e2) == int:
        return e1 + e2
      raise Exception("Need two ints to add")
    if x.type == "DIFF":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      if type(e1) == type(e2) == int:
        return e1 - e2
      raise Exception("Need two ints to sub")
    if x.type == "PRODUKT":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      if type(e1) == type(e2) == int:
        return e1 * e2
      raise Exception("Need two ints to mult")
    if x.type == "QUOSHUNT":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      if type(e1) == type(e2) == int:
        return e1 / e2
      raise Exception("Need two ints to divide")
    if x.type == "BIGGR":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      if type(e1) == type(e2):
        return max(e1,e2)
      raise Exception("Need two same types to big")
    if x.type == "SMALLR":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      if type(e1) == type(e2):
        return min(e1,e2)
      raise Exception("Need two same types to small")
    if x.type == "BOTH":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      if type(e1) == type(e2) == bool:
        return e1 and e2
      raise Exception("Need two bools to and")
    if x.type == "EITHER":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      if type(e1) == type(e2) == bool:
        return e1 + e2
      raise Exception("Need two bools to or")
    if x.type == "NOT":
      e1 = evaluate(x.arg1,env)
      if type(e1) == bool:
        return not e1
      raise Exception("Need bool to not")
    if x.type == "MOD":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      if type(e1) == type(e2) == int:
        return e1 % e2
      raise Exception("Need two ints to mod")
    if x.type == "SAEM":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      if type(e1) == type(e2):
        return e1 == e2
      raise Exception("Need two same times to equate")
    if x.type == "DIFFRINT":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      if type(e1) == type(e2):
        return e1 != e2
      raise Exception("Need two same time to not equate")
    if x.type == "HAS":
      e1 = evaluate(x.arg2,env)
      e2 = evaluate(x.arg3,[(x.arg1,e1)]+env)
      return e2
    if x.type == "IF":
      e1 = evaluate(x.arg1,env)
      e2 = evaluate(x.arg2,env)
      e3 = evaluate(x.arg3,env)
      if type(e1) == bool:
        if e1:
          return e2
        else:
          return e3
      raise Exception("guard must be bool")
    raise Exception("has no meaning")

  return evaluate(tree,[])

'''
a = (lex("i has a var itz 42 \n (win), o rly? \n ya rly \n var \n no wai \n diff of 5 an 6 \n oic"))
b = (lex("84"))
c = (lex("\n"))
d = (lex("i has a var itz 4 \n (fail), o rly? \n ya rly \n var \n no wai \n diff of 8 an 6 \n oic"))
ap = (parse(a))
bp = parse(b)
dp = parse(d)
print((interp(ap)))
print((interp(bp)))
print((interp(dp)))
'''

def wrapper():
  a = None
  start = "$ "
  contents = ""
  while a != "#exit":
    try:
      a = input(start)
    except EOFError:
      print("")
      break
    if a != "":
      contents += a +"\n"
      start = ""
    elif a == "#exit":
      continue
    else:
      contents = contents.strip()
      '''
      l = lex(contents)
      print(l)
      p = parse(l)
      print("grammar good")
      e = interp(p)
      print(e)
      '''
      try:
        l = lex(contents)
        print(l)
        try:
          p = parse(l)
          print("grammar fine")
          try:
            print(interp(p))
          except:
            print("could not evaluate")
        except:
          print("grammar incorrect")
      except:
        print("could not lex")
      start = "$ "
      contents = ""
  exit(0);

wrapper()
