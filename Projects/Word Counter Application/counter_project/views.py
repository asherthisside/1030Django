from django.shortcuts import render 

def home(request):
    return render(request, 'index.html')

def result(request):
    text = request.POST['text']
    total_chars = len(text)
    total_words = len(text.split())
    uppercase_counter = lowercase_counter = vowels_counter = consontants_counter = numerals_counter = special_counter = 0
    uppercase_chars = []

    for i in text:
        if i.isalpha():
            # uppercase 
            if i.isupper():
                uppercase_counter += 1
                uppercase_chars.append(i)

            # lowercase 
            else:
                lowercase_counter += 1

            # vowels
            if i in "aeiou":
                vowels_counter += 1 

            # consonants
            else: 
                consontants_counter += 1

        elif i.isnumeric():
            numerals_counter += 1

        else: 
            special_counter += 1

    context = {
        'text': text,
        'characters': total_chars,
        'words': total_words,
        'uppercase': uppercase_counter,
        'lowercase': lowercase_counter,
        'vowels': vowels_counter,
        'consonants': consontants_counter,
        'numerals': numerals_counter,
        'special_chars': special_counter,
        'uppercase_chars': uppercase_chars,
        # 'lowercase_chars': lowercase_chars,
    }

    return render(request, 'result.html', context)


# <tr>
#                 <th>Lowrcase Characters</th>
#                 <td>
#                     {% for char in lowercase_chars %}
#                     {{ char }}
#                     {% endfor %}
#                 </td>
#             </tr>