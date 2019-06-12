init python:
    class book_readable_class(object):
        title = None
        pages = None
        contents = [["page_title", "page_text"]]
        
        page = 0
        overflow=None
        
        def __init__(self, title, contents, **kwargs):
            self.title = title
            self.contents = contents
            self.__dict__.update(**kwargs)
            
            self.pages = len(self.contents)-1
            
        # Show book screen
        def open(self, page=0):
            global current_book
            current_book = self
            self.page = max(0, min(page, self.pages))
            self.refresh()
            
        # Hide book screen
        def close(self):
            global current_book
            current_book = None
            self.page = 0
            renpy.hide_screen("book_menu")
            
        # Next page
        def next(self):
            self.page = min(self.page+1, self.pages)
            self.refresh()
            
        # Previous page
        def prev(self):
            self.page = max(self.page-1, 0)
            self.refresh()
            
        # Max 882 characters per page.
        def get_text(self):
            if len(self.contents[self.page][1]) > 882:
                self.overflow = self.contents[self.page][1][882:]
            else:
                self.overflow = None
            return self.contents[self.page][1][0:882]
            
        def get_title(self):
            return self.contents[self.page][0]
            
        def refresh(self):
            renpy.show_screen("book_menu", page=self.page, pages=self.pages, title=self.title, page_title=self.get_title(), page_text=self.get_text(), page_overflow=self.overflow)
            return
            
    def text_image_scale(tag, argument, contents):
        cropped = crop_image_zoom(argument, 250, 160)
        img = Transform(cropped[0], zoom=cropped[1])
        return [(renpy.TEXT_DISPLAYABLE, img)]
            
    config.custom_text_tags["tis"] = text_image_scale

    book_test = book_readable_class(title="My book", contents=[
                ["Examplar title", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque scelerisque, felis eu eleifend efficitur, augue quam viverra ipsum, a interdum risus libero in mi. Nullam condimentum mi et justo tristique gravida. Nulla at nisi tristique, eleifend diam eu, scelerisque justo. Pellentesque mi risus, accumsan id magna congue, ultrices ultrices purus. Etiam vulputate augue nec lacinia cursus. Integer gravida lacus quis tristique sollicitudin. Aenean in cursus dui, ut mattis augue. Nam et condimentum massa. Cras porta, orci in blandit eleifend, nisl mi lacinia leo, eu consequat quam odio at sapien. Pellentesque volutpat, nulla ac venenatis cursus, mi ex iaculis leo, eget suscipit turpis nunc vitae tortor. Quisque accumsan quam sollicitudin tincidunt condimentum. Etiam sit amet risus ac sapien tincidunt bibendum id eget sapien. Suspendisse tempus volutpat nibh, sit amet ultrices eros dignissim eget. Integer semper faucibus mattis. Etiam mattis ipsum ac lectus volutpat, a euismod nisl feugiat. Aliquam lectus justo, interdum a porttitor a, aliquet vel augue. {tis=interface/icons/cards.png}{/tis}"],
                ["", "Mauris vestibulum quam nec est bibendum, eget pharetra orci ullamcorper. Phasellus blandit augue nibh, condimentum dictum nibh ultricies ut. Duis in nulla quis ante dignissim luctus ac in nibh. Pellentesque quis justo egestas, euismod nisi sit amet, tempor nulla. Duis tempor nisl urna, ut suscipit quam lacinia a. Nullam efficitur mauris in erat porttitor, vel sollicitudin arcu rutrum. Nulla eros nisi, condimentum ac sem et, tristique gravida arcu. Phasellus non diam eleifend, varius diam id, iaculis libero. Duis sollicitudin eget mauris sed blandit. Vestibulum mattis massa urna, ut interdum orci egestas vehicula. Pellentesque tempor eget ligula eget fringilla. Nullam facilisis mi turpis, id vestibulum neque vehicula a. Proin cursus lectus sed cursus fermentum. Donec ullamcorper nunc et velit lacinia venenatis sit amet eget justo. Curabitur vehicula vulputate urna, ut maximus enim viverra sit amet. Vivamus at tortor a mauris egestas aliquet ultricies eu quam. Donec nec lacus sit amet turpis congue volutpat. Cras et felis interdum, sollicitudin arcu nec, porta lacus. Phasellus congue at dui sed consequat. Sed mollis nulla convallis gravida accumsan. Pellentesque maximus dui ut quam maximus malesuada. Pellentesque id dapibus nibh. Ut elementum nunc at consectetur efficitur. Aliquam sit amet pellentesque sapien. Nam eleifend odio in condimentum gravida. Morbi pellentesque in nulla eu suscipit. Praesent eget nunc felis. Ut pellentesque massa a ligula suscipit, at placerat elit blandit. Sed pulvinar accumsan sem, a imperdiet justo egestas sit amet. Fusce eget neque non nisl rutrum faucibus eget id dui. Aliquam erat volutpat."],
                ["Notes", "Vestibulum mattis massa urna, ut interdum orci egestas vehicula. Pellentesque tempor eget ligula eget fringilla. Nullam facilisis mi turpis, id vestibulum neque. Proin cursus lectus sed cursus fermentum. Donec ullamcorper nunc et velit lacinia venenatis sit amet eget justo.\n\n{b}Vehicula{/b}:\n{size=-2}1. Phasellus non diam eleifend.\n2. varius diam id, iaculis libero.\n3. Duis sollicitudin eget mauris sed blandit.{/size}\n\n Etiam at massa nec nunc convallis consequat ac vitae arcu. Aliquam faucibus metus sit amet risus ullamcorper finibus. Aenean euismod maximus augue, vitae dictum arcu vehicula quis. Nunc porta leo quis mauris luctus, ac pharetra sem volutpat. Nulla odio tellus, scelerisque vel risus tempor, sodales accumsan libero. Duis rhoncus, arcu dignissim consectetur faucibus, leo enim iaculis massa, sed luctus purus odio et neque."]])
                
    current_book = None
    
label test_book:
    $ book_test.open()
    
    label book_after_init:

    $ _return = ui.interact()
    
    if _return == "next":
        $ current_book.next()
        show screen book_animator("book_page_next", 0.5)
        with d1
        jump book_after_init
    elif _return == "prev":
        $ current_book.prev()
        show screen book_animator("book_page_prev", 0.5)
        with d1
        jump book_after_init
    elif _return == "start":
        $ current_book.open()
        show screen book_animator("book_page_start", 0.5)
        with d1
        jump book_after_init
    elif _return == "Close":
        $ current_book.close()
        jump main_room
    
screen book_menu(page, pages, title, page_title, page_text, page_overflow):
    tag book_menu
    zorder 6
    
    button style "empty" action NullAction()
    
    add im.Alpha("interface/blackfade.png", 0.5)
    add "interface/book/book_open.png"
       
    imagebutton:
        xpos 720
        ypos 100
        # Next
        if page < pages:
            idle im.Alpha("interface/book/hover.png", 0)
            hover "interface/book/hover.png"
            action Return("next")
        # Fast Back to start
        else:
            xanchor 0.5
            yanchor 0.5
            xoffset 79
            yoffset 87
            idle "interface/book/back.png"
            hover "interface/book/back.png"
            action Return("start")
         
    # Previous
    if page > 0:
        imagebutton:
            xpos 243
            ypos 100
            idle im.Alpha(im.Flip("interface/book/hover.png", horizontal=True), 0)
            hover im.Flip("interface/book/hover.png", horizontal=True)
            action Return("prev")
            
    frame:
        style "empty"
        xpos 280 ypos 130
        xsize 250
        ysize 300
        text "[page_title]" ypos -20 size 16 xalign 0.5
        text "[page_text]" size 12
        #text str(page+1) xalign 0.5 ypos 350 size 11 # fix page calc
        
    frame:
        style "empty"
        xpos 600 ypos 130
        xsize 250
        ysize 300
        if page_overflow != None:
            text "[page_overflow]" size 12
        #text str(page+2) xalign 0.5 ypos 350 size 11
    use top_bar_close_button
    
screen book_animator(img, timer):
    tag animator
    zorder 7
    
    add img 
    timer timer action [Hide("book_animator"), With(Dissolve(0.1))]
    
image book_page_next:
    contains:
        "interface/book/book_open.png"
    contains:
        #"interface/book_of_secrets/book_anim_01.png"
        #pause.1
        "interface/book/page_02.png"
        pause.08
        "interface/book/page_03.png"
        pause.08
        "interface/book/page_04.png"
        pause.08
        "interface/book/page_05.png"
        pause.08
        "interface/book/page_06.png"
        pause.08
        "interface/book/page_07.png"
        pause.08
        "blank"
        
image book_page_prev:
    contains:
        "interface/book/book_open.png"
    contains:
        xoffset 40
        #"interface/book_of_secrets/book_anim_01.png"
        #pause.1
        im.Flip("interface/book/page_02.png", horizontal=True)
        pause.08
        im.Flip("interface/book/page_03.png", horizontal=True)
        pause.08
        im.Flip("interface/book/page_04.png", horizontal=True)
        pause.08
        im.Flip("interface/book/page_05.png", horizontal=True)
        pause.08
        im.Flip("interface/book/page_06.png", horizontal=True)
        pause.08
        im.Flip("interface/book/page_07.png", horizontal=True)
        pause.08
        "blank"
    
image book_page_start:
    contains:
        "interface/book/book_open.png"
    contains:
        "interface/book/reverse_01.png"
        pause.07
        "interface/book/reverse_02.png"
        pause.07
        "blank"
        repeat 3 #book_page_max was too slow