from rest_framework import serializers

def process_attributes_head(title_text, title_style, title_id, title_class, title_tag):
    return '<' + str(title_tag) + ' class="' + str(title_class) + '" style="' + str(title_style) + '" id="' + title_id + '"> ' + str(title_text) + ' </' + str(title_tag) + '>'

def process_attributes_image(image_style, image_src, image_alt, image_class, image_id):
    return '<img class="' + str(image_class) + '" style="' + str(image_style) + '" id="' + str(image_id) + '" src="' + str(image_src) + '" alt="' + str(image_alt) + '">'

def process_attributes_button(button_style, button_content, button_class, button_id, button_href):
    if button_href == '':
        return '<button class="' + str(button_class) + '" style="' + str(button_style) + '" id="' + str(button_id) + '">' + str(button_content) + ' Me</button>'
    else:
        return '<a class="' + str(button_class) + '" style="' + str(button_style) + '" id="' + str(button_id) + '" href="' + str(button_href) + '">' + str(button_content) + ' Me</a>'


def process_attributes_text(text_style, text_content, text_class, text_id):
    return '<p class="' + str(text_class) + '" style="' + str(text_style) + '" id="' + str(text_id) + '"> ' + str(text_content) + ' </p>'

def read_template_html():
    with open('codeAPI/Template/index.html', 'r', encoding='utf-8') as f:
        return f.read()


class AttributeSerializer(serializers.Serializer):
    element_name = serializers.CharField(max_length=50, required=True)
    tag = serializers.CharField(max_length=20, required=True)
    children = serializers.ListField(child=serializers.DictField(), required=False)

    def to_representation(self, instance):
        children = instance.get("children", [])
        html_attributes = []
        html_attributes_text = ""

        for child in children:
            if child.get("element_name") == "Title":
                #html_attributes.append(process_attributes_head(child.get("content"), child.get("style"),
                #                                               child.get("id"), child.get("class"), child.get("tag")))
                html_attributes_text = html_attributes_text + process_attributes_head(child.get("content"), child.get("style"),
                                                               child.get("id"), child.get("class"), child.get("tag")) + " "
            elif child.get("element_name") == "Text":
                #html_attributes.append(process_attributes_text(child.get("style"), child.get("content"),
                 #                                              child.get("class"), child.get("id")))
                html_attributes_text = html_attributes_text + process_attributes_text(child.get("style"), child.get("content"),
                                                               child.get("class"), child.get("id")) + " "
            elif child.get("element_name") == "Image":
                #html_attributes.append(process_attributes_image(child.get("style"), child.get("src"), child.get("alt"),
                #                                               child.get("class"), child.get("id")))
                html_attributes_text = html_attributes_text + process_attributes_image(child.get("style"), child.get("src"), child.get("alt"),
                                                                child.get("class"), child.get("id")) + " "
            elif child.get("element_name") == "Button":
                #html_attributes.append(process_attributes_button(child.get("style"), child.get("content"),
                #                                                child.get("class"), child.get("id"),
                 #                                                child.get("href")))
                html_attributes_text = html_attributes_text + process_attributes_button(child.get("style"), child.get("content"),
                                                                 child.get("class"), child.get("id"),
                                                                 child.get("href")) + " "

        html_content = read_template_html()
        html_content = html_content.replace('code_text', html_attributes_text)

        return {
           "HTML": html_content
        }
