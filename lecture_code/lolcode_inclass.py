import re
# tokens: win, fail, ints, sum, of, an, not
'''
grammar
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
    elif re.match(int_tok, string):
      matched = re.match(int_tok,string) 
      num = matched.group(0)
      toks.append((num,"INT"))
      string = string[len(num):]
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
'''

'''
grammar
S -> sum of S an S | T
T -> not T | P
P -> win|fail|int
LL(k)
'''

def parser(toks):
  (tree,leftover) = parse_s(toks)
  if leftover == []:
    return tree
  else:
    print("Malformed sentence")

class Node:
  def __init__(self,typ,arg1,arg2):
    self.type = typ
    self.arg1 = arg1
    self.arg2 = arg2

  def __str__(self):
    res = str(self.type) + "\n"
    res += str(self.arg1) + "\n"
    if self.arg2:
      res += str(self.arg2) + "\n"
    return res

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
    (subtree,leftover) = parse_t(toks[1])  
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
'''
print(parser(lexer("diff of 3 an sum of 5 an 6")))
