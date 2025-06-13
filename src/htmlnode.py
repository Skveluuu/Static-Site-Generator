
class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        result = " " +" ".join(map(lambda props: f'{props[0]}="{props[1]}"', self.props.items()))
        return result
    
    def __repr__(self):
        return f"(HTMLNode:{self.tag}, {self.value}, {self.children}, {self.props})"
    
        
class LeafNode(HTMLNode):
    def __init__(self,tag, value, props=None):
        super().__init__(tag, value, props)
    
    def to_html(self):
        spacehold=" "
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.props == None:
            spacehold = ""
        return f"<{self.tag}{spacehold}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag=tag, children=children, props=props,value=None)


