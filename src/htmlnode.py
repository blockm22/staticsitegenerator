class HTMLNode():
    def __init__(self,tag = None,value = None,children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html
            
    def __repr__(self):
        print(f"tag is {self.tag}")
        print(f"value is {self.value}")
        print(f"children is {self.children}")
        print(f"props is {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props= None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return str(self.value)
        if self.props:
            attributes = self.props_to_html()
        else:
            attributes = ""
        return "<" + self.tag + attributes + ">" + self.value + "</" + self.tag + ">" 

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props= None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        children_html = [child.to_html() for child in self.children]
        return f'<{self.tag}>{"".join(children_html)}</{self.tag}>'