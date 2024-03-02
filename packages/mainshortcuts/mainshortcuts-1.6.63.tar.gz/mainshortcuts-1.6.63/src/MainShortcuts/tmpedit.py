value={}
dict={
  "self": {
    "functions": [
      "__neg__",
      "__pos__",
      "__abs__",
      "__invert__",
      "__complex__",
      "__int__",
      "__float__",
      "__index__",
      "__trunc__",
      "__floor__",
      "__ceil__"
      ],
    "text": [
      "  def {METHOD}(self):",
      "    return self.data.{METHOD}(self)"
      ]
    },
  "self,other": {
    "functions": [
      "__add__",
      "__and__",
      "__divmod__",
      "__eq__",
      "__floordiv__",
      "__ge__",
      "__gt__",
      "__iadd__",
      "__iand__",
      "__idivmod__",
      "__ifloordiv__",
      "__ilshift__",
      "__imatmul__",
      "__imod__",
      "__imul__",
      "__ior__",
      "__irshift__",
      "__isub__",
      "__itruediv__",
      "__ixor__",
      "__le__",
      "__lshift__",
      "__lt__",
      "__matmul__",
      "__mod__",
      "__mul__",
      "__ne__",
      "__or__",
      "__radd__",
      "__rand__",
      "__rdivmod__",
      "__rfloordiv__",
      "__rlshift__",
      "__rmatmul__",
      "__rmod__",
      "__rmul__",
      "__ror__",
      "__rrshift__",
      "__rshift__",
      "__rsub__",
      "__rtruediv__",
      "__rxor__",
      "__sub__",
      "__truediv__",
      "__xor__"
      ],
    "text": [
      "  def {METHOD}(self,other):",
      "    if type(self)==type(other):",
      "      return self.data.{METHOD}(other.data)",
      "    else:",
      "      return self.data.{METHOD}(other)"
      ]
    }
  }
with open("values.py","r") as f:
  text=f.read()
for k,v in dict.items():
  for i in v["functions"]:
    if hasattr(value,i):
      text+=("\n".join(v["text"])).format(METHOD=i)+"\n"
with open("values.py","w") as f:
  f.write(text)
