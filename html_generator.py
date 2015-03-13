def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

#print generate_concept_HTML('title','description')

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

#print make_HTML(concept)

LIST_OF_CONCEPTS = [['Why Computers are Stupid', '''The phrase "computers are stupid" refers 
                    to how they interpret instructions literally. This 
                    means that small typos can cause big problems'''],
                    ['Python', 'Python is a programming Language'],
                    ['For Loop', 'For Loops allow you to iterate over lists'],
                    ['Lists', 'Lists are sequences of data']]

def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ''
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML
    
print make_HTML_for_many_concepts(LIST_OF_CONCEPTS)
