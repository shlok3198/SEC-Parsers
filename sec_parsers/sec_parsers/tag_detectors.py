from detectors import Detector
from style_detection import detect_link,detect_bold_from_html,detect_strong_from_html,detect_emphasis_from_html,\
    detect_italic_from_html,detect_underline_from_html,detect_table,detect_table_of_contents,detect_image

class StyleTagDetector(Detector):
    def __init__(self, style=None, **kwargs):
        super().__init__(**kwargs)
        self.style = style


class LinkTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style='link', **kwargs)

    def detect(self,element):
        if detect_link(element):
            return 'link;'
        else:
            return ''
        
class BoldTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style='bold', **kwargs)

    def detect(self,element):
        if detect_bold_from_html(element):
            return 'bold;'
        else:
            return ''

class StrongTagDetector(StyleTagDetector):
    def __init__(self, **kwargs):
        super().__init__(style ='strong', **kwargs)

    def detect(self,element):
        if detect_strong_from_html(element):
            return 'strong;'
        else:
            return ''
        
class EmphasisTagDetector(Detector):
    def __init__(self, **kwargs):
        super().__init__(style='emphasis',**kwargs)

    def detect(self,element):
        if detect_emphasis_from_html(element):
            return 'emphasis;'
        else:
            return ''
        
class ItalicTagDetector(Detector):
    def __init__(self, **kwargs):
        super().__init__(style='italic',**kwargs)

    def detect(self,element):
        if detect_italic_from_html(element):
            return 'italic;'
        else:
            return ''

class UnderlineTagDetector(Detector):
    def __init__(self, **kwargs):
        super().__init__(style='underline',**kwargs)

    def detect(self,element):
        if detect_underline_from_html(element):
            return 'underline;'
        else:
            return ''
        
class TableTagDetector(Detector):
    def __init__(self, **kwargs):
        super().__init__(style='table',**kwargs)

    def detect(self,element):
        if detect_table(element):
            if detect_table_of_contents(element) == "toc":
                return 'table of contents;'
            else:
                return 'table;'
        else:
            return ''
        
class ImageTagDetector(Detector):
    def __init__(self, **kwargs):
        super().__init__(style='image', **kwargs)

    def detect(self,element):
        if detect_image(element):
            return 'image;'
        else:
            return ''
        