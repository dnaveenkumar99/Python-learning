# class Person:
#     def __init__(self):
#         self.__name:""
#     def setter(self,val):
#         self.__name=val
#     def getter(self):
#         return self.__name
# p1=Person()
# p1.setter("Uday")
# res=p1.getter()
# print(res)


class Person:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,val):
        self.__name=val
    getset=property(getter,setter)
p1=Person()
p1.getset="Uday"
res=p1.getset
print(res)


# p1=Person()
# Cursor calls Person(), a new blank object is created, __init__ runs on it: self.name="" sets a slot name.
# Cursor pops back. p1 now points to { name: "" }.
# p1.getset="Uday"
#
# This line looks like a plain attribute assignment, like self.name="" was — but it isn't.
# Before writing anything, the cursor first checks: does Person have something called getset that is a gatekeeper object?
# Yes — it's the property object from Phase 1. So instead of just storing "Uday" directly, the cursor detours through the setter recipe:
#
# It calls setter(p1, "Uday") — exactly as if you had written p1.setter("Uday") yourself.
# Inside setter, self.__name=val (already rewritten to self._Person__name=val) runs, creating a new slot on p1 called _Person__name, holding "Uday".
# That finishes, and the cursor comes back to the line p1.getset="Uday", which is now considered complete.
#
# State of p1 right now:
#
# p1 → { name: "", _Person__name: "Uday" }
#
# Notice: no slot literally named getset is ever created on p1. getset only exists on the blueprint as the gatekeeper; on the actual object, the data lives at _Person__name.
#
# res=p1.getset
#
# Same trick, but for reading. The cursor checks: is getset a gatekeeper object on Person? Yes. So instead of directly fetching a slot, it detours through the getter recipe:
#
# It calls getter(p1) — as if you'd written p1.getter() yourself.
# Inside, return self.__name (rewritten to return self._Person__name) looks up _Person__name on p1, finds "Uday", and sends it back.
# The cursor stores that returned value into res.
# res → "Uday"
# print(res)
#
# Prints "Uday".
