class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props != None:
            return " ".join(f'{key}="{value}"' for key,value in self.props.items())
        else:
            return None
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value and self.tag != "img":
            raise ValueError
        
        if not self.tag:
            return self.value
        
        if self.tag == "img":
              return f"<{self.tag} {self.props_to_html()}>"
        if self.props == {} or self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError
        if not self.children:
            raise ValueError("The children are missing, call FBI")
        
        html_repr = f"<{self.tag}>"
        
        for node in self.children:
            html_repr += node.to_html()
        
        return html_repr+f"</{self.tag}>"
        


