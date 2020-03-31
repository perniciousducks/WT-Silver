label chibi_test:
    call her_chibi("stand", "right", "base")
    call her_walk("mid")
    call her_walk("desk")
    call her_walk("door")
    call her_walk("right")
    call her_walk(path=[("desk",None),("mid",None),("desk",None),("door",None),("right",None)])
    call ctc
    jump chibi_test
