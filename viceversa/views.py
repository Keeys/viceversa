from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def reverse(request):
    # get from home html 'name=usertext'
    user_text = request.GET['usertext'] 

    # split string and calculate number of words
    word_list = user_text.split()
    number_of_words = len(word_list)
  
    # reverse entered text in string
    reversed_text = user_text[::-1]

    return render(request, 'reverse.html', {
        'usertext':user_text, 
        'reversedtext':reversed_text,
        'numberofwords':number_of_words
        })