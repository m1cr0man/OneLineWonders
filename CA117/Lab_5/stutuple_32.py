Student,show_student=__import__("collections").namedtuple("Student",["firstname","surname","id"]),lambda s:print("First name: {}\n{:>10}: {}\n{:>10}: {}".format(s.firstname,"Surname",s.surname,"ID",s.id))
