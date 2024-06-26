import re
# tokens: win, fail, ints, sum, of, an, not
'''
grammar
A -> i has a x itz y; A |S
S -> sum of S an S | diff of S and S| T
T -> not T | P
P -> win|fail|int
LL(k)

sum of 3 an 4 => 7
sum of (sum of 4 an 6) an 7 => 17
not win => fail
sum of 12 an 13 
'''

# not 3
# sum of 3 an 4 -> lexer -> list of tokens: 
# [SUM_TOK, OF_TOK, (3,int), AN_TOK, (4,int)]

def lexer(string):
  win_tok = re.compile("^win") 
  fail_tok = re.compile("^fail") 
  int_tok = re.compile("^-?[0-9]+")
  sum_tok = re.compile("^sum")   
  diff_tok = re.compile("^diff")   
  of_tok = re.compile("^of")
  an_tok = re.compile("^an")
  not_tok = re.compile("^not")
  i_tok = re.compile("^i")
  has_tok = re.compile("^has")
  a_tok = re.compile("^a")
  itz_tok = re.compile("^itz")
  semi_tok = re.compile("^;")
  var_tok = re.compile("^[a-z][a-z0-9]*")
  toks = []
  while string != "":
    if re.match(win_tok, string):
      toks.append("WIN_TOK")
      string = string[3:]
    elif re.match(fail_tok, string):
      toks.append("FAIL_TOK")
      string = string[4:]
    elif re.match(sum_tok, string):
      toks.append("SUM_TOK")
      string = string[3:]
    elif re.match(diff_tok, string):
      toks.append("DIFF_TOK")
      string = string[4:]
    elif re.match(an_tok, string):
      toks.append("AN_TOK")
      string = string[2:]
    elif re.match(of_tok, string):
      toks.append("OF_TOK")
      string = string[2:]
    elif re.match(not_tok, string):
      toks.append("NOT_TOK")
      string = string[3:]
    elif re.match(itz_tok, string):
      toks.append("ITZ_TOK")
      string = string[3:]
    elif re.match(has_tok, string):
      toks.append("HAS_TOK")
      string = string[3:]
    elif re.match(a_tok, string):
      toks.append("A_TOK")
      string = string[1:]
    elif re.match(i_tok, string):
      toks.append("I_TOK")
      string = string[1:]
    elif re.match(semi_tok, string):
      toks.append("SEMI_TOK")
      string = string[1:]
    elif re.match(int_tok, string):
      matched = re.match(int_tok,string) 
      num = matched.group(0)
      toks.append((num,"INT"))
      string = string[len(num):]
    elif re.match(var_tok, string):
      matched = re.match(var_tok,string) 
      var = matched.group(0)
      toks.append((var,"VAR"))
      string = string[len(var):]
    else:
      string = string[1:]
  return toks
'''
print(lexer("3"))
print(lexer("13"))
print(lexer("sum of 3 an 6"))
print(lexer("sum of 3 an 6 not"))
print(lexer("not not not"))
print(lexer("of an of sum 42 -19"))
print(lexer("of diffrint of sum 42 -19"))
print(lexer("i has a var itz 4;var"))
print(lexer("i has a x9 itz 4;var"))
'''

'''
grammar
A -> i has a x itz A;A | S
S -> sum of S an S | T
T -> not T | P
P -> win|fail|int|var
LL(k)
'''

def parser(toks):
  (tree,leftover) = parse_a(toks)
  if leftover == []:
    return tree
  else:
    print("Malformed sentence")

def add(x=3,y=4):
  return x + y

class Node:
  def __init__(self,typ,arg1,arg2,arg3=None):
    self.type = typ
    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

  def __str__(self):
    res = str(self.type) + "\n"
    res += str(self.arg1) + "\n"
    if self.arg2:
      res += str(self.arg2) + "\n"
    return res

#A -> i has a x itz A;A | S
def parse_a(toks):
  if toks[0] == "I_TOK":
    if toks[1] == "HAS_TOK" and toks[2] == "A_TOK":
      var = toks[3]
      if toks[4] == "ITZ_TOK":
        (subtree1,leftover) = parse_a(toks[5:])
        if leftover[0] == "SEMI_TOK":
          (subtree2,leftover2) = parse_a(leftover[1:])
          return Node("binding",var[0],subtree1,subtree2),leftover2
        else:
          print("missing semicolon on line z")
      else:
        print("Missing the 'itz' keyword")
    else:
      print("missing keywords after the 'I'")
  else:
    return parse_s(toks) 

def parse_s(toks):
  if toks[0] == "SUM_TOK":
    # we now know we are making an S sentence
    if toks[1] == "OF_TOK": #then we know the next keyword is good
      (subtree1,leftover1) = parse_s(toks[2:]) 
      # parsed an s sentence,
      if leftover1[0] == "AN_TOK":
        (subtree2,leftover2) = parse_s(leftover1[1:])
        return Node("add",subtree1,subtree2),leftover2
      else:
        print("malformed sentence: expected 'AN' keyword")
    else:
      print("malformed: expected an 'OF' keyword")
  elif toks[0] == "DIFF_TOK":
    # we now know we are making an S sentence
    if toks[1] == "OF_TOK": #then we know the next keyword is good
      (subtree1,leftover1) = parse_s(toks[2:]) 
      # parsed an s sentence,
      if leftover1[0] == "AN_TOK":
        (subtree2,leftover2) = parse_s(leftover1[1:])
        return Node("sub",subtree1,subtree2),leftover2
      else:
        print("malformed sentence: expected 'AN' keyword")
    else:
      print("malformed: expected an 'OF' keyword")
  else:
    return parse_t(toks)

def parse_t(toks):
  if toks[0] == "NOT_TOK":
    (subtree,leftover) = parse_t(toks[1:])  
    return Node("negate",subtree,None),leftover
  else:
    return parse_p(toks)

def parse_p(toks):
  if toks[0] == "WIN_TOK":
    return Node("win",None,None),toks[1:]
  elif toks[0] == "FAIL_TOK":
    return Node("fail",None,None),toks[1:]
  elif type(toks[0]) == tuple:
    if toks[0][1] == "INT":
      return Node("int",toks[0][0],None),toks[1:]
    elif toks[0][1] == "VAR":
      return Node("var",toks[0][0],None),toks[1:]
    else:
      print("should not be reached")
  else:
    raise Exception("malformed sentence") 

'''
print(parser(lexer("3")))
print(parser(lexer("13")))
print(parser(lexer("sum of 3 an 6")))
print(parser(lexer("sum of 3 an 6 not")))
print(parser(lexer("not not not")))
print(parser(lexer("of an of sum 42 -19")))
print(parser(lexer("of diffrint of sum 42 -19")))
print(parser(lexer("diff of 3 an sum of 5 an 6")))
'''

def interp(tree,env=[]):
  tipe = tree.type
  if tipe == "win":
   return True
  elif tipe == "fail":
    return False
  elif tipe == "int":
    return int(tree.arg1)
  elif tipe == "var":
    def lookup(env,var):
      for (variable,val) in env:
        if var == variable:
          return val
      print("unbound var")
      return None
    v = lookup(env,tree.arg1)
    return v
  elif tipe == "binding":
    v1 = interp(tree.arg2,env)
    v2 = interp(tree.arg3,[(tree.arg1,v1)] + env)
    return v2 
  elif tipe == "negate":
    v1 = interp(tree.arg1,env)
    v2 = not v1
    return v2
  elif tipe == "add":
    v1 = interp(tree.arg1,env)
    v2 = interp(tree.arg2,env)
    print(env)
    v3 = v1 + v2
    return v3
  elif tipe == "sub":
    v1 = interp(tree.arg1,env)
    v2 = interp(tree.arg2,env)
    v3 = v1 - v2
    return v3
  else:
    print("meaningless sentence")
'''
print(interp(parser(lexer("3"))))
print(interp(parser(lexer("13"))))
print(interp(parser(lexer("sum of 3 an 6"))))
print(interp(parser(lexer("sum of 3 an diff of 5 an 16"))))
print(interp(parser(lexer("win"))))
print(interp(parser(lexer("not win"))))
print(interp(parser(lexer("not not not win"))))
print(interp(parser(lexer("not not fail"))))
print(interp(parser(lexer("not not 3"))))
'''
print(interp(parser(lexer("i has a var1 itz 4; i has a var2 itz 6; sum of var1 an var2"))))
